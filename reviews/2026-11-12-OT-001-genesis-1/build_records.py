"""Reproduce the manually authored Genesis 1 comparison records."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"

# These are passage-specific translations and observations, not generated glosses.
# The whole publisher running text was read before this record was written.
ROWS = [
    ("In the beginning God made the heaven and the earth.", "The opening temporal phrase qualifies God's act of making; the subject is God and the two coordinated objects are heaven and earth. English normally omits the Greek articles with these cosmic nouns. The inherited 'made' represents the verb without replacing it with an etymological or doctrinal explanation. Retain the familiar cadence; this clause alone does not specify a philosophical account of creation."),
    ("Now the earth was unseen and unprepared, and darkness was over the abyss, and a spirit of God was moving over the water.", "The contrastive connective introduces the earth's condition. The two adjectives describe it as unseen and not prepared or formed: 'unseen and unformed' is a defensible contextual rendering, not the different Hebrew-based formula 'formless and void.' The imperfect of the movement verb describes an ongoing scene without specifying a bird or adding creative action. 'Spirit of God' retains the benchmark interpretation; 'a spirit/breath/wind of God' remains a translation question because absence of the article alone settles neither reference nor capitalization. 'Deep' renders the abyss; singular water is retained."),
    ("And God said, 'Let light come to be.' And light came to be.", "The divine command and its fulfillment use related forms of the same verb. The established 'Let there be light / there was light' communicates the command/result and preserves the repeated light. No 'again,' elapsed period, or explanatory actor is added."),
    ("And God saw the light, that it was good; and God separated between the light and between the darkness.", "The first clause evaluates the light; the second names God again as the agent of separation. English 'divided the light from the darkness' realizes the repeated 'between' construction idiomatically, without claiming the dark was called evil. The second divine subject remains explicit."),
    ("And God called the light Day, and the darkness He called Night. And evening came, and morning came: one day.", "Both naming clauses and both coming-to-be clauses remain visible. The last expression uses the cardinal 'one,' unlike the subsequent ordinal days; preserve 'one day' rather than normalize it to 'the first day.' Capitalized Day and Night are editorial naming conventions, not a Greek manuscript distinction."),
    ("And God said, 'Let a firmament come to be in the midst of the water, and let it separate between water and water.' And it was so.", "The firmament is commanded into existence and assigned a separating function. 'Firmament' preserves the established traditional term; its contextual sense is the sky structure separating waters, not an inserted modern scientific mechanism. The command's two clauses and the Greek fulfillment sentence at this verse are retained. The supplied English subject in 'let it divide' realizes the Greek participial construction."),
    ("And God made the firmament, and separated between the water that was beneath the firmament and the water above the firmament.", "The Greek names God as subject in the first clause; that subject governs the following separation verb. The inherited English supplies God again to make the same referent explicit, rather than reflecting a second occurrence of the Greek noun. Firmament recurs in both water descriptions. 'Beneath' and 'above' preserve the opposing locations; the relative clause 'that was' can be represented by the English prepositional modifier without changing its referent."),
    ("And God called the firmament Heaven. And God saw that it was good. And evening came, and morning came: a second day.", "The selected Greek contains the evaluation 'God saw that it was good' here; preserve it even where another textual tradition omits it. Naming, evaluation, and the doubled evening/morning formula remain distinct. The final day expression is ordinal, unlike verse 5."),
    ("And God said, 'Let the water beneath heaven be gathered into one gathering, and let dry land appear.' And it was so. And the water beneath heaven was gathered into its gatherings, and dry land appeared.", "The command speaks of one gathering; the fulfillment has plural gathering places. The inherited wording preserves this number difference and the expanded Greek fulfillment rather than harmonizing it with a shorter tradition. 'Place' and 'gathering places' express the result/location sense of the gathering noun; the close draft makes the repeated lexical relationship visible. 'Dry land' supplies the natural English head noun for the substantivized adjective."),
    ("And God called the dry land Earth, and the collections of waters He called Seas. And God saw that it was good.", "The naming clauses distinguish dry land from collected waters. 'Gathered waters' expresses the collections as an English noun phrase; Seas remains plural. The evaluation concerns the resulting scene; no causal or theological explanation is added."),
    ("And God said, 'Let the earth sprout grassy vegetation sowing seed according to kind and according to likeness, and a fruit-bearing tree making fruit, whose seed is in it according to kind upon the earth.' And it was so.", "The command includes vegetation, seed, kind and likeness, and fruit-bearing trees whose seed is within. The benchmark's collective vegetation and plural trees are natural English for the source's collective categories. 'Each' distributes the tree description rather than adding a new botanical claim. Grass/herbage is compressed into 'vegetation'; whether 'grassy vegetation' would better preserve the nested phrase remains a lexical question for specialist review. The repeated kind/likeness wording is retained rather than abbreviated to a single classification."),
    ("And the earth brought forth grassy vegetation sowing seed according to kind and according to likeness, and a fruit-bearing tree making fruit, whose seed is in it according to kind upon the earth. And God saw that it was good.", "The fulfillment substantially repeats the command rather than replacing it with a summary. The inherited wording maintains the sequence vegetation, sowing, kind, likeness, tree, fruit and seed within. The collective and grammatical choices are the same as verse 11; the open question about the grassy/herbage description applies here too. The closing evaluation remains a separate clause."),
    ("And evening came, and morning came: a third day.", "The two repeated event clauses and the ordinal third remain. 'There was' is the accepted English realization of the coming-to-be formula; no duration beyond the text's day label is supplied."),
    ("And God said, 'Let lights come to be in the firmament of heaven for illumination of the earth, to separate between the day and the night; and let them be for signs and for seasons and for days and for years.'", "The selected Greek expressly includes illumination of the earth before the day/night purpose. The benchmark retains it and all four functions: signs, seasons, days, years. 'Seasons' is a contextual reading of appointed times; neither a festival calendar nor astronomical detail is inserted. The period before 'Let them serve' provides a spoken clause boundary for the second coordinated command; the speech continues into verse 15."),
    ("And let them be for illumination in the firmament of heaven, so as to shine upon the earth.' And it was so.", "The illumination function is repeated from verse 14 and followed by its purpose. 'Be lights ... to shine' preserves this rather than deleting a seeming redundancy. The speech closes here and the narrator's fulfillment clause follows; the boundary must survive export."),
    ("And God made the two great lights, the great light for rule of the day and the lesser light for rule of the night, and the stars.", "The Greek labels both lights great, then describes the first as great and the second with a comparative lesser. The inherited 'greater' makes the contextual comparison explicit; it is an English relational rendering, not the exact morphology of the first adjective. 'To rule' expresses the assigned function. 'He made' before stars supplies the verb already governing that final coordinated object; it does not add a second event. Sun and moon are not named in the source or inserted here."),
    ("And God placed them in the firmament of heaven, so as to shine upon the earth,", "God remains the subject, the lights the object, and shining on the earth the purpose. The comma deliberately carries the purpose sequence into verse 18; the verse boundary is not a sentence boundary."),
    ("and to rule the day and the night, and to separate between the light and the darkness. And God saw that it was good.", "The two coordinated infinitives continue verse 17's purpose clause. English 'to rule ... and to divide' preserves their parallelism. The Greek introduces this verse with 'and'; in the inherited sentence the comma plus continuation of the infinitive series serves this connection. The final evaluation is a new finite clause with God as explicit subject."),
    ("And evening came, and morning came: a fourth day.", "Retain the doubled formula and the ordinal fourth. No extra liturgical response or 'behold' is introduced for cadence."),
    ("And God said, 'Let the waters bring forth moving creatures of living beings, and birds flying upon the earth along the firmament of heaven.' And it was so.", "The Greek command makes waters the subject of bring forth and coordinates the living moving creatures and flying birds. The inherited English keeps that relation rather than silently changing to a separate command 'let birds fly.' 'Across' gives an intelligible spatial rendering of the phrase with firmament; its precise spatial nuance remains open. The fulfillment sentence belongs to the selected Greek and remains present."),
    ("And God made the great sea creatures and every living being of moving animals which the waters brought forth according to their kinds, and every winged bird according to kind. And God saw that they were good.", "The sea-creature term is not narrowed to modern whales; the collective living/moving phrase and waters as producer are retained. The Greek alternates plural kinds for the aquatic creatures and singular kind for the bird category, reflected in the English. The evaluation is plural 'good'; 'they were good' makes that natural in English."),
    ("And God blessed them, saying, 'Grow and multiply and fill the waters in the seas, and let the birds multiply upon the earth.'", "The blessing contains three plural commands and then a separate third-person command for the birds. 'Grow' preserves the source's growth verb without substituting a different Hebrew-based formula automatically. 'Let the birds multiply' keeps the change in grammatical person. Divine speech to creatures takes ordinary imperatives, not Thou forms."),
    ("And evening came, and morning came: a fifth day.", "Both event clauses and the fifth-day ordinal remain as in the recurring formula. The elevated cadence is achieved through source repetition, not additional words."),
    ("And God said, 'Let the earth bring forth a living being according to kind: four-footed animals and creeping things and wild beasts of the earth according to kind.' And it was so.", "The source introduces a singular collective living being before the category list. English plural 'living creatures' renders the collective category, not an added claim about a single individual. Four-footed animals are retained rather than prematurely equated with domesticated cattle; the following verse uses a different livestock term. The repeated kind formula and fulfillment remain."),
    ("And God made the wild beasts of the earth according to kind, and the cattle according to kind, and all the creeping things of the earth according to their kind. And God saw that they were good.", "Propose singular 'their kind' in the final classification phrase: the Greek has singular kind with plural their, unlike the plural kinds in 1:21. The singular English is intelligible for a distributed class and preserves this source distinction. The three animal classes and repeated kind formulas remain. 'All' qualifies the creeping things here. 'Cattle' keeps the established broader traditional livestock term; its possible modern narrowing should be checked at read-aloud review. Plural 'they were good' reflects the plural evaluation."),
    ("And God said, 'Let Us make a human being according to Our image and according to likeness, and let them rule the fish of the sea and the birds of heaven and the cattle and all the earth and all the creeping things that creep upon the earth.'", "The source switches from a singular collective human term to plural 'let them rule.' The inherited 'man ... them' preserves that structure but 'man' here denotes humanity, not males alone, as verse 27 confirms. Us/Our capitalization follows the benchmark and does not establish the identity of the plural speakers. The phrase about likeness shares the image phrase's possessive sense in English. The object list includes all the earth; it must not be dropped to match another tradition."),
    ("And God made the human being; according to God's image He made him; male and female He made them.", "The source repeats the making verb three times and shifts singular him to plural them. The benchmark retains both repetition and number, and the explicit male/female pair. 'Man' is the collective human referent established in verse 26. No explanatory claim about social roles is inserted into the text."),
    ("And God blessed them, saying, 'Grow and multiply and fill the earth and subdue it, and rule the fish of the sea and the birds of heaven and all the cattle and all the earth and all the creeping things that creep upon the earth.'", "The five coordinated plural imperatives are preserved, with a sentence break for natural speech before rule. The selected Greek repeats all with cattle, earth and creeping things, and the benchmark retains the broad list. Subdue and rule are not softened into an unexpressed ethical paraphrase; interpretation belongs outside the translation."),
    ("And God said, 'Behold, I have given you every seed-bearing plant sowing seed which is upon all the earth, and every tree which has in itself fruit with seed for sowing; it shall be food for you,", "The demonstrative attention word, completed giving, plural recipients and two food categories are retained. 'Plant sowing seed' represents the plant adjective and participle together. In the tree phrase the adjective qualifies the seed as suitable for sowing; 'fruit with seed for sowing' restructures the genitive phrase into intelligible English. The literary draft compresses that quality to 'containing seed'; this remains a point for lexical review. The future 'shall be' is retained. The sentence continues into the animals' allocation in verse 30."),
    ("and to all the wild beasts of the earth and to all the birds of heaven and to every creeping thing that creeps upon the earth which has in itself a living soul, every green plant for food.' And it was so.", "The repeated dative recipients continue the giving verb in verse 29; the inherited 'I have given' makes that governing verb audible across the verse boundary and is grammatically supplied, not a new Greek verb here. 'Has life within it' represents the living-being/life expression without importing an immortal-soul doctrine. The close draft's living soul refers to animate life, not the different breath noun in Genesis 2:7. 'Every' distributes the animal classes and green plants. The fulfillment returns to narration after the quotation."),
    ("And God saw all the things that He had made, and behold, they were very good. And evening came, and morning came: a sixth day.", "The whole set of things made is evaluated. Greek plural 'good' is naturally collective English 'it was very good' in the benchmark; the intensifier very and behold are both warranted here. Both repeated event clauses and the ordinal sixth remain. No retrospective commentary is added."),
]

baseline = json.loads((ROOT / "genesis/verses.json").read_text(encoding="utf-8"))
units = baseline["chapters"][0]["verses"]
assert len(units) == len(ROWS) == 31
records = []
for verse, (close, analysis) in zip(units, ROWS):
    candidate = verse["text"].replace("their kinds", "their kind") if verse["id"] == "v1-25" else verse["text"]
    changed = candidate != verse["text"]
    records.append({
        "record_type": "focused_running_text_comparison",
        "review_id": "OT-001-genesis-" + verse["id"].removeprefix("v"),
        "batch_id": "OT-001",
        "book_id": "genesis",
        "reference": verse["reference"],
        "verse_anchor": verse["id"],
        "reading_section_id": "1",
        "baseline_commit": BASELINE,
        "baseline_text": verse["text"],
        "candidate_text": candidate,
        "candidate_sha256": hashlib.sha256(candidate.encode()).hexdigest(),
        "decision": "propose_revision" if changed else "retain_provisionally",
        "source": {
            "edition": "Rahlfs–Hanhart 2006",
            "url": "https://www.die-bibel.de/en/bible/LXX/GEN.1",
            "accessed_on": "2026-11-12",
            "running_text_read": True,
            "apparatus_consulted": False,
        },
        "drafts": {"close": close, "spoken": candidate, "literary": candidate},
        "analysis": analysis,
        "review": {
            "reviewer": "OpenAI Codex assistant",
            "type": "AI",
            "scope": "Whole-verse running-text comparison and independently phrased close draft; not exhaustive token alignment or specialist certification.",
            "all_tokens_accounted_for": False,
            "independent_greek": None,
            "human_read_aloud": None,
            "editorial_acceptance": None,
        },
        "benchmark_change": changed,
        "publication": {"staging": None, "production": None},
    })

payload = {
    "batch_id": "OT-001",
    "scope": "Genesis 1:1–31",
    "status": "focused_comparison_and_close_drafts_prepared_full_alignment_pending",
    "baseline_commit": BASELINE,
    "records": records,
}
(HERE / "focused-reviews.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(f"Wrote {len(records)} Genesis 1 focused comparisons; 30 readings retained, one revision proposed.")
