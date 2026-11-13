"""Serialize authored passage decisions; this script does not translate or read Greek.

Usage: python tools/package_ot_batch.py reviews/<batch-directory>
Inputs: batch.json, authored-notes.tsv (anchor, analysis, optional question),
and optional wording.json (explicit candidate/close/display overrides by anchor).
"""
import argparse
from collections import OrderedDict
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '39a2bb990f252f9c867879f14942b200c4a86aa5'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def sha(data):
    return hashlib.sha256(data.encode('utf-8') if isinstance(data,str) else data).hexdigest()

def package(directory):
    directory=(ROOT/directory).resolve()
    assert directory.is_relative_to(ROOT/'reviews')
    config=read(directory/'batch.json')
    path=config['book_id']+'/verses.json'
    raw=subprocess.check_output(['git','-C',str(ROOT),'show',BASELINE+':'+path])
    assert (ROOT/path).read_bytes().replace(b'\r\n',b'\n')==raw.replace(b'\r\n',b'\n'), 'Original book changed'
    source=read(directory/'wording.json') if (directory/'wording.json').exists() else {}
    notes={}
    for line in (directory/'authored-notes.tsv').read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        columns=line.split('\t')
        assert 2<=len(columns)<=3 and all(columns[:2]), 'Each authored row requires anchor and analysis'
        anchor=columns[0]
        assert anchor not in notes, 'Duplicate authored anchor '+anchor
        notes[anchor]={'analysis':columns[1], 'questions':[columns[2]] if len(columns)==3 and columns[2] else []}
    data=json.loads(raw)
    if isinstance(data,dict):chapters=data['chapters']
    else:
        groups=OrderedDict()
        for v in data:groups.setdefault(v['chapter'],[]).append(v)
        chapters=[{'chapter':c,'verses':vs} for c,vs in groups.items()]
    records=[]
    selected={str(c['section']):c for c in config['sources']}
    assert len(selected)==len(config['sources'])
    for chapter in chapters:
        section=str(chapter.get('section',chapter['chapter']))
        if section not in selected:continue
        access=selected[section]
        assert access['complete_running_text_read'] is True and access['url'] and access['accessed_on']
        for v in chapter['verses']:
            anchor=v['id']
            assert anchor in notes, 'Missing authored decision '+anchor
            choice=source.get(anchor,{})
            candidate=choice.get('candidate',v['text'])
            assert isinstance(candidate,str) and candidate.strip()
            reference=v.get('reference',config['book']+' '+v.get('ref',''))
            row={'record_type':'focused_running_text_comparison','review_id':config['batch_id']+'-'+config['book_id']+'-'+anchor,
              'book_id':config['book_id'],'reference':reference,'verse_anchor':anchor,'reading_section_id':section,
              'baseline_commit':BASELINE,'baseline_text':v['text'],'candidate_text':candidate,'candidate_sha256':sha(candidate),
              'decision':'retain_provisionally' if candidate==v['text'] else 'propose_revision',
              'source':{'edition':config['edition'],'url':access['url'],'accessed_on':access['accessed_on'],'running_text_read':True,'apparatus_consulted':False},
              'drafts':{'close':choice.get('close',candidate),'spoken':choice.get('spoken',candidate),'literary':candidate},
              'draft_policy':'Identical working stages deliberately retain wording supported by the authored comparison. These are AI stages, not human reading-aloud review.',
              'analysis':notes[anchor]['analysis'],'unresolved_questions':notes[anchor]['questions'],
              'review':{'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Authored passage-specific running-text comparison; complete token and apparatus work not credited.',
                        'all_tokens_accounted_for':False,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
              'benchmark_change':config['book_id']=='genesis' and chapter['chapter']<=11 and candidate!=v['text'],
              'publication':{'staging':None,'production':None}}
            if 'display' in choice:
                assert ' '.join(choice['display'].replace('\\n','\n').split())==' '.join(candidate.split())
                row['candidate_display_text']=choice['display']
            assert all(row['drafts'][s].strip() for s in ('close','spoken','literary'))
            records.append(row)
    assert len(records)==config['expected_units']
    assert len({r['verse_anchor'] for r in records})==len(records)
    assert set(notes)=={r['verse_anchor'] for r in records}, 'Unmatched authored decisions'
    assert set(source)<=set(notes), 'Unmatched wording override'
    def write(name,value):
        (directory/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    changed=sum(r['decision']=='propose_revision' for r in records)
    write('focused-reviews.json',{'batch_id':config['batch_id'],'scope':config['scope'],'records':records})
    write('validation.json',{'status':'passed','date':config['date'],'units':len(records),'proposed':changed,'retained':len(records)-changed,
      'checks':['Original book matches frozen baseline','Every scoped unit has exactly one authored decision','No unscoped or duplicate decisions','Nonempty close/spoken/literary stages','Explicit candidate hashes and unchanged stable identities'],
      'limits':'Serialization and structural checks only; source reading is an explicitly recorded AI activity, not something this script performs. No human or apparatus review credited.'})
    print(json.dumps({'batch':config['batch_id'],'units':len(records),'proposed':changed,'retained':len(records)-changed},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('directory')
    package(parser.parse_args().directory)
