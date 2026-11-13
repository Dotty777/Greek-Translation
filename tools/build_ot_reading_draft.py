"""Build the complete inherited OT reader with precisely matched, unaccepted overlays.

Run from any directory: python tools/build_ot_reading_draft.py
Only the dated OT edition directory is written. All inputs are checked against
the frozen baseline; new passage reviews are the only allowed text overlays.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from collections import OrderedDict

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
OUT = ROOT / "editions/2026-11-12-ot-reading-draft"
EDITION_ID = "Saints-English-OT-provisional-2026-11-12"
AS_OF = "2026-11-13"
AS_OF_DISPLAY = "13 November 2026"
REVIEW_DIRS = [
    "reviews/2026-11-12-OT-001-genesis-1",
    "reviews/2026-11-12-OT-002-genesis-2-3",
    "reviews/2026-11-12-OT-003-jonah",
    "reviews/2026-11-12-OT-004-genesis-4",
    "reviews/2026-11-12-OT-005-genesis-5-11",
    "reviews/2026-11-12-OT-006-genesis-12-20",
    "reviews/2026-11-12-OT-007-genesis-21-30",
    "reviews/2026-11-12-OT-008-genesis-31-37",
    "reviews/2026-11-12-OT-009-genesis-38-44",
    "reviews/2026-11-12-OT-010-genesis-45-50",
    "reviews/2026-11-12-OT-011-exodus-1-2",
    "reviews/2026-11-12-OT-012-exodus-3-15",
    "reviews/2026-11-12-OT-013-exodus-16-27",
    "reviews/2026-11-12-OT-014-exodus-28-40",
    "reviews/2026-11-12-OT-015-leviticus-1-3",
    "reviews/2026-11-13-OT-016-leviticus-4-7",
    "reviews/2026-11-13-OT-017-leviticus-8-10",
    "reviews/2026-11-13-OT-018-leviticus-11-13",
    "reviews/2026-11-13-OT-019-leviticus-14-15",
    "reviews/2026-11-13-OT-020-leviticus-16-19",
    "reviews/2026-11-13-OT-021-leviticus-20-22",
    "reviews/2026-11-13-OT-022-leviticus-23-24",
    "reviews/2026-11-13-OT-023-leviticus-25-27",
    "reviews/2026-11-13-OT-024-numbers-1-2",
    "reviews/2026-11-13-OT-025-numbers-3-4",
    "reviews/2026-11-13-OT-026-numbers-5-6",
    "reviews/2026-11-13-OT-027-numbers-7",
    "reviews/2026-11-13-OT-028-numbers-8-10",
    "reviews/2026-11-13-OT-029-numbers-11-12",
    "reviews/2026-11-13-OT-030-numbers-13-14",
    "reviews/2026-11-13-OT-031-numbers-15-16",
    "reviews/2026-11-13-OT-032-numbers-17-18",
    "reviews/2026-11-13-OT-033-numbers-19-20",
    "reviews/2026-11-13-OT-034-numbers-21-22",
    "reviews/2026-11-13-OT-035-numbers-23-24",
    "reviews/2026-11-13-OT-036-numbers-25-26",
    "reviews/2026-11-13-OT-037-numbers-27-29",
    "reviews/2026-11-13-OT-038-numbers-30-31",
    "reviews/2026-11-13-OT-039-numbers-32-33",
    "reviews/2026-11-13-OT-040-numbers-34-36",
    "reviews/2026-11-13-OT-041-deuteronomy-1-2",
    "reviews/2026-11-13-OT-042-deuteronomy-3-4",
    "reviews/2026-11-13-OT-043-deuteronomy-5-7",
    "reviews/2026-11-13-OT-044-deuteronomy-8-10",
    "reviews/2026-11-13-OT-045-deuteronomy-11-13",
    "reviews/2026-11-13-OT-046-deuteronomy-14-16",
    "reviews/2026-11-13-OT-047-deuteronomy-17-20",
    "reviews/2026-11-13-OT-048-deuteronomy-21-23",
    "reviews/2026-11-13-OT-049-deuteronomy-24-26",
    "reviews/2026-11-13-OT-050-deuteronomy-27-28",
    "reviews/2026-11-13-OT-051-deuteronomy-29-31",
    "reviews/2026-11-13-OT-052-deuteronomy-32-34",
    "reviews/2026-11-13-OT-053-joshua-1-3",
    "reviews/2026-11-13-OT-054-joshua-4-6",
    "reviews/2026-11-13-OT-055-joshua-7-9",
    "reviews/2026-11-13-OT-056-joshua-10-12",
    "reviews/2026-11-13-OT-057-joshua-13-14",
    "reviews/2026-11-13-OT-058-joshua-15",
    "reviews/2026-11-13-OT-059-joshua-16-18",
    "reviews/2026-11-13-OT-060-joshua-19-20",
    "reviews/2026-11-13-OT-061-joshua-21-22",
    "reviews/2026-11-13-OT-062-joshua-23-24",
]


def sha(data):
    return hashlib.sha256(data.encode("utf-8") if isinstance(data, str) else data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def norm(text):
    return " ".join(text.split())


def has_three_drafts(review):
    return all(isinstance(review.get('drafts', {}).get(stage), str) and review['drafts'][stage].strip()
               for stage in ('close', 'spoken', 'literary'))


def unchanged(path):
    """Compare exact content except Git's Windows checkout CRLF conversion."""
    actual = (ROOT / path).read_bytes()
    expected = git("show", f"{BASELINE}:{path}")
    return actual.replace(b"\r\n", b"\n") == expected.replace(b"\r\n", b"\n")


