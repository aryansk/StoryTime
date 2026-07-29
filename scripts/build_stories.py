#!/usr/bin/env python3
"""
Author StoryTime catalog stories from compact specs and emit validated JSON.

The compact specs are the source of truth for metadata and branching. Existing
catalog JSON is the source of truth for edited scene prose and choice
consequences. Each build overlays that editorial copy onto the generated
structure before writing, so a catalog rebuild cannot silently replace a
finished edit with compact authoring text.

Usage:
    python3 scripts/build_stories.py          # write files
    python3 scripts/build_stories.py --check   # dry run, validate only
    python3 scripts/build_stories.py --refresh-editorial-copy

The last command deliberately replaces catalog prose with the compact spec
copy. It should only be used when that destructive editorial reset is intended.

Scene spec format (a dict per scene):
    {
        "id":    "s1",
        "title": "Scene Title",          # optional sceneTitle
        "text":  "Prose for the scene.",
        "choices": [
            ("Choice label", "Consequence flavor.", "target_id"),
            ...
        ],
    }
An ending scene has no "choices" and an "end" key holding the ending title:
    {"id": "good", "title": "...", "text": "...", "end": "The Ending Title"}
"""
import json
import hashlib
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "StoryTime2.0" / "Resources" / "Catalog"


def polished_consequence(raw, choice, story_id, scene_id, choice_index):
    """Turn terse authoring labels into immersive consequence beats.

    The compact specs intentionally use tags such as ``Brave.`` and
    ``Honest.`` because those labels also feed Choice DNA. They worked as
    metadata, but felt abrupt and repetitive in the reader. We retain the
    exact label for personality matching while wrapping it in varied prose.
    Longer hand-written consequences pass through untouched.
    """
    label = (raw or "").strip().rstrip(".!?")
    if not label:
        return raw
    if len(label.split()) > 2 or len(label) > 36:
        return raw

    key = f"{story_id}:{scene_id}:{choice_index}:{choice}".encode()
    variant = int(hashlib.sha256(key).hexdigest()[:8], 16) % 6
    safe_choice = choice.strip().rstrip(".!?")
    beats = [
        f"You commit to “{safe_choice}.” The story records the instinct as “{label}” and carries it forward.",
        f"“{safe_choice}” closes one possibility and opens another. The moment leaves a clear note behind: {label}.",
        f"The decision settles the question for now. Its verdict—{label}—follows you into whatever comes next.",
        f"There is no taking “{safe_choice}” back. {label} shapes the silence before the next moment arrives.",
        f"You let the choice stand. The path shifts almost imperceptibly, marked by one lasting impulse: {label}.",
        f"The choice lands, and the scene changes around it. If it has a name, that name is {label}.",
    ]
    return beats[variant]


def story(meta, scenes):
    """Build the full CatalogStory dict from meta + scene specs."""
    node_ids = {s["id"] for s in scenes}
    nodes = []
    for s in scenes:
        choices = []
        for choice_index, (label, consequence, target) in enumerate(s.get("choices", [])):
            if target not in node_ids:
                raise ValueError(f"{meta['id']}: choice in {s['id']} -> missing node {target!r}")
            choices.append({
                "text": label,
                "consequence": polished_consequence(
                    consequence, label, meta["id"], s["id"], choice_index
                ),
                "nextNodeId": target,
            })
        is_ending = "end" in s and not choices
        nodes.append({
            "id": s["id"],
            "text": s["text"],
            "sceneTitle": s.get("title"),
            "choices": choices,
            "isEnding": is_ending,
            "endingTitle": s.get("end"),
        })
    start = scenes[0]["id"]
    decision_nodes = sum(1 for n in nodes if n["choices"])
    # Mini-tagged stories opt out of the 20-decision rule by design.
    is_mini = "mini" in (meta.get("tags") or [])
    if decision_nodes < 20 and not is_mini:
        print(f"  ! {meta['id']}: only {decision_nodes} decision nodes (<20)")
    return {
        "id": meta["id"],
        # The visible catalog title is the original movie/show name. The
        # in-app framing is "what would you have done in <X>?" so the title
        # mirrors the source. (The invented meta["title"] is preserved in
        # scene/ending titles only.)
        "title": meta["sourceTitle"],
        "sourceTitle": meta["sourceTitle"],
        "kind": meta["kind"],
        "synopsis": meta["synopsis"],
        "releaseYear": meta.get("releaseYear"),
        "addedAt": meta["addedAt"],
        "genre": meta["genre"],
        "tags": meta.get("tags", []),
        "rating": meta.get("rating"),
        "loved": meta.get("loved", False),
        "nextStoryId": meta.get("nextStoryId"),
        "startNodeId": start,
        "nodes": nodes,
    }


