"""Build authored Genesis 38–44 records from frozen text and manual analysis."""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"

def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

raw = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASELINE}:genesis/verses.json"])
assert (ROOT / "genesis/verses.json").read_bytes().replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n")
book = json.loads(raw)
notes = {}
for line in (HERE / "notes.tsv").read_text(encoding="utf-8").splitlines():
    key, note = line.split("\t", 1)
    assert key not in notes
    notes[key] = note

revisions = {
    "41:40": "“You shall be over my house, and all my people shall obey your command; only in the throne shall I be above you.”",
    "42:38": "And he said, “My son shall not go down with you, for his brother is dead, and he alone is left; and he will fall sick on the way you go, and you shall bring down my old age with sorrow into Hades.”",
    "43:11": "And Israel their father said to them, “If it is so, do this: take some of the fruits of the land in your vessels, and carry down gifts to the man, resin and honey, incense and stacte, terebinth nuts and nuts.",
}
close = {
    "41:40": "“You shall be over my house, and all my people shall obey at your mouth; only in the throne shall I be above you.”",
    "42:38": "And he said, “My son shall not go down with you, for his brother has died and he alone remains; and it will happen that he falls sick on the way you go, and you shall bring down my old age with sorrow into Hades.”",
}
questions = {
    "38:2": ["Name-authority reconciliation of Shua with the selected feminine relative; no other textual form adopted."],
    "38:14": ["Specific garment denoted by the covering term."],
    "38:18": ["Necklace/chain identification and ring's exact function."],
    "38:26": ["Precise contextual force of the perfect vindication verb and comparison."],
    "38:29": ["Syntax and imagery of the barrier-breaking question; name interpretation."],
    "39:1": ["Ancient official senses of eunuch and archimageiros; inherited chief cook is provisional, not an etymological proof of kitchen duties."],
    "39:6": ["Precise scope of the food exception; no assumed euphemistic meaning."],
    "39:9": ["Syntax and authority scope of nothing above me."],
    "40:2": ["Administrative versus anatomical sense of eunuchs."],
    "40:4": ["Chief prison official's title and relationship to other named offices."],
    "40:10": ["Branches versus stems/bases for the vine divisions."],
    "40:16": ["Identity of the coarse-grain/bread basket contents; specialist lexical and comparative evidence needed."],
    "40:19": ["Wood/tree as execution structure; no apparatus or material reconstruction consulted."],
    "41:2": ["Marsh-growth term and precise plant identity."],
    "41:10": ["Chief cook as ancient office title; not assumed equivalent to a modern chef."],
    "41:12": ["Ancient official sense of chief cook in the retelling."],
    "41:16": ["Subject and construction of the answer/deliverance expression; inherited paraphrase remains provisional."],
    "41:18": ["Same plant-identity question as 41:2."],
    "41:23": ["Adjacent versus sequential force of the participial description of the later ears."],
    "41:25": ["Predictive force of the Greek present; about to do is contextual English."],
    "41:35": ["Practical relation of all-food collection to the preceding one-fifth levy; no harmonizing deletion."],
    "41:38": ["Interpretive capitalization and contextual sense of spirit of God in Pharaoh's speech."],
    "41:40": ["Confirm command as idiomatic realization of mouth; literal image remains an alternative."],
    "41:45": ["Egyptian name transliterations and priestly title; no identity assertion about Potiphar/Potiphera."],
    "41:47": ["Sheaves versus handfuls for the harvest noun."],
    "41:51": ["Scope of the elliptical all my father's things expression."],
    "42:9": ["Contextual sense of tracks of the country; no substitution of another tradition's nakedness expression."],
    "42:12": ["Same territorial-track expression as 42:9."],
    "42:38": ["Independent discourse review of the restored future assertion within Jacob's feared scenario, as distinct from the explicit conditional in 44:29."],
    "43:8": ["Dependents/household sense of the collective baggage term."],
    "43:11": ["Specialist verification of incense and exact identities of stacte, terebinth product and nuts; no modern botanical species asserted."],
    "43:16": ["Slaughtered animals in hospitality; cultic significance not assumed from the noun alone."],
    "43:23": ["Commercial force of acceptable/good silver and full receipt; opening reassurance's precise idiom."],
    "43:28": ["Implicit speaker of the selected blessing sentence."],
    "44:5": ["First-person cup versus my lord in the scripted quotation; exact force of the divination claim."],
    "44:15": ["Contextual force of Joseph's divination claim; no independent claim of historical practice."],
    "44:22": ["Referent of he will die: father or son; retain pronoun pending full syntax review."],
}

