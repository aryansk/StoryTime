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

        nodes = story.get("nodes", [])
        node_ids = {n["id"] for n in nodes if "id" in n}

        start = story.get("startNodeId")
        if start not in node_ids:
            fail(f"startNodeId '{start}' not in nodes")
            errors += 1

        unreachable = node_ids.copy()
        unreachable.discard(start)

        endings = 0
        for n in nodes:
            choices = n.get("choices", [])
            if n.get("isEnding"):
                endings += 1
                if choices:
                    fail(f"node '{n['id']}' marked isEnding but has choices")
                    errors += 1
            for ch in choices:
                nxt = ch.get("nextNodeId")
                if nxt and nxt not in node_ids:
                    fail(f"choice in '{n['id']}' points to missing node '{nxt}'")
                    errors += 1
                if nxt:
                    unreachable.discard(nxt)

        ok(f"{len(nodes)} nodes, {endings} ending(s)")
        if unreachable:
            ok(f"{len(unreachable)} unreachable nodes (warning): "
               f"{sorted(unreachable)[:5]}")

    print()
    if errors:
        print(f"✗ {errors} error(s)")
        return 1
    print(f"✓ all {len(seen_ids)} stories valid")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
    sys.exit(validate(target))
