"""Build the bounded Genesis 2–3 proposal records from the preserved benchmark."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"

# These are individual observations made after reading the publisher's two
# complete running-text chapters on 12 November 2026. They are not token audits.
NOTES = {
    "2:1": "The passive completion clause includes heaven, earth and their whole ordered array. 'Thus' realizes the opening connective as a narrative conclusion, while 'ordered array' represents the arrangement/content sense of kosmos without importing a modern astronomical definition. No change is proposed; this observation does not settle every possible sense of kosmos.",
    "2:2": "The displayed Greek says sixth day for completion and seventh day for cessation. Both distinct days and the repeated works clauses are retained. 'Rested from' represents cessation from the works; it should not be expanded into an assertion of divine fatigue. No Hebrew-based seventh-day substitution is proposed, and no variant apparatus was consulted.",
    "2:3": "Blessing and hallowing are separate actions; the causal clause explains the sanctification of the seventh day. The unusual 'had begun to make' follows the displayed Greek beginning verb rather than harmonizing the clause to a more familiar English Bible. The temporal relation is represented naturally with English past perfect. Fuller lexical and aspect review remains open.",
    "2:4": "The book/origin formula and its temporal introduction are present. This unit ends with a comma because the objects of 'made' continue into 2:5; it should not be treated as a self-contained sentence. The source names God here without Lord, and the inherited wording preserves that distinction. The singular Greek coming-to-be expression is rendered naturally with its coordinated English antecedents.",
    "2:5": "The plants belong syntactically with the preceding making clause; the two 'before' expressions and the reasons concerning rain and a human cultivator are retained. 'Every green plant' and 'every plant' leave the two expressions recognizably distinct without inventing a botanical taxonomy. The punctuation is an English readability decision. Detailed construction alignment remains pending.",
    "2:6": "The source presents a spring rising from the earth and watering its entire face. The inherited rendering preserves spring rather than substituting the familiar mist reading, and 'whole face' keeps the source's image. The imperfect verbs describe the scene; simple English past is acceptable here, with 'was rising/was watering' a possible aspect-explicit alternative that is not required to establish continuous action.",
    "2:7": "The sequence is formation from earth's dust, breathing life's breath into the face, and becoming a living soul. The source says face rather than nostrils, and the English preserves that reading. 'Living soul' follows the established register; 'living being' is a translation alternative, not evidence for a separate substance being added. The construction does not by itself settle a philosophical account of human composition.",
    "2:8": "Lord God is explicit, with planting, an eastern location in Eden, and placement of the formed human. 'Toward the east' follows the spatial reading of the directional expression. Garden is the established rendering of paradeisos and is retained rather than introducing a claim about a later afterlife sense. Eden spelling follows the inherited name authority pending a complete names register.",
    "2:9": "The inherited wording accounts for the trees' visual beauty, food, life and knowledge, but leaves the source's eti unexpressed. Propose 'also caused' to preserve its additive force, consistent with 'also formed' in 2:19. The knowledge-tree construction is compressed into intelligible English without claiming its syntax has no difficulty. 'Knowledge' remains preferable here to adding moral autonomy or an explanation of the tree's power.",
    "2:10": "The source shifts to present-tense geographical description, which the English preserves in 'flows' and 'divides'. Four branches is a contextual river rendering of the four beginnings/heads expression; it is not a claim that the Greek uses the ordinary noun for a tree branch. The purpose of watering the garden remains explicit. No modern river identification is added.",
    "2:11": "Pishon, Havilah, the whole surrounding land, and the gold location are preserved under inherited English naming conventions. 'First' renders the first member of the four-river enumeration, whose Greek is literally 'one'. The name forms are not silently standardized to transliteration. Identifying a particular modern river or territory would require evidence beyond this running-text comparison.",
    "2:12": "The goodness of the gold and two stone expressions are retained. 'Carbuncle' is a traditional rendering of anthrax in a gemstone context, not a verified modern mineral identification; 'green stone' deliberately remains broad. Modern readers may mistake carbuncle for a skin condition, so a terminology note or a later reviewed replacement is needed. No specialist mineralogical or lexicon source was consulted here.",
    "2:13": "The second river, Gihon, encircles the whole land named Ethiopia in the Greek. The established geographical name is retained rather than automatically changing it to Cush or assigning modern national borders. The verse's coordination with the preceding river description is clear through the continued enumeration even without an extra initial 'And'. Exact historical geography remains outside this comparison.",
    "2:14": "The third/fourth ordering, Tigris, Euphrates and the directional relationship to the Assyrians are represented. 'Opposite Assyria' is a contextual geographical rendering; 'east of' would be more specific than the wording alone establishes. The Greek uses the people designation, so the territorial English form is an interpretive simplification to retain for specialist geographical review.",
    "2:15": "The Lord God's taking and placing actions and the two purposes of working and guarding the garden are preserved. 'Tend' is a contextual rendering of working/cultivating; 'keep' carries the guarding sense but may benefit from explanation to present-day readers. The relative clause 'whom He had formed' is present in the displayed Greek and correctly remains in the English.",
    "2:16": "The command explicitly names Adam. The eating noun-plus-verb construction is represented by the permissive emphasis 'may freely eat'; it does not introduce freedom from every later restriction. The addressee is singular in this verse. Ordinary 'you' follows the standard because God is speaking to a human, while the following verse's plural must be recorded rather than silently normalized.",
    "2:17": "The prohibition and emphatic death warning are retained. Unlike 2:16, the displayed prohibition, eating condition and death verb address a plural 'you'; English you is number-neutral, so no singular Thou is introduced. This number shift needs a reader/review note. 'Surely die' realizes the death noun-plus-verb emphasis. The temporal clause does not by itself resolve the narrative or theological manner of dying.",
    "2:18": "The not-good judgment, the human's solitude and the plural 'Let Us make' all remain explicit. 'Corresponding to him' renders the relational expression without adding a theory of rank or reducing the helper to an occupation. Devotional capital Us is inherited editorial styling; the Greek first-person plural does not by itself identify its participants or authorize a doctrinal gloss.",
    "2:19": "The additional forming action is marked by 'also'; the earth, all field animals, all heavenly birds, bringing to Adam, naming purpose and naming result remain represented. Simple narrative past follows the Greek sequence without imposing a harmonizing 'had previously formed'. 'Each living creature' unpacks the naming construction naturally. The narrative chronology and its relation to chapter one remain interpretation questions.",
    "2:20": "All three animal groups and the passive statement that no like helper was found for Adam are preserved. 'Gave names' is natural English for the naming idiom. 'Like himself' reflects the likeness expression here and should not be mechanically conformed to the different wording of 2:18. No statement is added about which agent conducted the unsuccessful search.",
    "2:21": "The divine action brings an altered state and sleep, followed by taking one of Adam's ribs/sides and replacing it with flesh. 'Deep sleep' is a contextual English choice for ekstasis, not an assertion that its every occurrence means sleep. Rib is plausible for the anatomical scene; side is a legitimate alternative requiring specialist review. The inherited subject of 'he slept' correctly remains Adam.",
    "2:22": "The source uses a building verb for the transformation of the taken rib into a woman. Propose 'built' in place of 'fashioned' to retain that concrete image and distinguish it from the earlier forming vocabulary. 'Built the rib ... into a woman' is unusual but intelligible English. Rib/side remains an unresolved lexical choice from 2:21; this proposal changes the verb only.",
    "2:23": "The declaration repeats bone and flesh with their matching possessive phrases, followed by the naming explanation. 'At last' is a contextual rendering of the emphatic now after the preceding lack of a helper; 'now' is a closer alternative. The Greek has 'her man/husband', supporting the inherited relational wording. English Woman cannot reproduce the Greek woman/man word relationship and should not be presented as etymological evidence.",
    "2:24": "The reason, future leaving, joining to the wife, explicit two, and one-flesh result are retained. 'Cleave' preserves the traditional register and is appropriate when understood as adhering rather than splitting; a plain-language note may be helpful. The Greek joining verb is passive in form, represented by an idiomatic English relational verb. No New Testament quotation is consulted or harmonized in this OT-only batch.",
    "2:25": "The two are identified as Adam and his wife, and both their nakedness and absence of shame are preserved. The imperfect description is naturally expressed with 'were' and 'were not ashamed'. No innocence doctrine, duration or claim of their inability to feel shame is inserted. The verse closes the scene before the serpent narrative.",
    "3:1": "The superlative description is rendered by 'more cunning than all', appropriate to the serpent's narrative conduct without changing it into an explicit supernatural identity. The questioning introduction preserves the serpent's challenge. The negative plus every-tree wording can raise an any-tree/not-every-tree scope question; 'any tree' is retained as the broad prohibition being challenged, with the issue flagged for fuller syntax review.",
    "3:2": "The woman's reply gives permission to eat garden-tree fruit. 'Trees' represents the Greek generic singular as a natural English class reference; 'may eat' expresses permission in the reply rather than a simple prediction of eating. The statement continues into the exception at 3:3, so the cross-unit quotation must remain intact. This does not revise the earlier command to match her report.",
    "3:3": "The central tree, prohibition on eating, additional prohibition on touching and purpose/fear of dying are all in the woman's reported speech. The touching clause is retained here even though it is absent from 2:17; harmonizing the two would remove a narrative distinction. Plural address is represented by ordinary you. 'Lest' keeps the negative purpose/result connection in the established register.",
    "3:4": "The serpent negates the emphatic death statement, and the inherited 'surely not die' makes his contradiction clear. The second-person verb is plural, as in the woman's report. This verse is a character's speech, not a narrator's assertion that death will not occur. No qualification such as immediately or spiritually is introduced.",
    "3:5": "The source has a past knowing verb followed by an eating condition and future eye-opening and becoming clauses. Propose present/future English within the serpent's direct speech so 'you ate ... would be' is not mistaken for an already completed meal. Preserve 'God knew' rather than silently changing that source tense. The plural gods remains, without deciding whether the comparison denotes deities or divine beings. No doctrinal explanation is inserted.",
    "3:6": "The three evaluations concern food, sight and contemplation. The inherited beautiful-to-contemplate wording avoids importing 'make one wise' from a different source tradition. The woman eats, gives to her husband with her, and the final Greek eating verb is plural; 'they ate' preserves that detail. The two eating statements are not collapsed, and no extra chronology is inferred.",
    "3:7": "The opening of both pairs of eyes, recognition of nakedness, sewing of fig leaves and making of coverings are present. Propose 'coverings about their waists' because the garment term is more specific than unqualified coverings and refers to something girded around the body. This is not an assertion about a precise garment pattern or its dimensions; the narrative image is simply made clearer.",
    "3:8": "The source describes the sound/voice of the Lord God walking at evening, followed by Adam and his wife hiding from His face among the garden's trees. The inherited sound and evening choices are retained; a cool breeze is not supplied. The singular wood/tree expression is understood collectively in this setting. Whether sound or voice best suits the scene remains a lexical decision for fuller review.",
    "3:9": "The Lord God calls Adam, names him directly and asks where he is. The source's proper name in the spoken question is retained rather than omitted as redundant. Ordinary you is correct because Adam is being addressed. The question is not expanded into an explanation of what God knew or intended.",
    "3:10": "Adam addresses God directly, so Thy and Thou didst follow the established divine-address convention. The walking modifier belongs to the addressed figure, and the English makes that relationship audible. The hearing, fear, present nakedness and hiding clauses remain distinct. Voice is possible for the same noun rendered sound in 3:8; the difference is flagged for contextual lexical consistency rather than mechanically normalized.",
    "3:11": "Both questions are preserved: disclosure of nakedness and eating from the sole prohibited tree. The source explicitly has the only-tree restriction, so 'alone' is warranted here. The second Greek question carries an interrogative particle whose nuance is naturally expressed as a question rather than an added assertion of guilt. The rather formal 'of which alone' construction remains intelligible but merits human read-aloud review.",
    "3:12": "Adam refers to the woman God gave with him and emphatically says that she gave to him, followed by his own admission of eating. Divine address is preserved. Fruit is supplied from context, since the Greek says from the tree without repeating that noun; this is intelligible ellipsis support, not a new proposition. The dash makes the emphatic subject audible without adding an accusation beyond the speech.",
    "3:13": "The question and woman's answer retain their respective speakers. Deceived renders the source verb without importing an account of the serpent's method. Her 'I ate' remains an explicit first-person action alongside the deception statement. The English does not convert either into a narrator's moral judgment or erase her agency.",
    "3:14": "The reason for the curse, comparison with cattle and field creatures, movement on breast and belly, eating earth and lifetime duration are preserved. Both body terms remain, unlike renderings that mention belly alone. 'Above all' interprets the comparative force of the Greek from/all construction; the exact force merits specialist review. No zoological change or identification of the serpent is added.",
    "3:15": "The repeated enmity relationships and the head/heel contrast remain explicit. The Greek repeats the same watching/keeping verb; 'watch for' preserves that repetition rather than substituting crush and bruise from another textual tradition. The masculine pronoun is represented by He, whose initial capital also follows sentence position. Its relation to the collective seed and the precise hostile sense of the verb remain unresolved; no messianic identification is inserted.",
    "3:16": "The emphatic multiplication, sorrows and groaning, childbirth in sorrow, orientation toward the husband and his ruling are represented. 'Greatly multiply' realizes the repeated Greek verbal construction without awkward English doubling. 'You shall turn toward' interprets the noun for turning; desire, recourse or orientation remain contextual alternatives for specialist study. The text is not expanded into an imperative approving the husband's rule.",
    "3:17": "Adam's listening and eating, the sole prohibited tree, the earth's curse in his works/labours, painful eating and lifelong duration are preserved. The source associates the curse with works, so no silent replacement by the more familiar 'because of you' is made. 'Eat of it' supplies the normal relation between earth and its produce rather than requiring literal consumption of soil. The exact force of the works phrase remains provisional.",
    "3:18": "The earth is the continuing subject that produces thorns and thistles for Adam; his eating of field vegetation follows. The inherited wording retains both plant groups and does not impose modern taxonomic identifications. 'Plants' is a contextual broad rendering of the vegetation term, linked with chapter two's field description. No dietary prescription beyond the sentence is inferred.",
    "3:19": "Sweat of the face, eating one's bread, return to the earth, derivation from it and the repeated earth wording are preserved. The source here says earth, unlike the dust wording of 2:7; the distinction should remain. 'Return' renders the endpoint of going away to earth in context. The elevated 'unto' is retained without introducing archaic pronouns for the human addressee.",
    "3:20": "The source explicitly supplies the meaningful name Life and relates it to all the living. The English retains that transparent name rather than silently replacing it with Eve. 'Was' is an English narrative copula; the Greek explanatory phrase lacks an expressed copula. This wording does not claim that all subsequent childbirth had already occurred at naming.",
    "3:21": "The Lord God's making and clothing actions remain distinct, with Adam and his wife both recipients. Garments of skin represents the leather/skin tunics without specifying an animal species. The Greek gives no separate slaughter, sacrificial rite or explanation of procurement, so none is added. A more specific 'tunics' is a possible lexical refinement to assess alongside reader comprehension.",
    "3:22": "The becoming-like-one-of-us clause concerns knowing good and evil; the prevention clause then lists reaching, taking, eating and living forever. Propose deleting 'also' before 'from the tree of life': the source coordinates the actions with and, but does not separately mark this taking as 'also'. The unfinished-speech dash is an English presentation choice. Plural Us is retained without specifying its referent or resolving the speech's tone.",
    "3:23": "The Lord God sends Adam out of the garden of delight to work the earth from which he was taken. Garden of delight follows the source's wording here instead of silently replacing it with the place-name Eden used earlier. The cultivation purpose and origin clause are both retained. The verse remains distinct from the stronger driving-out action that follows.",
    "3:24": "The source has both driving Adam out and settling him opposite the garden, then stationing cherubim and a turning flaming sword to guard the life-tree's way. The inherited wording preserves Adam as the object of settlement rather than transferring that clause to the cherubim. Opposite is retained without supplying east. The agent of the actions remains God, and no angelic rank or weapon mechanism is invented.",
}

REVISIONS = {
    "2:9": "And God also caused every tree that was beautiful to behold and good for food to spring up from the earth, with the tree of life in the midst of the garden, and the tree of the knowledge of good and evil.",
    "2:22": "And the Lord God built the rib He had taken from Adam into a woman, and brought her to Adam.",
    "3:5": "For God knew that on the day you eat of it, your eyes will be opened, and you will be as gods, knowing good and evil.”",
    "3:7": "And the eyes of both were opened, and they knew that they were naked. And they sewed fig leaves together and made coverings about their waists.",
    "3:22": "And God said, “Behold, Adam has become as one of Us, knowing good and evil. And now, lest he stretch forth his hand and take from the tree of life, and eat, and live for ever—”",
}

source = json.loads((ROOT / "genesis/verses.json").read_text(encoding="utf-8"))
records = []
for chapter in source["chapters"]:
    if chapter["chapter"] not in (2, 3):
        continue
    for verse in chapter["verses"]:
        short_ref = verse["reference"].split(" ", 1)[1]
        candidate = REVISIONS.get(short_ref, verse["text"])
        changed = candidate != verse["text"]
        records.append({
            "record_type": "focused_running_text_comparison",
            "review_id": "OT-002-genesis-" + short_ref.replace(":", "-"),
            "book_id": "genesis",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": str(chapter["chapter"]),
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
            "decision": "propose_revision" if changed else "retain_provisionally",
            "source": {
                "edition": "Rahlfs–Hanhart 2006",
                "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{chapter['chapter']}",
                "accessed_on": "2026-11-12",
                "running_text_read": True,
                "apparatus_consulted": False,
            },
            "analysis": NOTES[short_ref],
            "review": {
                "reviewer": "OpenAI Codex assistant",
                "type": "AI",
                "scope": "Focused running-text comparison",
                "all_tokens_accounted_for": False,
                "independent_greek": None,
                "human_read_aloud": None,
                "editorial_acceptance": None,
            },
            "benchmark_change": changed,
            "publication": {"staging": None, "production": None},
        })

assert len(records) == 49
assert len(NOTES) == 49
assert len({r["verse_anchor"] for r in records}) == 49
assert sum(r["benchmark_change"] for r in records) == 5
out = {
    "schema_version": "1.0",
    "batch_id": "OT-002",
    "scope": "Genesis 2–3; all 49 inherited anchored units",
    "status": "focused_comparison_draft_not_accepted",
    "date": "2026-11-12",
    "baseline_commit": BASELINE,
    "benchmark_preserved": True,
    "counts": {"compared_units": 49, "proposed_revisions": 5, "retained_units": 44, "accepted_units": 0},
    "limitations": "AI running-text comparison only. No full token alignment, specialist lexicon consultation, critical apparatus, Göttingen collation, independent human Greek review, human reading aloud, editorial acceptance or website deployment is claimed. Original Genesis benchmark files remain unchanged.",
    "records": records,
}
(HERE / "focused-reviews.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(out["counts"]))