records, chapter_counts = [], {}
for chapter in book["chapters"]:
    n = chapter["chapter"]
    if not 38 <= n <= 44:
        continue
    chapter_counts[str(n)] = len(chapter["verses"])
    for verse in chapter["verses"]:
        key = verse["reference"].removeprefix("Genesis ")
        candidate = revisions.get(key, verse["text"])
        changed = candidate != verse["text"]
        record = {
            "record_type": "focused_running_text_comparison",
            "review_id": "OT-009-genesis-" + key.replace(":", "-"),
            "book_id": "genesis",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": str(chapter.get("section", n)),
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": digest(candidate),
            "decision": "propose_revision" if changed else "retain_provisionally",
            "source": {"edition": "Rahlfs–Hanhart 2006", "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}", "accessed_on": "2026-11-12", "running_text_read": True, "apparatus_consulted": False},
            "analysis": notes[key],
            "drafts": {"close": close.get(key, candidate), "spoken": candidate, "literary": candidate},
            "draft_stage_note": "Working drafts agree where the scoped analysis supports retention; no separate human read-aloud or literary approval is claimed.",
            "unresolved_questions": questions.get(key, []),
            "review": {"reviewer": "OpenAI Codex assistant", "type": "AI", "scope": "Focused running-text comparison with close, spoken and literary working candidates", "all_tokens_accounted_for": False, "apparatus": None, "independent_greek": None, "human_read_aloud": None, "editorial_acceptance": None},
            "benchmark_change": False,
            "publication": {"staging": None, "production": None},
        }
        if changed:
            assert not verse.get("poetic_line_breaks", verse.get("line_breaks", 0)), "Preserve changed verse's recorded poetry before proceeding"
            assert "\n" not in verse.get("display_text", verse["text"])
            record["candidate_display_text"] = candidate
            record["translation_alternatives"] = [{"reading": verse["text"], "category": "translation_alternative", "disposition": "Inherited alternative retained in baseline; proposed wording remains unaccepted."}]
        records.append(record)

assert len(records) == 239
assert list(chapter_counts.values()) == [30, 23, 23, 57, 38, 34, 34]
assert set(notes) == {r["reference"].removeprefix("Genesis ") for r in records}
assert len({r["verse_anchor"] for r in records}) == 239
assert all(r["candidate_sha256"] == digest(r["drafts"]["literary"]) for r in records)
counts = {"units": len(records), "chapters": 7, "proposed_revisions": sum(r["decision"] == "propose_revision" for r in records), "retained_provisionally": sum(r["decision"] == "retain_provisionally" for r in records), "token_aligned": 0, "editorially_accepted": 0}
write("focused-reviews.json", {"batch_id": "OT-009", "scope": "Genesis 38–44, every existing unit", "date": "2026-11-12", "status": "focused_running_text_comparison_drafted_full_alignment_pending", "counts": counts, "chapter_counts": chapter_counts, "records": records})
write("sources.json", {"batch_id": "OT-009", "accessed_on": "2026-11-12", "edition": "Septuaginta, Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft", "source_access": [{"chapter": n, "scope": f"Genesis {n}:1–{chapter_counts[str(n)]}", "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}", "running_text_read": True, "apparatus_read": False} for n in range(38, 45)], "access_note": "All seven complete running-text chapters were actually retrieved and read. Source locators and analysis are retained; the modern critical text is not reproduced in full.", "lexicons_consulted_for_this_batch": [], "limits": "No specialist lexicon, printed apparatus, manuscript or Göttingen collation consulted. Lexical and grammatical analyses are provisional AI judgments."})
write("validation.json", {"status": "passed", "counts": counts, "checks": ["Exact original Genesis file matches frozen baseline", "All 239 units in source order with original references and anchors", "Seven chapter counts verified", "Every unit has manually authored passage-specific analysis", "Candidate hashes match literary drafts", "All changed candidates are prose; no recorded poetry breaks altered", "No independent human, apparatus, acceptance or publication status credited"], "limits": "Structural validation is not Greek-language certification."})
print(json.dumps(counts))
