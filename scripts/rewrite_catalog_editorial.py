#!/usr/bin/env python3
"""Story-by-story editorial rewrite with structural safety checks.

The script uses the configured Gemini API to rewrite reader-facing copy while
preserving metadata and node identity. It supplies an acyclic branch plan,
validates the structured response, caches approved payloads, and writes the
same result to the iOS and Android catalogs only when ``--apply`` is present.

Examples:
    python3 scripts/rewrite_catalog_editorial.py --story fm-the-matrix
    python3 scripts/rewrite_catalog_editorial.py --all --workers 3
    python3 scripts/rewrite_catalog_editorial.py --all --workers 3 --apply
"""

import argparse
import concurrent.futures
import hashlib
import json
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IOS_CATALOG = ROOT / "StoryTime2.0" / "Resources" / "Catalog"
ANDROID_CATALOG = (
    ROOT / "StoryTimeAndroid" / "app" / "src" / "main" / "assets" / "Catalog"
)
DEFAULT_CACHE = Path("/tmp/storytime-editorial-rewrite-v2")
WORD_RE = re.compile(r"\b[\w]+(?:[’'-][\w]+)*\b", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
PRINT_LOCK = threading.Lock()
REQUEST_LOCK = threading.Lock()
NEXT_REQUEST_AT = 0.0
COOLDOWN_UNTIL = 0.0
MIN_REQUEST_INTERVAL_SECONDS = 3.2

PROSE_BANS = (
    "both choices lead",
    "comes either way",
    "what comes next",
    "the story records",
)

CONSEQUENCE_BANS = (
    "what comes next",
    "begins to watch",
)

SENSITIVE_STORIES = {
    "black-swan-the-role",
    "dahmer-the-neighbor",
    "euphoria-the-meeting",
    "fb-beloved",
    "fm-american-history-x",
    "fm-grave-of-fireflies",
    "fm-saving-private-ryan",
    "fm-schindlers-list",
    "house-of-dynamite-eighteen",
    "speak-no-evil-the-weekend",
    "tell-me-lies-the-friendship",
    "zero-day-the-network",
}

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "nodes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "text": {"type": "string"},
                    "choices": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "consequence": {"type": "string"},
                                "nextNodeId": {"type": "string"},
                            },
                            "required": ["text", "consequence", "nextNodeId"],
                        },
                    },
                },
                "required": ["id", "text", "choices"],
            },
        },
    },
    "required": ["id", "nodes"],
}


def words(value):
    return len(WORD_RE.findall(value or ""))


def normalized(value):
    return " ".join(value.casefold().split())


def stable_rank(*parts):
    return int.from_bytes(
        hashlib.sha256("\0".join(parts).encode()).digest()[:4], "big"
    )


def branch_plan(story):
    decisions = [node for node in story["nodes"] if node.get("choices")]
    endings = [node for node in story["nodes"] if not node.get("choices")]
    if not decisions or not endings:
        raise ValueError(f"{story['id']}: needs decisions and endings")

    targets = {}
    for index, node in enumerate(decisions):
        choice_count = len(node["choices"])
        if index == len(decisions) - 1:
            pool = [ending["id"] for ending in endings]
        else:
            pool = [decisions[index + 1]["id"]]
            if index + 2 < len(decisions):
                pool.append(decisions[index + 2]["id"])
            if index + 3 < len(decisions):
                pool.append(decisions[index + 3]["id"])
        targets[node["id"]] = [
            pool[choice_index % len(pool)] for choice_index in range(choice_count)
        ]

    # Guarantee every ending is reachable without breaking the choice-0 chain
    # that makes every decision node reachable.
    slots = []
    for node in reversed(decisions):
        for choice_index in range(len(node["choices"]) - 1, 0, -1):
            slots.append((node["id"], choice_index))
    last = decisions[-1]
    for choice_index in range(len(last["choices"])):
        slot = (last["id"], choice_index)
        if slot not in slots:
            slots.append(slot)
    if len(slots) < len(endings):
        raise ValueError(f"{story['id']}: insufficient tail choices for endings")
    for ending, (node_id, choice_index) in zip(endings, slots):
        targets[node_id][choice_index] = ending["id"]
    return targets