class LegacyPoetry(HTMLParser):
    """Extract only requested verse paragraphs, excluding numbers and notes."""
    def __init__(self, wanted):
        super().__init__(convert_charrefs=True)
        self.wanted, self.found = wanted, {}
        self.active, self.depth, self.skip, self.parts = None, 0, 0, []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.active is None:
            if tag == "p" and attrs.get("id") in self.wanted:
                self.active = attrs["id"]
                self.depth, self.skip, self.parts = 1, 0, []
            return
        if tag == "br":
            if not self.skip:
                self.parts.append("\n")
            return
        if tag in {"img", "hr", "input", "meta", "link"}:
            return
        self.depth += 1
        if self.skip:
            self.skip += 1
        elif tag == "sup" or (tag == "span" and ("number" in attrs.get("class", "") or "vertical-align:super" in attrs.get("style", ""))):
            self.skip = 1

    def handle_endtag(self, tag):
        if self.active is None or tag == "br":
            return
        if self.skip:
            self.skip -= 1
        self.depth -= 1
        if self.depth == 0:
            self.found[self.active] = "\n".join(norm(x) for x in "".join(self.parts).split("\n")).strip()
            self.active = None

    def handle_data(self, data):
        if self.active is not None and not self.skip:
            self.parts.append(data)


