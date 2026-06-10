#!/usr/bin/env python3
"""
Author StoryTime catalog stories from compact specs and emit validated JSON.

This is the *source of truth* for the app-original "after the credits" stories
adapted from the curator's 2025-26 watch list. Each spec lists scenes; the
generator wires choices, marks endings, writes one JSON file per story, and
merges the entries into index.json without touching hand-written stories it
does not manage.

Usage:
    python3 scripts/build_stories.py          # write files
    python3 scripts/build_stories.py --check   # dry run, validate only

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
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "StoryTime2.0" / "Resources" / "Catalog"


def story(meta, scenes):
    """Build the full CatalogStory dict from meta + scene specs."""
    node_ids = {s["id"] for s in scenes}
    nodes = []
    for s in scenes:
        choices = []
        for label, consequence, target in s.get("choices", []):
            if target not in node_ids:
                raise ValueError(f"{meta['id']}: choice in {s['id']} -> missing node {target!r}")
            choices.append({"text": label, "consequence": consequence, "nextNodeId": target})
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


def build(specs, check=False):
    built = [story(meta, scenes) for meta, scenes in specs]

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
    build(SPECS, check="--check" in sys.argv)
