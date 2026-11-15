"""Authored Genesis 4 source comparison; regeneration does not perform review."""
from pathlib import Path
import json, hashlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = '39a2bb990f252f9c867879f14942b200c4a86aa5'
notes = [
"The source names Adam and Eve and uses knowing for sexual union, followed by conception and birth. The speech uses acquired/gained a human being through God, not a replacement of the divine title by a Hebrew name. Retain gained and through, with the agency of the final phrase explicit but without expanding it to a claim about the child's identity.",
"The added-to-give-birth idiom warrants again here. Abel is explicitly Cain's brother. Abel becomes a sheep shepherd while Cain is described as working the earth; the adversative connective and contrasting occupations are retained. The English narrative past realizes the Greek ongoing description of Cain's work without adding a new occupation.",
"The temporal transition is after days, followed by Cain bringing an offering from the earth's fruits to the Lord. Some time is intelligible for the indefinite interval; it does not specify a festival or harvest date. Offering renders the sacrificial noun broadly enough for produce; no animal is supplied.",
"Abel himself also brings from the firstborn of his sheep and their fat. The English repeats offering from the preceding sentence as the governing sense of what was brought. The second clause names God and calls the objects gifts. Looked with favour is a contextual rendering of the regard shown; the next verse establishes the contrast. It is not a claim that a separate Greek word for favour occurs here.",
"The contrast is between regard for Abel and no attention to Cain and his offerings. Cain's great distress and fallen face follow. Retain distressed rather than importing an anger term from another tradition. The Greek construction about distress is less direct than the English passive; the experiencer is still Cain. His face is not described as changing color.",
"The speaker is the Lord God; both why questions are present. The first concerns Cain's becoming deeply distressed and the second his fallen face. The inherited present-state English represents the resulting condition without inventing a motive. The divine question continues into the next verse.",
"The selected Greek frames a negative rhetorical question around offering rightly and failing to divide rightly, then commands stillness and states a turning toward Cain and his future rule. The 19 source tokens are accounted for in the review record; this is not an apparatus judgment. Retain the inherited reading provisionally. The antecedent of the two third-person pronouns is unresolved; him must not silently be glossed Abel, sin, or the offering. The first turning clause is verbless; shall be is supplied from the prospective setting, while the following rule verb is explicitly future. The text does not contain the familiar alternate image of sin crouching at a door.",
"Cain's invitation to the field is present in the selected Greek and must not be removed to match a shorter tradition. The temporal clause places both brothers in the field before Cain rises against Abel and kills him. Repeated brother emphasizes their relationship. Slew is an established traditional equivalent for killed, without a claim about the weapon or method.",
"God asks where Abel your brother is. Cain denies knowing and asks whether he is his brother's keeper. The Greek negative-question particle expects a negative answer in Cain's response; a rhetorical English question carries that stance without adding commentary or affirming that his answer is true.",
"The voice of the brother's blood is singular and cries from the earth to God. The English preserves the personification, the source of the cry and its destination. The first question concerns Cain's action. No claim about the audible physical nature of blood or an added plurality of murdered descendants belongs in the translation.",
"The declaration uses cursed from the earth, then personifies the earth as opening its mouth to receive the blood from Cain's hand. Keep both from phrases, the brother relationship and the hand image. The preposition after cursed can invite discussion of exclusion from the soil or the ground's involvement; do not resolve that question by replacing it with a different comparative construction.",
"The tilling clause is introduced by an explanatory connective and leads to the ground no longer giving its strength. The inherited when gives the recurring circumstance naturally; for/because is the closer connective and remains an alternative for syntax review. The concluding state is groaning and trembling upon the earth, not an imported fugitive/wanderer pair. The close draft exposes the connective rather than silently claiming the two constructions identical.",
"The comparison is my guilt/charge greater than my being forgiven. Guilt is a provisional sense of the accusation/responsibility noun; the infinitive is passive and its person is Cain. Retain too great for me to be forgiven instead of automatically importing punishment too great to bear. Whether the line is a despairing assertion or would benefit from interrogative English remains open; the printed running text uses a declarative presentation.",
"The selected Greek begins with if and continues with hiding from the divine face, groaning and trembling, and the threat from every finder. Thou/Thy properly address God singularly. Whoever represents the distributive every person finding me. Preserve the conditional opening rather than turning it into an unqualified historical claim that expulsion has already occurred.",
"The response opens not so and contains a difficult sevenfold-vengeance construction, followed by the Lord God's placing a sign for Cain to prevent his killing by a finder. The inherited incur sevenfold vengeance is retained provisionally as the contextual consequence for the killer, not certified as a transparent word-for-word rendering of the unusual Greek verb/object combination. Mark does not identify a body location, physical form, ethnicity or hereditary trait. The difficult vengeance clause requires specialist and apparatus review.",
"Cain leaves God's face/presence and lives in the land whose Greek name is Naid, opposite Edem. Retain established English Nod/Eden as name-authority forms rather than normalizing all names to fresh transliterations. Opposite is the selected spatial wording; do not silently substitute east simply because it is familiar from another source.",
"The conception/birth sequence names Enoch. The city-building description is durative in form: he was building, followed by naming it after his son. The implied builder is naturally Cain in context; the text does not quantify the city's inhabitants or say it was completed before the naming. The inherited chronology remains intact.",
"The genealogy contains Enoch, Gaidad, Maiel, Methuselah and Lamech in that order, with four linked generations after Enoch. Gaidad and Maiel reflect the selected Greek names and are not silently changed to conventional alternate forms. The repeated begetting relation is retained. Similar names in another genealogy do not establish personal identity.",
"Lamech takes two wives for himself. The source calls one Adah and the second Zillah; the inherited first is the natural counterpart to second rather than a separately attested ordinal. Both women remain distinct. The verse reports the action without added evaluation or an explanation of legal status.",
"Adah bears Jabal, identified as father of tent-dwelling livestock keepers. The inherited coordination dwell in tents and keep livestock expresses the two linked descriptors. Father is retained as the source's ancestral/origin expression without inserting an exclusive claim that no earlier person used a tent or kept an animal.",
"The brother is Jubal, and the source uses a demonstrating/introducing verb with psaltery and lyre. Introduced is retained provisionally; the text does not require invented to mean no preceding instrument existed. These are plucked-string instrument terms, not a substituted modern keyboard or generic music claim. Instrument identification remains a specialist question.",
"Zillah also bears Thobel. The source describes hammer work and smithing in bronze and iron, and names Noema as his sister. The inherited Thobel/Naamah uses the existing name policy and retains the selected source's shorter male name; do not insert Cain. With the hammer realizes the hammer-worker description rather than adding an independently narrated action.",
"The speech addresses Adah and Zillah in parallel hearing clauses and repeats first-person injury language. Retain the unusual to my own hurt/bruising as a provisional rendering rather than silently changing it to because he wounded me. Whether the injury phrases state result, disadvantage or the occasion of the killing is unresolved. The paired man/young man may be poetic parallelism; the translation does not decide that there were two killings. Existing poetic line breaks must be preserved.",
"The Greek uses a perfect vengeance verb with from Cain and from Lamech, not Cain as its explicit subject, and expresses seventy times seven. The inherited Cain has been avenged is retained only provisionally: its implied beneficiary/subject interpretation needs review against the from construction. The close alternative exposes that preposition without resolving whether it denotes source, agency or an exaction from the named person. This is Lamech's poetic claim, not a new narrator endorsement or divine promise.",
"Adam again appears with Eve, conception and a son's birth. The source at this point does not add the adverb again, so none is introduced into the verse. The feminine speaking participle identifies the mother's naming explanation: God has raised up another seed in Abel's place, whom Cain killed. Seed and raised up preserve the Greek imagery without forcing an individual messianic referent.",
"A son is born to Seth, receives the name Enosh, and this man hoped to call upon the Lord God's name. The selected Greek hope verb is retained; it is not replaced with the familiar began formulation. He naturally refers to Enosh, but the evidence does not warrant a historical claim that no one previously invoked God. Lord God remains the actual pair of titles.",
]
close_overrides = {
    3: 'And it came to pass after some days that Cain brought an offering to the Lord from the fruits of the earth.',
    7: 'If you offer rightly but do not divide rightly, have you not sinned? Be still. Toward you is his turning, and you shall rule over him.”',
    12: 'For you till the earth, and it shall no longer give you its strength. You shall be groaning and trembling upon the earth.”',
    19: 'And Lamech took two wives for himself. The name of the one was Adah, and the name of the second was Zillah.',
    24: 'For vengeance has been exacted sevenfold from Cain, but from Lamech seventy times seven.',
}
uncertain = {
    7: ['Pronoun antecedents; offering/dividing construction; precise force of turning; implied time of the verbless clause.'],
    11: ['Force of from after cursed.'],
    12: ['Explanatory connective versus temporal English when.'],
    13: ['Sense of guilt/charge and declarative versus interrogative presentation.'],
    15: ['Unusual sevenfold-vengeance verb/object construction; mark form unspecified.'],
    21: ['Exact ancient instrument identification and force of introduced.'],
    23: ['Injury phrases and whether man/young man are parallel referents.'],
    24: ['Force of from Cain / from Lamech and whether the inherited passive subject correctly represents the construction.'],
}
# Complete running-text token accounting for the hard opening calibration verse.
# Morphology is AI analysis, not a consulted morphological database.
token_rows = [
('οὐκ','οὐ','negative particle','not','grammatical','Moved to the English rhetorical question about sinning.'),
('ἐὰν','ἐάν','conditional conjunction','If','explicit','Introduces the conditional protasis.'),
('ὀρθῶς','ὀρθῶς','adverb','rightly','explicit','First rightly modifies offering.'),
('προσενέγκῃς','προσφέρω','aorist active subjunctive second singular','you offer','explicit','The conditional form does not itself assert that Cain did offer rightly.'),
('ὀρθῶς','ὀρθῶς','adverb','rightly','explicit','Second rightly modifies dividing and remains repeated.'),
('δὲ','δέ','postpositive connective','but','explicit','Contrast within the condition.'),
('μὴ','μή','negative particle','do not','grammatical','Negates dividing in the subjunctive condition.'),
('διέλῃς','διαιρέω','aorist active subjunctive second singular','you ... divide','explicit','Do is English auxiliary support; the precise ritual division is not supplied.'),
('ἥμαρτες','ἁμαρτάνω','aorist active indicative second singular','have you ... sinned','explicit','English perfect gives the present consequence in the rhetorical question.'),
('ἡσύχασον','ἡσυχάζω','aorist active imperative second singular','Be still','explicit','Command to settle/be still without inventing an object or duration.'),
('πρὸς','πρός','preposition with accusative','toward','explicit','Direction of the turning.'),
('σὲ','σύ','second-person singular accusative pronoun','you','explicit','Addressee of the preposition is Cain.'),
('ἡ','ὁ','feminine nominative singular article','His turning','grammatical','English possessive construction replaces a separate definite article.'),
('ἀποστροφὴ','ἀποστροφή','feminine nominative singular noun','turning','explicit','Nominal clause has no expressed verb; shall be is prospective English supply.'),
('αὐτοῦ','αὐτός','third-person singular genitive pronoun, masculine/neuter form','His','explicit','Antecedent unresolved; capitalization is only sentence-initial.'),
('καὶ','καί','coordinating conjunction','and','explicit','Links the final rule statement.'),
('σὺ','σύ','second-person singular nominative pronoun','you','explicit','Explicit subject contrasts with the preceding third-person referent.'),
('ἄρξεις','ἄρχω','future active indicative second singular','shall rule over','explicit','Future and government of the genitive realized by the English phrase.'),
('αὐτοῦ','αὐτός','third-person singular genitive pronoun, masculine/neuter form','him','explicit','Object of rule; masculine English follows inherited choice but referent remains open.'),
]
book = json.loads((ROOT/'genesis/verses.json').read_text(encoding='utf-8'))
verses = next(c['verses'] for c in book['chapters'] if c['chapter']==4)
assert len(verses)==len(notes)==26
records=[]
for n,(v,note) in enumerate(zip(verses,notes),1):
    text=v['text']
    record={
      'record_type':'focused_running_text_comparison', 'review_id':f'OT-004-genesis-4-{n}',
      'book_id':'genesis','reference':v['reference'],'verse_anchor':v['id'],'reading_section_id':'4',
      'baseline_commit':BASELINE,'baseline_text':text,'candidate_text':text,
      'candidate_sha256':hashlib.sha256(text.encode()).hexdigest(),'decision':'retain_provisionally',
      'source':{'edition':'Rahlfs–Hanhart 2006','url':'https://www.die-bibel.de/en/bible/LXX/GEN.4','accessed_on':'2026-11-12','running_text_read':True,'apparatus_consulted':False},
      'drafts':{'close':close_overrides.get(n,text),'spoken':text,'literary':text},
      'draft_policy':'Stages retain identical wording where the source comparison supports the inherited English; close alternatives expose selected constructions. These are AI working stages, not human read-aloud results.',
      'analysis':note,'unresolved_questions':uncertain.get(n,[]),
      'review':{'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Verse-specific Greek running-text comparison; verse 7 additionally has all 19 source tokens aligned.','all_tokens_accounted_for':n==7,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
      'benchmark_change':False,'publication':{'staging':None,'production':None}}
    if n==7:
        record['greek_tokens']=[{'token_id':f'GEN-4-7-{i:02d}','form':a,'lemma':b,'morphology':c,'english_spans':d.split(' ... '),'realization_type':e,'rationale':f} for i,(a,b,c,d,e,f) in enumerate(token_rows,1)]
        record['supplied_english']=[{'text':'shall be','rationale':'The turning clause is verbless; prospective time is inferred from the following future rule clause. The close draft uses is to expose this choice.'}]
        record['token_scope']='Whitespace-separated lexical tokens of the displayed verse; punctuation represented by English clause boundaries. The 19-word excerpt is the bounded source quotation for this batch.'
    records.append(record)
(HERE/'focused-reviews.json').write_text(json.dumps({'batch_id':'OT-004','scope':'Genesis 4:1–26','status':'provisional_draft_review_pending','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Genesis 4: 26 retained candidates; one verse with 19 token alignments; unresolved decisions remain open.')
