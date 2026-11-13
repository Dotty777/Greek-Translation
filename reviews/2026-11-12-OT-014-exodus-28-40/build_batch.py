"""Format manually authored comparisons against frozen English; no automatic Greek review."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
BASE='39a2bb990f252f9c867879f14942b200c4a86aa5'
BATCH='OT-014'
DATE='2026-11-12'
LIMITS='AI source-led focused running-text comparison and provisional draft stages only. No exhaustive token alignment, specialist lexicon consultation, critical apparatus, Göttingen collation, independent human Greek review, human reading aloud, editorial acceptance or publication is claimed.'


def labels(start,end):
    return [str(n) for n in range(start,end+1)]


# Independently recorded from the complete publisher pages actually read.
PUBLISHER_LABELS={
    28:labels(1,22)+['29','29a']+labels(30,43),29:labels(1,46),30:labels(1,38),31:labels(1,18),
    32:labels(1,8)+labels(10,35),33:labels(1,23),34:labels(1,35),
    35:labels(1,7)+labels(9,12)+['12a','13','14','16']+labels(19,35),
    36:labels(1,38),37:labels(1,21),38:labels(1,27),39:labels(1,23),
    40:labels(1,6)+['8','9','10']+labels(12,27)+['29']+labels(33,38),
}
PROPOSALS={'30:21':('statute for him and his generations','statute for them, for him and his generations')}
CLOSE={
    '28:13':('small rosettes','small shields'),
    '29:9':('consecrate Aaron’s hands','perfect Aaron’s hands'),
    '33:6':('from Mount Horeb onward','from Mount Horeb'),
    '34:25':('offer the blood','slaughter the blood'),
    '36:26':('the two ends of the oracle-piece','the two little wings at the edge of the oracle-piece'),
    '38:8':('sheltering the propitiatory cover','overshadowing the propitiatory cover'),
    '39:17':('the bread of the Presence','the bread set before'),
    '40:23':('the bread of the Presence','the bread of presentation'),
}
UNRESOLVED={
    '28:4':'Technical garment distinctions and consistent glossary equivalents.',
    '28:7':'Exact attachment of the paired shoulder sections.',
    '28:9':'Ancient emerald term versus modern mineral identity.',
    '28:10':'Generational versus strictly birth-order arrangement.',
    '28:13':'Little-shield fitting versus inherited rosette identification.',
    '28:14':'Braids, floral work and front attachment construction.',
    '28:17':'Ancient gem identities in the first row.',
    '28:18':'Ancient gem identities in the second row.',
    '28:19':'Ligure and other third-row gemstone identifications.',
    '28:20':'Fourth-row gemstone identifications.',
    '28:30':'Manifestation and Truth objects and ritual function.',
    '28:32':'Textile border and integrated joining construction.',
    '28:34':'Elliptical floral/bell/pomegranate arrangement.',
    '28:37':'Headband/turban terminology and attachment.',
    '29:3':'On-basket preposition and basket shape.',
    '29:9':'Completion/perfection idiom for consecrated hands.',
    '29:27':'Distinct separation/contribution ritual terms.',
    '29:28':'Deliverance-sacrifice category and glossary.',
    '29:37':'Sanctification-through-contact ritual scope.',
    '29:40':'Unspecified base measure for the tenth and ancient metrology.',
    '29:43':'Middle appointment verb: arrangement/meeting nuance.',
    '30:3':'Grating term on incense altar.',
    '30:4':'Ring/bracket layout and repeated side language.',
    '30:9':'Technical distinction between offering and sacrifice.',
    '30:12':'Visitation/counting and downfall idioms.',
    '30:21':'Restored plural followed by singular statute referent; human review pending.',
    '30:23':'Myrrh, cinnamon and cane identifications and ancient weights.',
    '30:24':'Iris plant or part and sacred measure.',
    '30:29':'Contact-sanctification scope.',
    '30:32':'Ordinary-flesh prohibition in relation to priestly anointing.',
    '30:34':'Four incense ingredients and their ancient identities.',
    '30:38':'Enjoyment nuance supplied to the smelling verb.',
    '31:3':'Capitalization and theological force of divine spirit.',
    '31:6':'Eliab and other approved Greek-associated name forms.',
    '32:4':'Engraving-tool and casting production sequence.',
    '32:12':'Evil/calamity relation in the mercy petition.',
    '32:18':'Song-leading, victory/rout and wine-song expressions.',
    '32:29':'Hand-filling and son/brother relation behind at the cost of.',
    '32:30':'Unusual after-the-next-day temporal construction.',
    '33:6':'From-Horeb spatial/temporal force; onward is interpretive.',
    '33:9':'Implicit speaking subject and inherited capitalized He.',
    '33:11':'Face-to-face idiom in relation to later face prohibition.',
    '33:23':'Behind/back expression and anthropomorphic imagery.',
    '34:5':'Implicit subject of calling on the divine name.',
    '34:12':'Singular/plural stumbling-block construction.',
    '34:22':'Middle-of-year festival dating and calendar reconciliation.',
    '34:25':'Compressed slaughter/blood expression and ritual noun.',
    '34:28':'Implicit subject of writing the Ten Words.',
    '34:29':'Speaking-pronoun referents in the glorification clause.',
    '35:6':'Doubled/spun scarlet textile construction.',
    '35:11':'Stretching elements versus inherited cords.',
    '35:22':'From-women donor relation and five ornament identifications.',
    '35:31':'Divine spirit capitalization and knowledge scope.',
    '36:7':'Work/material expression and surplus clause.',
    '36:12':'Interwoven same-material construction.',
    '36:13':'Gem identity and clasp/setting vocabulary.',
    '36:16':'Final doubled qualifier in relation to dimensions.',
    '36:17':'First gem-row modern identifications.',
    '36:18':'Second gem-row modern identifications.',
    '36:19':'Ligure and other third-row identifications.',
    '36:20':'Fourth gem-row identifications.',
    '36:22':'Braid/fringe/chain craft terminology.',
    '36:23':'Small-shield fittings versus rosettes.',
    '36:25':'Braids, joinings and shoulder fitting layout.',
    '36:26':'Little-wing/flap image and rear/inner orientation.',
    '36:27':'Multiple spatial qualifiers in ring attachment.',
    '36:30':'Intact border and seam technique.',
    '36:35':'Distinct head coverings and linen garments.',
    '36:37':'Holy-dedication noun and supplied emblem interpretation.',
    '37:7':'Hundred-by-hundred expression and southwest orientation.',
    '37:9':'Repeated hundred-by-hundred expression.',
    '37:13':'Second-flank and either-side arrangement.',
    '37:16':'Height-and-breadth five-cubit construction.',
    '38:12':'Ancient table vessel shapes/functions.',
    '38:16':'Nut-shaped supports and seventh fitting relationships.',
    '38:17':'Tray/scoop implement identification.',
    '38:19':'Scope of bronze modifier over ring groups.',
    '38:20':'Capitals, gate object and final silvering pronoun.',
    '38:22':'Korah censers notice and chronology; apparatus not consulted.',
    '38:23':'Firepan/base/bowls technical identities.',
    '38:24':'Network position below firepan and halfway extent.',
    '38:26':'Mirrors of fasting women, erection-day clause and implicit he.',
    '39:1':'Selected 720-shekel total; no apparatus or modern weight reconciliation.',
    '39:4':'Capital versus expected base/sockets equipment term.',
    '39:5':'Gilding verb within silver accounting context.',
    '39:17':'Conventional Presence term versus set-out bread.',
    '39:19':'Singular veil with two entrances and object count.',
    '40:8':'Set-the-tent-about and sanctify-all-around construction.',
    '40:18':'Capital term in tent assembly sequence.',
    '40:23':'Conventional Presence term versus bread of presentation.',
}


def write(name,data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def replace_once(text,pair):
    old,new=pair
    assert text.count(old)==1,(old,text)
    return text.replace(old,new,1)


def main():
    raw=subprocess.check_output(['git','-C',str(ROOT),'show',f'{BASE}:exodus/verses.json'])
    original=json.loads(raw)
    assert (ROOT/'exodus/verses.json').read_bytes().replace(b'\r\n',b'\n')==raw.replace(b'\r\n',b'\n')
    notes={}
    for line in (HERE/'analysis.txt').read_text(encoding='utf-8').splitlines():
        key,note=line.split('|',1)
        assert key not in notes and len(note)>90
        notes[key]=note
    records=[]
    for chapter in original['chapters']:
        n=chapter['chapter']
        if n not in PUBLISHER_LABELS: continue
        actual=[v['reference'].split(':')[1] for v in chapter['verses']]
        assert actual==PUBLISHER_LABELS[n],(n,actual)
        for verse in chapter['verses']:
            key=verse['reference'].split(' ',1)[1]
            baseline=verse['text']; candidate=baseline
            if key in PROPOSALS: candidate=replace_once(baseline,PROPOSALS[key])
            close=replace_once(candidate,CLOSE[key]) if key in CLOSE else candidate
            records.append({'record_type':'focused_running_text_comparison','review_id':f'{BATCH}-exodus-{key.replace(":","-")}',
                'batch_id':BATCH,'book_id':'exodus','reference':verse['reference'],'verse_anchor':verse['id'],'reading_section_id':str(n),'baseline_commit':BASE,
                'baseline_text':baseline,'candidate_text':candidate,'candidate_sha256':hashlib.sha256(candidate.encode('utf-8')).hexdigest(),
                'decision':'propose_revision' if candidate!=baseline else 'retain_provisionally',
                'source':{'edition':'Rahlfs–Hanhart 2006','url':f'https://www.die-bibel.de/en/bible/LXX/EXO.{n}','accessed_on':DATE,'running_text_read':True,'apparatus_consulted':False},
                'drafts':{'close':close,'spoken':candidate,'literary':candidate},
                'draft_stage_note':'Stages may retain identical wording after the recorded source comparison; stage labels do not certify independent drafting or human read-aloud review.',
                'analysis':notes[key],'unresolved_questions':[UNRESOLVED[key]] if key in UNRESOLVED else [],
                'review':{'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Verse-specific Greek running-text comparison and provisional close/spoken/literary choices','all_tokens_accounted_for':False,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
                'benchmark_change':False,'publication':{'staging':None,'production':None}})
    keys={r['reference'].split(' ',1)[1] for r in records}
    assert keys==set(notes) and len(records)==405
    assert set(PROPOSALS)<=keys and set(CLOSE)<=keys and set(UNRESOLVED)<=keys
    assert len({r['verse_anchor'] for r in records})==len(records)
    counts={'units':len(records),'proposed_revisions':len(PROPOSALS),'retained_provisionally':len(records)-len(PROPOSALS),'draft_stage_records':len(records),'distinct_close_stage_alternatives':len(CLOSE),'units_with_explicit_unresolved_questions':len(UNRESOLVED),'token_aligned':0,'independently_reviewed':0,'human_read_aloud':0,'editorially_accepted':0}
    write('focused-reviews.json',{'schema_version':'1.0','batch_id':BATCH,'scope':'Exodus 28–40; all 405 inherited units in selected Greek order','date':DATE,'baseline_commit':BASE,'status':'focused_comparison_and_provisional_drafts_full_alignment_pending','counts':counts,'limitations':LIMITS,'records':records})
    write('sources.json',{'batch_id':BATCH,'accessed_on':DATE,'edition':'Septuaginta, edited by Alfred Rahlfs; second revised edition edited by Robert Hanhart, 2006, Deutsche Bibelgesellschaft','source_access':'All displayed Greek running text of all thirteen chapters was actually read and compared with inherited English. Exodus 29 was reopened after the initial response ended at verse 38 to read 39–46. Source numbering was recorded separately and checked against every stored reference.','sources':[{'id':f'E-EXO-{n}','url':f'https://www.die-bibel.de/en/bible/LXX/EXO.{n}','scope':f'Exodus {n}; complete displayed running text','displayed_verse_labels':refs,'accessed_on':DATE,'apparatus_accessed':False} for n,refs in PUBLISHER_LABELS.items()],'baseline':{'repository':'https://github.com/Dotty777/Greek-Translation','commit':BASE,'path':'exodus/verses.json','canonical_git_sha256':hashlib.sha256(raw).hexdigest()},'other_consultation':'No specialist lexicon, manuscript images, critical apparatus or Göttingen volume was consulted.','reproduction':'No complete Greek chapter text is redistributed; source locators, original English choices and analytical references are retained.'})
    write('structure.json',{'batch_id':BATCH,'status':'stored_order_matches_displayed_publisher_order','chapters':[{'chapter':n,'units':len(refs),'publisher_labels':refs,'stored_labels_match':True} for n,refs in PUBLISHER_LABELS.items()],'observations':['28 omits numbered 23–28 and includes 29a after 29','32 omits numbered 9','35 omits numbered 8,15,17,18 and includes 12a after 12','36 contains priestly garments; 37 tent and court; 38 ark and other furnishings; 39 totals and delivery','40 omits numbered 7,11,28,30–32','These are selected-source numbering differences, not missing inherited units; no other textual tradition was used to fill them'],'limits':'This compares visible running-text verse labels and stored order only; it is not a critical-apparatus or manuscript collation.'})
    write('validation.json',{'status':'passed','batch_id':BATCH,'date':DATE,'counts':counts,'checks':['All 405 inherited units included in exact order','Publisher verse-label inventories independently recorded and matched for all 13 chapters','405 unique manually authored source-specific notes','Exact frozen text, IDs and references retained as baseline','Explicit bounded proposal and close-stage replacements each match once','Exact UTF-8 candidate SHA-256 hashes generated','Three provisional draft fields on every record','No all-token or human acceptance claims','Original Exodus text unchanged apart from checkout newline representation','Generated files UTF-8 with LF newlines'],'limits':LIMITS})
    readme=f'''# OT-014 — Exodus 28–40

**405 units · 13 complete selected-Greek chapters · 1 proposal · 12 November 2026**

Every displayed publisher Greek chapter was read and compared with the inherited Saints English at `{BASE}`. All 405 stored units have individually authored analytical notes and close, spoken and literary stages. Eight close alternatives expose lexical or idiomatic choices without becoming automatic reading changes. Agreement among stages is provisional and does not represent three independent translations.

The one reading proposal is **Exodus 30:21**, restoring **“for them”** before **“for him and his generations”** to preserve both the Greek plural and following singular referent. The other 404 candidates remain inherited wording with provisional retention. No original Scripture was edited.

## Selected Greek order and difficult readings

[The structure inventory](structure.json) matches all stored verse labels against the publisher's displayed order. Exodus 28 includes 29a and omits 23–28; 32 omits 9; 35 includes 12a and omits 8, 15, 17–18; 40 omits 7, 11, 28 and 30–32. The selected chapter arrangement places garments in 36, tent/court in 37, furnishings in 38, and totals/delivery in 39. These are preserved source structures, not empty slots filled from another edition.

Provisional difficult readings include small-shield/rosette fittings, gemstone identities, garment construction, the hundred-by-hundred dimensions in 37:7 and 37:9, the Korah-censer notice in 38:22, fasting women in 38:26, capitals terminology, gilding within silver accounting in 39:5, and the compact setting-about instruction in 40:8. The selected totals 720 shekels in 39:1 and 1,500 in 39:6 remain intact. None of these is represented as resolved by a manuscript or specialist lexical review.

- [Focused records and drafts](focused-reviews.json)
- [Actual source access and all displayed verse labels](sources.json)
- [Validation](validation.json)

`analysis.txt` contains the authored judgments. `build_batch.py` formats them against frozen inherited text and independently recorded source labels; it does not automatically translate or review Greek. Run `python reviews/2026-11-12-OT-014-exodus-28-40/build_batch.py` from the repository root.

{LIMITS} Original Scripture, shared tracking files and accepted benchmarks remain untouched. No full copyrighted Greek text is redistributed.
'''
    (HERE/'README.md').write_text(readme,encoding='utf-8',newline='\n')
    print(json.dumps(counts,indent=2))


if __name__=='__main__': main()
