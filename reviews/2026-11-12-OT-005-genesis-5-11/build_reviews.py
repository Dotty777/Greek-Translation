"""Rebuild Genesis 5–11 records from authored source observations, not an API translation."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
DATE = "2026-11-12"
ROWS = {}


def add(ref, close, analysis, candidate=None, unresolved=None):
    assert ref not in ROWS, ref
    ROWS[ref] = {"close": close, "analysis": analysis, "candidate": candidate,
                 "unresolved_questions": unresolved or []}


# Every age below was read in the displayed Rahlfs–Hanhart Genesis 5 text.
# The structured tuples preserve source numbers, not inferred chronologies.
add("5:1", "This is the book of the origin of human beings. On the day God made Adam, He made him according to God's image.",
    "The genealogy formula refers to human beings, then names Adam. God is maker and the image is God's. Generations is the established contextual heading for the origin/genealogy noun; mankind represents its plural human referent. No divine likeness clause is added from another verse.")
add("5:2", "Male and female He made them and blessed them; He named their name Adam on the day He made them.",
    "The source applies the name Adam to the plural male-and-female pair. The inherited named them Adam retains that surprising collective designation instead of silently changing it to a male individual. The making, blessing and naming actions and the temporal clause remain distinct.")
add("5:3", "Adam lived 230 years and begot according to his own form and his own image, and named him Seth.",
    "The displayed age is 230. Form/appearance and image are two expressions; own likeness and image is a defensible contextual rendering. A son is supplied as the English object of begot from the naming clause, not an additional Greek noun. Seth is the established English form of the displayed name.")
add("5:4", "Adam's days after begetting Seth were 700 years, and he begot sons and daughters.",
    "The 700 years are explicitly after Seth's begetting, not Adam's total age. Both sons and daughters remain. The inherited wording preserves the days/years idiom naturally; 230 plus 700 agrees with the following total, without establishing an absolute creation date.")
add("5:5", "All Adam's days that he lived were 930 years, and he died.",
    "The source gives total 930 and an explicit death clause. This agrees arithmetically with 230 plus 700 in 5:3–4. The qualifying lived phrase and all are preserved rather than compressing the line to an unexplained number.")

GEN5 = [
    (6, "Seth", "Enosh", 205, 707, 912, "The established Enosh represents the displayed Enos name."),
    (9, "Enosh", "Cainan", 190, 715, 905, "Cainan is retained distinctly from the later post-flood bearer of the same name."),
    (12, "Cainan", "Mahalalel", 170, 740, 910, "Mahalalel is the inherited English form of the displayed Maleleel name."),
    (15, "Mahalalel", "Jared", 165, 730, 895, "Jared represents the displayed Iared; no spelling change is imposed."),
    (18, "Jared", "Enoch", 162, 800, 962, "This Enoch belongs to Seth's line; he is not silently equated with chapter four's namesake."),
    (25, "Methuselah", "Lamech", 167, 802, 969, "The displayed 167 and 802 are preserved despite the resulting flood-chronology tension."),
]
for first, parent, child, before, after, total, names_note in GEN5:
    add(f"5:{first}", f"{parent} lived {before} years and begot {child}.",
        f"The Greek explicitly gives {before} years before {child}'s begetting. Subject, child and age match the inherited English. {names_note} This is a running-text number check, not apparatus collation.")
    add(f"5:{first+1}", f"{parent} lived {after} years after begetting {child}, and begot sons and daughters.",
        f"The post-begetting interval is {after}, separate from the preceding {before}. The named child's temporal role and the additional sons-and-daughters formula are retained. The Greek does not give separate ages or names for those additional children.")
    add(f"5:{first+2}", f"All {parent}'s days were {total} years, and he died.",
        f"The stated total {total} equals the displayed intervals {before} + {after}. The all-days formula and explicit death are retained. Arithmetic agreement within this lifespan does not prove agreement with every other chronology in the narrative.",
        unresolved=["Summing the displayed ages places Methuselah's death fourteen years after the flood year; apparatus and chronology review remain open."] if parent == "Methuselah" else None)

add("5:21", "Enoch lived 165 years and begot Methuselah.",
    "The displayed age is 165, and Methuselah is the named offspring. The inherited English agrees. This must not be changed to 65 from a different source tradition. The naming convention is retained without claiming a fresh onomastic authority.")
add("5:22", "Enoch pleased God for 200 years after begetting Methuselah, and begot sons and daughters.",
    "The selected Greek says pleased God, not walked with God. The 200 years modify the period after Methuselah's begetting, and the additional sons and daughters remain. The English does not add perfection or a cause for Enoch's later transfer.")
add("5:23", "All Enoch's days were 365 years.",
    "The total 365 equals 165 plus 200. This verse has no death clause, unlike the surrounding lifespan totals; the inherited omission is therefore substantive and must remain. No symbolism of the number is inserted into Scripture.")
add("5:24", "Enoch pleased God and was not being found, because God transferred him.",
    "Pleasing God is repeated. The passive not being found and the divine transfer are both retained; transferred does not specify a destination absent from this sentence. The inherited was not found is natural English for the imperfect. No death or immortality explanation is added.")
add("5:28", "Lamech lived 188 years and begot a son,",
    "The source gives 188 and an unnamed son whose name follows in 5:29. The inherited sentence break is an English presentation choice; the discourse remains continuous. This Lamech is in the listed line and is not conflated with chapter four's Lamech.")
add("5:29", "and named him Noah, saying, 'This one will give us rest from our works, from the pains of our hands and from the earth which the Lord God cursed.'",
    "The future promise includes three from-phrases: works, pains of hands and the cursed earth. The inherited rest/toil wording preserves these relations. Lord God is explicit. The name's significance is the speaker's explanation, not an independently verified etymological claim or an assertion that the whole curse is already removed.")
add("5:30", "Lamech lived 565 years after begetting Noah and begot sons and daughters.",
    "The post-Noah interval is 565. Noah's identity and the additional offspring formula are preserved. Combined with 188 before Noah this yields the displayed next-verse total 753; no familiar alternate figures are imported.")
add("5:31", "All Lamech's days were 753 years, and he died.",
    "The displayed 753 agrees with 188 plus 565. The total and death clause remain distinct from Noah's following introduction. The verse provides a lifespan, not a directly stated calendar date for Lamech's death.")
add("5:32", "Noah was 500 years old, and Noah begot three sons: Shem, Ham and Japheth.",
    "The source expressly says three sons and repeats Noah as subject. Age 500 and the order Shem, Ham, Japheth are retained. The collective birth summary does not independently establish triplets, simultaneous birth or each son's precise birth year.")

add("6:1", "It happened when human beings began to become numerous on the earth and daughters were born to them,",
    "Human increase and the birth of daughters form the temporal setting for 6:2. The inherited comma and that at the next verse join the Greek introductory construction into readable English. Daughters remains explicit; no population estimate is supplied.")
add("6:2", "the sons of God saw that the daughters of human beings were beautiful and took wives for themselves from all whom they chose.",
    "The participial seeing leads to taking wives, with beauty and selection explicit. Sons of God is preserved without deciding whether the designation is angelic, royal or human. The relative selection clause is not rewritten to imply universal marriage to every woman.",
    unresolved=["The identity of sons of God requires contextual and historical study; this batch does not resolve it."])
add("6:3", "The Lord God said, 'My spirit will certainly not remain in these human beings forever because they are flesh; their days will be 120 years.'",
    "Remaining, rather than striving, follows the displayed verb. These men preserves the demonstrative and flesh the stated reason. Spirit capitalization is inherited interpretation. The emphatic negative is carried by the firm shall not. The 120 years are retained without deciding whether they describe a lifespan limit or a period until judgment.",
    unresolved=["Reference of spirit and function of the 120 years remain interpretive questions."])
add("6:4", "Giants were on the earth in those days and afterward, whenever the sons of God went in to the daughters of human beings and they bore children for themselves; those were the giants from of old, the renowned men.",
    "Giants occurs twice in the source. The temporal afterward and recurring whenever construction are retained. The childbirth clause's reflexive pronoun and subject relationships are not completely transparent; the inherited bore children to them is a contextual interpretation rather than an exhaustive syntax solution. No angelic name or genetic explanation is added.",
    unresolved=["Subject and reflexive attachment in the childbirth clause require specialist syntax review."])
add("6:5", "The Lord God saw that people's wicked deeds had multiplied on the earth and that everyone diligently planned evil in his heart every day,",
    "The source's adverb describes diligence or intentness; inherited continually blurs that with the separate all-days expression. Propose intently with every day, and keep the heart as the location of thought. English past tense fits the reported object of saw, while the Greek present describes habitual activity. This is a lexical-contextual proposal without a consulted specialist lexicon.",
    "And the Lord God saw that the wickedness of mankind had multiplied upon the earth, and that each one intently devised evil in his heart every day.")
add("6:6", "and God considered that He had made the human being on the earth, and reflected.",
    "The source has two verbs of consideration or thought. The inherited took to heart and pondered maintains both rather than substituting a different-language repentance-and-grief formula. It does not specify an emotional state beyond the chosen verbs. The transition from 6:5 is preserved despite the English sentence break.")
add("6:7", "God said, 'I will wipe out the human being I made from the face of the earth, from human to livestock and from creeping things to heaven's birds, because I was angered that I made them.'",
    "The wiping-out promise extends across the animal list. The source's anger verb differs from the consideration verbs in 6:6, which the inherited wording preserves. Am angered represents a resulting state from the Greek past form; was angered is the close alternative. Mankind I have made is awkward but understandable and not silently replaced by a narrower group.")
add("6:8", "But Noah found favor before the Lord God.",
    "The contrast singles out Noah and his finding favor before Lord God. Grace is an established English rendering here, with favor a useful close-stage alternative. The sentence does not name the cause of the favor or define a later theological category.")
add("6:9", "These are Noah's generations. Noah was a righteous human being, complete in his generation; Noah pleased God.",
    "Righteous, complete/blameless and pleasing God are distinct descriptions. Blameless is a contextual moral rendering, not a statement that the source says sinless. The generation phrase and repeated Noah remain. The selected verb is pleased rather than walked, matching the Enoch language in chapter five.")
add("6:10", "Noah begot three sons: Shem, Ham and Japheth.",
    "The explicit count three and all three names in source order are retained. This repetition of 5:32 should not be deleted for variety or used alone to infer the sons' birth intervals.")
add("6:11", "The earth was corrupted before God, and the earth was filled with injustice.",
    "Earth is repeated as subject, and corruption and injustice are separate descriptions. Unrighteousness is defensible for the latter term, though injustice is a clearer close-stage equivalent. No replacement by violence alone is warranted from this displayed Greek word without further contextual argument.")
add("6:12", "The Lord God saw the earth, and it was corrupted, because all flesh had corrupted its way on the earth.",
    "Divine observation, the earth's corrupted state and its cause are retained. All flesh is a collective subject with a singular way/possessive relationship. The English its preserves that relationship. The repeated corruption wording is meaningful and not replaced by varied moral adjectives.")
add("6:13", "God said to Noah, 'The time of every human being has come before Me, because the earth was filled with injustice from them, and behold, I am destroying them and the earth.'",
    "Time has come follows the actual Greek rather than inserting end as a noun. The people are the stated source of injustice, and both them and earth are objects of destruction. I am destroying renders the present announcement. The text does not independently specify the scope of earth in modern geographical terms.")
add("6:14", "Therefore make yourself an ark from squared timbers; make the ark into compartments, and pitch it inside and outside with pitch.",
    "The source specifies squared timbers, not a named wood species. The nest-like divisions are rendered compartments. The repeated pitch noun/verb is represented by coating with pitch, and both inside and outside remain. No measurements or engineering explanation are added to this verse.")
add("6:15", "Thus make the ark: its length 300 cubits, its width 50 cubits and its height 30 cubits.",
    "The dimensions are 300 length, 50 width and 30 height, with cubits repeated. The inherited English preserves all values and their axes. No meter conversion is inserted because the exact cubit measure has not been established in this batch.")
add("6:16", "Make the ark drawing it together, and complete it above to a cubit; make the door from the side, and make it with ground-level, second and third levels.",
    "Taper toward the top is an interpretation of the gathering/drawing-together participle; the source does not explicitly say window here. The cubit-at-top instruction is difficult, so it is retained provisionally without claiming a settled roof design. Side door and three level terms remain distinct.",
    unresolved=["The gathering construction and cubit completion need lexical/syntax and architectural review; taper is provisional."])
add("6:17", "Behold, I am bringing the flood, water upon the earth, to destroy all flesh under heaven in which is a spirit of life; everything on the earth will die.",
    "The flood and its water are identified, followed by destruction purpose and death result. Breath of life is a contextual rendering of the spirit/breath noun, unlike the different life-soul expression at 1:30. All flesh and everything are not narrowed by an explanatory limitation. No divine title is inferred from the breath phrase.")
add("6:18", "I will establish My covenant with you; you shall enter the ark, you, your sons, your wife and your sons' wives with you.",
    "The covenant is God's and is established with singular Noah; the ensuing entrants include the full named household. But is a contextual contrast in the inherited wording, where the source connective is and. The sequence of wife and sons is preserved here without harmonizing other household lists.")
add("6:19", "From all livestock, all creeping things, all wild beasts and all flesh, bring two by two from all into the ark to nourish them with yourself; they shall be male and female.",
    "All four categories and the two-by-two distribution are present. Sustain is a contextual rendering of feeding/nourishing and is broader than merely placing animals aboard. The male/female pairing remains explicit. Two of each is idiomatic but should not be treated as a resolution of chapter seven's sevenfold clean-animal instruction.")
add("6:20", "From all flying birds by kind, all livestock by kind and all earth-creeping creatures by their kind, two by two from all will enter to you to be nourished with you, male and female.",
    "Unlike 6:19's command to bring, this clause says the creatures will enter to Noah. The final kind noun is singular with a plural possessive; propose their kind in place of their kinds to keep the source form consistent. Sustained represents the feeding purpose, and the male/female phrase remains.",
    "Of all the winged birds according to their kind, all the cattle according to their kind, and all the creeping things upon the earth according to their kind, two of each shall come to you, male and female, to be sustained with you.")
add("6:21", "You shall take for yourself from all the foods that you will eat and gather them to yourself, and it shall be for you and them to eat.",
    "The source shifts from singular Noah's taking/gathering to plural you will eat. The inherited impersonal that is eaten hides that future addressee. Propose you shall eat while retaining natural number-neutral English you; note the plural explicitly here. Some of renders the partitive from without demanding every existing item of food be taken.",
    "“And take for yourself some of every kind of food that you shall eat, and gather it to yourself. It shall be food for you and for them.”")
add("6:22", "Noah did all that the Lord God commanded him; thus he did.",
    "Both the all-commanded statement and the repeated thus-he-did conclusion are retained. Lord God is the explicit commander, Noah the actor. Repetition is source-grounded emphasis, not needless padding to be removed for a smoother summary.")

add("7:1", "The Lord God said to Noah, 'Enter the ark, you and all your household, because I have seen you righteous before Me in this generation.'",
    "The command addresses Noah singular and includes all his household. The reason is God's seeing Noah as righteous in this generation. Household does not itself list additional persons beyond the family elsewhere enumerated, and no historical demographic conclusion is added.")
add("7:2", "From the clean livestock bring to yourself seven by seven, male and female; from the unclean livestock two by two, male and female,",
    "The source repeats seven and two distributively and explicitly pairs male/female in both groups. By sevens/by twos preserves that form without silently expanding seven into seven pairs or a total of fourteen. Clean status is retained but not defined by a later dietary list in this verse.",
    unresolved=["The exact count implied by seven by seven should receive specialist contextual review before numerical expansion."])
add("7:3", "and from clean birds of heaven seven by seven, male and female, and from unclean birds two by two, male and female, to sustain seed over all the earth.",
    "The displayed Greek separately lists clean and unclean birds, each with its number and sex pairing. These distinctions must not be shortened to an undifferentiated bird rule. Preserve seed as the continuity image; their is supplied from the creatures as its natural English referent.")
add("7:4", "For after seven more days I am bringing rain on the earth for 40 days and 40 nights, and I will wipe out every living thing I made from earth's face.",
    "The seven-day interval precedes the forty-day-and-night rainfall. The source's rising/existing-life noun is contextually rendered every living thing, not a literal resurrection. The speaker is the agent of both bringing and wiping out. All three time values are retained.")
add("7:5", "Noah did everything that the Lord God commanded him.",
    "The obedience formula names Noah, Lord God and all that was commanded. It does not include the extra so-he-did clause of 6:22; the inherited shorter wording therefore preserves the actual difference rather than harmonizing the repetitions.")
add("7:6", "Noah was 600 years old, and the flood of water came upon the earth.",
    "Noah's age 600 is connected with the flood's arrival. The inherited when expresses that temporal relation naturally. The source is a flood of water, not an unspecified disaster; the age must remain distinct from the 601st year in 8:13.")
add("7:7", "Noah and his sons and his wife and his sons' wives with him entered the ark because of the flood water.",
    "All household categories and the causal reason for entry remain. The source lists sons before wife here; the English preserves the order in its with phrase. Nothing in this verse gives names for the wives or permits adding household servants.")
add("7:8", "From the birds and the clean livestock and the unclean livestock and all creeping things upon the earth,",
    "This unit is a fronted source/category list whose verb appears in 7:9. Birds come first, and clean and unclean livestock are separately mentioned. The trailing comma preserves the cross-verse construction; it must not be exported as an isolated completed sentence.")
add("7:9", "two by two they entered to Noah into the ark, male and female, as God commanded him.",
    "The source says entered to Noah, whereas inherited with Noah can imply merely simultaneous accompaniment. Propose came to Noah in the ark-entry construction to make him the destination/person approached. Pairing and correspondence with God's command remain; this does not recalculate the sevens.",
    "two by two they came into the ark to Noah, male and female, as God had commanded him.")
add("7:10", "After the seven days, the flood water came upon the earth.",
    "The definite seven-day interval links back to the warning. The waters' arrival is repeated rather than deleted as redundant with 7:6. English condenses the double it-came-to-pass construction without creating a new event or changing its temporal relationship.")
add("7:11", "In Noah's 600th year, in the second month on its 27th day, on that day all the springs of the abyss burst and the floodgates of heaven opened,",
    "The displayed date is second month, twenty-seventh day, not the familiar seventeenth. All springs of the deep and heavenly floodgates form the paired water sources. On that day is repeated emphasis. No geological mechanism or alternative calendar is supplied.")
add("7:12", "and the rain was upon the earth for 40 days and 40 nights.",
    "Both forty-day and forty-night expressions are retained. Rain is the subject, with the earth as its location. The verse continues the event description after 7:11; the inherited sentence break is acceptable English and is not treated as a separate later rain period.")
add("7:13", "On that day Noah, Shem, Ham, Japheth, Noah's sons, Noah's wife and his sons' three wives with him entered the ark.",
    "The source explicitly names all three sons and counts their wives as three. The repeated Noah relations help identify the group and remain in the inherited text. Very in on that very day is an English emphatic rendering of the demonstrative; it is not an additional time datum.")
add("7:14", "and all wild beasts by kind, all livestock by kind, every moving creeping creature on earth by kind and every bird by kind",
    "The four animal classes and repeated kind expressions form the subject continued into 7:15. The English mixture of all and every is distributive and natural. The final unit has no verb in isolation, so the lack of closing punctuation must be preserved in reading output.")
add("7:15", "entered to Noah into the ark, two by two from all flesh in which is a spirit of life.",
    "As in 7:9, the source says to Noah, not merely with Noah. Propose came to Noah while retaining entry into the ark. Breath of life is a contextual rendering of the spirit/breath term and the two-by-two description remains. No animal kind is dropped from the preceding subject list.",
    "came into the ark to Noah, two by two of all flesh in which is the breath of life.")
add("7:16", "Those going in entered male and female from all flesh, as God commanded Noah, and the Lord God shut the ark outside him.",
    "The first sentence repeats entry and male/female pairing. The second explicitly names Lord God as closer of the ark, with the outside relation marking Noah inside. From the outside is natural English, though him is not repeated. God and Lord God differ within the verse and are preserved.")
add("7:17", "The flood was on the earth for 40 days and 40 nights; the water increased and lifted the ark, and it rose from the earth.",
    "Both days and nights are present in this selected Greek, as in the inherited English. The water lifts the ark, which becomes the subject of being raised. The repeated duration is retained without deciding whether this sentence introduces another forty-day interval.")
add("7:18", "The water prevailed and increased greatly over the earth, and the ark was borne upon the water.",
    "The imperfect verbs portray the developing flood. Floated is a contextual rendering of the ark being carried upon water. Water is grammatically singular in Greek; English waters is a normal collective rendering, not a new count of separate bodies of water.")
add("7:19", "The water prevailed exceedingly, exceedingly upon the earth and covered all the high mountains beneath heaven.",
    "The Greek intensifies with an adverb and related adverb together; the inherited one exceedingly compresses the deliberate repetition. Propose exceedingly, exceedingly to expose that emphasis in the literary candidate, with spoken cadence needing human review. All high mountains beneath heaven remains unchanged.",
    "And the waters prevailed exceedingly, exceedingly upon the earth, and covered all the high mountains beneath heaven.")
add("7:20", "The water was raised 15 cubits above and covered all the high mountains.",
    "The numeral is fifteen cubits. Above them in the inherited text supplies the mountains from the immediate context; the source says above without an expressed object. This is an intelligible contextual choice, not proof of a modern topographic measurement or an identified mountain summit.")
add("7:21", "All flesh moving upon the earth died: birds, livestock, wild beasts, every creeping thing moving upon earth and every human being.",
    "The classes culminate in every human being, and the moving-on-earth description is repeated. The inherited mankind is a collective rendering of that final distributive expression. No aquatic category is added to this stated list and no scientific extinction claim is inferred beyond its words.")
add("7:22", "Everything that has breath of life, and everyone who was on the dry land, died.",
    "This verse uses the breath noun, distinct from spirit/breath in 7:15. The two coordinated descriptions link life's breath and dry-land location. The inherited past had fits narration; the generic Greek present does not require a new present-day assertion. Dry land is not silently changed to the broader earth.")
add("7:23", "He wiped out every living thing on the face of all the earth, from human to livestock, creeping things and heaven's birds; they were wiped out, and Noah alone was left with those in the ark with him.",
    "The source moves from an implied singular wiping-out subject to passive wiping-out and then survivors. He follows the divine subject context rather than adding a newly named agent. Only modifies Noah together with those with him, not Noah alone to the exclusion of his household and the animals.")
add("7:24", "The water was raised on the earth for 150 days.",
    "The selected verb is raised/high, with 150 days as duration. Remained high is a natural contextual rendering that avoids implying a new discrete upward movement each day. The duration is kept separate from the forty days of rain; their relationship requires narrative chronology, not arithmetic addition by default.")

add("8:1", "God remembered Noah and all the wild beasts, livestock, birds and creeping things with him in the ark; God brought a wind on the earth, and the water subsided.",
    "The remembering includes Noah and every animal class, with all repeated before each category in the Greek and retained in the inherited English. Wind is a contextual sense of the spirit/breath noun. God is explicitly repeated before the bringing action. Remembered is not expanded into an assertion of prior forgetfulness.")
add("8:2", "The springs of the abyss and the floodgates of heaven were covered, and rain from heaven was held back.",
    "The two source openings from 7:11 are now closed/covered, and heavenly rain is restrained. The passive verbs do not name an agent within this clause. Closed is a natural contextual rendering of covered; it does not substitute a new mechanical explanation for the floodgates image.")
add("8:3", "The water was receding as it went away from the earth; the water was receding and diminishing after 150 days.",
    "The source repeats the recession verb and uses imperfect forms for receding and diminishing after 150 days. Inherited had receded and diminished can suggest completed recession by that point. Propose continued to recede and diminish after the stated interval, keeping the first steady withdrawal and the second repeated description.",
    "And the waters steadily withdrew from the earth; after one hundred and fifty days the waters continued to recede and diminish.")
add("8:4", "The ark settled in the seventh month, on its 27th day, on the mountains of Ararat.",
    "The seventh month and twenty-seventh day match the displayed source; neither is normalized to the seventeenth. Mountains is plural, so no single modern summit is named. Rested is an apt inherited rendering of settled/sat in the ark's narrative setting.")
add("8:5", "The water continued diminishing until the tenth month; in the eleventh month, on its first day, the mountain tops appeared.",
    "The source names the tenth month for diminishing and the eleventh for visible mountain tops. The inherited English correctly preserves that sequence even if it looks unlike a familiar account. First day and plural tops remain. The numbers are not corrected by internal harmonization or an unconsulted apparatus.")
add("8:6", "After 40 days Noah opened the ark's window which he had made,",
    "Forty days precede opening the window. The source now uses an actual window noun, unlike the difficult top instruction in 6:16. The relative which he made may attach to window or ark in English; the narrative does not separately date its construction. The sentence continues into the raven action.",
    unresolved=["The relative clause's precise attachment should be checked in the full construction."])
add("8:7", "and he sent the raven to see whether the water had subsided; it went out and did not return until the water dried from the earth.",
    "The source explicitly gives the testing purpose and the raven's non-return until drying. That is retained rather than substituting going to and fro from another tradition. Until marks the stated limit but does not by itself prove that the raven returned afterward.")
add("8:8", "He sent the dove after it to see whether the water had subsided from the earth's face.",
    "The dove follows the raven. The masculine pronoun can refer back to the raven, making after it contextually apt; it is not changed to a claim that the dove flew physically behind Noah. The purpose and earth's face are retained without adding a new waiting interval.")
add("8:9", "The dove found no rest for its feet and returned to him into the ark, because water was on the whole face of all the earth; he stretched out his hand, took it and brought it to himself into the ark.",
    "Failure to find foot-rest motivates the return. Noah's three actions—reaching, taking and bringing inside—remain distinct, and the destination is repeated. The inherited whole face of the earth naturally combines the Greek repeated totality wording. No statement about the dove's exhaustion is supplied.")
add("8:10", "He waited another seven days and again sent the dove out from the ark.",
    "Another seven and again are both explicitly grounded in the Greek. The ark is the departure point and the dove is the same repeated bird. The text gives no new reason for selecting the interval, and none is added.")
add("8:11", "The dove returned to him toward evening and had an olive leaf, a stalk, in its mouth; Noah knew the water had subsided from the earth.",
    "The source has an olive leaf followed by the difficult stalk/twig term. Inherited olive sprig with a leaf is a plausible construal, retained provisionally rather than certified as exact botany. Mouth is naturally beak for a bird. Freshly plucked is not inserted because this displayed word does not transparently say that.",
    unresolved=["Relation of leaf and stalk/twig needs specialist lexical and botanical review; close-stage apposition intentionally exposes the difficulty."])
add("8:12", "He waited another seven days and again sent the dove, and it did not return to him any more.",
    "A second seven-day wait and another sending are explicit. The negative add-to-return idiom means it no longer returned. The inherited no more conveys this without retaining an awkward literal addition verb or inventing where the dove settled.")
add("8:13", "In Noah's 601st year, the first month on its first day, the water vanished from the earth; Noah uncovered the ark's roof which he made and saw the water had vanished from the earth's face.",
    "The year is 601, with first month and first day. Removal/uncovering of the roof is distinct from the earlier window opening. The source repeats water's disappearance before and after Noah's observation, and the inherited English preserves that. Covering is retained as a broad roof term; it is not equated with the door.")
add("8:14", "In the second month, on its 27th day, the earth dried.",
    "The second month and twenty-seventh day are explicit. The land's drying is a later statement than the water's disappearance in 8:13; the inherited dry preserves the resulting state without collapsing the two dates. No modern calendar conversion is attempted.")
add("8:15", "The Lord God spoke to Noah, saying,",
    "The full Lord God title and Noah as recipient introduce the following exit command. The inherited wording agrees. Its lack of a complete quoted command within this unit is intentional, so the verse must remain joined to 8:16 in reading flow.")
add("8:16", "'Go out from the ark, you and your wife and your sons and your sons' wives with you,",
    "The exit imperative is singular to Noah, with the household added. Wife precedes sons here, and that order is retained rather than harmonized to earlier lists. Come out is a natural English directional rendering; it does not establish the speaker's physical location.")
add("8:17", "and bring out with yourself all wild beasts with you and all flesh from birds to livestock and every moving creeping thing on the earth; grow and multiply on the earth.'",
    "Bring out is singular, while grow and multiply shift to plural. Ordinary English imperatives leave that distinction implicit, so it is recorded here. All animal groups and the earth location remain. The command does not add a separate swarm verb from another version.")
add("8:18", "Noah went out, and his wife and his sons and his sons' wives with him,",
    "The exit fulfillment repeats the household members in the order of 8:16. With him is compressed into the inherited with phrase and all persons remain represented. The source continues into the animals' exit; the English sentence break does not establish a different departure day.")
add("8:19", "all wild beasts and all livestock and every bird and every moving creeping thing on earth went out of the ark according to their kind.",
    "All four animal groups exit the ark. The final Greek kind is singular with a plural possessive; propose their kind instead of their kinds, matching the same construction at 6:20. No claim is made that this grammatical category is identical with a modern biological species.",
    "And all the wild beasts, all the cattle, every bird, and every creeping thing that moves upon the earth came out of the ark according to their kind.")
add("8:20", "Noah built an altar to God, took from all the clean livestock and all the clean birds, and offered whole burnt offerings on the altar.",
    "God is the recipient, without Lord in this clause. The two clean animal classes and whole-burnt offering term are retained. Every kind is an English distributive construal of from all, not an extra Greek kind noun. The source does not enumerate the number sacrificed or state that every survivor was offered.")
add("8:21", "The Lord God smelled a fragrant odor and, reflecting, said, 'I will not again curse the earth because of human works, because human thought is intently set on evil from youth; therefore I will not again strike all living flesh as I did.'",
    "The sensory image and reflective speech are retained. Human works are the stated reason, and intentness from youth remains distinct from time duration. The two not-again clauses promise no repetition in the expressed scope; the inherited never again is idiomatic. This does not erase every possible judgment or define a doctrine of inherited guilt.")
add("8:22", "All the earth's days, seed and harvest, cold and heat, summer and spring will not cease by day and night.'",
    "The selected Greek has summer and spring, not winter; the inherited wording preserves it. Seedtime is contextual for seed in this agricultural pair. Day and night are accusative time expressions after the paired nouns, so by day or night is defensible. A continuous agrarian cycle is stated without an imported climate model.")

add("9:1", "God blessed Noah and his sons and said to them, 'Grow and multiply and fill the earth and subdue it.'",
    "The blessing addresses Noah and the sons together with four plural imperatives. Subdue it is present in this selected Greek and must not be dropped to match a shorter tradition. No modern political mandate is added to the source's earth-directed wording.")
add("9:2", "Your dread and fear will be upon all earth's wild beasts, all heaven's birds, all things moving on earth and all sea fish; I have given them under your hands.",
    "The two fear terms and all four animal categories are retained. Of you in the inherited phrase interprets the possessive as fear inspired by the human addressees, not their fear of animals. The giving is expressed as completed with current effect, and the hand image is preserved.")
add("9:3", "Every living moving creature will be food for you; as the green herbage, I have given you everything.",
    "The living-creature grant and comparison with vegetation are present. The inherited as I gave supplies the earlier giving from context; it does not reflect an additional finite verb in this clause. Everything refers within the food comparison and is not expanded into an unrestricted moral permission.")
add("9:4", "But flesh in the blood of life you shall not eat.",
    "The exception combines flesh, blood and life in a compact construction. Lifeblood is a natural English compound for the relation and keeps the prohibition intelligible. The source addresses the group plurally. It does not settle every later ritual rule or directly specify a preparation technique.")
add("9:5", "For I will require your blood, of your lives; from the hand of every beast I will require it, and from the hand of a brother-human I will require the human's life.",
    "The source repeats require three times, including beasts and a fellow human as accountable parties. The inherited English retains that sequence and the blood/life linkage. Surely expresses rhetorical weight rather than a separate certainty adverb. The precise brother/fellow-human construction deserves syntactic review; no class of exempt humans is added.",
    unresolved=["The attachment and breadth of the brother/fellow-human expression require fuller syntactic study."])
add("9:6", "The one shedding a human's blood shall be poured out in return for his blood, because I made the human being in God's image.",
    "The source's passive subject is formally the blood-shedder, with a difficult in-return-for-his-blood phrase. Inherited his own blood shall be shed is an intelligible metonymic interpretation, not a literal repetition of a second blood subject. I made is first-person in this Greek and is correctly retained. No human execution agent is supplied.",
    unresolved=["Whose blood the exchange phrase denotes and how to express the person-as-poured-out construction need specialist syntax review."])
add("9:7", "But you, grow and multiply and fill the earth and multiply upon it.'",
    "The second-person plural is emphatic, and multiply appears twice with filling between. The inherited English preserves the repetition instead of replacing the last verb with a synonym or importing swarm. This closes the speech without adding another covenant clause.")
add("9:8", "God spoke to Noah and his sons with him, saying,",
    "Both Noah and his sons receive the new speech. God is the title here, and the with-him relationship remains. The unit is intentionally an introduction whose saying is completed by 9:9, not a self-contained quotation.")
add("9:9", "'I, behold, am establishing My covenant for you and for your seed after you,",
    "The present establishment and explicit possessive covenant are retained. Seed is collective and includes those after the current addressees. The emphatic I plus behold is naturally expressed with Behold, I. No named later nation or institution is inserted as the sole descendant group.")
add("9:10", "and for every living creature with you, from birds and livestock to all the earth's wild beasts with you, from all that left the ark.",
    "The living-creature scope includes the listed birds, livestock and wild beasts. The repeated with-you connection and ark-exit scope are preserved. The source has a living-soul expression; creature is its contextual English realization, not a denial or assertion of a philosophical soul theory.")
add("9:11", "I will establish My covenant with you; all flesh will not again die from flood water, and there will not again be a flood of water to destroy all the earth.'",
    "The two negative future statements concern all flesh and destruction of the whole earth. The inherited English does not promise that no individual will ever die in a flood. Both covenant establishment and its announced flood scope remain, with no new mechanism or universal prohibition on water disasters.")
add("9:12", "The Lord God said to Noah, 'This is the covenant sign I give between Me and you and every living creature with you for everlasting generations:'",
    "The fuller Lord God title returns here. The sign links God, the plural human addressees and living creatures, with lasting generations as its scope. The repetition of between is compressed naturally in English, without excluding the animals or changing the sign into the covenant itself.")
add("9:13", "'I set My bow in the cloud; it will be a sign of covenant between Me and the earth.'",
    "Bow and cloud are singular in the source. Retaining bow leaves the visible image without an inserted scientific explanation. The speaker's possessive and the covenant relation to earth are explicit. The present setting does not independently resolve whether the physical phenomenon had existed before.")
add("9:14", "'When I gather clouds over the earth, My bow will be seen in the cloud,'",
    "The source repeats the cloud word in verbal and nominal forms. Gather clouds is idiomatic English for that weather action, and shall appear naturally renders the passive be seen. The divine speaker remains the agent of the clouding, without adding an unexpressed viewer for the bow.")
add("9:15", "'and I will remember My covenant between Me and you and every living creature in all flesh; the water will not again become a flood to wipe out all flesh.'",
    "Remembering the covenant leads to the reiterated flood limit. Every living creature in all flesh is represented by the inherited of-all-flesh wording without treating creature and flesh as two distinct covenant parties. Wipe out echoes the earlier destruction language and remains the stated result being denied.")
add("9:16", "'My bow will be in the cloud, and I will look so as to remember an everlasting covenant between Me and every living creature in all flesh upon the earth.'",
    "Looking has an expressed remembering purpose. The inherited look upon it supplies the bow as the obvious object and coordinates remember naturally. Everlasting qualifies the covenant. No inference is made that divine remembrance requires correction of a previous lapse.")
add("9:17", "God said to Noah, 'This is the sign of the covenant I established between Me and all flesh upon the earth.'",
    "The summary again distinguishes sign from covenant and extends the stated relation to all flesh on earth. The source uses a past covenant-establishing form, represented by have established. God rather than Lord God is retained at this verse.")
add("9:18", "Noah's sons who left the ark were Shem, Ham and Japheth; Ham was Canaan's father.",
    "All three sons and the repeated Ham identification remain. The relation to Canaan prepares the next episode but does not itself assign guilt. The inherited name spellings are preserved, and no additional son is inferred from the narrative's later kinship language.")
add("9:19", "These three are Noah's sons; from these people were scattered over all the earth.",
    "The explicit three is repeated, and the dispersion clause has an unstated plural subject. People is supplied in the inherited text to make that referent intelligible. Present are becomes were in English narration without changing identity. No modern ethnicity or map is equated with the three figures.")
add("9:20", "Noah began as a man cultivating the ground and planted a vineyard.",
    "The source's began plus cultivator-of-earth wording is compressed into began to till the ground. That is natural but not proof that Noah invented agriculture. Vineyard planting remains the second action, and no earlier grape-growing history is asserted or denied.")
add("9:21", "He drank from the wine, became drunk and was uncovered in his house.",
    "Drinking, drunkenness and uncoveredness are distinct. The source says house, so it is retained rather than substituted with tent from another textual form. Lay is supplied in the inherited reading though the Greek does not explicitly state posture; propose was uncovered to avoid adding that detail.",
    "And he drank of the wine and became drunk, and was uncovered in his house.")
add("9:22", "Ham, Canaan's father, saw his father's nakedness and went out and told his two brothers outside.",
    "The source explicitly repeats Canaan's father and specifies two brothers outside. Saw and reported are the stated actions. No sexual act, motive or additional misconduct is invented to explain the later curse; such interpretations require evidence outside this sentence.")
add("9:23", "Shem and Japheth took the garment, put it over their two backs and went backward; they covered their father's nakedness, their faces turned backward, and did not see his nakedness.",
    "The garment, backward movement, covering and explicit non-seeing are retained. Shoulders is a contextual English rendering of the backs as the garment's support, not a literal body-word match. The source repeats nakedness three times, and the inherited text retains all three occurrences. No claim about what they had previously seen is added.")
add("9:24", "Noah became sober from the wine and learned what his younger son had done to him,",
    "The selected verb concerns recovering sobriety, not explicitly waking from sleep. Propose became sober instead of awoke to avoid importing sleep from the scene. Younger follows the comparative form; youngest remains a contextual possibility requiring kinship review, not an automatic replacement.",
    "And Noah became sober from his wine and knew what his younger son had done to him.",
    ["The younger/youngest relationship and the precise referent of son remain contextual questions."])
add("9:25", "and said, 'Cursed is Canaan; he will be a household slave to his brothers.'",
    "Canaan is the named subject of the curse, not Ham or an entire modern population. Household slave represents the paired servant/household-servant expression without importing a Hebrew-based servant-of-servants superlative. The future relationship to brothers remains; this reported curse is not an instruction endorsing enslavement.")
add("9:26", "He said, 'Blessed is the Lord, Shem's God; Canaan will be his servant.'",
    "The blessing names the Lord as Shem's God. His servant has an unresolved pronoun attachment in isolation, which the inherited English preserves rather than deciding between God and Shem by a new noun. The text does not say Shem himself is the one called blessed.",
    unresolved=["Antecedent of his in the servant clause requires fuller discourse review."])
add("9:27", "'May God enlarge Japheth, and let him dwell in Shem's houses; let Canaan become their servant.'",
    "The wish for enlargement, dwelling clause and plural their-servant conclusion are retained. Houses is plural in this Greek, not tents. The implied subject of dwelling can be read as Japheth or God; lower-case he preserves the inherited interpretation without adding a name. The ambiguity is explicitly open.",
    unresolved=["The implied subject of dwell may be Japheth or God; a final editorial choice requires review."])
add("9:28", "Noah lived 350 years after the flood.",
    "The interval is 350 after the flood, not a total lifespan. It is retained without shifting the calculation to the ark exit. Combined with the 600-year flood age it matches the following 950 total at the stated precision.")
add("9:29", "All Noah's days were 950 years, and he died.",
    "The total 950 and death clause close Noah's life record. The total equals 600 plus 350 from the cited narrative ages. This internal arithmetic does not settle the exact anniversary or the more complex dates during the flood year.")

add("10:1", "These are the generations of Noah's sons, Shem, Ham and Japheth; sons were born to them after the flood.",
    "The genealogy heading includes all three sons in the stated order and dates their offspring after the flood. Generations is the established heading word. The source does not say that every name later listed is a biological son in the same immediate generation; list relationships must be read individually.")
add("10:2", "Japheth's sons: Gomer, Magog, Madai, Javan, Elishah, Tubal, Meshech and Tiras.",
    "All eight displayed names are preserved in order, including Elishah here as well as in 10:4. The inherited forms are conventional equivalents of the Greek spellings, not fresh transliterations. The apparent repeated Elishah is not silently deleted or reconciled with another genealogy.",
    unresolved=["The repeated placement of Elishah needs source/apparatus review; no correction is adopted."])
add("10:3", "Gomer's sons: Ashkenaz, Riphath and Togarmah.",
    "The three offspring and their order match the displayed Aschanaz, Riphath and Thorgama forms. Established English spelling is retained. No modern ethnic identity or geographic location is inferred from phonetic resemblance.")
add("10:4", "Javan's sons: Elishah and Tarshish, Kittians and Rhodians.",
    "The source has two personal/place-like names followed by the plural Kittians and Rhodians. Those ethnonym forms and Rhodians rather than Dodanim are retained. Elishah also appears at 10:2; the two placements are preserved as source data, not harmonized away.")
add("10:5", "From these the islands of the nations were separated in their land, each according to language, in their tribes and nations.",
    "The islands/nations, territorial setting, language, tribes and nations are all present. Their lands in the inherited text distributes the Greek singular land over the groups; it does not claim the Greek noun is plural. Each refers contextually to the groups in the genealogical geography, not necessarily to each island as a speaker.")
add("10:6", "Ham's sons: Cush, Mizraim, Put and Canaan.",
    "Four names are listed in this order. Cush/Mizraim/Put are inherited English equivalents of Chous/Mesraim/Phoud. No modern nation is substituted and no curse is attached to this entire genealogy from the separate Canaan episode.")
add("10:7", "Cush's sons: Seba, Havilah, Sabtah, Raamah and Sabteca; Raamah's sons: Sheba and Dedan.",
    "The five-member list and then the two-member list remain distinct. Both Seba and Sheba correspond to the same displayed Saba spelling in their respective positions; their different English forms are inherited naming conventions, not a lexical distinction proved by Greek orthography. Raamah maps the displayed Regma provisionally.",
    unresolved=["A full name authority should document conventional Hebrew-shaped equivalents and the repeated Greek Saba form."])
add("10:8", "Cush begot Nimrod; he began to be a giant upon the earth.",
    "The source names Nebrod, represented by inherited Nimrod, and uses giant rather than merely mighty man. The began-to-be construction is retained. It does not establish biological size, parentage beyond Cush or a moral evaluation by itself.")
add("10:9", "He was a giant hunter before the Lord God; therefore they will say, 'Like Nimrod, a giant hunter before the Lord.'",
    "The first divine title is Lord God and the repeated saying has Lord alone. The reporting verb is future plural they will say, whereas inherited it is said changes tense and voice. A customary or gnomic future can justify the inherited present as a contextual rendering; the future active is therefore a proposal exposing the Greek form, not proof that the inherited tense was wrong. Before remains neutral between presence and a more adversarial interpretation.",
    "He was a giant hunter before the Lord God; therefore they shall say, “Like Nimrod, a giant hunter before the Lord.”")
add("10:10", "The beginning of his kingdom was Babylon, Erech, Akkad and Calneh, in Shinar's land.",
    "Four names are coordinated as the beginning of the kingdom. The inherited Akkad and Calneh are conventional mappings for the displayed Archad and Chalanne, not spelling evidence obtained here. Babylon and Shinar remain distinct place labels; no empire chronology is added.",
    unresolved=["Archad/Akkad and Chalanne/Calneh should be reconciled in the project name authority."])
add("10:11", "From that land Asshur went out and built Nineveh, Rehoboth city and Calah,",
    "Asshur is the apparent named subject of went out in this Greek reading; it is not silently converted into Nimrod traveling to Assyria. The three building objects continue into Dasem in 10:12. The city designation with Rehoboth is retained rather than treated as another independent place name.")
add("10:12", "and Dasem between Nineveh and Calah; this is the great city.",
    "Dasem is the displayed name and is retained, not substituted by Resen. The between relation is explicit. The demonstrative great-city comment may refer to the immediately named city or the larger described setting; the inherited this leaves that interpretation open.",
    unresolved=["Referent of this in the great-city comment needs contextual/geographical study."])
add("10:13", "Mizraim begot the Ludim, Enemetim, Lubim and Naphtuhim,",
    "The four plural group names are preserved in sequence and the sentence continues into 10:14. Enemetim follows the Greek-specific inherited form. Begot is genealogical group language here; it is not proof that each ethnonym describes one individual person.")
add("10:14", "the Pathrusim and Casluhim, from where the Philistines came, and the Caphtorim.",
    "The final three group names remain, with the Philistine origin parenthesis placed after Casluhim as in the displayed source. From whom in the inherited wording interprets the locative from-where with people as antecedent. It is not relocated after Caphtorim to harmonize a different tradition.")
add("10:15", "Canaan begot Sidon the firstborn and the Hittite,",
    "Sidon's firstborn status and the Hittite as a following singular collective designation are retained. The inherited his supplies Canaan as the natural possessor. The source begins a list continuing through 10:18, so the comma and continuity matter.")
add("10:16", "and the Jebusite and the Amorite and the Girgashite,",
    "All three singular ethnic designations and their order are retained within Canaan's list. They are not silently pluralized into a census. The inherited comma sequence realizes the repeated coordination naturally while the governing begot remains in 10:15.")
add("10:17", "and the Hivite and the Arkite and the Sinite,",
    "The source has Euaios, Aroukaios and Asennaios; the inherited Hivite, Arkite and Sinite are retained as established mappings. This comparison verifies list position and count, not the historical equivalence of every conventional spelling. No additional ethnic group is inferred from the Greek endings.")
add("10:18", "and the Arvadite and the Zemarite and the Hamathite; after this the Canaanite tribes were scattered.",
    "The last three group names close the list, followed by dispersal of the Canaanite tribes. The inherited mappings for Aradios, Samaraios and Amathi remain provisional name-authority decisions. The after-this transition and plural tribes are retained; no date or direction of scattering is supplied.")
add("10:19", "Canaanite borders were from Sidon as far as Gerar and Gaza, as far as Sodom and Gomorrah, Admah and Zeboiim, up to Lasha.",
    "Both route-like as-far-as expressions and the final Lasha limit remain. Toward in the inherited text is natural directional phrasing, not surveyed coordinates. All named places are preserved in order. Modern border identifications are outside this running-text check.")
add("10:20", "These are Ham's sons in their tribes, according to their languages, in their territories and nations.",
    "The summary distinguishes tribes, languages, territories and nations. The inherited according-to construction groups tribes and languages for English flow without dropping either. This is a genealogical-geographical summary, not an explanation of the origin of a modern racial classification.")
add("10:21", "To Shem also offspring were born, the father of all Eber's sons and brother of the elder Japheth.",
    "The source calls Shem father of Eber's descendants and brother of Japheth the elder. The Greek genitive elder attaches naturally to Japheth in this wording, as the inherited text indicates. Children is supplied for the birth idiom. No simultaneous-birth claim is made from chapter five's age summary.")
add("10:22", "Shem's sons: Elam, Asshur, Arphaxad, Lud, Aram and Cainan.",
    "The displayed list includes Cainan as a sixth name; it is retained despite his later placement under Arphaxad. The five other names and order are unchanged. This batch does not resolve the genealogical level of sons or erase an apparent overlap using another source.",
    unresolved=["Cainan's list position versus the successive begetting chain needs apparatus and genealogical review."])
add("10:23", "Aram's sons: Uz, Hul, Gether and Meshech.",
    "The four displayed names correspond to inherited Uz, Hul, Gether and Meshech. The final Greek Mosoch supports retaining Meshech rather than importing Mash. Shared spelling with an earlier name does not establish that both refer to the same individual or people.")
add("10:24", "Arphaxad begot Cainan, Cainan begot Shelah, and Shelah begot Eber.",
    "All three begetting links are explicit, including the intermediate Cainan. The inherited chain agrees and must not be shortened to Arphaxad–Shelah from another tradition. It anticipates the grouped Cainan material preserved under the existing 11:13 anchor.")
add("10:25", "Two sons were born to Eber: one was named Peleg because the earth was divided in his days; his brother was named Joktan.",
    "The source says one rather than firstborn. The inherited first can be understood as list order, but close one avoids implying birth seniority. The earth-division explanation belongs to the name report; it does not specify geological continental separation or a modern date.")
add("10:26", "Joktan begot Almodad, Sheleph, Hazarmaveth and Jerah,",
    "These first four names begin Joktan's list, continuing through 10:29. The inherited forms correspond to the displayed Elmodad, Saleph, Asarmoth and Iarach in order. No unconsulted etymology is used to replace them with translated meanings.")
add("10:27", "and Hadoram, Uzal and Diklah,",
    "The next three names match the positions of Odorra, Aizel and Dekla. Conventional inherited English spellings remain pending a complete names register. The line is a continuation, not a new father-and-sons genealogy.")
add("10:28", "and Abimael and Sheba,",
    "Two names, Abimael and Sabeu in the displayed Greek, remain as inherited Abimael and Sheba. The latter is not automatically equated with every previous Saba/Sheba occurrence. Both entries and their position in Joktan's list are retained.")
add("10:29", "and Ophir, Havilah and Jobab; all these are Joktan's sons.",
    "The final three names and all-these summary close the list. The displayed Ouphir, Euila and Iobab map to the inherited forms. The genealogy's all is not omitted, and no gold-source geography is inserted from other passages.")
add("10:30", "Their dwelling extended from Mesha as far as Sephar, a mountain of the east.",
    "The two limits and the eastern mountain description are retained. The inherited the mountain is an English definiteness choice, not proof of a uniquely identified modern mountain. The source provides no coordinates, and this batch does not establish them.")
add("10:31", "These are Shem's sons in their tribes, according to their languages, in their territories and nations.",
    "The four classification dimensions parallel the Ham summary while the subject changes to Shem's descendants. All remain in the inherited text. Repetition is part of the genealogy's organization and is not removed as redundant prose.")
add("10:32", "These are the tribes of Noah's sons according to their generations and nations; from these the islands of the nations were scattered on earth after the flood.",
    "The source expressly repeats islands of the nations, with dispersion after the flood. The inherited text retains islands rather than simplifying it to nations alone. The according-to genealogy and nation terms remain distinct, without claiming each tribe corresponds one-to-one with an island.")

add("11:1", "The whole earth was one lip, and one voice belonged to all.",
    "Lip and voice are two speech images. The inherited one language and shared speech is an intelligible contextual rendering rather than a claim about vocal anatomy. The universal scope and repeated one are preserved. No historical language is identified as the common speech.")
add("11:2", "As they moved from the east, they found a plain in Shinar's land and settled there.",
    "The source direction is from the east; it is retained rather than silently changed to eastward. Finding the plain and settling are separate actions. Shinar follows the inherited place authority, with no modern coordinates or migration date added.")
add("11:3", "Each person said to his neighbor, 'Come, let us make bricks and fire them with fire.' Brick served them for stone, and bitumen was their mortar.",
    "The source repeats the brick root and explicitly names fire. The two substitute building materials are contrasted with stone and mortar. The inherited make bricks/burn them in the fire preserves the process naturally without inventing kiln technology or a motive for lacking stone.")
add("11:4", "They said, 'Come, let us build a city and tower for ourselves, whose head will reach heaven, and make a name for ourselves before we are scattered over all earth's face.'",
    "The source says before scattering, not lest scattering occur. That distinction is preserved. Head is naturally summit for the tower, and ourselves repeats the collective purpose. Reach unto heaven reflects the height image without asserting a physical plan to invade a divine realm.")
add("11:5", "The Lord came down to see the city and tower that the sons of human beings built.",
    "The divine title is Lord alone. Both city and tower are objects of seeing, with human builders named. Children of men is an established idiom for the Greek human-descendants phrase. The descent image is preserved without an explanatory claim about God's previous inability to observe.")
add("11:6", "The Lord said, 'Behold, one people and one lip belong to all, and they began to do this; now nothing they undertake to do will fail them.'",
    "The source joins one people and one speech with the beginning of this activity. Nothing will fail them is a reasonable idiomatic rendering of the negative-plus-all construction. This reports the speaker's assessment in context, not a scientific assertion of human omnipotence. No unexpressed evil adjective is added to their plans.")
add("11:7", "'Come, let Us go down and confuse their language there, so that each may not understand his neighbor's voice.'",
    "The source has a negative purpose clause without a separate no-longer expression. Propose may not understand instead of may no longer understand, preserving the mutual communication sense without an additional temporal adverb. The plural deliberation is retained; capital Us is inherited editorial styling, not identification of its participants.",
    "“Come, let Us go down and confound their language there, so that they may not understand one another’s speech.”")
add("11:8", "The Lord scattered them from there over all earth's face, and they stopped building the city and the tower.",
    "The source explicitly includes both city and tower in the cessation clause. Both remain in English rather than reducing the object to the city alone. Scattering from there answers the prior speech; no timeline or number of new language groups is supplied.")
add("11:9", "Therefore its name was called Confusion, because there the Lord confused the lips of all the earth, and from there the Lord God scattered them over all earth's face.",
    "The source names the place by the translated meaning Confusion. Its plural lips is a speech metaphor and does not require multiple pre-existing languages; propose the collective speech instead of languages. Lord appears in the first explanation and Lord God in the second, preserved in the candidate. No automatic substitution of Babel or Babylon is made.",
    "Therefore its name was called Confusion, because there the Lord confounded the speech of the whole earth, and from there the Lord God scattered them over the face of the whole earth.")
add("11:10", "These are Shem's generations: Shem was 100 years old when he begot Arphaxad, in the second year after the flood.",
    "The source explicitly gives age 100 and second year after the flood. These are retained without forcing Shem's birth into the same year as all sons in 5:32. Generations marks a new genealogy and does not mean the upcoming list contains only one generation.")
add("11:11", "Shem lived 500 years after begetting Arphaxad and begot sons and daughters, and died.",
    "The post-Arphaxad interval is 500, with both offspring categories and an explicit death. The implied total 600 is an arithmetic observation, not a number printed in this verse; it is therefore not inserted into the candidate text.")
add("11:12", "Arphaxad lived 135 years and begot Cainan.",
    "The displayed age is 135 and the son is Cainan. Both are retained rather than substituted with another tradition's age or Shelah as direct offspring. This begetting links to the full Cainan material in the next stored unit.")
add("11:13", "Arphaxad lived 430 years after begetting Cainan and begot sons and daughters, and died. Cainan lived 130 years and begot Shelah. Cainan lived 330 years after begetting Shelah and begot sons and daughters, and died.",
    "The publisher places three genealogical statements under this verse: Arphaxad's 430 later years and death, Cainan's 130 before Shelah, and Cainan's 330 afterward with offspring and death. All remain inside the existing v11-13 anchor. No invented 13a/13b verse identity or omitted Cainan is used. Arphaxad's 565 and Cainan's 460 totals are derived only in the separate number audit.")

GEN11 = [
    (14, "Shelah", "Eber", 130, 330),
    (16, "Eber", "Peleg", 134, 370),
    (18, "Peleg", "Reu", 130, 209),
    (20, "Reu", "Serug", 132, 207),
    (22, "Serug", "Nahor", 130, 200),
    (24, "Nahor", "Terah", 79, 129),
]
for first, parent, child, before, after in GEN11:
    add(f"11:{first}", f"{parent} lived {before} years and begot {child}.",
        f"The displayed pre-begetting age is {before}, with {parent} as subject and {child} as offspring. The inherited names and number agree. No other edition's chronology is substituted; a full name authority and apparatus audit remain separate work.")
    add(f"11:{first+1}", f"{parent} lived {after} years after begetting {child}, begot sons and daughters, and died.",
        f"The source gives {after} years after {child}, followed by sons, daughters and death. All clauses remain in the inherited text. The implied {before + after}-year lifespan is an arithmetic sum, not an explicitly printed total here, so it is not added to Scripture.")

add("11:26", "Terah lived 70 years and begot Abram, Nahor and Haran.",
    "Age 70 introduces three named sons in this order. As in Noah's summary, it does not alone prove that all three were born simultaneously or identify each birth year. Abram is retained rather than prematurely renamed Abraham, and Haran the person remains distinct from Harran the place.")
add("11:27", "These are Terah's generations: Terah begot Abram, Nahor and Haran, and Haran begot Lot.",
    "The repeated three-son list and Haran–Lot link are explicit. The relative generations are not compressed into a list of Terah's direct sons that would wrongly include Lot. The established name forms preserve the narrative's family structure.")
add("11:28", "Haran died before Terah his father in the land where he was born, in the country of the Chaldeans.",
    "The source says country of the Chaldeans and does not name Ur here. The inherited in the presence of preserves a spatial reading of before, while death during Terah's lifetime is also contextually relevant. No city is imported or birthplace assigned beyond the given country.",
    unresolved=["The spatial/temporal nuance of before his father merits contextual review."])
add("11:29", "Abram and Nahor took wives: Abram's wife was named Sara, and Nahor's Milcah, Haran's daughter; Haran was father of Milcah and Iscah.",
    "Both marriages, Milcah's parentage and the two daughters of Haran are preserved. Sara is the established pre-name-change form and should not be normalized to Sarah. The source does not identify Iscah with Sara, so that traditional inference is not inserted.")
add("11:30", "Sara was barren and did not bear children.",
    "The state and the repeated lack of childbearing are both present. The inherited wording agrees and is not expanded into a medical diagnosis or permanent impossibility. The imperfect narrative describes her situation at this stage of the account.")
add("11:31", "Terah took Abram his son, Lot son of Haran his son's son, and Sara his daughter-in-law, Abram's wife; he led them from the Chaldeans' country to go to Canaan, came as far as Harran and settled there.",
    "Terah is the singular actor in taking, leading, coming and settling. All kinship links are retained, especially Lot as grandson through Haran. Country of Chaldeans remains without Ur. The intended Canaan destination is distinct from actual Harran settlement; inherited but is a contextual contrast rather than a separate Greek adversative.")
add("11:32", "Terah's days in Harran were 205 years, and Terah died in Harran.",
    "The displayed Greek explicitly attaches in Harran to the 205-year days statement and repeats Harran at death. Both locations and the number remain even though a literal residence-length reading creates chronological questions. No silent harmonization to a simple total lifetime is adopted.",
    unresolved=["How the in-Harran lifespan phrase relates to Terah's earlier years needs textual and chronological study."])


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8", newline="\n")


def build():
    raw = subprocess.check_output(["git", "show", BASELINE + ":genesis/verses.json"], cwd=ROOT)
    source = json.loads(raw)
    current = json.loads((ROOT / "genesis/verses.json").read_text(encoding="utf-8"))
    expected = [(str(c["chapter"]), v) for c in source["chapters"] if 5 <= c["chapter"] <= 11 for v in c["verses"]]
    actual = [(str(c["chapter"]), v) for c in current["chapters"] if 5 <= c["chapter"] <= 11 for v in c["verses"]]
    assert expected == actual, "The local benchmark differs from the pinned source; inspect before rebuilding."
    assert len(expected) == 193
    assert set(ROWS) == {v["reference"].split(" ", 1)[1] for _, v in expected}
    records = []
    for chapter, verse in expected:
        ref = verse["reference"].split(" ", 1)[1]
        authored = ROWS[ref]
        candidate = authored["candidate"] or verse["text"]
        changed = candidate != verse["text"]
        record = {
            "record_type": "focused_running_text_comparison",
            "review_id": "OT-005-genesis-" + ref.replace(":", "-"),
            "batch_id": "OT-005",
            "book_id": "genesis",
            "reference": verse["reference"],
            "verse_anchor": verse["id"],
            "reading_section_id": chapter,
            "baseline_commit": BASELINE,
            "baseline_text": verse["text"],
            "candidate_text": candidate,
            "candidate_sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
            "decision": "propose_revision" if changed else "retain_provisionally",
            "source": {
                "edition": "Rahlfs–Hanhart 2006",
                "url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{chapter}",
                "accessed_on": DATE,
                "running_text_read": True,
                "apparatus_consulted": False,
            },
            "drafts": {"close": authored["close"], "spoken": candidate, "literary": candidate},
            "draft_stage_note": "The close draft was authored from the displayed Greek. Spoken and literary stages retain the stated candidate after contextual comparison; identical stages do not constitute human read-aloud review.",
            "analysis": authored["analysis"],
            "unresolved_questions": authored["unresolved_questions"],
            "review": {
                "reviewer": "OpenAI Codex assistant",
                "type": "AI",
                "scope": "Focused whole-unit running-text comparison with authored close draft; not exhaustive token accounting.",
                "all_tokens_accounted_for": False,
                "independent_greek": None,
                "human_read_aloud": None,
                "editorial_acceptance": None,
            },
            "benchmark_change": changed,
            "publication": {"staging": None, "production": None},
        }
        if changed and verse.get("poetic_line_breaks", 0):
            raise AssertionError("A changed poetic unit needs explicit display-text treatment: " + ref)
        records.append(record)
    changes = [r for r in records if r["benchmark_change"]]
    result = {
        "schema_version": "1.0", "batch_id": "OT-005", "date": DATE,
        "scope": "Genesis 5–11; all 193 inherited stored units, including the full grouped Cainan passage at 11:13",
        "status": "focused_comparison_draft_not_accepted",
        "baseline_commit": BASELINE, "benchmark_preserved": True,
        "counts": {"compared_units": len(records), "proposed_revisions": len(changes),
                   "retained_units": len(records)-len(changes), "accepted_units": 0},
        "limitations": "AI source-led running-text review only. Full Greek token accounting, specialist lexical evidence, apparatus/Göttingen collation, independent qualified Greek review, human reading aloud, acceptance and website publication remain pending.",
        "records": records,
    }
    write_json("focused-reviews.json", result)
    sources = {
        "batch_id": "OT-005", "accessed_on": DATE,
        "edition": "Septuaginta, Alfred Rahlfs; second revised edition, Robert Hanhart, 2006, German Bible Society",
        "access_method": "Publisher chapter pages retrieved through web tools and the complete displayed running text read before authoring each chapter's observations.",
        "pages": [{"url": f"https://www.die-bibel.de/en/bible/LXX/GEN.{n}",
                   "scope": f"Genesis {n}:1–{count}", "stored_units": count,
                   "running_text_accessed": True, "apparatus_accessed": False}
                  for n, count in [(5,32),(6,22),(7,24),(8,22),(9,29),(10,32),(11,32)]],
        "additional_sources_consulted": [],
        "redistribution": "Full publisher Greek is not reproduced. Records contain source locators, English working drafts and analysis. Public access is not claimed as a redistribution grant.",
        "special_locators": {
            "Genesis 11:13": "Publisher's unit 13 includes Arphaxad's latter years and both Cainan statements; preserved under v11-13.",
            "Genesis 5:25–27": "Displayed Methuselah ages 167, 802 and 969 retained; no alternate reading adopted.",
            "Genesis 8:5": "Tenth month in the first clause and eleventh month in the second retained.",
        },
    }
    write_json("sources.json", sources)
    ages = [
        {"name":"Adam", "before":230, "after":700, "stated_total":930, "references":["5:3","5:4","5:5"]},
        *[{"name":p,"before":b,"after":a,"stated_total":t,"references":[f"5:{v}",f"5:{v+1}",f"5:{v+2}"]} for v,p,_,b,a,t,_ in GEN5],
        {"name":"Enoch","before":165,"after":200,"stated_total":365,"references":["5:21","5:22","5:23"]},
        {"name":"Lamech","before":188,"after":565,"stated_total":753,"references":["5:28","5:30","5:31"]},
    ]
    for age in ages:
        age["sum_matches_stated_total"] = age["before"] + age["after"] == age["stated_total"]
    assert all(a["sum_matches_stated_total"] for a in ages)
    birth_chain = [230,205,190,170,165,162,165,167,188]
    flood_year = sum(birth_chain) + 600
    methuselah_death = sum(birth_chain[:7]) + 969
    number_audit = {
        "scope": "Manually read displayed ages and dates with arithmetic checks; not a manuscript chronology reconstruction.",
        "genesis_5": ages,
        "genesis_11": [
            {"name":"Shem","before":100,"after":500,"derived_total":600},
            {"name":"Arphaxad","before":135,"after":430,"derived_total":565},
            {"name":"Cainan","before":130,"after":330,"derived_total":460,"all_latter_material_anchor":"v11-13"},
            *[{"name":p,"before":b,"after":a,"derived_total":b+a} for _,p,_,b,a in GEN11],
        ],
        "noah": {"begetting_summary_age":500,"flood_age":600,"post_flood_years":350,"stated_lifespan":950},
        "terah": {"begetting_summary_age":70,"days_in_harran":205,"unresolved":"The source attaches in Harran to the days statement; do not silently remove it to harmonize chronology."},
        "flood_dates": [
            {"reference":"7:11","year_of_noah":600,"month":2,"day":27},
            {"reference":"8:4","month":7,"day":27},
            {"reference":"8:5","diminishing_until_month":10,"visible_tops_month":11,"day":1},
            {"reference":"8:13","year_of_noah":601,"month":1,"day":1},
            {"reference":"8:14","month":2,"day":27},
        ],
        "unresolved_methuselah_flood_tension": {
            "method": "Illustrative sequential sum of the named-line begetting ages, treating each as the father's elapsed age. This is an arithmetic inference, not an absolute historical date.",
            "flood_relative_year":flood_year,"methuselah_death_relative_year":methuselah_death,
            "difference_years":methuselah_death-flood_year,
            "action":"Preserve displayed numbers and flag for apparatus/contextual chronology review; do not invent a resolving variant or alter the source.",
        },
    }
    assert number_audit["unresolved_methuselah_flood_tension"]["difference_years"] == 14
    write_json("number-audit.json", number_audit)
    assert len({r["verse_anchor"] for r in records}) == 193
    assert all(r["candidate_sha256"] == hashlib.sha256(r["candidate_text"].encode()).hexdigest() for r in records)
    validation = {
        "batch_id":"OT-005", "result":"pass", "stored_units":193,
        "chapter_counts":{str(n):sum(r["reading_section_id"]==str(n) for r in records) for n in range(5,12)},
        "checks":["All assigned references covered exactly once in original order", "Exact baseline text and IDs match pinned Git snapshot", "Original local Genesis data equals pinned scoped snapshot", "All candidate SHA-256 checksums match UTF-8 text", "All three draft stages populated", "All explicit chapter-five age sums agree with stated totals", "Grouped Cainan text remains within v11-13", "No changed poetic unit lacks display-text handling", "All review/acceptance/publication limits remain explicit"],
        "proposals":[r["reference"] for r in changes],
        "not_claimed":["Exhaustive token alignment","Critical apparatus collation","Independent human Greek review","Human read-aloud review","Editorial acceptance","Website deployment"],
    }
    write_json("validation.json", validation)
    print(json.dumps(result["counts"]))


if __name__ == "__main__":
    build()