class ReaderParser(HTMLParser):
    """Round-trip the actual reader text and IDs, independent of its renderer."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.texts, self.parts, self.key = [], [], [], None
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if self.key is None and "data-reading-key" in attrs:
            self.key, self.parts, self.depth = attrs["data-reading-key"], [], 1
        elif self.key is not None:
            if tag == "br":
                self.parts.append("\n")
            else:
                self.depth += 1

    def handle_endtag(self, tag):
        if self.key is not None and tag != "br":
            self.depth -= 1
            if self.depth == 0:
                self.texts.append((self.key, "".join(self.parts)))
                self.key = None

    def handle_data(self, data):
        if self.key is not None:
            self.parts.append(data)


def normalize_chapters(data):
    if isinstance(data, dict):
        return data["chapters"], "chapter_container"
    groups = OrderedDict()
    for verse in data:
        groups.setdefault(verse["chapter"], []).append(verse)
    return [{"chapter": chapter, "verses": verses} for chapter, verses in groups.items()], "flat_verse_array"


def load_reviews(required):
    records, sources, missing = [], [], []
    for directory in REVIEW_DIRS:
        path = ROOT / directory / "focused-reviews.json"
        if not path.exists():
            missing.append(directory)
            continue
        content = read_json(path)
        batch = content if isinstance(content, list) else content.get("reviews", content.get("records", content.get("focused_reviews")))
        if not isinstance(batch, list):
            raise ValueError(f"Unknown review container: {path}")
        for review in batch:
            review = copy.deepcopy(review)
            review["evidence_path"] = f"{directory}/focused-reviews.json"
            records.append(review)
        sources.append({"path": f"{directory}/focused-reviews.json", "sha256": sha(path.read_bytes()), "records": len(batch)})
    if required and missing:
        raise ValueError(f"Required review inputs missing: {missing}")
    return records, sources, missing


def build(required=False):
    OUT.mkdir(parents=True, exist_ok=True)
    checks = []

    def check(name, passed, details=None):
        checks.append({"check": name, "passed": bool(passed), "details": details})
        if not passed:
            raise AssertionError(f"{name}: {details}")

    progress = json.loads(git("show", f"{BASELINE}:progress.json"))
    selected = progress["books"][:43]
    check("Exactly the inherited 43 OT books in project order", len(selected) == 43 and selected[0]["book"] == "Genesis" and selected[-1]["book"] == "Malachi")
    reviews, review_sources, missing_reviews = load_reviews(required)
    review_map = {}
    for r in reviews:
        key = (r["book_id"], r["verse_anchor"])
        check(f"Unique review identity {key}", key not in review_map)
        review_map[key] = r

    books, history, inventory, all_units, changes, source_files = [], [], [], [], [], []
    used_reviews = set()
    recovered_poetry = 0
    for item in selected:
        book_id = item["records"].strip("/")
        path = f"{book_id}/verses.json"
        baseline_raw = git("show", f"{BASELINE}:{path}")
        check(f"Frozen inherited Scripture unchanged: {book_id}", unchanged(path))
        raw = baseline_raw
        data = json.loads(raw)
        chapters, schema = normalize_chapters(data)
        wanted_poetry = {v["id"] for c in chapters for v in c["verses"] if "display_text" not in v and v.get("poetic_line_breaks", v.get("line_breaks", 0))}
        poetry = {}
        if wanted_poetry:
            html_paths = list((ROOT / book_id).glob("*.html"))
            check(f"Unique inherited HTML for poetry: {book_id}", len(html_paths) == 1)
            html_path = html_paths[0].relative_to(ROOT).as_posix()
            html_raw = git("show", f"{BASELINE}:{html_path}")
            check(f"Inherited poetry HTML unchanged: {book_id}", unchanged(html_path))
            parser = LegacyPoetry(wanted_poetry)
            parser.feed(html_raw.decode("utf-8-sig"))
            poetry = parser.found
            check(f"Poetry positions recovered: {book_id}", set(poetry) == wanted_poetry)
            source_files.append({"path": html_path, "sha256": sha(html_raw), "use": "Recover recorded poetry breaks only; source wording must match verses.json"})
        division = item["staging_path"].split("/")[2]
        book = {"book_id": book_id, "book": item["book"], "division": division, "original_schema": schema,
                "inherited_metadata": {k: v for k, v in data.items() if k != "chapters"} if isinstance(data, dict) else {}, "chapters": []}
        book_units = []
        for position, chapter in enumerate(chapters, 1):
            section = copy.deepcopy({k: v for k, v in chapter.items() if k != "verses"})
            section_id = f"{book_id}-section-{position}"
            section.update({"reading_section_id": section_id, "position": position,
                            "title": chapter.get("title", f"{item['book']} {chapter['chapter']}"), "verses": []})
            for original in chapter["verses"]:
                reference = original.get("reference", f"{item['book']} {original.get('ref', '')}")
                anchor = original["id"]
                unit_id = f"{section_id}-{anchor}"
                text = original["text"]
                display = original.get("display_text", text).replace("\\n", "\n")
                if anchor in poetry:
                    check(f"Poetry text agrees with JSON {book_id}/{anchor}", norm(poetry[anchor]) == norm(text))
                    display = poetry[anchor]
                    recovered_poetry += 1
                unit = {"unit_id": unit_id, "id": anchor, "reference": reference, "text": text, "display_text": display,
                        "inherited_unit": copy.deepcopy(original), "review_status": "inherited_draft_without_new_comparison",
                        "candidate_sha256": sha(text)}
                key = (book_id, anchor)
                if key in review_map:
                    r = review_map[key]
                    check(f"Review matches frozen commit {key}", r.get("baseline_commit") == BASELINE)
                    check(f"Review matches inherited reading section {key}", str(r.get("reading_section_id")) == str(chapter.get("section", chapter["chapter"])))
                    check(f"Review matches exact inherited reference {key}", r["reference"] == reference)
                    check(f"Review matches exact inherited wording {key}", r["baseline_text"] == text)
                    check(f"Review candidate hash agrees {key}", r["candidate_sha256"] == sha(r["candidate_text"]))
                    changed = r["candidate_text"] != text
                    check(f"Review decision agrees with wording {key}", r.get("decision") == ("propose_revision" if changed else "retain_provisionally"))
                    check(f"Review benchmark flag agrees {key}", bool(r.get("benchmark_change")) == (changed and book_id == 'genesis' and chapter['chapter'] <= 11))
                    check(f"Review records source-access metadata {key}", r.get('source', {}).get('running_text_read') is True and bool(r.get('source', {}).get('url')) and bool(r.get('source', {}).get('accessed_on')))
                    if book_id in ('genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua'):
                        source_code = {'genesis': 'GEN', 'exodus': 'EXO', 'leviticus': 'LEV', 'numbers': 'NUM', 'deuteronomy': 'DEU', 'joshua': 'JOS'}[book_id]
                        check(f"Source locator matches chapter {key}", r['source']['url'].rstrip('/').endswith(f"/LXX/{source_code}.{chapter['chapter']}"))
                    if (chapter['chapter'] >= 4 and book_id == 'genesis') or book_id in ('exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua'):
                        check(f"Continuation has three draft stages {key}", has_three_drafts(r))
                        check(f"Literary stage agrees with candidate {key}", r['drafts']['literary'] == r['candidate_text'])
                    if r.get("review", {}).get("all_tokens_accounted_for"):
                        tokens = r.get("greek_tokens", [])
                        check(f"Token accounting has nonempty unique identities {key}", bool(tokens) and len({t['token_id'] for t in tokens}) == len(tokens))
                        check(f"Each aligned token has a form and realization {key}", all(t.get('form') and t.get('realization_type') and t.get('rationale') and t.get('english_spans') for t in tokens))
                    candidate = r["candidate_text"]
                    unit.update({"text": candidate, "candidate_sha256": sha(candidate), "review_id": r.get("review_id"),
                                 "review_evidence": r["evidence_path"], "review_reading_section_id": r.get("reading_section_id"),
                                 "review_analysis": r.get("analysis", ""), "drafts": r.get("drafts", {}),
                                 "unresolved_questions": r.get("unresolved_questions", []), "source_url": r.get("source", {}).get("url"),
                                 "tokens_accounted_for": bool(r.get("review", {}).get("all_tokens_accounted_for")),
                                 "review_status": "unaccepted_wording_proposal" if candidate != text else "focused_comparison_retained_wording"})
                    if candidate != text:
                        if "\n" in display:
                            check(f"Poetic proposal supplies reviewed line breaks {key}", bool(r.get("candidate_display_text")) and "\n" in r["candidate_display_text"].replace("\\n", "\n"))
                        unit["display_text"] = r.get("candidate_display_text", candidate).replace("\\n", "\n")
                        check(f"Proposal display agrees with candidate text {key}", norm(unit["display_text"]) == norm(candidate))
                        changes.append({"book_id": book_id, "reading_section_id": section_id, "verse_anchor": anchor, "reference": reference,
                                        "baseline_text": text, "candidate_text": candidate, "candidate_sha256": sha(candidate),
                                        "benchmark_proposal": book_id == "genesis" and chapter["chapter"] <= 11,
                                        "editorial_acceptance": "pending", "evidence": r["evidence_path"],
                                        "rationale": r.get("analysis", r.get("rationale", "See the focused review record."))})
                    if "candidate_display_text" in r:
                        unit["display_text"] = r["candidate_display_text"].replace("\\n", "\n")
                        check(f"Reviewed display preserves candidate wording {key}", norm(unit["display_text"]) == norm(candidate))
                        if not changed and unit["display_text"] != display:
                            unit["display_review_note"] = "Poetic line breaks proposed by AI from the selected Greek clause parallels; wording retained and editorial acceptance pending."
                    used_reviews.add(key)
                check(f"Nonempty inherited and candidate text {book_id}/{anchor}", bool(text.strip()) and bool(unit["text"].strip()))
                unit["continuation_paragraphs"] = copy.deepcopy(original.get("continuation_paragraphs", []))
                section["verses"].append(unit)
                all_units.append(unit)
                book_units.append(unit)
            book["chapters"].append(section)
        books.append(book)
        source_files.append({"path": path, "sha256": sha(raw), "git_blob": git("rev-parse", f"{BASELINE}:{path}").decode().strip(), "use": "Inherited English Scripture and passage identities"})
        source_path = f"{book_id}/source-checks.json"
        source_raw = git("show", f"{BASELINE}:{source_path}")
        check(f"Source history unchanged: {book_id}", unchanged(source_path))
        source_files.append({"path": source_path, "sha256": sha(source_raw), "use": "Historical source claims; not newly certified"})
        history.append({"book_id": book_id, "book": item["book"], "source_record": source_path, "source_sha256": sha(source_raw),
                        "baseline_commit": BASELINE, "inherited_source_checks": json.loads(source_raw),
                        "new_review_claim": "Only the separately linked OT review records establish new comparison scope."})
        inventory.append({"book_id": book_id, "book": item["book"], "division": division, "reading_sections": len(chapters),
                          "stored_units": len(book_units), "continuation_paragraphs": sum(len(v["continuation_paragraphs"]) for v in book_units),
                          "fresh_focused_comparison_units": sum(v["review_status"] != "inherited_draft_without_new_comparison" for v in book_units),
                          "proposed_changed_units": sum(v["review_status"] == "unaccepted_wording_proposal" for v in book_units),
                          "token_aligned_units": sum(r.get("review", {}).get("all_tokens_accounted_for", False) for r in reviews if r["book_id"] == book_id),
                          "three_stage_draft_units": sum(has_three_drafts(r) for r in reviews if r["book_id"] == book_id),
                          "verse_path": path, "source_record": source_path, "original_schema": schema})

    check("Every supplied review maps to exactly one OT unit", used_reviews == set(review_map), list(set(review_map) - used_reviews))
    check("26,580 stored OT units preserved", len(all_units) == 26580)
    check("Unique scoped unit IDs", len({v["unit_id"] for v in all_units}) == len(all_units))
    continuations = sum(len(v["continuation_paragraphs"]) for v in all_units)
    check("All seven continuation paragraphs preserved", continuations == 7)
    esther = next(b for b in books if b["book_id"] == "esther")
    check("Esther six attached continuations preserved", sum(len(v["continuation_paragraphs"]) for c in esther["chapters"] for v in c["verses"]) == 6)
    psalms = next(b for b in books if b["book_id"] == "psalms")
    check("Psalm 151 retained", psalms["chapters"][-1]["chapter"] == 151)
    daniel = next(b for b in books if b["book_id"] == "daniel")
    check("Daniel preface and both additions retained", any(v["id"] == "v5-preface" for c in daniel["chapters"] for v in c["verses"]) and len(daniel["chapters"]) == 14)
    sirach = next(b for b in books if b["book_id"] == "sirach")
    check("Sirach prologue retained as distinct section", sirach["chapters"][0]["chapter"] == 0 and len(sirach["chapters"]) == 52)
    proverbs = next(b for b in books if b["book_id"] == "proverbs")
    check("Proverbs 34 sections retain inherited reading order", len(proverbs["chapters"]) == 34 and [c["chapter"] for c in proverbs["chapters"][-10:]] == [30, 24, 30, 31, 25, 26, 27, 28, 29, 31])
    nt_paths = [b["records"] for b in progress["books"][43:]] + ["editions/2026-11-12-nt-reading-draft", "reviews/2026-11-12-GT-003-john-1-1-18"]
    nt_diff = git("diff", "--name-only", BASELINE, "--", *nt_paths).decode().strip()
    check("Existing NT Scripture and review edition unchanged", not nt_diff, nt_diff or "No tracked differences against the baseline")

    counts = {"books": 43, "reading_sections": sum(b["reading_sections"] for b in inventory), "stored_units": len(all_units),
              "attached_continuation_paragraphs": continuations, "reading_paragraphs_including_continuations": len(all_units) + continuations,
              "fresh_focused_comparison_units": len(used_reviews), "inherited_without_new_comparison": len(all_units) - len(used_reviews),
              "proposed_changed_units": len(changes), "retained_after_focused_comparison": len(used_reviews) - len(changes),
              "new_token_aligned_units": sum(bool(r.get("review", {}).get("all_tokens_accounted_for")) for r in reviews),
              "aligned_source_tokens": sum(len(r.get("greek_tokens", [])) for r in reviews if r.get("review", {}).get("all_tokens_accounted_for")),
              "three_stage_draft_units": sum(has_three_drafts(r) for r in reviews),
              "independently_reviewed_units": 0, "human_read_aloud_units": 0, "new_editorially_accepted_units": 0,
              "recovered_poetry_units": recovered_poetry}
    manifest = {"edition_id": EDITION_ID, "title": "Bespoke Saints English — Complete Old Testament Reading Draft", "date": "2026-11-12", "updated": AS_OF,
                "baseline_repository": "https://github.com/Dotty777/Greek-Translation", "baseline_commit": BASELINE,
                "status": "complete_inherited_reading_manuscript_with_provisional_comparison_candidates",
                "scope": "All 43 selected Old Testament books only. Existing project selection, order, source histories and exceptional units preserved.",
                "source_policy": "Rahlfs–Hanhart 2006 provisional base with inherited book-specific records; Daniel uses Old Greek. No new Göttingen or full apparatus collation claimed.",
                "authorship": "Inherited Saints English manuscript plus separately evidenced AI candidate proposals. Not 26,580 freshly translated or independently reviewed units.",
                "counts": counts, "counting_policy": "Token-aligned units are a subset of the running-text comparison count, not an additional group. Three-stage drafts may deliberately retain the same wording; they do not credit human reading or acceptance.", "book_inventory": inventory, "review_inputs": review_sources, "missing_planned_review_inputs": missing_reviews,
                "source_files": source_files, "website_deployed": False,
                "remaining": ["Complete source-led comparison and word accounting across every OT unit", "Specialist lexical and textual decisions", "Relevant apparatus and Göttingen consultation", "Independent Greek review", "Human read-aloud review", "Editorial acceptance", "Separately authorized, verified publication"]}
    edition = {"edition_id": EDITION_ID, "baseline_commit": BASELINE, "status": manifest["status"], "counts": counts,
               "reading_notice": "Provisional manuscript. Focused comparisons and changed candidates are marked; all other text is inherited. Original accepted Genesis benchmark remains intact.", "books": books}
    write_json("old-testament.json", edition)
    write_json("manifest.json", manifest)
    write_json("source-history.json", {"baseline_commit": BASELINE, "notice": "Inherited historical records preserved verbatim as JSON values; not a newly certified full Greek audit.", "books": history})
    write_json("changes.json", {"status": "unaccepted_proposals", "changes": changes})
    write_change_ledger(changes)
    render_reader(edition, inventory)
    render_text(edition)
    # Round-trip the written files, rather than trusting generation alone.
    parsed = read_json(OUT / "old-testament.json")
    check("JSON file round-trips all inherited records and candidates", parsed == edition)
    expected = [(v["unit_id"], v["display_text"]) for b in books for c in b["chapters"] for v in c["verses"]]
    expected_with_cont = []
    for b in books:
        for c in b["chapters"]:
            for v in c["verses"]:
                expected_with_cont.append((v["unit_id"], v["display_text"]))
                expected_with_cont.extend((f"{v['unit_id']}-continuation-{i}", t) for i, t in enumerate(v["continuation_paragraphs"], 1))
    parser = ReaderParser()
    parser.feed((OUT / "Saints-English-Old-Testament.html").read_text(encoding="utf-8"))
    check("HTML exact ordered display text including every continuation", parser.texts == expected_with_cont)
    check("HTML IDs are globally unique", len(parser.ids) == len(set(parser.ids)))
    txt = (OUT / "Saints-English-Old-Testament.txt").read_text(encoding="utf-8")
    txt_parts = re.findall(r"^\[UNIT ([^\]]+)\]\n[^\n]*\n(.*?)\n\[/UNIT\]$", txt, re.M | re.S)
    check("TXT exact ordered display text including every continuation", txt_parts == expected_with_cont)
    check("Every candidate text hash rechecks", all(v["candidate_sha256"] == sha(v["text"]) for v in all_units))
    check("Original Genesis 1–11 benchmark Git content untouched", unchanged("genesis/verses.json"))
    write_readme(counts, missing_reviews)
    # Group routine per-unit checks, retaining failures as hard errors above.
    summary = [{"check": prefix, "passed": True, "cases": sum(c["check"].startswith(prefix) for c in checks)} for prefix in
               ["Unique review identity", "Review matches frozen commit", "Review matches inherited reading section", "Review matches exact inherited reference", "Review matches exact inherited wording", "Review candidate hash agrees", "Review decision agrees", "Review benchmark flag agrees", "Review records source-access metadata", "Source locator matches chapter", "Continuation has three draft stages", "Literary stage agrees with candidate", "Nonempty inherited and candidate text", "Poetry text agrees with JSON"]]
    compact_checks = [c for c in checks if not any(c["check"].startswith(s["check"]) for s in summary)] + [s for s in summary if s["cases"]]
    write_json("validation.json", {"status": "passed", "date": AS_OF, "counts": counts, "checks": compact_checks,
                                   "limits": "Structural/content checks and AI passage comparisons only; not independent Greek or human read-aloud review. No website publication. Browser visual checks, if performed, are recorded separately."})
    names = [p for p in OUT.iterdir() if p.is_file() and p.name != "checksums.json"]
    write_json("checksums.json", {"algorithm": "sha256", "excludes": "checksums.json (self-reference)", "files": {p.name: sha(p.read_bytes()) for p in sorted(names)}})
    print(json.dumps({"output": str(OUT), "counts": counts, "checks_passed": len(checks), "missing_planned_review_inputs": missing_reviews}, ensure_ascii=False, indent=2))


def render_reader(edition, inventory):
    e = html.escape
    counts = edition["counts"]
    parts = ["<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>Saints English · Old Testament reading draft</title>",
             """<style>
