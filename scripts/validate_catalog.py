#!/usr/bin/env python3
"""
Validate the StoryTime catalog: every story JSON parses, every node id
referenced by a choice resolves, the start node exists, and index.json
matches the per-story files.

Usage:
    python3 scripts/validate_catalog.py
    python3 scripts/validate_catalog.py path/to/Catalog
"""
import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_DIR = Path(__file__).resolve().parent.parent / "StoryTime2.0" / "Resources" / "Catalog"


def fail(msg: str) -> None:
    print(f"  ✗ {msg}")


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def validate(catalog_dir: Path) -> int:
    if not catalog_dir.exists():
        print(f"Catalog directory not found: {catalog_dir}")
        return 1

    index_path = catalog_dir / "index.json"
    if not index_path.exists():
        print(f"Missing index.json in {catalog_dir}")
        return 1

    try:
        index = json.loads(index_path.read_text())
    except json.JSONDecodeError as e:
        print(f"index.json is not valid JSON: {e}")
        return 1

    print(f"Validating catalog at {catalog_dir}")
    errors = 0

    seen_ids = set()
    for entry in index.get("stories", []):
        sid = entry.get("id")
        print(f"\n[{sid}] {entry.get('title')}")
        if not sid:
            fail("entry missing id")
            errors += 1
            continue
        if sid in seen_ids:
            fail(f"duplicate id {sid}")
            errors += 1
        seen_ids.add(sid)

        story_url = entry.get("storyURL")
        if not story_url:
            fail("entry missing storyURL")
            errors += 1
            continue
        story_path = catalog_dir / story_url
        if not story_path.exists():
            fail(f"story file not found: {story_path.name}")
            errors += 1
            continue

        try:
            story = json.loads(story_path.read_text())
        except json.JSONDecodeError as e:
            fail(f"{story_path.name}: invalid JSON: {e}")
            errors += 1
            continue

        if story.get("id") != sid:
            fail(f"id mismatch: index has '{sid}', file has '{story.get('id')}'")
            errors += 1

        # Index cards and story payloads must describe the same work; stale
        # index metadata otherwise produces one title/genre in discovery and
        # another after navigation.
        for field in ("title", "sourceTitle", "kind", "synopsis", "releaseYear",
                      "addedAt", "genre", "tags", "rating", "loved", "nextStoryId"):
            if entry.get(field) != story.get(field):
                fail(f"index/story mismatch for {field!r}")
                errors += 1

        rating = story.get("rating")
        if rating is not None and not (isinstance(rating, int) and 1 <= rating <= 5):
            fail(f"rating must be an int 1..5, got {rating!r}")
            errors += 1

        nodes = story.get("nodes", [])
        node_id_list = [n.get("id") for n in nodes if n.get("id")]
        node_ids = set(node_id_list)
        duplicate_nodes = sorted(k for k, count in Counter(node_id_list).items() if count > 1)
        if duplicate_nodes:
            fail(f"duplicate node id(s): {duplicate_nodes}")
            errors += 1

        start = story.get("startNodeId")
        if start not in node_ids:
            fail(f"startNodeId '{start}' not in nodes")
            errors += 1

        endings = 0
        for n in nodes:
            node_id = n.get("id", "<missing>")
            if not n.get("id"):
                fail("node missing id")
                errors += 1
            if not (n.get("text") or "").strip():
                fail(f"node '{node_id}' has empty text")
                errors += 1
            if not (n.get("sceneTitle") or "").strip():
                fail(f"node '{node_id}' has empty sceneTitle")
                errors += 1
            choices = n.get("choices", [])
            if n.get("isEnding"):
                endings += 1
                if choices:
                    fail(f"node '{node_id}' marked isEnding but has choices")
                    errors += 1
                if not (n.get("endingTitle") or "").strip():
                    fail(f"ending '{node_id}' has no endingTitle")
                    errors += 1
            elif len(choices) < 2:
                fail(f"decision node '{node_id}' offers fewer than two choices")
                errors += 1

            normalized_labels = [(c.get("text") or "").strip().casefold() for c in choices]
            if len(set(normalized_labels)) != len(normalized_labels):
                fail(f"node '{node_id}' repeats a choice label")
                errors += 1
            for ch in choices:
                nxt = ch.get("nextNodeId")
                if not (ch.get("text") or "").strip():
                    fail(f"choice in '{node_id}' has empty text")
                    errors += 1
                if not (ch.get("consequence") or "").strip():
                    fail(f"choice in '{node_id}' has empty consequence")
                    errors += 1
                if not nxt:
                    fail(f"choice in '{node_id}' has no nextNodeId")
                    errors += 1
                elif nxt not in node_ids:
                    fail(f"choice in '{node_id}' points to missing node '{nxt}'")
                    errors += 1

        # Real graph traversal. The old validator merely removed every node
        # that appeared as *any* target, which missed disconnected cycles.
        by_id = {n.get("id"): n for n in nodes if n.get("id")}
        reachable = set()
        frontier = [start]
        while frontier:
            current = frontier.pop()
            if current in reachable or current not in by_id:
                continue
            reachable.add(current)
            frontier.extend(
                c.get("nextNodeId") for c in by_id[current].get("choices", [])
                if c.get("nextNodeId")
            )
        unreachable = node_ids - reachable

        decision_nodes = sum(1 for n in nodes if n.get("choices"))
        ok(f"{len(nodes)} nodes, {decision_nodes} decision node(s), {endings} ending(s)")
        # Mini-tagged stories deliberately ship with ~6 decision nodes;
        # they have their own length contract, so don't cry wolf on them.
        is_mini = "mini" in (story.get("tags") or [])
        if decision_nodes < 20 and not is_mini:
            ok(f"only {decision_nodes} decision nodes (target is 20+) — warning")
        if unreachable:
            fail(f"{len(unreachable)} unreachable node(s): {sorted(unreachable)[:5]}")
            errors += 1

    print()
    if errors:
        print(f"✗ {errors} error(s)")
        return 1
    print(f"✓ all {len(seen_ids)} stories valid")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
    sys.exit(validate(target))
