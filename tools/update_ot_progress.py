"""Reconcile OT-only counters from the validated manuscript and exact review inputs."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EDITION = 'editions/2026-11-12-ot-reading-draft'

def read(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))

def write(path, value):
    (ROOT/path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')

def update():
    manifest = read(EDITION+'/manifest.json')
    validation = read(EDITION+'/validation.json')
    assert validation['status']=='passed' and validation['counts']==manifest['counts']
    assert not manifest['missing_planned_review_inputs']
    edition = read(EDITION+'/old-testament.json')
    assert edition['counts']==manifest['counts'] and edition['baseline_commit']==manifest['baseline_commit']
    progress = read('review-progress.json')
    frozen = json.loads(subprocess.check_output(['git','-C',str(ROOT),'show',manifest['baseline_commit']+':review-progress.json']))
    assert [b for b in progress['books'] if b['testament']=='NT'] == [b for b in frozen['books'] if b['testament']=='NT']
    assert progress['nt_manuscript']==frozen['nt_manuscript']
    nt_before = copy.deepcopy(progress['nt_manuscript'])
    records, batches = [], []
    for input_record in manifest['review_inputs']:
        assert hashlib.sha256((ROOT/input_record['path']).read_bytes()).hexdigest()==input_record['sha256'], 'Review changed since validated build: '+input_record['path']
        data=read(input_record['path'])
        rows=data.get('records',data.get('reviews'))
        records.extend(rows)
        folder=str(Path(input_record['path']).parent).replace('\\','/')
        batch_id=data.get('batch_id',folder.split('/')[-1][11:17])
        batches.append({'id':batch_id,'scope':data.get('scope',folder),'status':'provisional_running_text_draft_review_pending','evidence':[folder+'/README.md',input_record['path']]})
    assert len(records)==manifest['counts']['fresh_focused_comparison_units']
    next_item=None
    for book in edition['books']:
        for section in book['chapters']:
            if any(v['review_status']=='inherited_draft_without_new_comparison' for v in section['verses']):
                next_item=(book,section)
                break
        if next_item:
            break
    if next_item:
        book,section=next_item
        short={'genesis':'GEN','exodus':'EXO','leviticus':'LEV'}.get(book['book_id'],book['book_id'].upper())
        next_batch={'id':f"OT-{short}-{section['position']:03d}",'book':book['book'],'scope':section['title'],'status':'not_started',
          'first_step':'Access and read the selected Greek passage, draft by unit and compare the exact inherited text; preserve original files and identify unresolved choices.',
          'parallel_review_debt':'Complete token accounting and specialist review for compared passages. Genesis 4:7 token accounting does not resolve pronoun antecedents. Jonah 2:7 and 2:10 remain open.',
          'source_policy':manifest['source_policy']}
    else:
        next_batch={'id':'OT-REVIEW-DEBT','scope':'Full token, specialist, apparatus and human review across the OT','status':'pending'}
    inventory={b['book_id']:b for b in manifest['book_inventory']}
    ot_books=[]
    fresh_scope=[]
    for book in progress['books']:
        if book['testament']!='OT':
            continue
        info=inventory[book['book_id']]
        compared=info['fresh_focused_comparison_units']
        relevant=[r for r in records if r['book_id']==book['book_id']]
        paths=[i['path'] for i in manifest['review_inputs'] if any(r['book_id']==book['book_id'] for r in read(i['path']).get('records',[]))]
        token_records=[r for r in relevant if r.get('review',{}).get('all_tokens_accounted_for')]
        status=('complete_running_text_comparison_full_review_pending' if compared==info['stored_units'] else 'partial_running_text_comparison_review_pending') if compared else 'inherited_manuscript_inventoried_fresh_greek_work_pending'
        book.update({'programme_status':status,'total_units_verified_for_programme':info['stored_units'],
          'denominator_scope':'Structural inventory only; not certification of Greek accuracy.','denominator_evidence':EDITION+'/manifest.json',
          'manuscript_status':'included_in_complete_provisional_ot','new_programme_drafted_units':compared,
          'focused_running_text_compared_units':compared,'token_aligned_units':len(token_records),
          'three_stage_draft_units':info.get('three_stage_draft_units',0),
          'next_batch':next_batch['id'] if next_batch.get('book')==book['book'] else None})
        book['focused_comparison_evidence']=paths
        if compared:
            book['issues']=list(dict.fromkeys(book.get('issues',[])+['Provisional AI judgments; complete token/syntax, applicable apparatus, specialist and human review stages remain open.']))
            fresh_scope.append(f"{book['book']}: {compared} of {info['stored_units']} stored units compared; {len(token_records)} with explicit token accounting")
        token_paths=[i['path'] for i in manifest['review_inputs'] if any(r['book_id']==book['book_id'] and r.get('review',{}).get('all_tokens_accounted_for') for r in read(i['path']).get('records',[]))]
        book['stages']['source_collation'].update({'new_programme_units':len(token_records),'evidence':token_paths,
          'scope_note':'Only the specifically token-aligned records count here. Running-text AI alignment is not manuscript/apparatus collation or independent review.'})
        ot_books.append({**info,'inherited_without_new_comparison':info['stored_units']-compared,'status':status,'fully_reviewed_units':0,'newly_accepted_units':0,
                        'next_work':'Complete token accounting and outstanding specialist/human review' if compared==info['stored_units'] else 'Continue source-led drafting in project order; preserve open review debt'})
    progress.update({'updated':manifest['updated'],'status':'old_testament_only_greek_review_in_progress',
      'current_priority':'Continue through the entire 43-book Old Testament only, following the translation standard. Next source-led drafting scope: '+next_batch['scope']+'. Existing NT text and evidence remain unchanged.',
      'new_programme_drafted_units':sum(b.get('new_programme_drafted_units',0) for b in progress['books']),
      'counting_policy':'The OT manuscript contains inherited text and separately evidenced candidate drafts. Running-text comparison, token accounting (a subset), human review, acceptance and publication are separate counts. Earlier NT evidence is retained without new NT work. See ot_manuscript and old-testament-progress.json for exact current denominators.',
      'next_batch':next_batch,'ot_manuscript':{**manifest['counts'],'status':manifest['status'],'evidence':[EDITION+'/README.md',EDITION+'/manifest.json',EDITION+'/validation.json'],'website_publication':False}})
    new_by_id={b['id']:b for b in batches}
    progress['batches']=[new_by_id.pop(b['id'],b) for b in progress['batches']]+list(new_by_id.values())
    old=read('old-testament-progress.json')
    old.update({'updated':manifest['updated'],'status':'source_led_drafting_in_progress_full_review_incomplete','counts':manifest['counts'],
      'fresh_scope':fresh_scope,'draft_stage_scope':f"{manifest['counts']['three_stage_draft_units']} units have recorded close/spoken/literary stages, which may agree when no meaningful revision is justified. These are AI stages, not human reading-aloud review.",
      'review_evidence':[i['path'] for i in manifest['review_inputs']],'next_batch':next_batch,'books':ot_books})
    old['review_debt'][0]='Source-led drafting for all remaining OT units and separately review the seven attached continuation paragraphs.'
    old['review_debt'][1]='Complete token and construction accounting for every compared unit without an explicit full token ledger.'
    assert progress['nt_manuscript']==nt_before
    assert [b for b in progress['books'] if b['testament']=='NT']==[b for b in frozen['books'] if b['testament']=='NT']
    write('review-progress.json',progress)
    write('old-testament-progress.json',old)
    continuation=[]
    for item in manifest['review_inputs']:
        data=read(item['path'])
        if data.get('batch_id') in ('OT-001','OT-002','OT-003'):
            continue
        rows=data.get('records',data.get('reviews',[]))
        continuation.append((data,rows,Path(item['path']).parent.name))
    report=['# Old Testament continuation from Genesis 4','',
      f"**Updated {manifest['updated']} · provisional Greek-to-Saints English work**",'',
      f"This continuation adds {sum(len(rows) for _,rows,_ in continuation):,} focused comparison records. Across the current OT programme, {manifest['counts']['fresh_focused_comparison_units']:,} of {manifest['counts']['stored_units']:,} stored units have new comparisons; {manifest['counts']['inherited_without_new_comparison']:,} remain inherited text without a new comparison. The full 43-book task is still in progress.",'',
      '| Batch | Scope | Units compared | Wording proposals |','| --- | --- | ---: | ---: |']
    for data,rows,folder in continuation:
        report.append(f"| [{data['batch_id']}]({folder}/README.md) | {data['scope']} | {len(rows)} | {sum(r['decision']=='propose_revision' for r in rows)} |")
    report.extend(['',f"Next source-led drafting passage: **{next_batch['scope']}**. Complete token/construction accounting, applicable apparatus work, specialist decisions, independent human Greek review, human reading aloud and editorial acceptance remain open for the compared material.",'',
      'The [working reader](../'+EDITION+'/Saints-English-Old-Testament.html) exposes passage notes, alternatives and unresolved questions separately from Scripture. The [proposal ledger](../'+EDITION+'/PROPOSED-CHANGES.md) preserves exact before/after wording. Original Scripture files and the accepted Genesis 1–11 benchmark are unchanged. No New Testament work or website deployment is included.','',
      '[Scoped second AI checks](2026-11-12-OT-CONTINUATION-QA.json) are not independent human review. [Selected name decisions](../docs/OT-NAME-DECISIONS.json) begin a provisional register; it is not an approved exhaustive authority list.','',
      f"One compared unit, Genesis 4:7, has an explicit 19-token ledger; that unit is already included in the comparison total. The edition records {manifest['counts']['three_stage_draft_units']:,} close/spoken/literary draft sets, which may deliberately retain identical wording. These are working AI stages, not three human reviews.",''])
    (ROOT/'reviews/2026-11-12-OT-CONTINUATION.md').write_text('\n'.join(report),encoding='utf-8',newline='\n')
    print(json.dumps({'counts':manifest['counts'],'next_batch':next_batch,'nt_records_unchanged':True},ensure_ascii=False,indent=2))

if __name__=='__main__':
    update()