:root{color-scheme:light;--ink:#28352f;--muted:#59685f;--paper:#fbf8f1;--accent:#77552b;--line:#d8d2c5}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.75}a{color:#365d51;text-underline-offset:.18em}a:focus-visible,button:focus-visible,select:focus-visible{outline:3px solid #b78238;outline-offset:4px}.masthead{padding:4rem max(1.4rem,calc((100% - 1060px)/2));background:#e9eee7;border-bottom:1px solid var(--line)}.eyebrow,.label,nav,summary,.badge,button,select,footer{font-family:system-ui,sans-serif}.eyebrow{text-transform:uppercase;letter-spacing:.18em;font-size:.75rem}h1{font-weight:400;font-size:clamp(2.4rem,6vw,4.3rem);line-height:1.1;margin:.7rem 0 1rem}h2{font-size:2rem;font-weight:400;margin-top:0}h3{font-weight:400;font-size:1.6rem}.intro{max-width:740px;font-size:1.15rem}.notice{font-family:system-ui,sans-serif;max-width:860px;font-size:.88rem;color:#3c5145}.shell{max-width:1120px;margin:auto;padding:2rem 1.3rem;display:grid;grid-template-columns:220px minmax(0,1fr);gap:3rem}nav{font-size:.85rem}nav details{margin-bottom:.65rem}nav summary{font-weight:650;cursor:pointer}nav a{display:block;padding:.1rem 0}.book{margin-bottom:5rem}.book-head{padding-top:1rem;border-top:3px solid #506650}.chapter-links{display:flex;flex-wrap:wrap;gap:.3rem .9rem;font: .82rem system-ui,sans-serif;margin-bottom:2rem}.chapter{scroll-margin-top:1rem;margin-bottom:3.5rem}.verse{margin:0 0 1rem}.verse-label{display:block;font: .72rem system-ui,sans-serif;color:var(--muted);margin-bottom:.15rem}.reading-text{white-space:pre-line;font-size:1.12rem;margin:0;overflow-wrap:anywhere}.continuation{margin:.65rem 0 1rem 1rem}.badge{font-size:.68rem;color:#68511c;border:1px solid #cbbd95;border-radius:3px;padding:.1rem .3rem;margin-left:.4rem;white-space:nowrap}.candidate{border-left:2px solid #bba263;padding-left:1rem}.comparison{font: .85rem system-ui,sans-serif;color:var(--muted);margin:.7rem 0 1.3rem}.comparison summary{cursor:pointer}.baseline{white-space:pre-line}.source-note{font:.8rem system-ui,sans-serif;color:var(--muted)}.controls{font: .85rem system-ui,sans-serif;display:flex;gap:.8rem;flex-wrap:wrap;align-items:center;margin-bottom:1.5rem}select,button{padding:.55rem .7rem;border:1px solid #a7b5a9;background:#fff;color:#28352f;border-radius:4px;font:inherit}footer{padding:2rem 1.3rem;border-top:1px solid var(--line);font-size:.8rem;text-align:center}[hidden]{display:none!important}.skip{position:absolute;top:-100px;left:1rem}.skip:focus{top:1rem;background:white;padding:1rem} @media(max-width:760px){.shell{display:block;padding:1.5rem 1.1rem}nav{margin-bottom:2rem;columns:2}nav details{break-inside:avoid}.masthead{padding:2.5rem 1.1rem}.badge{white-space:normal}.reading-text{font-size:1.06rem}.book{margin-bottom:3rem}}@media print{nav,.controls,.chapter-links,.skip{display:none!important}.shell{display:block;max-width:none}.masthead{padding:1rem;background:white}.book{display:block!important;break-before:page}.chapter{break-before:page}body{background:white;color:#000}.comparison{font-size:9pt}.reading-text{font-size:11pt}.badge{font-size:8pt}a{color:inherit;text-decoration:none}}
</style></head><body><a class="skip" href="#reading">Skip to reading</a>""",
             f'<header class="masthead"><div class="eyebrow">Bespoke Saints English · updated {AS_OF_DISPLAY}</div><h1>The Old Testament</h1><p class="intro">The complete inherited reading manuscript, with the first Greek-led comparison drafts.</p><p class="notice"><strong>Provisional reading edition.</strong> 43 books · {counts["reading_sections"]:,} reading sections · 26,580 stored units. {counts["fresh_focused_comparison_units"]:,} units have new focused comparison records; {counts["proposed_changed_units"]:,} contain unaccepted wording proposals. Most text remains inherited. This is not a completed fresh Greek audit or an accepted release.</p><a href="#genesis-section-1">Begin reading Genesis</a></header><div class="shell"><nav aria-label="Old Testament books">']
    division_names = {"law": "Law", "judgement": "Judgement", "wisdom": "Wisdom", "providence": "Providence"}
    for division in division_names:
        parts.append(f'<details open><summary>{division_names[division]}</summary>')
        for book in edition["books"]:
            if book["division"] == division:
                parts.append(f'<a href="#book-{e(book["book_id"])}" data-book-link="{e(book["book_id"])}">{e(book["book"])}</a>')
        parts.append('</details>')
    parts.append('</nav><main id="reading"><div class="controls"><label for="book-picker">Reading view</label><select id="book-picker"><option value="all">All 43 books</option>')
    for book in edition["books"]:
        parts.append(f'<option value="{e(book["book_id"])}">{e(book["book"])}</option>')
    parts.append('</select><button id="print" type="button">Print reading edition</button><a href="PROPOSED-CHANGES.md">Proposed changes</a></div>')
    for book in edition["books"]:
        parts.append(f'<article class="book" id="book-{e(book["book_id"])}" data-book="{e(book["book_id"])}"><header class="book-head"><div class="eyebrow">{e(division_names[book["division"]])}</div><h2>{e(book["book"])}</h2><p class="source-note">Inherited source history: <a href="../../{e(book["book_id"])}/source-checks.json">book record</a>. Provisional; specialist and acceptance stages remain open.</p></header><div class="chapter-links" aria-label="Reading sections">')
        for chapter in book["chapters"]:
            parts.append(f'<a href="#{e(chapter["reading_section_id"])}">{e(chapter["title"])}</a>')
        parts.append('</div>')
        for chapter in book["chapters"]:
            parts.append(f'<section class="chapter" id="{e(chapter["reading_section_id"])}"><h3>{e(chapter["title"])}</h3>')
            for verse in chapter["verses"]:
                proposal = verse["review_status"] == "unaccepted_wording_proposal"
                reviewed = verse["review_status"] != "inherited_draft_without_new_comparison"
                badge = '<span class="badge">Proposal · acceptance pending</span>' if proposal else '<span class="badge">Compared · wording retained</span>' if reviewed else ''
                parts.append(f'<div class="verse{" candidate" if proposal else ""}" id="{e(verse["unit_id"])}"><span class="verse-label">{e(verse["reference"])}{badge}</span><p class="reading-text" data-reading-key="{e(verse["unit_id"])}">{e(verse["display_text"])}</p>')
                for i, para in enumerate(verse["continuation_paragraphs"], 1):
                    parts.append(f'<p class="reading-text continuation" data-reading-key="{e(verse["unit_id"])}-continuation-{i}">{e(para)}</p>')
                if reviewed:
                    parts.append(f'<details class="comparison"><summary>{"Compare inherited wording and evidence" if proposal else "Comparison evidence"}</summary>')
                    if proposal:
                        parts.append(f'<p class="baseline"><strong>Inherited wording:</strong> {e(verse["inherited_unit"]["text"])}</p>')
                    analysis = verse.get("review_analysis", "")
                    if not isinstance(analysis, str):
                        analysis = json.dumps(analysis, ensure_ascii=False)
                    parts.append(f'<p>{e(analysis)}</p>')
                    if verse.get("display_review_note"):
                        parts.append(f'<p>{e(verse["display_review_note"])}</p>')
                    if verse.get("source_url"):
                        parts.append(f'<p><a href="{e(verse["source_url"])}">Greek running text consulted</a></p>')
                    for stage, draft in verse.get("drafts", {}).items():
                        if draft and draft != verse["text"]:
                            parts.append(f'<p><strong>{e(stage.capitalize())} working draft:</strong> {e(draft)}</p>')
                    if verse.get("unresolved_questions"):
                        parts.append('<p><strong>Open questions:</strong></p><ul>')
                        for question in verse["unresolved_questions"]:
                            parts.append(f'<li>{e(str(question))}</li>')
                        parts.append('</ul>')
                    token_notice = 'The source words have an explicit AI alignment; interpretation can still be unresolved.' if verse.get("tokens_accounted_for") else 'Complete token accounting remains pending.'
                    parts.append(f'<p><a href="../../{e(verse["review_evidence"])}">Full review record</a>. {token_notice} Independent human Greek review, human reading aloud and editorial acceptance remain pending.</p></details>')
                parts.append('</div>')
            parts.append('</section>')
        parts.append('</article>')
    parts.append('''</main></div><footer>43-book Saints selection · Old Greek Daniel and all inherited special units retained · No website deployment.<br><a href="README.md">Scope and provenance</a> · <a href="manifest.json">Manifest</a> · <a href="source-history.json">Source histories</a> · <a href="validation.json">Validation</a></footer><script>
const picker=document.getElementById('book-picker');
if(matchMedia('(max-width:760px)').matches)document.querySelectorAll('nav details').forEach(d=>d.open=false);
function showBook(value){document.querySelectorAll('.book').forEach(b=>b.hidden=value!=='all'&&b.dataset.book!==value);picker.value=value;}
picker.addEventListener('change',()=>{showBook(picker.value);if(picker.value!=='all')document.getElementById('book-'+picker.value).scrollIntoView();});
document.querySelectorAll('[data-book-link]').forEach(a=>a.addEventListener('click',()=>showBook(a.dataset.bookLink)));
window.addEventListener('hashchange',()=>{const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));const book=target?.closest('.book');if(book&&book.hidden){showBook(book.dataset.book);target.scrollIntoView();}});
if(location.hash){const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));const book=target?.closest('.book');if(book)showBook(book.dataset.book);}
document.getElementById('print').addEventListener('click',()=>window.print());
</script></body></html>''')
    (OUT / "Saints-English-Old-Testament.html").write_text("\n".join(parts), encoding="utf-8", newline="\n")


def render_text(edition):
    parts = ["BESPOKE SAINTS ENGLISH — OLD TESTAMENT", "Provisional reading manuscript · 12 November 2026",
             "Inherited text with marked, unaccepted Greek-comparison proposals. Not a complete fresh Greek audit.",
             "Unit markers preserve exact identity and support verification. Continuations retain their parent anchor; no verse number is invented.", ""]
    for book in edition["books"]:
        parts.extend([f"=== {book['book']} ===", ""])
        for chapter in book["chapters"]:
            parts.extend([f"--- {chapter['title']} ---", ""])
            for verse in chapter["verses"]:
                tag = " [UNACCEPTED PROPOSAL]" if verse["review_status"] == "unaccepted_wording_proposal" else " [COMPARED; RETAINED]" if verse["review_status"] == "focused_comparison_retained_wording" else ""
                parts.extend([f"[UNIT {verse['unit_id']}]", verse["reference"] + tag, verse["display_text"], "[/UNIT]", ""])
                for i, paragraph in enumerate(verse["continuation_paragraphs"], 1):
                    parts.extend([f"[UNIT {verse['unit_id']}-continuation-{i}]", f"{verse['reference']} — attached continuation {i}", paragraph, "[/UNIT]", ""])
    (OUT / "Saints-English-Old-Testament.txt").write_text("\n".join(parts), encoding="utf-8", newline="\n")


def write_readme(counts, missing):
    text = f'''# Complete Old Testament — provisional reading draft

**43 books · {counts['reading_sections']:,} reading sections · 26,580 stored units · 7 attached continuation paragraphs · 12 November 2026**

The entire inherited Saints English Old Testament is assembled here. New focused Greek comparisons cover **{counts['fresh_focused_comparison_units']} units**, including **{counts['proposed_changed_units']} unaccepted wording proposals**. The other **{counts['inherited_without_new_comparison']:,} units remain inherited drafts without a new comparison in this batch**. This is a complete reading manuscript, not a completed fresh translation, exhaustive Greek audit or accepted release.

- [Read the Old Testament](Saints-English-Old-Testament.html) — standalone offline HTML with book selection, every reading section and expandable proposal comparisons. Download and open locally; all text remains available without JavaScript.
- [Plain-text edition](Saints-English-Old-Testament.txt) and [structured edition](old-testament.json).
- [Readable proposal ledger](PROPOSED-CHANGES.md), [machine-readable changes](changes.json), [manifest and book inventory](manifest.json), [validation](validation.json) and [file hashes](checksums.json).
- [Inherited source histories](source-history.json); these are preserved historical records, not newly certified review claims.

## Review boundaries

The working source remains Rahlfs–Hanhart 2006 subject to the book-specific histories; Daniel uses Old Greek. Fresh evidence resides in the dated OT batch directories listed in the manifest. Of the compared units, {counts['new_token_aligned_units']} have explicit token accounting ({counts['aligned_source_tokens']} source tokens); these are a subset of the comparison total. Three working draft stages are recorded for {counts['three_stage_draft_units']} units and may deliberately agree. These statuses do not imply critical-apparatus collation or resolved interpretation. Independent human Greek review, human read-aloud review, editorial acceptance and publication remain pending. No New Testament work is included or altered.

Each proposed wording change is visibly marked in the reader and plain text. The JSON retains the exact original unit, including display text and metadata, alongside its candidate. Genesis 1–11's accepted historical benchmark remains intact in the original book archive. Proposed corrections do not silently change that status.

## Exceptional units and reading order

Preserved: Psalm 151; all Greek Esther additions and six attached continuation paragraphs; the additional continuation at 1 Kings 8:53a; Daniel's separate chapter-five preface, furnace material, Susanna and Bel and the Dragon; Sirach's translator's prologue; all 34 Proverbs sections in the inherited reading order. Stored units and attached continuations are counted separately. Lettered/grouped references and meaningful gaps remain unchanged.

All 4,008 inherited display-text differences remain available in `inherited_unit`; escaped line breaks are rendered as line breaks. The {counts['recovered_poetry_units']} Genesis/Exodus units whose JSON recorded only a break count recover their exact breaks from matching inherited HTML; normalized wording is checked against the JSON before use. Existing poetry is preserved. Explicit AI-proposed lineation for retained wording is identified in its passage evidence; normalized words must still match the candidate exactly.

## Rebuild and verification

Run `python tools/build_ot_reading_draft.py --require-reviews` from the repository root. The script reads baseline `{BASELINE}`, verifies unchanged original Scripture and source histories, and overlays a review only when book, anchor, full reference, inherited text and candidate hash agree exactly. Duplicate or unmatched reviews stop the build.

The build checks source identity (allowing Git's Windows checkout line-ending conversion), every scoped passage ID/order, candidate hashes, all special units, full JSON round-trip and exact HTML/TXT text round-trips including continuations. Source hashes use canonical baseline Git bytes. It checks that the existing NT book directories and NT review editions have no tracked differences from the baseline. These are structural checks, not scholarly approval. Browser visual checks, if performed, are recorded separately.

The reader preserves each original anchor in JSON while using book-and-section-qualified DOM IDs to avoid cross-book collisions. Source locators remain in the inherited metadata; this compilation creates no new website routes. The flat source schemas for Leviticus, Numbers and Deuteronomy are grouped by their existing chapter order without changing any unit.

## Provenance and recovery

Baseline: `{BASELINE}`. The original book files are untouched. `manifest.json` records source SHA-256 hashes and review-input hashes; `checksums.json` covers all generated files except itself. To return to inherited wording, use each unit's `inherited_unit`, or omit this dated edition. `changes.json` records every before/after proposal. No staging or production deployment was made.
'''
    if missing:
        text += "\n## Build awaiting planned review inputs\n\nThis intermediate build has not yet received: " + ", ".join(f"`{x}`" for x in missing) + ". Rebuild with `--require-reviews` before delivering the completed batch.\n"
    if (OUT / "browser-validation.json").exists():
        browser_check = read_json(OUT / "browser-validation.json")
        current_browser_check = browser_check.get('status') == 'passed' and browser_check.get('reader_sha256') == sha((OUT / 'Saints-English-Old-Testament.html').read_bytes())
        if current_browser_check:
            text += f"\n## Browser verification\n\n[Browser checks](browser-validation.json) record {len(browser_check['checks'])} passing checks in local headless Chrome at desktop and phone widths, tied to the current reader's SHA-256. [Visual inspection](visual-verification.json) records the scope of the AI screenshot inspection. No human read-aloud, real-phone or assistive-technology review is implied. `verify-browser.cjs` reproduces the browser checks with configurable runtime paths.\n"
        else:
            text += "\n## Browser verification pending\n\nThe stored browser report belongs to an earlier reader revision. Rerun `verify-browser.cjs` and inspect the updated screenshots before crediting this build with browser verification.\n"
    (OUT / "README.md").write_text(text, encoding="utf-8", newline="\n")


def write_change_ledger(changes):
    lines = ["# Old Testament wording proposals", "", f"**{len(changes)} proposals · 12 November 2026 · editorial acceptance pending**", "",
             "These are evidence-linked AI proposals in the dated reading draft. The original book files and the accepted Genesis 1–11 historical benchmark remain unchanged. No website text has been replaced.", ""]
    for change in changes:
        rationale = change["rationale"]
        if not isinstance(rationale, str):
            rationale = json.dumps(rationale, ensure_ascii=False, indent=2)
        lines.extend([f"## {change['reference']}", "", "**Status:** " + ("Proposed correction to the accepted historical benchmark; owner decision required." if change["benchmark_proposal"] else "Proposed revision; acceptance pending."), "",
                      "**Inherited**", "", "> " + change["baseline_text"].replace("\n", "\n> "), "",
                      "**Proposed**", "", "> " + change["candidate_text"].replace("\n", "\n> "), "",
                      "**Reason and limits**", "", rationale, "", f"[Focused evidence](../../{change['evidence']}) · anchor `{change['verse_anchor']}`", ""])
    (OUT / "PROPOSED-CHANGES.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-reviews", action="store_true", help="Fail if any registered review input is missing")
    args = parser.parse_args()
    build(args.require_reviews)
