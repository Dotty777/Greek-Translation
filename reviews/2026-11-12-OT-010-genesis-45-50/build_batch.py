"""Format individually authored Greek comparisons; this does not translate automatically."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = '39a2bb990f252f9c867879f14942b200c4a86aa5'
BATCH = 'OT-010'
DATE = '2026-11-12'
EXPECTED = {45:28,46:34,47:31,48:22,49:33,50:26}
LIMITS = 'AI source-led focused running-text comparison and provisional draft stages only. No exhaustive token alignment, specialist lexicon consultation, critical apparatus, Göttingen collation, independent human Greek review, human reading aloud, editorial acceptance or publication is claimed.'
CLOSE = {
    '45:20': ('regret your belongings', 'spare your belongings'),
    '47:12': ('according to each person', 'according to each body'),
    '49:6': ('my inward parts', 'my livers'),
    '49:12': ('joyful from wine', 'bright from wine'),
    '49:21': ('a spreading tree', 'a spreading stem'),
    '50:24': ('God shall surely visit you', 'God shall visit you with a visitation'),
    '50:26': ('they performed his burial rites', 'they buried him'),
}
UNRESOLVED = {
    '45:7':'Great remnant/survival construction and the two related remnant terms.',
    '45:20':'Eye-spare/regret idiom; close stage exposes the underlying expression.',
    '46:4':'Completion expression behind at last and the eye gesture.',
    '46:5':'Household travelling-party or baggage sense of the collective term.',
    '46:12':'Greek-associated Jemuel and inherited name-authority choices.',
    '46:20':'Expanded Egyptian genealogy and name forms need independent checking.',
    '46:21':'Benjamin genealogy generations and names need independent checking.',
    '46:27':'Nine and seventy-five retained; textual apparatus and genealogy reconciliation pending.',
    '47:5':'Long selected Greek unit and duplicated arrival/settlement statements; cross-edition numbering reconciliation pending.',
    '47:18':'Opening destruction/relationship idiom remains awkward.',
    '47:31':'Staff reading retained from selected Greek; no apparatus conclusion is claimed.',
    '48:7':'Place-name mapping and the unusual hippodrome distance term.',
    '48:12':'Plural bowing subject and knees/spatial arrangement.',
    '48:16':'God/angel invocation relationship; no ontological interpretation certified.',
    '48:20':'Plural-to-singular addressee shift in the blessing formula.',
    '48:22':'Shechem/portion wording and first-person sword-and-bow acquisition claim.',
    '49:1':'Temporal extent of latter days remains unspecified.',
    '49:6':'Literal livers versus inward-parts idiom and poetic register.',
    '49:9':'Shoot image, referent and second-to-third-person shift.',
    '49:10':'Reserved things as plural subject; pronoun referents and leader/thigh imagery.',
    '49:12':'Eye adjective: joyful/bright/colour nuance and relation to wine.',
    '49:14':'Precise sense of the allotments/resting places.',
    '49:17':'Serpent designation remains generic without specialist species identification.',
    '49:21':'Stem/tree form and construction connecting beauty and fruit.',
    '49:22':'Envied/admirable adjective and youngest-son return appeal.',
    '49:24':'From-there clause and relation of the one strengthening Israel to preceding phrases.',
    '49:25':'Attachment of initial from-phrase and causal relation of breasts/womb blessing.',
    '49:26':'Number shifts, prevailing blessing, dunes and final head/crown relationship all remain provisional.',
    '50:2':'Burial-preparer professional term versus contextual embalmers.',
    '50:8':'Whole-household versus remaining kindred scope.',
    '50:12':'Repeated burial report before subsequent carrying/burial; no chronological harmonization.',
    '50:17':'Second petition uses a receiving-wrongdoing idiom; pardon is contextual.',
    '50:23':'Born-upon-thighs idiom and kinship significance.',
    '50:26':'Burial verb in relation to coffin placement; close alternative is not an accepted change.',
}


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def write(name, data):
    (HERE/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def main():
    raw = subprocess.check_output(['git','-C',str(ROOT),'show',f'{BASE}:genesis/verses.json'])
    source = json.loads(raw)
    assert (ROOT/'genesis/verses.json').read_bytes().replace(b'\r\n',b'\n') == raw.replace(b'\r\n',b'\n')
    notes = {}
    for line in (HERE/'analysis.txt').read_text(encoding='utf-8').splitlines():
        key,note=line.split('|',1)
        assert key not in notes and len(note)>90
        notes[key]=note
    records=[]
    for chapter in source['chapters']:
        n=chapter['chapter']
        if n not in EXPECTED: continue
        assert len(chapter['verses'])==EXPECTED[n]
        for verse in chapter['verses']:
            key=verse['reference'].split(' ',1)[1]
            baseline=verse['text']
            close=baseline
            if key in CLOSE:
                old,new=CLOSE[key]
                assert baseline.count(old)==1
                close=baseline.replace(old,new,1)
            records.append({
                'record_type':'focused_running_text_comparison',
                'review_id':f'{BATCH}-genesis-{key.replace(":","-")}',
                'batch_id':BATCH,'book_id':'genesis','reference':verse['reference'],
                'verse_anchor':verse['id'],'reading_section_id':str(n),'baseline_commit':BASE,
                'baseline_text':baseline,'candidate_text':baseline,'candidate_sha256':digest(baseline),
                'decision':'retain_provisionally',
                'source':{'edition':'Rahlfs–Hanhart 2006','url':f'https://www.die-bibel.de/en/bible/LXX/GEN.{n}','accessed_on':DATE,'running_text_read':True,'apparatus_consulted':False},
                'drafts':{'close':close,'spoken':baseline,'literary':baseline},
                'draft_stage_note':'Stages may retain identical wording after the recorded source comparison; stage labels do not certify independent drafting or human read-aloud review.',
                'analysis':notes[key],'unresolved_questions':[UNRESOLVED[key]] if key in UNRESOLVED else [],
                'review':{'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Verse-specific Greek running-text comparison and provisional close/spoken/literary choices','all_tokens_accounted_for':False,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
                'benchmark_change':False,'publication':{'staging':None,'production':None},
            })
    keys={r['reference'].split(' ',1)[1] for r in records}
    assert keys==set(notes) and len(records)==174
    assert set(CLOSE)<=keys and set(UNRESOLVED)<=keys
    assert len({r['verse_anchor'] for r in records})==len(records)
    counts={'units':len(records),'proposed_revisions':0,'retained_provisionally':len(records),'draft_stage_records':len(records),'distinct_close_stage_alternatives':len(CLOSE),'units_with_explicit_unresolved_questions':len(UNRESOLVED),'token_aligned':0,'independently_reviewed':0,'human_read_aloud':0,'editorially_accepted':0}
    write('focused-reviews.json',{'schema_version':'1.0','batch_id':BATCH,'scope':'Genesis 45–50; all 174 inherited units','date':DATE,'baseline_commit':BASE,'status':'focused_comparison_and_provisional_drafts_full_alignment_pending','counts':counts,'limitations':LIMITS,'records':records})
    write('sources.json',{'batch_id':BATCH,'accessed_on':DATE,'edition':'Septuaginta, edited by Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft','source_access':'All displayed Greek running text for each of the six listed chapters was read and compared with the frozen inherited English. No chapter was represented solely by a title, search excerpt or another English translation.','sources':[{'id':f'E-GEN-{n}','url':f'https://www.die-bibel.de/en/bible/LXX/GEN.{n}','scope':f'Genesis {n}:1–{count}; full displayed chapter running text','accessed_on':DATE,'apparatus_accessed':False} for n,count in EXPECTED.items()],'baseline':{'repository':'https://github.com/Dotty777/Greek-Translation','commit':BASE,'path':'genesis/verses.json','canonical_git_sha256':hashlib.sha256(raw).hexdigest()},'other_consultation':'No specialist lexicon, manuscript images, critical apparatus or Göttingen volume was consulted in this batch.','reproduction':'No complete Greek chapter text is redistributed. Source locators, original English draft choices and brief analytical references are retained; no new blanket source-text license is asserted.'})
    write('validation.json',{'status':'passed','batch_id':BATCH,'date':DATE,'counts':counts,'checks':['All 174 inherited units present in chapter and verse order','Every verse has a unique individually authored source-specific analysis','Exact frozen baseline text, IDs and references retained','Candidate hashes generated from exact UTF-8 text','All close-alternative keys match exactly once','All units contain three provisional draft-stage fields','No changed poetry candidates; inherited display remains authoritative','No all-token, independent-human, human-reading, acceptance or publication completion asserted','Original Genesis archive unchanged apart from checkout line-ending representation','Generated text files use UTF-8 with LF newlines'],'limits':LIMITS})
    readme=f'''# OT-010 — Genesis 45–50

**174 units · 6 complete chapters · 174 provisional retentions · 12 November 2026**

All six complete publisher Greek chapters were read and compared with the frozen Saints English at `{BASE}`. Every record includes an individually authored verse-specific analysis and close, spoken and literary stages. Seven close-stage alternatives expose difficult idioms; no reading candidate is changed in this batch. Agreement between stages means a provisional shared choice, not three independently produced translations or final acceptance.

The most difficult passage is Genesis 49. Its inherited Greek-based features remain visible: the shoot in 49:9, reserved things in 49:10, agricultural Issachar in 49:14–15, Naphtali's tree in 49:21, and the opponents' broken bows in 49:24. Pronouns and attachments in 49:24–26, the eye adjective in 49:12 and the envied/admirable adjective in 49:22 remain unresolved. No familiar alternate-language reading has been inserted to make these easier. All original poetic line breaks remain unchanged because no reading candidate changes.

Other retained source distinctions include the expanded Genesis 46 genealogy and seventy-five total, the long 47:5 unit, enslavement in 47:21, staff in 47:31, plural bowing in 48:12, repeated burial in 50:12–13, belonging to God in 50:19, and thighs in 50:23. Names, ancient geography, ritual terms and numerical reconciliation still need specialist review.

- [Focused records and draft stages](focused-reviews.json)
- [Actual source access](sources.json)
- [Validation](validation.json)

`analysis.txt` contains the original judgments. `build_batch.py` only formats them against the frozen inherited text; it does not automatically translate or review Greek. Rebuild from the repository root with `python reviews/2026-11-12-OT-010-genesis-45-50/build_batch.py`.

{LIMITS} Original Scripture and shared tracking files are untouched. No copyrighted Greek corpus is redistributed.
'''
    (HERE/'README.md').write_text(readme,encoding='utf-8',newline='\n')
    print(json.dumps(counts,indent=2))


if __name__=='__main__':
    main()
