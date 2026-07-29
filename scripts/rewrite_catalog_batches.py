#!/usr/bin/env python3
"""Generate validated editorial rewrites in quota-aware three-story batches."""

import argparse
import concurrent.futures
import json
import os
import re
import threading
import time
import urllib.error
from pathlib import Path

import rewrite_catalog_editorial as editorial

DEFAULT_MODELS = (
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview",
)
BATCH_SCHEMA = {
    "type": "object",
    "properties": {
        "stories": {
            "type": "array",
            "items": editorial.RESPONSE_SCHEMA,
        }
    },
    "required": ["stories"],
}
PRINT_LOCK = threading.Lock()


def cached_story(path, cache_dir):
    story = json.loads(path.read_text())
    cache_path = cache_dir / path.name
    if not cache_path.exists():
        return None
    cached = json.loads(cache_path.read_text())
    targets = editorial.branch_plan(story)
    shaped = {
        "id": cached.get("id"),
        "nodes": [
            {
                "id": node.get("id"),
                "text": node.get("text"),
                "choices": node.get("choices", []),
            }
            for node in cached.get("nodes", [])
        ],
    }
    errors = editorial.validate_rewrite(story, shaped, targets)
    errors.extend(editorial.graph_errors(cached))
    return cached if not errors else None


def batch_prompt(items):
    instructions = """
Rewrite every supplied interactive story as a senior commercial-fiction editor.
Treat each story independently. Return exactly one output story for each input,
in the same order. Obey every story's required node IDs, choice counts, and
requiredNextNodeId values.

For every story:
- Preserve recognizable setting, character logic, emotional stakes, and genre,
  but write original transformative prose and copy no source dialogue.
- Use second person and present tense. Dramatize immediate pressure rather than
  summarizing plots or explaining game structure.
- Full story decision nodes: 60–105 words; endings: 80–130 words. Mini story
  decision nodes: 35–65 words; endings: 50–80 words.
- Never mention IDs, destination titles, branches, paths, routes, scenes,
  story structure, "both choices lead," "comes either way," or "what comes
  next."
- Choice labels: 4–12 words, grammatical, specific, with an action and motive
  or tradeoff. No one-word labels.
- Consequences: 22–48 words describing an immediate observable outcome. Vary
  openings. Do not use "You choose," "You commit," "the decision," "the
  choice," "who trusts you," or "begins to watch."
- Sibling choices must express different values, risks, information,
  relationships, or resources. Later prose should remember those differences.
- Endings must be distinct and reflect earlier motives without using a repeated
  recap formula.
- Use restraint and dignity around historical trauma, abuse, addiction, mental
  illness, war, and real people. Do not invent post-event biographies for real
  victims or survivors.
""".strip()
    payloads = []
    for story, targets in items:
        payloads.append(editorial.compact_story(story, targets))
    return instructions + "\n\nINPUT STORIES:\n" + json.dumps(
        payloads, ensure_ascii=False
    )


def normalize_redundant_openings(rewrite):
    """Drop only redundant model scaffolding before a concrete result.

    Lite models occasionally prepend "You choose/commit to ..." even when the
    following sentence already contains the observable consequence. Removing
    that first sentence preserves the substantive outcome and avoids replacing
    it with another template.
    """
    pattern = re.compile(
        r"^(?:You choose to|You commit to)[^.!?]*[.!?]\s+(.+)$",
        re.I | re.S,
    )
    for node in rewrite.get("nodes", []):
        for choice in node.get("choices", []):
            consequence = (choice.get("consequence") or "").strip()
            match = pattern.match(consequence)
            if match and editorial.words(match.group(1)) >= 15:
                choice["consequence"] = match.group(1).strip()
    return rewrite