def compact_story(story, targets):
    return {
        "id": story["id"],
        "title": story["title"],
        "sourceTitle": story.get("sourceTitle"),
        "kind": story.get("kind"),
        "genre": story.get("genre"),
        "tags": story.get("tags", []),
        "synopsis": story.get("synopsis"),
        "nodes": [
            {
                "id": node["id"],
                "sceneTitle": node.get("sceneTitle"),
                "endingTitle": node.get("endingTitle"),
                "isEnding": node.get("isEnding", False),
                "currentText": node.get("text", ""),
                "choices": [
                    {
                        "currentText": choice.get("text", ""),
                        "currentConsequence": choice.get("consequence", ""),
                        "requiredNextNodeId": targets[node["id"]][choice_index],
                    }
                    for choice_index, choice in enumerate(node.get("choices", []))
                ],
            }
            for node in story["nodes"]
        ],
    }


def prompt_for(story, targets, retry_feedback=None):
    mini = "mini" in (story.get("tags") or [])
    scene_range = "35–65" if mini else "60–105"
    ending_range = "50–80" if mini else "80–130"
    payload = json.dumps(compact_story(story, targets), ensure_ascii=False)
    feedback = ""
    if retry_feedback:
        feedback = (
            "\nA previous response was rejected for these exact reasons. "
            "Correct every one:\n- " + "\n- ".join(retry_feedback[:20]) + "\n"
        )
    return f"""
You are the senior interactive-fiction editor for a polished commercial
reading app. Rewrite the complete story below. Return only the schema fields.

Editorial requirements:
- Keep every node ID and node order exactly. Keep the exact number of choices
  in every node. Use every requiredNextNodeId exactly as nextNodeId.
- Write original transformative prose; do not copy dialogue from the source.
- Preserve recognizable setting, character logic, emotional stakes, and genre
  voice using the supplied material. Do not invent factual claims about real
  victims or historical events.
- Node prose must use second person, present tense, and dramatize an immediate
  situation rather than summarize a film or explain game structure.
- Decision-node prose should be {scene_range} words. Ending prose should be
  {ending_range} words. Favor specific sensory details, character reactions,
  subtext, and a concrete pressure that makes the decision difficult.
- Never mention node IDs, destination titles, branches, paths, routes, scenes,
  story structure, or phrases such as "both choices lead" and "comes either
  way."
- Choice labels must be 4–12 words, specific, grammatical, and express both an
  action and an intention or tradeoff. Avoid one-word labels.
- Consequences must be 22–48 words. Describe an immediate observable result
  that naturally sets up the required destination without naming it.
- Vary consequence openings. Do not use abstract scaffolding such as "You
  choose," "You commit," "the decision," "the choice," "what comes next,"
  "who trusts you," or "begins to watch."
- Sibling choices must feel materially different in values, risk, information,
  relationships, or resources. Carry those differences into later node prose
  where possible even when branches reconverge.
- Endings must explicitly reflect earlier motives and feel meaningfully
  distinct from sibling endings.
- Comedy should earn jokes through character and situation. Horror should use
  concrete dread rather than generic darkness. Romance should emphasize
  subtext and agency. Historical trauma, addiction, abuse, and real people
  require restraint, dignity, and no gamified victim-blaming.
{feedback}
Story and required branch plan:
{payload}
""".strip()


def wait_for_request_slot():
    global NEXT_REQUEST_AT
    with REQUEST_LOCK:
        now = time.monotonic()
        slot = max(now, NEXT_REQUEST_AT, COOLDOWN_UNTIL)
        NEXT_REQUEST_AT = slot + MIN_REQUEST_INTERVAL_SECONDS
    delay = slot - time.monotonic()
    if delay > 0:
        time.sleep(delay)


def impose_request_cooldown(seconds):
    global COOLDOWN_UNTIL, NEXT_REQUEST_AT
    with REQUEST_LOCK:
        until = time.monotonic() + max(1.0, seconds)
        COOLDOWN_UNTIL = max(COOLDOWN_UNTIL, until)
        NEXT_REQUEST_AT = max(NEXT_REQUEST_AT, COOLDOWN_UNTIL)


def call_gemini(
    prompt,
    model,
    api_key,
    grounded=False,
    thinking_level="low",
    response_schema=None,
    max_output_tokens=16384,
):
    endpoint = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.9,
            "topP": 0.95,
            "maxOutputTokens": max_output_tokens,
            "responseMimeType": "application/json",
            "responseSchema": response_schema or RESPONSE_SCHEMA,
        },
    }
    if model.startswith("gemini-3"):
        body["generationConfig"]["thinkingConfig"] = {
            "thinkingLevel": thinking_level
        }
    if grounded:
        body["tools"] = [{"google_search": {}}]
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    wait_for_request_slot()
    with urllib.request.urlopen(request, timeout=240) as response:
        result = json.loads(response.read())
    try:
        parts = result["candidates"][0]["content"]["parts"]
        text = "".join(part.get("text", "") for part in parts if part.get("text"))
    except (KeyError, IndexError) as error:
        raise ValueError(f"unexpected Gemini response: {result}") from error
    return json.loads(text)


