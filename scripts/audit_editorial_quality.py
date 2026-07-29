#!/usr/bin/env python3
"""Audit StoryTime prose for editorial risks that graph validation cannot see.

This complements ``validate_catalog.py``. It checks reader-facing word counts,
short passages, repeated/formulaic language, sibling-choice differentiation,
and choice-to-destination integrity. It does not attempt to judge factual or
franchise accuracy; those findings still require a human read.

Usage:
    python3 scripts/audit_editorial_quality.py
    python3 scripts/audit_editorial_quality.py --strict
    python3 scripts/audit_editorial_quality.py --report EDITORIAL_AUDIT.md
"""

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_CATALOG = (
    Path(__file__).resolve().parent.parent
    / "StoryTime2.0"
    / "Resources"
    / "Catalog"
)
WORD_RE = re.compile(r"\b[\w]+(?:[’'-][\w]+)*\b", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")

# These are known scaffolding phrases, not legitimate house style.
FORMULAIC_PHRASES = (
    "There is no taking “",
    "The decision settles the question for now.",
    "The choice lands, and the scene changes around it.",
    "You let the choice stand.",
    "The story records the instinct as",
    "marked by one lasting impulse:",
    "Both choices lead to",
    "comes either way; its meaning changes",
    "is already waiting. What changes is whether",
    "You cannot avoid",
    "The road still runs toward",
    "will follow either decision",
    "The paths divide here:",
    "opens the route to",
    "The distance between",
    "You choose to",
    "You commit to",
)


def word_count(value):
    return len(WORD_RE.findall(str(value or "")))


def normalized_sentence(value):
    return " ".join(value.casefold().strip(" “”—\t\r\n").split())


def load_stories(catalog):
    stories = []
    for path in sorted(catalog.glob("*.json")):
        if path.name == "index.json":
            continue
        stories.append((path, json.loads(path.read_text())))
    return stories


def audit(catalog):
    stories = load_stories(catalog)
    errors = []
    warnings = []
    rows = []
    narrative_sentences = defaultdict(list)
    consequences = defaultdict(list)

    for path, story in stories:
        story_id = story.get("id", path.stem)
        title = story.get("title", story_id)
        nodes = story.get("nodes", [])
        node_ids = {node.get("id") for node in nodes}
        is_mini = "mini" in (story.get("tags") or [])
        scene_word_floor = 18 if is_mini else 35
        story_word_floor = 450 if is_mini else 600
        narrative_words = 0
        choice_words = 0
        story_sentence_locations = defaultdict(list)
        short_scenes = []
        short_consequences = []
        missing_second_person = []
        one_word_labels = []
        convergent_nodes = []
        formulaic_hits = []

        for node in nodes:
            node_id = node.get("id", "<missing>")
            scene = node.get("sceneTitle") or node_id
            text = (node.get("text") or "").strip()
            text_words = word_count(text)
            narrative_words += text_words
            if text_words < scene_word_floor:
                short_scenes.append(f"{node_id} ({text_words})")
            if not re.search(
                r"\b(you|your|you’re|you've|you’ll|yourself)\b",
                text,
                re.I,
            ):
                missing_second_person.append(node_id)

            for sentence in SENTENCE_RE.split(text):
                normalized = normalized_sentence(sentence)
                if word_count(normalized) < 8:
                    continue
                location = f"{story_id}/{node_id}"
                narrative_sentences[normalized].append(location)
                story_sentence_locations[normalized].append(location)

            for phrase in FORMULAIC_PHRASES:
                if phrase.casefold() in text.casefold():
                    formulaic_hits.append(f"{node_id}: {phrase!r}")

            choices = node.get("choices", [])
            if choices and len({choice.get("nextNodeId") for choice in choices}) == 1:
                convergent_nodes.append(node_id)
            sibling_consequences = Counter(
                normalized_sentence(choice.get("consequence", ""))
                for choice in choices
            )
            if any(value and count > 1 for value, count in sibling_consequences.items()):
                errors.append(
                    f"{story_id}/{node_id}: sibling choices repeat a consequence"
                )

            for choice_index, choice in enumerate(choices, start=1):
                label = (choice.get("text") or "").strip()
                consequence = (choice.get("consequence") or "").strip()
                target = choice.get("nextNodeId")
                choice_words += word_count(label) + word_count(consequence)
                if word_count(label) == 1:
                    one_word_labels.append(f"{node_id}/choice-{choice_index}")
                if target not in node_ids:
                    errors.append(
                        f"{story_id}/{node_id}/choice-{choice_index}: "
                        f"missing destination {target!r}"
                    )
                if word_count(consequence) < 10:
                    short_consequences.append(
                        f"{node_id}/choice-{choice_index} "
                        f"({word_count(consequence)})"
                    )
                for phrase in FORMULAIC_PHRASES:
                    if phrase.casefold() in consequence.casefold():
                        formulaic_hits.append(
                            f"{node_id}/choice-{choice_index}: {phrase!r}"
                        )
                normalized = normalized_sentence(consequence)
                if normalized:
                    consequences[normalized].append(
                        f"{story_id}/{node_id}/choice-{choice_index}"
                    )

        for sentence, locations in story_sentence_locations.items():
            if len(locations) > 1:
                warnings.append(
                    f"{story_id}: repeated narrative sentence in "
                    f"{len(locations)} scenes: {sentence[:100]!r}"
                )

        reader_words = narrative_words + choice_words
        if short_scenes:
            warnings.append(
                f"{story_id}: {len(short_scenes)} scene passage(s) below "
                f"{scene_word_floor} words: {', '.join(short_scenes[:8])}"
                + (" ..." if len(short_scenes) > 8 else "")
            )
        if short_consequences:
            warnings.append(
                f"{story_id}: {len(short_consequences)} consequence(s) below "
                f"10 words: {', '.join(short_consequences[:8])}"
                + (" ..." if len(short_consequences) > 8 else "")
            )
        if formulaic_hits:
            warnings.append(
                f"{story_id}: {len(formulaic_hits)} formulaic passage(s): "
                f"{', '.join(formulaic_hits[:8])}"
                + (" ..." if len(formulaic_hits) > 8 else "")
            )
        if len(missing_second_person) > max(2, len(nodes) // 4):
            warnings.append(
                f"{story_id}: second-person voice missing from "
                f"{len(missing_second_person)} node(s): "
                f"{', '.join(missing_second_person[:8])}"
                + (" ..." if len(missing_second_person) > 8 else "")
            )
        if one_word_labels:
            warnings.append(
                f"{story_id}: {len(one_word_labels)} one-word choice label(s): "
                f"{', '.join(one_word_labels[:8])}"
                + (" ..." if len(one_word_labels) > 8 else "")
            )
        decision_count = sum(1 for node in nodes if node.get("choices"))
        if (
            decision_count
            and len(convergent_nodes) / decision_count > 0.5
        ):
            warnings.append(
                f"{story_id}: {len(convergent_nodes)}/{decision_count} "
                "decision nodes immediately converge"
            )
        if reader_words < story_word_floor:
            warnings.append(f"{story_id}: only {reader_words} reader-facing words")
        elif reader_words > 4500:
            warnings.append(f"{story_id}: {reader_words} reader-facing words")
        rows.append(
            {
                "id": story_id,
                "title": title,
                "kind": story.get("kind", "unknown"),
                "narrative": narrative_words,
                "choices": choice_words,
                "total": reader_words,
            }
        )

    repeated_sentences = sorted(
        (
            (len(locations), sentence, locations)
            for sentence, locations in narrative_sentences.items()
            if len(locations) >= 4
        ),
        reverse=True,
    )
    repeated_consequences = sorted(
        (
            (len(locations), consequence, locations)
            for consequence, locations in consequences.items()
            if len(locations) >= 4
        ),
        reverse=True,
    )
    for count, sentence, _ in repeated_sentences:
        warnings.append(
            f"catalog: narrative sentence repeated {count} times: "
            f"{sentence[:120]!r}"
        )
    for count, consequence, _ in repeated_consequences:
        warnings.append(
            f"catalog: consequence repeated {count} times: "
            f"{consequence[:120]!r}"
        )

    return {
        "rows": rows,
        "errors": errors,
        "warnings": warnings,
        "repeated_sentences": repeated_sentences,
        "repeated_consequences": repeated_consequences,
    }


def render_report(result):
    rows = result["rows"]
    totals = [row["total"] for row in rows]
    lines = [
        "# StoryTime Editorial Audit",
        "",
        "Automated editorial QA for the bundled story catalog. Structural",
        "validation remains in `scripts/validate_catalog.py`; plot accuracy,",
        "voice, pacing, and IP review still require human judgment.",
        "",
        "## Summary",
        "",
        f"- Stories: {len(rows)}",
        f"- Reader-facing words: {sum(totals):,}",
        f"- Average words per story: {statistics.mean(totals):,.0f}",
        f"- Median words per story: {statistics.median(totals):,.0f}",
        f"- Automated errors: {len(result['errors'])}",
        f"- Automated warnings: {len(result['warnings'])}",
        "",
        "## Errors",
        "",
    ]
    lines.extend(
        f"- {message}" for message in result["errors"]
    )
    if not result["errors"]:
        lines.append("- None.")

    lines.extend(["", "## Highest-priority warnings", ""])
    lines.extend(
        f"- {message}" for message in result["warnings"][:100]
    )
    if not result["warnings"]:
        lines.append("- None.")

    lines.extend(["", "## Manual review batches", ""])
    sorted_rows = sorted(rows, key=lambda row: row["id"])
    for index in range(0, len(sorted_rows), 20):
        batch = sorted_rows[index:index + 20]
        batch_number = index // 20 + 1
        lines.append(
            f"### Batch {batch_number}: {batch[0]['id']} to {batch[-1]['id']}"
        )
        lines.append("")
        for row in batch:
            lines.append(f"- {row['title']} — {row['total']:,} words")
        lines.append("")

    lines.extend(
        [
            "## Human-review rubric",
            "",
            "- Verify plot, character, setting, and source-title accuracy.",
            "- Read every branch transition and confirm the consequence leads",
            "  naturally into the destination scene.",
            "- Remove repeated sentence shapes and generic dramatic filler.",
            "- Confirm second-person voice, tense, and tone stay consistent.",
            "- Check that sibling choices express meaningfully different values.",
            "- Confirm each ending reflects the decisions that can reach it.",
            "- Review commercial, licensing, and attribution implications.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", nargs="?", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    result = audit(args.catalog)
    rows = result["rows"]
    totals = [row["total"] for row in rows]
    print(
        f"{len(rows)} stories, {sum(totals):,} reader-facing words, "
        f"{len(result['errors'])} error(s), "
        f"{len(result['warnings'])} warning(s)"
    )
    for message in result["errors"]:
        print(f"ERROR: {message}")
    for message in result["warnings"][:25]:
        print(f"WARN: {message}")
    if len(result["warnings"]) > 25:
        print(f"... {len(result['warnings']) - 25} more warning(s)")

    if args.report:
        args.report.write_text(render_report(result))
        print(f"wrote {args.report}")

    if result["errors"] or (args.strict and result["warnings"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
