"""Rebuild the authored Genesis 12–20 comparison; never modifies book originals."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

raw = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASELINE}:genesis/verses.json"])
current = (ROOT / "genesis/verses.json").read_bytes()
assert current.replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n"), "Genesis original has changed"
book = json.loads(raw)
notes = {}
for line in (HERE / "notes.tsv").read_text(encoding="utf-8").splitlines():
    key, text = line.split("\t", 1)
    assert key not in notes
    notes[key] = text

revisions = {
    "12:19": "Why did you say, ‘She is my sister’? And I took her as my wife. And now, look, your wife is before you; take her and hurry away.”",
    "19:21": "And he said to him, “Behold, I have shown you favour in this matter also: I will not overthrow the city of which you have spoken.",
}
close_drafts = {
    "19:21": "And he said to him, “Behold, I have honoured your face in this matter also, so as not to overthrow the city of which you have spoken.",
}
open_questions = {
    "12:5": ["Social status of persons described as acquired; sense and English register of soul in this occurrence."],
    "12:6": ["Botanical identification of the high oak."],
    "13:10": ["Attachment of the comparative geography and Zoar limit."],
    "13:11": ["Geographic interpretation of the selected from-the-east wording; no harmonization attempted."],
    "14:1": ["Irregular opening case sequence and coordination of the named rulers."],
    "14:13": ["Appositional syntax around Mamre; meaning and name policy for the man from beyond."],
    "14:14": ["Social force of household-born and the explicit slave wording supplied by the inherited contextual rendering."],
    "14:20": ["Contextual identification of the pronominal giver and recipient of the tenth."],
    "15:2": ["Relationship of Masek, the feminine household-born expression, Damascus and Eliezer; full syntax and apparatus review required."],
    "15:3": ["Household-born person's status and inheritance expression."],
    "15:6": ["Reckoning agent and scope of righteousness; no later theological synthesis imported."],
    "15:11": ["Referent of with them and scene implied by Abram's sitting; selected verb must not be silently replaced by drove away."],
    "16:5": ["Independent check of the first-person attachment of the feminine seeing participle."],
    "16:12": ["Contextual sense of the rustic/wild adjective; force of opposite his brothers."],
    "16:13": ["Object of saw, force of before and syntax of the appearing participle; inherited interpretation unresolved."],
    "16:14": ["Syntax of the seeing expression in the well name; name-authority comparison for Barad/Bered."],
    "17:10": ["Readable representation of singular/plural address shifts without routinely supplying all."],
    "17:12": ["Singular household/seed references within plural group address."],
    "17:14": ["Precise force of destroyed from kindred; textual and interpretive review of eighth-day clause."],
    "18:3": ["Singular addressee identity and Lord capitalization without forcing a theological decision."],
    "18:6": ["Culinary identification and measure volume; no modern conversion assumed."],
    "18:7": ["Subject of the final hurried-to-prepare clause."],
    "18:8": ["Curds versus butter as the contextual dairy rendering."],
    "18:10": ["Exact force of the seasonal time expression and referent of behind him."],
    "18:21": ["Sense, voice and subject of the completion verb; relation to the cry and elliptical final purpose clause. Retention is not a resolved reading."],
    "18:23": ["Initial negative subjunctive as prohibition or rhetorical question; compare the alternative Do not destroy."],
    "18:30": ["Elliptical deferential opening; allow is supplied English support."],
    "19:14": ["Family relationships implied by the perfect having-taken participle; do not silently substitute betrothal."],
    "19:18": ["Singular lord addressed within a plural narrative; divine identification not settled."],
    "19:21": ["Specialist confirmation of the face-regarding idiom; retain literal alternative alongside favour proposal."],
    "19:31": ["Scope of earth/land in the daughter's statement; not the narrator's census."],
    "20:4": ["Unaware/ignorant sense without implying intellectual deficiency."],
    "20:10": ["Observation versus deliberation in the seeing participle."],
    "20:16": ["Face-honor idiom, feminine companions and scope of the closing truth imperative."],
    "20:18": ["Sense and attachment of from outside; idiomatic English remains unresolved."],
}

records = []
chapter_counts = {}
for chapter in book["chapters"]:
    n = chapter["chapter"]
    if not 12 <= n <= 20:
        continue
    chapter_counts[str(n)] = len(chapter["verses"])
    for verse in chapter["verses"]:
        key = verse["reference"].removeprefix("Genesis ")
        candidate = revisions.get(key, verse["text"])
        changed = candidate != verse["text"]
        record = {
            "record_type": "focused_running_text_comparison",
            "review_id": "OT-006-genesis-" + key.replace(":", "-"),
            "book_id": "genesis",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": str(chapter.get("section", n)),
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": digest(candidate),
            "decision": "propose_revision" if changed else "retain_provisionally",
            "source": {
                "edition": "Rahlfs–Hanhart 2006",
                "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}",
                "accessed_on": "2026-11-12",
                "running_text_read": True,
                "apparatus_consulted": False,
            },
            "analysis": notes[key],
            "drafts": {"close": close_drafts.get(key, candidate), "spoken": candidate, "literary": candidate},
            "draft_stage_note": "Working candidates share wording where the scoped Greek comparison supports retention; this is not a human read-aloud or final literary approval. See the passage-specific analysis for unresolved choices.",
            "unresolved_questions": open_questions.get(key, []),
            "review": {
                "reviewer": "OpenAI Codex assistant",
                "type": "AI",
                "scope": "Focused running-text comparison with close, spoken and literary working candidates",
                "all_tokens_accounted_for": False,
                "apparatus": None,
                "independent_greek": None,
                "human_read_aloud": None,
                "editorial_acceptance": None,
            },
            "benchmark_change": False,
            "publication": {"staging": None, "production": None},
        }
        if key == "19:21":
            record["translation_alternatives"] = [{"reading": "I have regarded your face", "category": "translation_alternative", "disposition": "Inherited literal image retained as an explicit alternative; favour is a contextual idiom proposal, not a claimed specialist lexical ruling."}]
        if key == "18:23":
            record["translation_alternatives"] = [{"reading": "Do not destroy the righteous with the ungodly", "category": "translation_alternative", "disposition": "Prohibitive reading of initial negative subjunctive; unresolved, not applied."}]
        records.append(record)

assert len(records) == 215
assert {r["reference"].removeprefix("Genesis ") for r in records} == set(notes)
assert list(chapter_counts.values()) == [20, 18, 24, 21, 16, 27, 33, 38, 18]
assert len({r["verse_anchor"] for r in records}) == 215
assert all(r["candidate_sha256"] == digest(r["drafts"]["literary"]) for r in records)
counts = {"units": 215, "chapters": 9, "proposed_revisions": sum(r["decision"] == "propose_revision" for r in records), "retained_provisionally": sum(r["decision"] == "retain_provisionally" for r in records), "token_aligned": 0, "editorially_accepted": 0}
write("focused-reviews.json", {"batch_id": "OT-006", "scope": "Genesis 12–20, every existing unit", "date": "2026-11-12", "status": "focused_running_text_comparison_drafted_full_alignment_pending", "counts": counts, "chapter_counts": chapter_counts, "records": records})
write("sources.json", {
    "batch_id": "OT-006",
    "accessed_on": "2026-11-12",
    "edition": "Septuaginta, Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft",
    "source_access": [{"chapter": n, "scope": f"Genesis {n}:1–{chapter_counts[str(n)]}", "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}", "running_text_read": True, "apparatus_read": False} for n in range(12, 21)],
    "access_note": "All nine complete running-text chapters were actually read in web retrieval. Genesis 18 and 19 were reopened to read portions truncated in the initial combined response. No critical text is reproduced in full.",
    "lexicons_consulted_for_this_batch": [],
    "limits": "No specialist lexicon, printed apparatus, manuscript or Göttingen collation was consulted. Analyses are provisional contextual AI judgments. Prior source-check records are historical evidence, not a substitute for this scoped reading.",
})
write("validation.json", {"status": "passed", "counts": counts, "checks": ["Exact frozen baseline verified against unchanged original", "All 215 references and anchors preserved in source order", "Nine chapter counts checked", "Every unit has authored passage-specific analysis", "Candidate hashes match literary drafts", "No token alignment, human review, acceptance or publication credited"], "limits": "Structural validation does not certify Greek correctness or resolve the recorded open questions."})
print(json.dumps(counts))