def graph_errors(story):
    nodes = story["nodes"]
    by_id = {node["id"]: node for node in nodes}
    start = story["startNodeId"]
    reachable = set()
    frontier = [start]
    while frontier:
        node_id = frontier.pop()
        if node_id in reachable or node_id not in by_id:
            continue
        reachable.add(node_id)
        frontier.extend(
            choice["nextNodeId"] for choice in by_id[node_id].get("choices", [])
        )
    errors = []
    missing = set(by_id) - reachable
    if missing:
        errors.append(f"unreachable nodes: {sorted(missing)}")
    for node in nodes:
        for choice in node.get("choices", []):
            if choice["nextNodeId"] not in by_id:
                errors.append(
                    f"{node['id']}: missing target {choice['nextNodeId']}"
                )
    return errors


def validate_rewrite(original, rewrite, targets):
    errors = []
    original_ids = [node["id"] for node in original["nodes"]]
    output_ids = [node.get("id") for node in rewrite.get("nodes", [])]
    if rewrite.get("id") != original["id"]:
        errors.append("story id changed")
    if output_ids != original_ids:
        errors.append("node IDs or order changed")
        return errors

    mini = "mini" in (original.get("tags") or [])
    scene_min = 28 if mini else 45
    ending_min = 38 if mini else 55
    seen_sentences = {}
    missing_second_person = []
    for source, edited in zip(original["nodes"], rewrite["nodes"]):
        text = (edited.get("text") or "").strip()
        minimum = ending_min if not source.get("choices") else scene_min
        if words(text) < minimum:
            errors.append(
                f"{source['id']}: text has {words(text)} words, minimum {minimum}"
            )
        if words(text) > 145:
            errors.append(f"{source['id']}: text exceeds 145 words")
        lowered = text.casefold()
        for phrase in PROSE_BANS:
            if phrase in lowered:
                errors.append(f"{source['id']}: banned prose phrase {phrase!r}")
        if not re.search(r"\b(you|your|you’re|you've|you’ll|yourself)\b", text, re.I):
            missing_second_person.append(source["id"])
        for sentence in SENTENCE_RE.split(text):
            key = normalized(sentence)
            if words(key) < 8:
                continue
            if key in seen_sentences:
                errors.append(
                    f"{source['id']}: repeats sentence from {seen_sentences[key]}"
                )
            seen_sentences[key] = source["id"]

        source_choices = source.get("choices", [])
        edited_choices = edited.get("choices", [])
        if len(source_choices) != len(edited_choices):
            errors.append(f"{source['id']}: choice count changed")
            continue
        sibling_labels = set()
        sibling_consequences = set()
        for index, choice in enumerate(edited_choices):
            label = (choice.get("text") or "").strip()
            consequence = (choice.get("consequence") or "").strip()
            label_words = words(label)
            consequence_words = words(consequence)
            if not 3 <= label_words <= 14:
                errors.append(
                    f"{source['id']}/choice-{index}: label has "
                    f"{label_words} words"
                )
            if not 14 <= consequence_words <= 60:
                errors.append(
                    f"{source['id']}/choice-{index}: consequence has "
                    f"{consequence_words} words"
                )
            if choice.get("nextNodeId") != targets[source["id"]][index]:
                errors.append(
                    f"{source['id']}/choice-{index}: target changed from plan"
                )
            lowered_consequence = consequence.casefold()
            for phrase in CONSEQUENCE_BANS:
                if phrase in lowered_consequence:
                    errors.append(
                        f"{source['id']}/choice-{index}: banned consequence "
                        f"phrase {phrase!r}"
                    )
            if normalized(label) in sibling_labels:
                errors.append(f"{source['id']}: repeated sibling label")
            if normalized(consequence) in sibling_consequences:
                errors.append(f"{source['id']}: repeated sibling consequence")
            sibling_labels.add(normalized(label))
            sibling_consequences.add(normalized(consequence))
    if len(missing_second_person) > max(2, len(original["nodes"]) // 4):
        errors.append(
            "second-person voice missing from too many nodes: "
            + ", ".join(missing_second_person[:10])
        )
    return errors


def merge_rewrite(original, rewrite):
    merged = json.loads(json.dumps(original))
    for target_node, edited_node in zip(merged["nodes"], rewrite["nodes"]):
        target_node["text"] = edited_node["text"].strip()
        for target_choice, edited_choice in zip(
            target_node.get("choices", []), edited_node.get("choices", [])
        ):
            target_choice["text"] = edited_choice["text"].strip()
            target_choice["consequence"] = edited_choice["consequence"].strip()
            target_choice["nextNodeId"] = edited_choice["nextNodeId"]
    return merged


def process_story(path, args, api_key):
    story = json.loads(path.read_text())
    targets = branch_plan(story)
    cache_path = args.cache_dir / f"{story['id']}.json"
    if cache_path.exists() and not args.force:
        cached = json.loads(cache_path.read_text())
        cached_rewrite = {
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
        errors = validate_rewrite(story, cached_rewrite, targets)
        errors.extend(graph_errors(cached))
        if errors:
            cache_path.unlink()
        else:
            return story["id"], cached, "cached"

    feedback = None
    last_error = None
    for attempt in range(1, args.retries + 1):
        try:
            rewrite = call_gemini(
                prompt_for(story, targets, feedback),
                args.model,
                api_key,
                grounded=(
                    story["id"] in SENSITIVE_STORIES
                    and not args.no_grounding
                ),
                thinking_level=args.thinking_level,
            )
            errors = validate_rewrite(story, rewrite, targets)
            if errors:
                feedback = errors
                last_error = "; ".join(errors[:8])
                with PRINT_LOCK:
                    print(
                        f"RETRY {story['id']} attempt {attempt}: "
                        f"{last_error}",
                        flush=True,
                    )
                continue
            merged = merge_rewrite(story, rewrite)
            errors = graph_errors(merged)
            if errors:
                feedback = errors
                last_error = "; ".join(errors)
                with PRINT_LOCK:
                    print(
                        f"RETRY {story['id']} attempt {attempt}: "
                        f"{last_error}",
                        flush=True,
                    )
                continue
            cache_path.write_text(
                json.dumps(merged, ensure_ascii=False, indent=2) + "\n"
            )
            return story["id"], merged, f"generated attempt {attempt}"
        except urllib.error.HTTPError as error:
            detail = error.read().decode(errors="replace")
            last_error = f"HTTP {error.code}: {detail}"
            if error.code not in (429, 500, 502, 503, 504):
                break
            if error.code == 429:
                match = re.search(r"retry in ([0-9.]+)s", detail, re.I)
                cooldown = float(match.group(1)) + 1.0 if match else 30.0
                impose_request_cooldown(cooldown)
            else:
                impose_request_cooldown(min(30, (2 ** attempt) + random.random()))
        except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as error:
            last_error = str(error)
            time.sleep(min(15, attempt * 2))
    raise RuntimeError(f"{story['id']}: {last_error}")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--story")
    group.add_argument("--all", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--model", default="gemini-3.6-flash")
    parser.add_argument(
        "--thinking-level",
        choices=("minimal", "low", "medium", "high"),
        default="low",
    )
    parser.add_argument("--no-grounding", action="store_true")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY is not configured")
    args.cache_dir.mkdir(parents=True, exist_ok=True)

    paths = sorted(
        path for path in IOS_CATALOG.glob("*.json") if path.name != "index.json"
    )
    if args.story:
        paths = [path for path in paths if path.stem == args.story]
        if not paths:
            raise SystemExit(f"unknown story id: {args.story}")

    failures = []
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max(1, args.workers)
    ) as executor:
        future_paths = {
            executor.submit(process_story, path, args, api_key): path
            for path in paths
        }
        for future in concurrent.futures.as_completed(future_paths):
            path = future_paths[future]
            try:
                story_id, rewritten, status = future.result()
                if args.apply:
                    encoded = (
                        json.dumps(rewritten, ensure_ascii=False, indent=2) + "\n"
                    )
                    (IOS_CATALOG / f"{story_id}.json").write_text(encoded)
                    (ANDROID_CATALOG / f"{story_id}.json").write_text(encoded)
                completed += 1
                with PRINT_LOCK:
                    print(
                        f"[{completed}/{len(paths)}] {story_id}: {status}",
                        flush=True,
                    )
            except Exception as error:
                failures.append(f"{path.stem}: {error}")
                with PRINT_LOCK:
                    print(f"FAILED {path.stem}: {error}", file=sys.stderr, flush=True)

    print(
        f"completed={completed} failed={len(failures)} "
        f"apply={args.apply} cache={args.cache_dir}"
    )
    if failures:
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