def preserve_editorial_copy(generated):
    """Overlay edited prose from the current catalog onto generated structure.

    Nodes are matched by stable node ID. Choices are matched by both their
    visible label and destination, so changing either in a compact spec opts
    that choice into newly generated copy rather than attaching a stale
    consequence to a different decision.
    """
    current_path = CATALOG / f"{generated['id']}.json"
    if not current_path.exists():
        return generated

    try:
        current = json.loads(current_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(
            f"{generated['id']}: cannot preserve editorial copy from "
            f"{current_path.name}: {error}"
        ) from error

    if current.get("id") != generated["id"]:
        raise ValueError(
            f"{generated['id']}: existing catalog payload has id "
            f"{current.get('id')!r}"
        )

    current_nodes = {
        node.get("id"): node for node in current.get("nodes", []) if node.get("id")
    }
    for node in generated["nodes"]:
        edited_node = current_nodes.get(node["id"])
        if not edited_node:
            continue
        edited_text = edited_node.get("text")
        if isinstance(edited_text, str) and edited_text.strip():
            node["text"] = edited_text

        edited_choices = {
            (choice.get("text"), choice.get("nextNodeId")): choice
            for choice in edited_node.get("choices", [])
        }
        for choice in node["choices"]:
            edited_choice = edited_choices.get(
                (choice.get("text"), choice.get("nextNodeId"))
            )
            if not edited_choice:
                continue
            edited_consequence = edited_choice.get("consequence")
            if isinstance(edited_consequence, str) and edited_consequence.strip():
                choice["consequence"] = edited_consequence

    return generated


def index_entry(s):
    return {
        "id": s["id"],
        "title": s["title"],
        "sourceTitle": s["sourceTitle"],
        "kind": s["kind"],
        "synopsis": s["synopsis"],
        "releaseYear": s["releaseYear"],
        "addedAt": s["addedAt"],
        "genre": s["genre"],
        "tags": s["tags"],
        "rating": s["rating"],
        "loved": s["loved"],
        "nextStoryId": s.get("nextStoryId"),
        "storyURL": f"{s['id']}.json",
    }


def build(specs, check=False, preserve_copy=True):
    built = [story(meta, scenes) for meta, scenes in specs]
    if preserve_copy:
        built = [preserve_editorial_copy(s) for s in built]

    # Catch duplicate IDs early — otherwise the later spec silently
    # overwrites the earlier one's JSON file and the bug only surfaces
    # at runtime when one of the stories quietly vanishes.
    seen: dict[str, int] = {}
    for s in built:
        seen[s["id"]] = seen.get(s["id"], 0) + 1
    dupes = sorted(sid for sid, n in seen.items() if n > 1)
    if dupes:
        raise ValueError(f"duplicate story id(s) in SPECS: {dupes}")

    # Merge into the existing index, preserving stories we don't manage.
    index_path = CATALOG / "index.json"
    index = json.loads(index_path.read_text())
    managed_ids = {s["id"] for s in built}
    kept = [e for e in index["stories"] if e["id"] not in managed_ids]
    entries = kept + [index_entry(s) for s in built]
    entries.sort(key=lambda e: e["addedAt"], reverse=True)
    index["stories"] = entries
    # CatalogService compares this value before downloading remote deltas.
    # Deriving it from the entries prevents a stale timestamp from hiding
    # newly authored stories.
    index["updatedAt"] = max(e["addedAt"] for e in entries)

    if check:
        print(f"OK (dry run): {len(built)} stories built, index would hold {len(entries)} entries")
        return

    for s in built:
        out = CATALOG / f"{s['id']}.json"
        out.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
        decision = sum(1 for n in s["nodes"] if n["choices"])
        print(f"  wrote {out.name}: {len(s['nodes'])} nodes, {decision} decisions")
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    print(f"  updated index.json: {len(entries)} entries")


if __name__ == "__main__":
    from stories_data import SPECS
    refresh_copy = "--refresh-editorial-copy" in sys.argv
    build(
        SPECS,
        check="--check" in sys.argv,
        preserve_copy=not refresh_copy,
    )
