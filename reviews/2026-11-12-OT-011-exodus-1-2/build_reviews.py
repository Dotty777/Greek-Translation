"""Reproduce authored Exodus 1–2 records; no automated source review is claimed."""
from pathlib import Path
import json, hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
BASELINE='39a2bb990f252f9c867879f14942b200c4a86aa5'
NOTES={
1:[
'The heading names the sons of Israel entering Egypt together with Jacob their father. The distributive whole-household expression is retained with each, and the past entry is distinguished from the following list. The source does not give a new migration date here.',
'The first four names are Reuben, Simeon, Levi and Judah in the displayed order. Established English forms are retained; punctuation carries the coordinated list into the next verse. No extra sons or clan labels are supplied.',
'The list continues Issachar, Zebulun and Benjamin. Benjamin belongs in this position in the selected reading; the sequence is not rearranged into birth order or another passage’s list.',
'Dan, Naphtali, Gad and Asher complete this list. The two pairs and all four identities remain; the following Joseph statement is kept in its own unit rather than incorporated as another name here.',
'Joseph is already in Egypt in the narrative setting, and the souls from Jacob number seventy-five. Retain souls as the traditional persons expression and the selected total; do not silently replace it with seventy or claim that this verse itself enumerates all seventy-five.',
'Joseph’s death, all his brothers and all that generation form the coordinated conclusion. All is repeated for the two groups. The verse does not imply that every death happened on the same day.',
'The Greek accumulates growth, multiplication, becoming numerous and great strength, with a doubled intensifier; it then makes the land the subject of multiplying them. The inherited unusual final clause and doubled exceedingly preserve the source’s emphasis. They are not normalized to the land being filled.',
'Another king arises over Egypt and does not know Joseph. The source does not name the dynasty or explain whether not knowing is historical ignorance or a refusal of recognition. Retain the wording without resolving that historical question.',
'The king addresses his own nation and characterizes Israel as a great multitude stronger than us. This is his speech, not a separately verified numerical population estimate. Behold and the explicit comparison are warranted.',
'The exhortation proposes crafty treatment because of feared growth and a possible war, followed by joining enemies, fighting and departure. The conditional war setting is preserved; the translation does not convert the feared sequence into an event already occurring.',
'The ruler installs work overseers for affliction, and the Israelites build fortified cities for Pharaoh. The selected Greek names Pithom, Rameses and On, identifying On as City of the Sun. All three are retained; no city is removed to match a shorter tradition.',
'The more/so-much-more comparison links affliction to increasing numbers and strength. The Greek repeats its intensifier twice, retained as exceedingly, exceedingly. Egyptians are the subject of loathing; the verse is not softened into mere administrative concern.',
'Egyptians exercise oppressive domination over Israel by force. The direct agency and force remain. The continuing narrative is linked to the detailed work conditions in the next verse without assigning a new ruler.',
'Painful life under hard labor is specified through clay, brickmaking and all work in the plains, with force repeated at the end. The coordinated domains remain distinct. Plains is the selected noun; agriculture is not inserted as its only possible activity.',
'The ruler speaks to the midwives of the Hebrews, naming Sepphora and Puah. The genitive identifies whom they serve without decisively settling the midwives’ own ancestry. The established names are retained rather than importing a different first name.',
'The instruction addresses the midwives in the plural and distinguishes male and female births in two conditional clauses. The opposed killing and preserving commands remain explicit. Child is necessary English support for the substantivized sex terms.',
'The midwives fear God, refuse the royal command and keep the male infants alive. The final imperfect describes their life-preserving activity in the scene; the wording does not add an unexpressed frequency or claim that no infant died from any cause.',
'The king summons the midwives and asks why they did this and kept the males alive. The accusation repeats the previous life-preservation wording. The question remains his rather than a narrator’s condemnation of the women.',
'The women contrast Hebrew and Egyptian childbirth and say births occur before the midwives enter. The final and they bore is present in the source after the quoted explanation. Preserve that narration without adding a biological theory or independently judging the truthfulness of every part of their reply.',
'God treats the midwives well, while the people multiply and grow very strong. The separate subjects and benefits remain. The Greek has a single intensifier here, unlike the doubled formulas in 1:7 and 1:12; the translation keeps that distinction.',
'Because the midwives feared God, the displayed Greek uses a plural making verb with a feminine plural reflexive: they made houses for themselves. Preserve the midwives’ grammatical agency instead of silently replacing it with God giving them households. The literal/domestic force of houses remains a translation question.',
'Pharaoh commands all his people, widening the addressed group from the midwives. The order concerns every male born to the Hebrews and contrasts every female kept alive. River is retained; a proper name is not added where the Greek gives a common noun.',
],
2:[
'A man from Levi’s tribe takes a daughter of Levi and has her as wife. The supplied one and as his wife make the partitive and marriage expression natural in English. The source does not name the parents here or state their exact relationship beyond tribe.',
'The woman conceives and bears a male. The seeing and hiding forms are plural, preserved by they, and the concealment lasts three months. Beautiful is a contextual rendering of the appearance adjective; the source does not yet make a prediction about the child’s future office.',
'Plural inability to hide him is followed by the mother’s action: basket, bitumen-pitch coating, placing the child and setting the basket in the marsh beside the river. These agents and locations remain distinct. The Greek basket term is not the Genesis ark term.',
'His sister keeps watch from a distance to learn the outcome for him. The purpose and distance are retained. The verse does not name her or state that she had already arranged the princess’s arrival.',
'Pharaoh’s daughter comes to bathe; her attendants walk by the river; seeing the basket, she sends one attendant and takes it up through that action. Had it brought to her makes the mediated action natural without introducing a new named servant. The basket remains in the marsh.',
'The opened basket contains a weeping child, whom the princess spares or regards with compassion. Had compassion is a contextual rendering of the same general sparing verb discussed in the Jonah proposal; that does not require mechanically identical English. She identifies him as one of the Hebrew children.',
'The sister offers to call a nursing woman from among the Hebrews, who will nurse the child for the princess. The speaker remains the sister, not the mother. The two for-you relationships are represented without making the princess the physical nurse.',
'The princess gives a singular go command. The young woman then calls the child’s mother. Young woman is the source’s age-category term; no exact age is supplied, and the mother is not falsely described as an unrelated nurse.',
'The princess commands keeping and nursing the child for her, then promises wages. The woman takes the child and nurses him. Repeated for me preserves the princess’s claimed relationship, while the narrative nursing agent remains the woman.',
'After the child grows, he is brought to the princess and becomes her son. The source records the name Moses and her water-taking explanation. The translation preserves the narrative wordplay without asserting a new linguistic derivation of the Egyptian name.',
'Many days pass and Moses grows before going to his brothers, identified as Israel’s sons. He observes their suffering and an Egyptian striking one of those brothers. The repeated kinship labels remain, and the historical present is rendered as narrative past.',
'Moses looks in both directions, sees no one, strikes the Egyptian and hides him in sand. Struck down is supported by the subsequent account of killing. The verse gives no weapon; none is supplied. Seeing no one is Moses’s observation, not an assurance that the event had no witness.',
'The second day presents two Hebrew men fighting. Moses addresses the one doing wrong and asks why he strikes his neighbor. The participle assigns wrongdoing within this encounter; the translation does not reverse the parties or turn neighbor into a named relative.',
'The man challenges Moses’s authority as ruler and judge and compares a threatened killing with yesterday’s Egyptian death. Moses fears and asks whether the matter has become so evident. Keep the question and the source’s yesterday rather than treating the challenge as a completed second killing.',
'Pharaoh hears and seeks Moses’s death. Moses withdraws from his presence and resides in Midian, then the arrival in Midian is repeated before sitting at the well. The deliberate repetition is preserved; it is not treated as an accidental duplicate to remove.',
'The priest has seven daughters tending their father Jethro’s sheep. They draw until the troughs are filled, and the Greek repeats father Jethro in the watering purpose. Retain both name occurrences and seven; do not harmonize the different paternal name that follows in 2:18.',
'The shepherds drive the women away; Moses rises, rescues them, draws water and waters their sheep. The Greek expressly includes his drawing water. Retain all actions rather than summarize rescue alone or attribute the watering back to the shepherds.',
'The daughters come to their father Reuel, who asks why their return was quick today. Preserve Reuel here alongside the Jethro wording in 2:16; the present record does not establish an alias, family reconstruction or textual solution.',
'The women call their rescuer an Egyptian man and recount rescue, drawing water and watering their sheep. Egyptian is their reported identification; it does not override the narrator’s earlier Levite ancestry. All three actions correspond to 2:17.',
'The father asks where the man is and why they left him in this manner, then commands an invitation so he may eat bread. Propose like this to represent the manner adverb lost in the inherited question. Bread remains the concrete food/meal expression, without inventing a larger feast.',
'Moses is settled with the man, who gives his daughter Zipporah as wife. The inherited intransitive settled is natural for the Greek passive without naming an unstated resettling agent. Zipporah’s established English name is retained; similarity to the midwife name does not establish identity.',
'The woman conceives and bears a son; Moses names him Gershom and explains his sojourner status in a foreign land. The speech is first person and present. The selected verse contains no second son, so no additional birth is imported here.',
'After many days the Egyptian king dies. Israel groans deeply and cries because of labor, and the labor-related cry rises to God. The causal phrase is repeated and preserved. The king’s death is not silently equated with an end to oppression.',
'God hears the groaning and remembers His covenant with Abraham, Isaac and Jacob. God is repeated as grammatical subject, and all three patriarchs remain named. Remembered is narrative covenant language; the translation adds no theory of previous divine forgetfulness.',
'God looks on Israel and becomes known to them: the final verb is passive in the selected Greek. Preserve the manifestation/recognition wording instead of replacing it with the familiar active God knew. The manner of becoming known is not explained in this verse.',
]}
CLOSE={
'1:1':'These are the names of the sons of Israel who had entered Egypt together with Jacob their father—each with his entire household entered—:',
'1:21':'Since the midwives feared God, they made houses for themselves.',
'2:5':'Pharaoh’s daughter came down to bathe at the river, and her attendants walked beside the river. Seeing the basket in the marsh, she sent her attendant and took it up.',
'2:21':'Moses was settled with the man, who gave his daughter Zipporah to Moses as wife.',
}
OPEN={'1:15':['Ethnic identity of midwives is not determined solely by of the Hebrews.'], '1:21':['Literal houses versus a domestic/household sense.'], '2:3':['Precise ancient basket and coating materials; no new specialist lookup.'], '2:6':['Contextual compassion/spare choice; full lexical study remains open.'], '2:16':['Jethro/Reuel name relationship remains unresolved; preserve both source names.'], '2:18':['Relationship of Reuel here to Jethro in 2:16; no apparatus solution claimed.']}
book=json.loads((ROOT/'exodus/verses.json').read_text(encoding='utf-8'))
records=[]
for chapter in book['chapters'][:2]:
    c=chapter['chapter']
    assert len(chapter['verses'])==len(NOTES[c])
    for n,(v,analysis) in enumerate(zip(chapter['verses'],NOTES[c]),1):
        ref=f'{c}:{n}'
        candidate=v['text'].replace('Why have you left the man behind?', 'Why have you left the man behind like this?') if ref=='2:20' else v['text']
        records.append({'record_type':'focused_running_text_comparison','review_id':f'OT-011-exodus-{c}-{n}','book_id':'exodus','reference':v['reference'],'verse_anchor':v['id'],'reading_section_id':str(c),
          'baseline_commit':BASELINE,'baseline_text':v['text'],'candidate_text':candidate,'candidate_sha256':hashlib.sha256(candidate.encode()).hexdigest(),'decision':'propose_revision' if candidate!=v['text'] else 'retain_provisionally',
          'source':{'edition':'Rahlfs–Hanhart 2006','url':f'https://www.die-bibel.de/en/bible/LXX/EXO.{c}','accessed_on':'2026-11-12','running_text_read':True,'apparatus_consulted':False},
          'drafts':{'close':CLOSE.get(ref,candidate),'spoken':candidate,'literary':candidate},'draft_policy':'Identical stages deliberately retain source-compatible inherited phrasing after comparison. These are AI working stages, not three human reviews.',
          'analysis':analysis,'unresolved_questions':OPEN.get(ref,[]),'review':{'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Verse-specific running-text comparison; not full token alignment.','all_tokens_accounted_for':False,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
          'benchmark_change':False,'publication':{'staging':None,'production':None}})
assert len(records)==47
(HERE/'focused-reviews.json').write_text(json.dumps({'batch_id':'OT-011','scope':'Exodus 1–2','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Exodus 1–2: 47 comparisons; 46 retained, one proposal; no acceptance credited.')
