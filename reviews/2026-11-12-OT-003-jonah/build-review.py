"""Build the bounded Jonah review from the preserved baseline and authored notes."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
LEXICON = "https://atlas.perseus.tufts.edu/dictionaries/entry/urn:cite2:scaife-viewer:dictionary-entries.atlas_v1:middle-liddell.perseus-eng2-n34599/"

NOTES = {
"1:1": "The arrival of the Lord's word, Jonah as recipient, his patronymic and the introduction of direct speech are retained. The opening narrative conjunction is not separately expressed in the inherited opening sentence; its discourse function remains visible in the transition into the command. This is a focused comparison, not full token accounting.",
"1:2": "The two singular imperatives command rising and going; the further imperative commands proclamation within Nineveh. The causal clause concerns the outcry arising from the city's wickedness, not simply its size. The inherited wording preserves the great-city description, the outcry and the direction toward God. No additional object such as repentance is supplied for proclaim.",
"1:3": "The purpose of Jonah's rising is flight, in deliberate contrast to the preceding command. But expresses that contextual contrast although the connective itself is the ordinary narrative conjunction. Three occurrences of Tarshish and both departures from the Lord's presence are retained. The sequence of descent, finding, payment and boarding is preserved; them identifies the people aboard without inventing a named company.",
"1:4": "The Lord is the explicit subject who rouses the wind; the great surge follows, and the ship is in danger of being shattered. The final imperfect construction describes danger rather than an accomplished shipwreck. Wind is the contextual sense of the noun elsewhere capable of spirit; the candidate does not imply a new divine title or agent.",
"1:5": "The sailors' fear and repeated crying, the equipment thrown overboard and the purpose of relief are preserved. Each with their god reflects the displayed singular distributive with a plural possessive without deciding whether the gods were shared. Lighten their load supplies an English object for the relief construction and merits further syntax review. Jonah's contrasting descent, sleeping and snoring remain distinct; snoring is not reduced to sleep.",
"1:6": "The officer approaches Jonah, questions his snoring and orders rising and invocation of Jonah's god. The rescue clause has purpose/hope rather than a guarantee. Ship's officer avoids an unsupported modern rank for the bow-related title; exact nautical terminology remains open. The god is the speaker's anaphoric designation and is not silently converted into the narrator's theological identification.",
"1:7": "The distributive speakers address their neighbors and propose lot casting to discover whose responsibility explains the calamity. The action and its outcome are separate clauses; the lot falls on Jonah. Learn conveys coming to know in this context. The inherited English retains the recurrence of lot instead of varying it for literary effect.",
"1:8": "The question about the calamity is retained even after the lot has identified Jonah. The four questions concern work, point of departure, country and people. Smoothing the last two into a coordinated question does not merge country with ethnic affiliation. No answer such as Hebrew is imported from another textual tradition.",
"1:9": "The displayed Greek identifies Jonah as a servant of the Lord; that reading is retained rather than replaced by a familiar Hebrew-based self-identification. Worship renders the verb of reverence without converting it into a claim about his conduct. The Lord is identified as God of heaven and maker of the sea and dry land, both creation objects being preserved.",
"1:10": "Greatly afraid represents the cognate verb/noun expression of great fear. The sailors' question is followed by two causal explanations: they knew Jonah was fleeing because he had told them. The inherited pluperfect appropriately locates his disclosure before their reaction. The repeated subject men is retained in the explanatory clause.",
"1:11": "The question joins the action toward Jonah with the sea's prospective subsiding. English so that expresses the expected outcome of the Greek coordinated future construction without changing the addressees. The continued intensification of the sea is retained in kept raising a greater surge. This is not an instruction from the narrator to harm Jonah.",
"1:12": "Jonah directs the men to lift and throw him into the sea, with subsiding as the stated result. He identifies himself as the reason for this great surge. I know is appropriate for the resulting state conveyed by the Greek perfect; it is not weakened to speculation. You is plural here, though ordinary English does not mark that number.",
"1:13": "The men strive to return toward land but are unable. The purposive infinitive and explicit negative are retained. The text does not specify rowing, so strained remains suitably general. The continued, intensified movement of the sea against them explains their inability and parallels the preceding increase.",
"1:14": "The sailors petition the Lord not to let them perish on account of this man's life and not to charge them with innocent blood. Innocent renders the blood adjective in this juridical plea, without certifying Jonah's entire character. The strongly negative opening and subsequent prohibition are both represented. Thou/hast/didst follow direct singular divine address; the conclusion concerns God's action according to His will.",
"1:15": "The men take Jonah and throw him out into the sea; the sea then ceases its tossing. The distinct action and result are retained. The sentence does not yet include the sea creature, which belongs to the following source-numbered chapter. No miraculous mechanism beyond the stated cessation is added.",
"1:16": "Fear with great fear, sacrifice to the Lord and vows form the sailors' response. The inherited wording retains the emphatic fear expression, the Lord as object/recipient and the sequence of sacrifice and vows. It does not explain the practical timing of sacrifice or import a later conversion narrative.",
"2:1": "The Lord commands a great sea creature to swallow Jonah. The creature's size is explicit, but a modern species is not. Three days and three nights and Jonah's location in the belly are retained. This is source-numbered 2:1, not silently reassigned to 1:17; the chapter division is part of the edition's stable identity.",
"2:2": "Jonah prays to the Lord his God from the creature's belly. The possessive and location are retained, and the comma continues into the next unit's introduction of speech. Prayer is not described as occurring after emergence. The verse boundary and open syntactic continuation remain intact.",
"2:3": "The first clause narrates Jonah's cry in distress and God's listening; the second turns to direct divine address. Hades remains a named underworld image rather than a doctrinal expansion. Voice of my cry is an English synthesis of the displayed cry/voice genitives; the precise attachment remains a syntax-review item, not a claim of exhaustive alignment. The change from He to Thou follows the source's person change.",
"2:4": "God is addressed as the one who cast Jonah into sea-depths. Rivers and the two wave terms remain separate images; the repeated divine possessive is retained. All qualifies the billows in the coordinated phrase. The candidate neither relocates the setting to a literal river nor removes the poem's images in favor of an explanatory paraphrase.",
"2:5": "The speaker's banishment from God's eyes and the question about looking again toward the sanctuary are retained. The question particle is not replaced by an unconditional assurance that he will return. Again is warranted by the construction meaning to add/continue to look, unlike an ornamental insertion. Sanctuary is the inherited rendering of the temple noun; its exact contextual referent remains for review.",
"2:6": "The verse has enclosing water, the uttermost abyss and the head's descent into mountain clefts. The difficult expression reaching as far as life is retained provisionally rather than changed to neck from another language or tradition. Up to my life is awkward English and needs a better Greek-grounded spoken draft. The imagery is not converted into a geographical or anatomical claim.",
"2:7": "The land's bars/restraints are everlasting, followed by a third-person imperative with ruin/corruption as its apparent nominative subject. The inherited let the ruin of my life rise up preserves that difficult surface construction. It is NOT treated as a resolved translation: the sense and genitive attachment require specialist syntax, broader usage and apparatus comparison. The wording must not be silently changed to an accomplished Thou didst bring up my life, which is not this displayed Greek construction.",
"2:8": "The temporal infinitival construction places recollection of the Lord during the failing of Jonah's life. The following optative is retained as a wish, may my prayer come, not as a report that the prayer already arrived. Direct Thee/Thy follows the shift back to address. Into the holy sanctuary preserves the source's destination image.",
"2:9": "The subject is people attending to vain and false things; abandoned retains the aorist predicate instead of automatically converting it to a present maxim. Their mercy preserves the possessive but leaves its referent unresolved: mercy they should show or mercy available to them need contextual/lexical review. Guard is formally close yet may obscure attending to or observing; no accepted replacement is claimed.",
"2:10": "The contrastive I, voiced praise and thanksgiving, future sacrifice and repayment of vows are retained. The final genitive form relating to deliverance followed by to the Lord is syntactically difficult; the inherited for deliverance to the Lord is provisional and not idiomatic resolved English. It must not be recast as the familiar Salvation belongs to the Lord without evidence that this accounts for the selected Greek syntax. Lexical sense and attachment remain explicit open issues.",
"2:11": "The displayed passive states that the sea creature was commanded, without an expressed agent in this clause. The inherited passive therefore avoids adding the Lord as an explicit grammatical subject. It then expels Jonah onto dry land. The repeated creature designation and the destination are retained without implying a species.",
"3:1": "The word comes to Jonah a second time, explicitly linking this commission with the first. Second time is a stated feature, not inferred repetition. The inherited introductory sentence and colon retain the recipient, divine source and speech transition; the initial narrative conjunction is represented by the sequence of sentences rather than a separate And.",
"3:2": "Rising, going and proclaiming are again commanded to Jonah singular. The proclamation is tied to the former message already spoken to him. The inherited English preserves that backward reference instead of changing it to an unspecified future message. Nineveh's great-city description and proclamation within it are both retained.",
"3:3": "Jonah rises and goes in accordance with the Lord's speech. Great before God keeps the explicit divine dative visible, although an intensive interpretation of the phrase remains possible. The approximate three-day journey is not turned into a precise diameter, circumference or modern distance; the Greek itself does not supply that geographical clarification.",
"3:4": "The approximate one-day entry, the two speech verbs and the three-day warning are retained. The displayed Rahlfs–Hanhart running text reads three, so forty is not substituted from familiar versions. The future passive leaves the overthrowing agent implicit. These are source-specific observations, not a new manuscript/apparatus collation.",
"3:5": "The Ninevites believe God, proclaim a fast and put on sackcloth from greatest to least. People is a contextual collective rendering of the word for men here; it does not assert a different census. Greatest/least preserves social breadth without forcing an age-only interpretation. The plural action remains separate from the king's response in the next unit.",
"3:6": "The report reaches the king, who rises, removes his robe, puts on sackcloth and sits in ashes. The sequence and royal contrast are retained. Off himself represents the reflexive wording. No explanation of court ritual or extra confession is inserted into the Scripture sentence.",
"3:7": "The passive proclamation comes from the king and his nobles. The prohibition separately names people, livestock, cattle and sheep, and forbids tasting, grazing and drinking water. The repeated negatives are represented by taste nothing and let them not. The inherited quotation ends here because the following Greek verbs narrate actions rather than continuing imperative commands.",
"3:8": "The Greek now narrates sackcloth, earnest crying and turning with past indicative verbs. The candidate preserves that form instead of harmonizing them into commands. Each with his evil way and their hands retains the source's shift between distributive singular and collective plural. The shared subject including livestock is not silently rewritten, though the practical distribution of actions is an interpretation issue.",
"3:9": "Propose a natural future result clause: so that we shall not perish. The displayed emphatic negative with a subjunctive expresses non-perishing, but certainly do not is awkward under the opening who-knows question and can sound like an independent present guarantee. The question remains conditional on God's possible relenting; shall not carries the firm negative without adding an assurance outside that question. His fierce anger represents the paired wrath terms. Full mood/discourse review remains open.",
"3:10": "God sees their deeds, specifically their turning from evil ways, and relents concerning the threatened calamity. The inherited wording preserves the object of relenting and the explicit final non-performance. It neither changes deeds into words alone nor adds a theological account of divine repentance. The repeated God and the final He did not do it remain visible.",
"4:1": "The selected Greek emphasizes grief with a cognate noun and adds disturbance/confusion. Grieved with great grief and disturbed retain both rather than importing anger as the sole description from familiar renderings. No psychological diagnosis is inferred. The verse's contrast with the city's rescue is left to the narrative context.",
"4:2": "Jonah's prayer recalls his earlier words at home and links his prior flight with his knowledge of God's character. The source lists mercy, compassion, patience, abundant mercy and relenting over calamities; all are retained. Thou art follows singular divine address. Was quick to flee is a provisional contextual rendering of the anticipatory verb; its exact temporal nuance remains open rather than an etymology-based certainty.",
"4:3": "The compound divine address Master Lord is retained. The imperative asks God to take Jonah's life; the reason compares dying with living. The inherited better than construction naturally renders the comparison without adding now to the death wish beyond the opening and now. No moral judgment about Jonah's request is supplied in the verse.",
"4:4": "The Lord asks whether Jonah is greatly grieved. The intensifying adverb is rendered deeply, and ordinary you is used because Jonah, not God, is addressed. The Greek question here is not silently changed into the familiar question whether Jonah is right to be angry. The state expressed by the perfect is retained in the English present description.",
"4:5": "Jonah exits and sits opposite the city, makes a shelter and sits under its shade to see the outcome. Opposite is retained without importing an eastern direction. The two sitting descriptions and the repeated city preserve the narrative's arrangement. Shelter avoids asserting a specific tent material or festival significance.",
"4:6": "The Lord God commands the gourd; its growth over Jonah's head supplies shade and protection from his troubles. The source's repeated head/shading language is substantially retained, along with great joy in parallel to the earlier great grief. Gourd is the inherited general botanical designation, not a confirmed modern species. The troubles may include discomfort and distress; no single diagnosis is imposed.",
"4:7": "The next-day dawn, God's command to a worm, the worm's striking of the gourd and its drying are retained. It struck grammatically refers to the worm before the plant becomes the subject of dried up. The narrative does not specify how the worm damaged the plant, and the candidate adds no mechanism.",
"4:8": "The sunrise triggers a commanded hot, scorching wind, then the sun strikes Jonah's head. The two heat expressions and striking repetition are retained. Lost heart follows the Greek verb rather than asserting a medical faint; renounced his life is a provisional rendering of the refusal/disavowal expression. Jonah repeats the preference for death, without an added account of attempted self-harm.",
"4:9": "God repeats the question about great grief, now explicitly concerning the gourd. Jonah replies with the same intensity and the limit even to death. Ordinary singular you preserves the addressee policy, while I retains the response's emphasis. The candidate does not turn the question into a moral right-to-anger formula absent from this displayed wording.",
"4:10": "Propose had pity on for the past form of pheidomai with the gourd as its concern. In context Jonah mourned its loss; You spared can misleadingly imply that he successfully preserved it. The same verb recurs in 4:11, where the proposed have pity on preserves that link. Middle Liddell was consulted for the general range of sparing, mercy and care; the choice here is a contextual inference, not a specialist LXX entry or apparatus verdict. The denied labor/nurture and repeated night are unchanged.",
"4:11": "Propose have pity on to match the same verb in 4:10 while retaining the divine first-person future question. Its contextual implication includes sparing the city, not merely an abstract emotion. The great-city description, more than 120,000 people, right/left ignorance and many livestock are retained. The people are not identified as infants, and the concluding question is not replaced by a doctrinal explanation. The lexical choice remains a proposal requiring review.",
}

REVISIONS = {
"3:9": "“Who knows whether God will relent and turn from His fierce anger, so that we shall not perish?”",
"4:10": "The Lord said, “You had pity on the gourd, over which you did not toil and which you did not nurture, which came to be in a night and perished in a night.",
"4:11": "And shall I not have pity on Nineveh, the great city, in which dwell more than one hundred and twenty thousand people who do not know their right from their left, and much livestock?”",
}

UNRESOLVED = {
"1:5": ["Distributive each with plural their god; grammar of the cargo-lightening purpose."],
"1:6": ["Exact ancient nautical office; anaphoric divine designation in the officer's speech."],
"2:3": ["Attachment of cry and voice genitives."],
"2:5": ["Force of the question and sanctuary referent."],
"2:6": ["An idiomatic rendering of the life-threatening water expression that accounts for the selected Greek."],
"2:7": ["Sense of ruin/corruption as apparent subject of the imperative; genitive attachment; relevant apparatus and broader Greek usage."],
"2:9": ["Sense of observing/guarding and referent of their mercy."],
"2:10": ["Function and attachment of the final genitive deliverance expression and dative to the Lord; idiomatic English remains unresolved."],
"3:3": ["Divine dative's force and exact journey measure."],
"3:8": ["Distribution of narrated actions over people and animals; distributive singular/plural shift."],
"3:9": ["Independent review of mood, emphatic negation and the result clause within the who-knows question."],
"4:2": ["Precise nuance of the anticipatory flight verb."],
"4:6": ["Botanical identification; scope of troubles."],
"4:8": ["Contextual nuance of losing heart and renouncing life."],
"4:10": ["Specialist LXX review of pheidomai with hyper; whether pity or spare best preserves the two-verse analogy."],
"4:11": ["Same lexical decision as 4:10; retain sparing as a contextual implication of pity."],
}

baseline = json.loads((ROOT / "jonah/verses.json").read_text(encoding="utf-8"))
records = []
for chapter in baseline["chapters"]:
    for verse in chapter["verses"]:
        key = verse["reference"].removeprefix("Jonah ")
        candidate = REVISIONS.get(key, verse["text"])
        record = {
            "record_type": "focused_running_text_comparison",
            "review_id": f"OT-003-jonah-{key.replace(':', '-')}",
            "book_id": "jonah",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": str(chapter["section"]),
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
            "decision": "propose_revision" if candidate != verse["text"] else "retain_provisionally",
            "source": {
                "edition": "Rahlfs–Hanhart 2006",
                "url": f"https://www.die-bibel.de/en/bible/LXX/JON.{chapter['chapter']}",
                "accessed_on": "2026-11-12",
                "running_text_read": True,
                "apparatus_consulted": False,
            },
            "analysis": NOTES[key],
            "unresolved_questions": UNRESOLVED.get(key, []),
            "review": {
                "reviewer": "OpenAI Codex assistant",
                "type": "AI",
                "scope": "Focused running-text comparison",
                "all_tokens_accounted_for": False,
                "independent_greek": None,
                "human_read_aloud": None,
                "editorial_acceptance": None,
            },
            "benchmark_change": False,
            "publication": {"staging": None, "production": None},
        }
        if key in ("4:10", "4:11"):
            record["lexical_evidence"] = [{
                "source": "Middle Liddell, pheidomai, Scaife ATLAS",
                "url": LEXICON,
                "accessed_on": "2026-11-12",
                "scope": "General lexical entry read; no specialist Septuagint lexicon or exhaustive occurrence study claimed.",
            }]
            record["translation_alternatives"] = [{
                "reading": "spared / spare",
                "disposition": "Inherited alternative retained in the baseline; proposed pity language is not accepted replacement.",
            }]
        records.append(record)

assert len(records) == 48
assert len(NOTES) == len(records)
assert [len(c["verses"]) for c in baseline["chapters"]] == [16, 11, 10, 11]
assert len({r["verse_anchor"] for r in records}) == 48
assert sum(r["decision"] == "propose_revision" for r in records) == 3

document = {
    "batch_id": "OT-003",
    "scope": "Jonah 1–4; all 48 existing LXX-numbered units (16/11/10/11).",
    "date": "2026-11-12",
    "status": "focused_running_text_comparison_drafted_full_alignment_pending",
    "source_access": "All four publisher running-text chapters were retrieved and read on 12 November 2026. This does not establish apparatus access or manuscript collation.",
    "counts": {"units": 48, "retained_provisionally": 45, "proposed_revisions": 3, "token_aligned": 0, "editorially_accepted": 0},
    "records": records,
}
(HERE / "focused-reviews.json").write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(document["counts"]))
