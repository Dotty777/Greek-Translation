"""Build authored Exodus 3–15 focused reviews from frozen text and manual notes."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
BATCH = "OT-012"
DATE = "2026-11-12"


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


raw = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASELINE}:exodus/verses.json"])
assert (ROOT / "exodus/verses.json").read_bytes().replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n")
book = json.loads(raw)
notes = {}
for line in (HERE / "notes.tsv").read_text(encoding="utf-8").splitlines():
    key, note = line.split("\t", 1)
    assert key not in notes, key
    notes[key] = note

revisions = {
    "4:28": "Moses told Aaron all the words the Lord had sent, and all the signs He had commanded him.",
    "8:4": "Pharaoh called Moses and Aaron and said, “Pray to the Lord for me, and let Him remove the frogs from me and my people. I will let the people go so that they may sacrifice to the Lord.”",
    "9:17": "Yet you still act against My people, refusing to let them go.",
    "10:7": "And Pharaoh’s attendants said to him, “How long shall this be a hindrance to us? Let the people go, that they may serve their God. Or do you want to know that Egypt is destroyed?”",
    "12:3": "Speak to the whole congregation of the sons of Israel, saying: On the tenth day of this month, each shall take an animal from the flock for the ancestral households, one animal for each household.",
    "12:4": "If those in the house are too few to be sufficient for an animal from the flock, he shall join with his nearest neighbour. According to the number of persons, each person’s sufficient portion shall be reckoned for the animal.",
    "12:5": "Your animal from the flock shall be without blemish, a male a year old; you shall take it from the lambs and from the young goats.",
    "12:21": "Moses called the whole council of elders of the sons of Israel and said to them, “Go and take an animal from the flock for your families, and slaughter the Passover.",
}
close = {
    "4:28": "Moses reported to Aaron all the Lord’s words which He had sent, and all the signs which He had commanded him.",
    "8:4": "Pharaoh called Moses and Aaron and said, “Pray concerning me to the Lord, and let Him remove the frogs from me and from my people; and I will release the people, so that they may sacrifice to the Lord.”",
    "9:17": "Still, then, you act against My people by not releasing them.",
}
questions = {
    "3:12": ["Preserve the singular Moses/plural delivered-community shift in full alignment."],
    "3:16": ["Syntax of visiting the people and the events; inherited seen is contextual support."],
    "4:10": ["Exact force of the weak-voice and slow-tongue descriptions, without medical diagnosis."],
    "4:11": ["Overlapping hearing/speech ranges of the adjacent sensory adjectives."],
    "4:24": ["Referent of the threatened him; no name supplied."],
    "4:25": ["Owner of the feet, action at them, and reference of the child's blood declaration."],
    "4:26": ["Departure pronouns and the repeated declaration's causal relation."],
    "4:28": ["Independent syntax review of the words as object of sent; no explicit personal object is supplied."],
    "5:19": ["Speech attribution and discourse relation of saying after the scribes' distress."],
    "6:12": ["Degree and sense of the speech-deficiency adjective."],
    "6:14": ["Reconcile inherited English names with Greek forms in the name authority, without changing stable IDs."],
    "6:26": ["Contextual organization implied by the collective force/host term."],
    "7:7": ["Referent of the singular final speaking verb."],
    "7:9": ["Exact ancient creature range of dragon versus serpent; no modern species asserted."],
    "7:10": ["Same creature-range question as 7:9."],
    "7:12": ["Same creature-range question as 7:9; retain the narrator's return to staff terminology."],
    "7:19": ["What wood and stone denote; no unexpressed containers supplied."],
    "7:20": ["Implicit singular striking agent in the joint-obedience account."],
    "8:8": ["Temporal appointment versus boundary force of the frogs' limit noun."],
    "8:12": ["Specialist verification of the small-insect identification."],
    "8:13": ["Same insect-identity question as 8:12."],
    "8:14": ["Same insect-identity question as 8:12."],
    "8:17": ["Exact ancient dog-fly identification; no modern species asserted."],
    "8:18": ["Force of the exceptional-treatment verb and inherited marvellously distinguish."],
    "8:20": ["Same dog-fly identity question as 8:17."],
    "8:22": ["Genitive relation and exact cultural referent of Egyptian abominations."],
    "9:4": ["Unusual final none-at-all idiom in the livestock distinction."],
    "9:6": ["Discourse scope of all livestock relative to the field qualification and later livestock references; do not silently harmonize."],
    "9:14": ["Scope of the coordinated possessives following heart."],
    "9:17": ["Editorial punctuation versus possible rhetorical-question reading; precise sense of the uncommon action-against verb."],
    "9:31": ["Exact crop growth-stage terminology."],
    "9:32": ["Ancient cereal identity behind inherited spelt."],
    "10:2": ["Plural addressees in the intergenerational telling and recognition."],
    "10:3": ["Respect/reverence versus shame/humbling nuance."],
    "10:7": ["Confirm broader human-group rendering versus the explicitly male restriction in 10:11."],
    "10:10": ["Tone and comparison syntax of Pharaoh's purported blessing; household/dependents collective."],
    "10:17": ["Accept/bear sin idiom versus forgive as contextual English."],
    "12:3": ["Confirm the inclusive flock-animal rendering from the immediate lamb-and-young-goat specification in 12:5."],
    "12:4": ["Portion reckoning syntax and inclusive flock-animal noun."],
    "12:5": ["Independent lexical review of the inclusive flock-animal rendering; no exact taxonomic claim."],
    "12:16": ["Seventh-day appointed/gathered adjective and scope of the preparation exception."],
    "12:19": ["Relationship between this resident-stranger term and other legal-status terms in 12:43–49."],
    "12:21": ["Same inclusive Passover-animal scope as 12:3–5."],
    "12:24": ["Plural command to singular household addressee shift."],
    "12:37": ["Contextual household/dependents meaning of the collective accompanying-group term."],
    "12:39": ["Exact preparation described by the hearth-cake noun."],
    "12:42": ["Vigil/watch syntax, its initial subject or beneficiary, and the repeated night formula."],
    "12:43": ["Relationship of outsider term to resident and sojourner terms later in the law."],
    "12:45": ["Precise social/legal distinction of sojourner versus the resident admitted in 12:48."],
    "12:48": ["Historical status of the incoming resident; avoid imposing a modern citizenship analogy."],
    "13:4": ["Exact seasonal referent supplied as grain for new things."],
    "13:8": ["Causal reference of because of this; do not reverse it without evidence."],
    "13:13": ["Permitted scope of the flock-animal substitution outside the explicit Passover goat allowance."],
    "13:15": ["Unexpressed subject of killed resolved as the Lord through editorial capitalization."],
    "13:16": ["Substantival unshakable/fixed expression and the contextual supply reminder."],
    "13:17": ["Causal force of the near-route clause within the fear-of-war explanation."],
    "13:20": ["Name authority for Greek Othom and inherited Etham."],
    "14:2": ["Local referent of before them and identification of the settlement."],
    "14:7": ["Ancient rank or chariot-crew function behind officers."],
    "14:8": ["Precise idiomatic force of high hand without imposing a single interpretation."],
    "14:16": ["Unusual raise-with-your-staff syntax; inherited English remains awkward pending a justified natural rendering."],
    "14:25": ["Force/difficulty nuance of the driving expression; no removed-wheels reading adopted."],
    "14:27": ["Directional sense of fleeing beneath the water in this selected reading."],
    "15:2": ["Predicate structure of helper, shelter and becoming salvation."],
    "15:4": ["Relation of chosen riders and the officers term; precise ancient military office."],
    "15:8": ["Exact imagery of the repeated stiffening/standing-fast verb."],
    "15:11": ["Masculine holy ones versus neuter holy things/places; no apparatus or lexical adjudication completed."],
    "15:13": ["Comfort/encourage/call construction with motion toward the holy dwelling; inherited wording is awkward and explicitly provisional."],
    "15:16": ["Acquisition versus narrower purchase sense; no payment specified."],
    "15:25": ["Recipients of ordinances and testing: Moses or corporate Israel; implicit subject and capitalization."],
}

records, chapter_counts = [], {}
poetic_retained = []
for chapter in book["chapters"]:
    n = chapter["chapter"]
    if not 3 <= n <= 15:
        continue
    chapter_counts[str(n)] = len(chapter["verses"])
    for verse in chapter["verses"]:
        key = verse["reference"].removeprefix("Exodus ")
        candidate = revisions.get(key, verse["text"])
        changed = candidate != verse["text"]
        poetry = verse.get("poetic_line_breaks", verse.get("line_breaks", 0))
        record = {
            "record_type": "focused_running_text_comparison",
            "review_id": BATCH + "-exodus-" + key.replace(":", "-"),
            "book_id": "exodus",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": str(chapter.get("section", n)),
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": digest(candidate),
            "decision": "propose_revision" if changed else "retain_provisionally",
            "source": {"edition": "Rahlfs–Hanhart 2006", "url": f"https://www.die-bibel.de/en/bible/LXX/EXO.{n}", "accessed_on": DATE, "running_text_read": True, "apparatus_consulted": False},
            "analysis": notes[key],
            "drafts": {"close": close.get(key, candidate), "spoken": candidate, "literary": candidate},
            "draft_stage_note": "Working drafts agree where the scoped analysis supports retention; unresolved readings remain provisional in every stage. No separate human read-aloud or literary approval is claimed.",
            "unresolved_questions": questions.get(key, []),
            "review": {"reviewer": "OpenAI Codex assistant", "type": "AI", "scope": "Focused running-text comparison with close, spoken and literary working candidates", "all_tokens_accounted_for": False, "apparatus": None, "independent_greek": None, "human_read_aloud": None, "editorial_acceptance": None},
            "benchmark_change": False,
            "publication": {"staging": None, "production": None},
        }
        if changed:
            assert not poetry, "A changed poetic unit needs reviewed candidate_display_text from original HTML"
            assert "\n" not in verse.get("display_text", verse["text"])
            record["candidate_display_text"] = candidate
            record["translation_alternatives"] = [{"reading": verse["text"], "category": "translation_alternative", "disposition": "Inherited alternative retained in baseline; proposed wording remains unaccepted."}]
        elif poetry:
            poetic_retained.append(verse["reference"])
        records.append(record)

assert len(records) == 368
assert list(chapter_counts.values()) == [22, 31, 23, 30, 29, 28, 35, 29, 10, 51, 22, 31, 27]
assert set(notes) == {r["reference"].removeprefix("Exodus ") for r in records}
assert len({r["verse_anchor"] for r in records}) == 368
assert all(r["candidate_sha256"] == digest(r["drafts"]["literary"]) for r in records)
assert len(set(notes.values())) == len(notes)
counts = {"units": len(records), "chapters": 13, "proposed_revisions": sum(r["decision"] == "propose_revision" for r in records), "retained_provisionally": sum(r["decision"] == "retain_provisionally" for r in records), "token_aligned": 0, "editorially_accepted": 0}
assert counts["proposed_revisions"] == 8
write("focused-reviews.json", {"batch_id": BATCH, "scope": "Exodus 3–15, every existing unit", "date": DATE, "status": "focused_running_text_comparison_drafted_full_alignment_pending", "counts": counts, "chapter_counts": chapter_counts, "records": records})
write("sources.json", {"batch_id": BATCH, "accessed_on": DATE, "edition": "Septuaginta, Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft", "source_access": [{"chapter": n, "scope": f"Exodus {n}:1–{chapter_counts[str(n)]}", "url": f"https://www.die-bibel.de/en/bible/LXX/EXO.{n}", "running_text_read": True, "apparatus_read": False} for n in range(3, 16)], "access_note": "All thirteen complete running-text chapters were actually retrieved and read, including the full Song of the Sea. Source locators and analysis are retained; the modern critical text is not reproduced in full.", "lexicons_consulted_for_this_batch": [], "limits": "No specialist lexicon, printed apparatus, manuscript or Göttingen collation consulted. Lexical and grammatical analyses are provisional AI judgments. Editorial punctuation is not represented as a manuscript variant."})
write("validation.json", {"status": "passed", "counts": counts, "retained_poetic_units": poetic_retained, "checks": ["Exact original Exodus JSON matches frozen baseline after line-ending normalization", "All 368 units in source order with original references and anchors", "Thirteen chapter counts verified, including LXX 7:1–29 and 8:1–28", "Every unit has unique manually authored passage-specific analysis", "Candidate hashes match literary drafts", "All eight changed candidates are prose and have candidate_display_text", "Every recorded poetic unit is retained unchanged; no poetry line breaks were edited", "No independent human, apparatus, acceptance or publication status credited"], "limits": "Structural validation is not Greek-language certification; original poetry display must continue to be recovered from the unchanged source HTML by the reading-draft builder."})
for path in HERE.iterdir():
    if path.is_file() and path.suffix in {".py", ".tsv", ".json", ".md"}:
        assert b"\r" not in path.read_bytes(), f"Non-LF output: {path.name}"
print(json.dumps(counts))
