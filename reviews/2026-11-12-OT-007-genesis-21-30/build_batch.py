"""Rebuild OT-007 from individually authored analyses and frozen inherited text.

This formatter does not translate or perform a Greek review automatically.
analysis.txt contains the actual verse-specific AI judgments after source reading.
"""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
BATCH = "OT-007"
DATE = "2026-11-12"
EXPECTED = {21:34,22:24,23:20,24:67,25:34,26:35,27:46,28:22,29:35,30:43}
LIMITS = "AI source-led focused running-text comparison and provisional draft stages only. No exhaustive token alignment, specialist lexicon consultation, critical apparatus, Göttingen collation, independent human Greek review, human reading aloud, editorial acceptance or publication is claimed."


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write(name, value):
    (HERE/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")


def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text)
    return text.replace(old, new, 1)


def main():
    raw = subprocess.check_output(["git", "-C", str(ROOT), "show", f"{BASE}:genesis/verses.json"])
    source = json.loads(raw)
    current = (ROOT/'genesis/verses.json').read_bytes()
    assert current.replace(b'\r\n',b'\n') == raw.replace(b'\r\n',b'\n')
    analyses = {}
    for line in (HERE/'analysis.txt').read_text(encoding='utf-8').splitlines():
        ref, note = line.split('|',1)
        assert ref not in analyses and len(note)>90
        analyses[ref]=note
    proposals = {"21:30": ("from my hand", "from me")}
    # These bounded close-stage alternatives expose idioms; the spoken/literary
    # candidate remains the inherited reading unless an explicit proposal exists.
    close_changes = {
        "21:8": ("a great feast", "a great reception"),
        "21:18": ("Arise, take the child, and hold him with your hand", "Rise, take the child, and grasp him with your hand"),
        "22:8": ("God will provide for Himself", "God will see to it for Himself"),
        "22:17": ("surely I will bless you, and greatly multiply your seed", "surely, blessing I will bless you, and multiplying I will multiply your seed"),
        "23:8": ("If it is your will", "If you have it in your soul"),
        "24:10": ("some of all his master’s good things", "from all his master’s good things"),
        "24:23": ("is there room with your father for us to lodge", "is there a place with your father for us to lodge"),
        "25:27": ("a man without pretence", "an unaffected man"),
        "26:28": ("We have clearly seen", "Seeing, we have seen"),
        "27:33": ("was exceedingly astonished", "was struck with an exceedingly great astonishment"),
        "28:22": ("I will surely give a tenth to Thee", "I will tithe a tenth to Thee"),
        "29:14": ("a full month", "a month of days"),
        "30:27": ("I would divine by signs", "I would interpret omens"),
        "30:30": ("wherever I set my foot", "at my foot"),
    }
    unresolved = {
        "21:14": "Attachment of the child in the shoulder/loading clause; retain provisional attachment without age harmonization.",
        "21:15": "Botanical specificity of the fir term needs specialist confirmation.",
        "21:22": "Groomsman/court-title sense and approved Ahuzzath transliteration.",
        "22:8": "Seeing/providing idiom and its relationship to the naming language in 22:14.",
        "22:13": "Sabek plant identification; do not claim botanical certainty.",
        "22:21": "Names and Syrians designation require authority-list reconciliation.",
        "22:22": "Greek-associated Azau and other names need approved-form reconciliation.",
        "22:24": "Concubine and sons' name forms require authority-list review.",
        "23:13": "Relational idiom in the opening appeal to Ephron.",
        "24:22": "Ancient ornament types and weight denominations; no specialist metrology consultation.",
        "24:62": "South/southwest orientation and place-name mapping.",
        "24:63": "Meditation/conversation sense of the activity verb.",
        "25:8": "Death idiom and inherited supplied noun 'strength'.",
        "25:17": "Death idiom and inherited supplied noun 'strength'.",
        "25:27": "Aplastos: without pretence/simple/unaffected; no settled moral characterization or specialist lexicon finding. Singular house retained.",
        "26:10": "Ignorance/unwitting offence and the hypothetical near-event construction.",
        "26:32": "Displayed negative 'no water' retained; apparatus and alternate textual comparison pending.",
        "27:39": "Preposition: source/participation versus separation from richness/dew. Positive inherited reading remains provisional.",
        "27:40": "Unexpressed object in 'when you cast down'; breaking-loose and pulling-down interpretations unresolved.",
        "28:21": "Boundary between the vow's conditions and consequences.",
        "29:17": "Weak-eye description; no diagnosis or settled cosmetic interpretation.",
        "29:34": "On-my-side relationship idiom.",
        "30:8": "Sunanastrephomai context: dealings/interaction/contending; inherited contested rendering retained provisionally.",
        "30:23": "Possessive attachment in the Greek reproach statement.",
        "30:27": "Divination/omen verb with modal particle and conditional opening; do not claim a completed consultation as certain.",
        "30:30": "Foot/arrival/under-my-care idiom; inherited expansive wording remains provisional.",
        "30:37": "Styrax/walnut/plane botanical identifications remain provisional.",
        "30:39": "Breeding and colour vocabulary; no scientific or specialist lexical verification.",
        "30:41": "Reproductive verb and timing; do not import stronger/weaker animals from another text.",
    }
    records, consumed = [], set()
    for chapter in source['chapters']:
        n=chapter['chapter']
        if n not in EXPECTED: continue
        assert len(chapter['verses'])==EXPECTED[n]
        for v in chapter['verses']:
            key=v['reference'].split(' ',1)[1]
            baseline=v['text']; candidate=baseline
            if key in proposals: candidate=replace_once(baseline,*proposals[key])
            close=candidate
            if key in close_changes: close=replace_once(candidate,*close_changes[key])
            records.append({
                "record_type":"focused_running_text_comparison", "review_id":f"{BATCH}-genesis-{key.replace(':','-')}",
                "batch_id":BATCH, "book_id":"genesis", "reference":v['reference'], "verse_anchor":v['id'],
                "reading_section_id":str(n), "baseline_commit":BASE, "baseline_text":baseline,
                "candidate_text":candidate, "candidate_sha256":digest(candidate),
                "decision":"propose_revision" if candidate!=baseline else "retain_provisionally",
                "source":{"edition":"Rahlfs–Hanhart 2006", "url":f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}", "accessed_on":DATE, "running_text_read":True, "apparatus_consulted":False},
                "drafts":{"close":close, "spoken":candidate, "literary":candidate},
                "draft_stage_note":"Stages may retain identical wording after the recorded source comparison; stage labels do not certify independent drafting or human read-aloud review.",
                "analysis":analyses[key], "unresolved_questions":[unresolved[key]] if key in unresolved else [],
                "review":{"reviewer":"OpenAI Codex assistant", "type":"AI", "scope":"Verse-specific Greek running-text comparison and provisional close/spoken/literary choices", "all_tokens_accounted_for":False, "independent_greek":None, "human_read_aloud":None, "editorial_acceptance":None},
                "benchmark_change":False, "publication":{"staging":None,"production":None}
            })
            consumed.add(key)
    assert consumed==set(analyses) and len(records)==360
    assert set(proposals)<=consumed and set(close_changes)<=consumed and set(unresolved)<=consumed
    assert len({r['verse_anchor'] for r in records})==len(records)
    counts={"units":len(records),"proposed_revisions":sum(r['candidate_text']!=r['baseline_text'] for r in records),"retained_provisionally":sum(r['candidate_text']==r['baseline_text'] for r in records),"draft_stage_records":len(records),"distinct_close_stage_alternatives":len(close_changes),"units_with_explicit_unresolved_questions":len(unresolved),"token_aligned":0,"independently_reviewed":0,"human_read_aloud":0,"editorially_accepted":0}
    write('focused-reviews.json',{"schema_version":"1.0","batch_id":BATCH,"scope":"Genesis 21–30; all 360 inherited units","date":DATE,"baseline_commit":BASE,"status":"focused_comparison_and_provisional_drafts_full_alignment_pending","counts":counts,"limitations":LIMITS,"records":records})
    write('sources.json',{"batch_id":BATCH,"accessed_on":DATE,"edition":"Septuaginta, edited by Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft","source_access":"All displayed Greek running text for each listed chapter was read, then compared with the frozen inherited English. The long Genesis 24 page was reopened to include verses 54–67 after the first web response ended at verse 53.","sources":[{"id":f"E-GEN-{n}","url":f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}","scope":f"Genesis {n}:1–{count}; full displayed chapter running text","accessed_on":DATE,"apparatus_accessed":False} for n,count in EXPECTED.items()],"baseline":{"repository":"https://github.com/Dotty777/Greek-Translation","commit":BASE,"path":"genesis/verses.json","canonical_git_sha256":hashlib.sha256(raw).hexdigest()},"other_consultation":"No specialist lexicon, manuscript images, critical apparatus or Göttingen volume was consulted in this batch.","reproduction":"No complete Greek chapter text is redistributed. Source locators, original English draft choices and brief analytical references are retained; no new blanket source-text license is asserted."})
    write('validation.json',{"status":"passed","batch_id":BATCH,"date":DATE,"counts":counts,"checks":["All 360 inherited units present in chapter and verse order","Every verse has a unique manually authored source-specific analysis","Exact frozen baseline texts, IDs and references retained","Candidate SHA-256 values generated from exact UTF-8 text","All explicit proposal and close-draft keys resolve exactly once","All records have three provisional draft-stage fields","No all-token, independent-human, human-reading, acceptance or publication completion asserted","Original Genesis archive unchanged apart from checkout line-ending representation","Generated text files use UTF-8 with LF newlines"],"limits":LIMITS})
    readme=f'''# OT-007 — Genesis 21–30

**360 units · 10 complete chapters · {counts['proposed_revisions']} proposal · 12 November 2026**

All displayed publisher Greek running text in these chapters was read and compared with the inherited Saints English at `{BASE}`. [The records](focused-reviews.json) contain a verse-specific analysis and close, spoken and literary stages for every unit. Where the inherited reading fits the recorded analysis, stages can agree; these fields do not imply three independent translations. Fourteen close-stage alternatives expose particular Greek idioms without automatically replacing the reading candidate.

The sole wording proposal is **Genesis 21:30: “from my hand” → “from me”**, removing a body-part addition absent from the displayed expression. All 359 other candidates retain inherited wording provisionally. Retention is not final acceptance or resolution of every issue.

## Difficult readings retained for review

Genesis 21:14's shoulder/child attachment is unresolved; 21:16 explicitly retains the child as the one crying. Genesis 25:27 retains “without pretence” provisionally for aplastos, with simple/unaffected alternatives and singular house preserved. Genesis 27:39–40 retains the inherited positive richness/dew reading and difficult “when you cast down” clause, with prepositional force and missing object explicitly unresolved. Genesis 30:27 retains potential divination language rather than claiming a completed omen consultation; 30:8, 30:30 and the breeding vocabulary also remain open.

Names, ancient weights, geography and botanical identifications have bounded notes rather than invented specialist certification. Preserved textual distinctions include the field in 21:33, earrings in 24:22, brothers in 24:55, possessions in 24:59, mother's house in 24:67, negative water report in 26:32, and doubled “exceedingly” in 30:43.

## Evidence, status and rebuild

- [Actual source access](sources.json), [focused records and drafts](focused-reviews.json), [validation](validation.json).
- `analysis.txt` contains the individually authored judgments; `build_batch.py` formats them against the frozen source. It does not automatically perform a translation or Greek review.
- Run `python reviews/2026-11-12-OT-007-genesis-21-30/build_batch.py` from the repository root. Outputs use LF newlines.

{LIMITS} Original Scripture and shared tracking files are untouched. None of these chapters belongs to the accepted Genesis 1–11 benchmark. No copyrighted Greek corpus is redistributed.
'''
    (HERE/'README.md').write_text(readme,encoding='utf-8',newline='\n')
    print(json.dumps(counts,indent=2))


if __name__=='__main__': main()