def run_batch(index, model, paths, cache_dir, api_key):
    items = []
    for path in paths:
        story = json.loads(path.read_text())
        items.append((story, editorial.branch_plan(story)))
    last_error = None
    for attempt in range(1, 4):
        try:
            response = editorial.call_gemini(
                batch_prompt(items),
                model,
                api_key,
                grounded=False,
                thinking_level="low" if "pro" in model else "minimal",
                response_schema=BATCH_SCHEMA,
                max_output_tokens=32768,
            )
            break
        except urllib.error.HTTPError as error:
            detail = error.read().decode(errors="replace")
            last_error = f"HTTP {error.code}: {detail}"
            if error.code == 429:
                match = re.search(r"retry in ([0-9.]+)s", detail, re.I)
                editorial.impose_request_cooldown(
                    float(match.group(1)) + 1.0 if match else 30.0
                )
            elif error.code in (500, 502, 503, 504):
                editorial.impose_request_cooldown(5.0 * attempt)
            else:
                raise
    else:
        raise RuntimeError(last_error)
    outputs = response.get("stories", [])
    by_id = {item.get("id"): item for item in outputs}
    accepted = []
    rejected = []
    for story, targets in items:
        rewrite = by_id.get(story["id"])
        if not rewrite:
            rejected.append((story["id"], ["missing from batch output"]))
            continue
        rewrite = normalize_redundant_openings(rewrite)
        errors = editorial.validate_rewrite(story, rewrite, targets)
        if errors:
            rejected.append((story["id"], errors))
            continue
        merged = editorial.merge_rewrite(story, rewrite)
        errors = editorial.graph_errors(merged)
        if errors:
            rejected.append((story["id"], errors))
            continue
        (cache_dir / f"{story['id']}.json").write_text(
            json.dumps(merged, ensure_ascii=False, indent=2) + "\n"
        )
        accepted.append(story["id"])
    with PRINT_LOCK:
        print(
            f"batch={index} model={model} accepted={len(accepted)} "
            f"rejected={len(rejected)}",
            flush=True,
        )
        for story_id, errors in rejected:
            print(
                f"  reject {story_id}: {'; '.join(errors[:5])}",
                flush=True,
            )
    return accepted, [story_id for story_id, _ in rejected]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=editorial.DEFAULT_CACHE,
    )
    parser.add_argument("--batch-size", type=int, default=3)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--max-batches", type=int)
    parser.add_argument(
        "--models",
        nargs="+",
        default=list(DEFAULT_MODELS),
    )
    args = parser.parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY is not configured")

    all_paths = sorted(
        path
        for path in editorial.IOS_CATALOG.glob("*.json")
        if path.name != "index.json"
    )
    pending = [
        path
        for path in all_paths
        if cached_story(path, args.cache_dir) is None
    ]
    batches = [
        pending[index:index + args.batch_size]
        for index in range(0, len(pending), args.batch_size)
    ]
    if args.max_batches is not None:
        batches = batches[:args.max_batches]
    print(
        f"cached={len(all_paths) - len(pending)} pending={len(pending)} "
        f"batches={len(batches)}",
        flush=True,
    )
    model_use = {model: 0 for model in args.models}
    assignments = []
    for index, batch in enumerate(batches, start=1):
        model = min(args.models, key=lambda item: model_use[item])
        if model_use[model] >= 18:
            raise SystemExit("insufficient per-model request budget")
        model_use[model] += 1
        assignments.append((index, model, batch))

    accepted = []
    rejected = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=min(args.workers, len(args.models))
    ) as executor:
        futures = [
            executor.submit(
                run_batch,
                index,
                model,
                batch,
                args.cache_dir,
                api_key,
            )
            for index, model, batch in assignments
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                batch_accepted, batch_rejected = future.result()
                accepted.extend(batch_accepted)
                rejected.extend(batch_rejected)
            except Exception as error:
                rejected.append(f"batch-error:{error}")
                print(f"batch failed: {error}", flush=True)

    print(
        f"accepted={len(accepted)} rejected={len(rejected)} "
        f"cache_total={len(list(args.cache_dir.glob('*.json')))}",
        flush=True,
    )
    if rejected:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
