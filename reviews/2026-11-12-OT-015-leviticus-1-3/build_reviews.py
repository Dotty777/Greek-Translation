"""Package authored comparisons after reading the complete Greek of Leviticus 1–3.

This script checks and serializes the decisions below; it does not translate Greek.
"""
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASELINE = '39a2bb990f252f9c867879f14942b200c4a86aa5'
NOTES = {
1: [
'The opening call takes Moses as its object; the following clause names the Lord as speaker from the Tent of Testimony. Retain the connected calling and speaking, without adding a new location or changing the established tent designation.',
'The instruction first addresses Moses in the singular, then the community in the plural. The conditional individual brings gifts from livestock, specified as cattle and flock. English you spans these grammatical shifts; no universal requirement to offer on every occasion is added.',
'The conditional cattle offering is a whole burnt offering, male and unblemished, brought to the tent door as acceptable before the Lord. Acceptable describes the offered gift; the English does not insert the distinct claim that willingness is the only condition.',
'A singular hand is laid upon the offering’s head. The acceptable-for-him phrase and the purpose of making atonement for him remain distinct. The two masculine pronouns are interpreted with the offerer in view; the construction and atonement terminology remain open to specialist review.',
'The slaughtering verb is plural; Aaron’s sons are then explicitly identified as the priests who bring and pour the blood. Preserve those agents and the altar’s location at the tent doors, without silently changing the initial they to a singular offerer.',
'The plural skinning participle precedes the plural dividing verb. When they have skinned expresses that sequence; limb by limb renders the repeated body-part construction without specifying a different cutting method.',
'Aaron’s sons, expressly called priests, place fire on the altar and pile wood on the fire. Keep both repeated locations and the order of actions rather than replacing the sequence with a general command to prepare the altar.',
'The divided pieces, head and fat are separately named and piled by the priests. The wood, fire and altar form a nested sequence of locations. All the named parts and repeated relations remain in the inherited text.',
'The washing is plural and concerns entrails and feet; the priests then place everything on the altar. Offering, sacrifice and the pleasant-aroma expression remain separate predicates. Sweet savour is an inherited register choice, not an assertion about taste.',
'The flock category specifies lambs and young goats and requires an unblemished male. The displayed Greek also includes laying a singular hand on its head here; preserve that clause instead of shortening the verse to match another tradition.',
'The animal is slaughtered on the north side of the altar before the Lord, with plural slaughterers. Aaron’s sons pour its blood around the altar. The cardinal direction and the distinction between slaughtering and pouring are explicit.',
'Division limb by limb includes the head and fat, followed by the priests piling the portions on wood over the altar fire. The coordinated body parts are not treated as separate additional animals or as optional portions.',
'The washing verb remains plural, but a singular priest brings and places all on the altar. Preserve that number change rather than harmonizing both clauses to the same agent. The offering/sacrifice/aroma formula repeats the earlier wording.',
'The bird-offering condition addresses you in the singular, while the following bringing clause uses a third-person subject and his gift. Preserve this source shift. Turtledoves and pigeons are alternatives; no unexpressed age restriction is added.',
'The singular priest brings the bird, removes its head, places the item on the altar and drains the blood at the altar’s base. Pinch off is retained as the provisional ritual verb; the precise technique and the omitted object of placing require specialist review.',
'The crop is removed with the feathers, then cast beside the altar eastward at the ash place. Preserve both orientation and disposal location. The anatomical and feather wording follows the displayed Greek without substituting a different account of the removed material.',
'Breaking the bird open by its wings is followed by a prohibition on dividing it. Keep those opposed actions and the wood/fire location. The final offering, sacrifice and aroma formula is preserved; the exact ritual handling is not independently reconstructed.'
],
2: [
'Soul denotes the person presenting the gift here, without asserting a separate disembodied actor. Fine flour, oil and frankincense are distinct ingredients; the concluding sacrifice predicate remains. The close draft exposes person as the contextual alternative to inherited soul.',
'The gift is brought to Aaron’s sons. A full handful of flour with oil and all its frankincense supplies the memorial portion placed by the priest. The taking participle and postponed priest subject need care; the close draft makes the priest the taking agent explicitly, while the inherited he remains provisional.',
'The remainder belongs to Aaron and his sons and is characterized by the holy-of-holies formula among the Lord’s sacrifices. Most holy renders that superlative construction without relocating the food into the sanctuary’s inner room.',
'The oven-baked offering specifies both unleavened loaves mixed with oil and unleavened wafers spread with oil. Mixing and coating remain different actions. The repeated gift-to-the-Lord phrase is retained instead of being removed as redundant.',
'The griddle offering has fine flour mixed with oil and is unleavened. The shift to second-person your is preserved. Griddle remains a provisional utensil rendering; the passage does not supply a modern recipe or exact cooking temperature.',
'The plural objects of breaking and pouring follow the preceding preparation. Retain pieces and oil upon them rather than making the pronoun singular for smoother English. The concluding identification as a sacrifice to the Lord remains.',
'The second cooking arrangement uses a different Greek noun from the griddle of verse 5. Hearth is retained provisionally, and the preparation remains fine flour with oil. A precise archaeological identification of the cooking surface or vessel has not been established.',
'The offering made from these preparations is brought to the Lord and then to the priest. The approaching participle leads into the priest’s action in verse 9. Keep the open sentence and flag its agent rather than deciding the relationship by inserting an unexpressed actor.',
'The priest removes the memorial portion and places it on the altar. The priest is repeated in the Greek and retained in English. Offering and pleasant aroma characterize that portion; the text does not say that the entire remainder is burned.',
'The remaining material belongs to Aaron and his sons. Unlike verse 3, the holiness formula is plural here, rendered most holy things, and the final category is offerings. Preserve these distinctions rather than mechanically copying the earlier sentence.',
'The prohibition concerns leaven in sacrifices brought to the Lord and then explicitly excludes any leaven or honey from being offered in the specified altar action. Neither substance is silently deleted, and this is read with the firstfruits qualification in the next verse.',
'The plural them can be brought as a firstfruits gift, while the altar prohibition has a singular passive verb. A Greek neuter plural subject can take a singular verb, so verbal number alone does not justify English it rather than they. Retain it provisionally as referring to the gift, expose they in the close alternative, and leave the antecedent question open. The firstfruits exception must be read with the preceding leaven/honey prohibition.',
'Every gift is salted; the salt of the Lord’s covenant must not cease from their sacrifices, and salt accompanies every gift to the Lord their God. All three clauses and the plural community address remain. No symbolic interpretation of the salt is inserted into Scripture.',
'The first-produce offering specifies new, roasted and crushed grain before repeating the offering instruction. Groats is retained provisionally for the prepared grain. The English does not substitute a particular modern species or omit the preparation modifiers.',
'Oil is poured and frankincense placed upon the preceding first-produce offering. The second-person instructions continue, followed by its identification as a sacrifice. The ingredients remain distinct and their handling is not merged into one action.',
'The priest offers the memorial portion from the prepared grain with oil and all its frankincense. Some of renders the partitive construction, not a stated fractional measure. The final offering-to-the-Lord formula closes the preparation.'
],
3: [
'The sacrifice is designated by the Greek deliverance/well-being term and may be male or female, in contrast to the male requirement for the preceding whole burnt offering. Retain deliverance as the inherited provisional label and preserve the unblemished requirement.',
'The offerer lays plural hands on the gift’s head and slaughters it; Aaron’s sons pour blood around the altar of whole burnt offerings. Both the plural hands and the singular slaughtering agent differ from forms in chapter 1 and remain explicit.',
'A plural bringing verb introduces the offering from the sacrifice of deliverance. Fat covering the belly and all fat upon it are named separately. The list continues into the kidneys and liver material in the next unit; no additional organ is supplied.',
'Two kidneys, their fat by the thighs and the lobe at the liver are distinct items. The parenthetic removal clause links the liver lobe with the kidneys. The inherited anatomical terms remain provisional, without claiming a verified modern dissection map.',
'Aaron’s sons offer the listed portions on the altar over the whole burnt offerings and wood on the fire. The repeated relations and plural whole burnt offerings remain. The aroma formula does not erase the distinction between this sacrifice and the underlying offerings.',
'The flock offering repeats the deliverance designation and allows either male or female, unblemished. Preserve both alternatives and the contrast with chapter 1. The passage specifies the offering’s condition without adding a new requirement about age.',
'If a lamb is brought as the gift, it is brought before the Lord. The clause leads directly into laying hands and slaughtering in verse 8. Retain the conditional form rather than treating every flock offering as necessarily a lamb.',
'Plural hands are laid on the lamb’s head, and the singular offerer slaughters it at the tent doors. Aaron’s sons then pour blood around the altar. The sequence and agency parallel verse 2, without adding the longer altar title where it is absent.',
'The recipient here is God, and the portions include fat, an unblemished loin and belly fat. The parenthesis joins the removal to the lower-back muscles. Preserve these unusual Greek anatomical expressions rather than replacing them with a familiar fat-tail formulation; exact anatomy remains unresolved.',
'Both kidneys, fat upon them by the thighs and the lobe at the liver continue the list. The removal participle associates the lobe with the kidneys and leads to the priest’s offering in verse 11. The English semicolon preserves the continuing construction.',
'A singular priest offers the listed material on the altar. The pleasant-aroma formula precedes offering to the Lord here; the inherited wording preserves that order. The English does not identify an additional food substance absent from the selected Greek.',
'The goat condition introduces another animal category, followed by bringing it before the Lord. The implied subject and object are supplied naturally by English from the offering context. The same condition continues through the following handling instructions.',
'The offerer lays plural hands on its head, but the slaughtering verb is plural here. Aaron’s sons again pour blood around the altar. Keep this shift instead of harmonizing the goat instructions to the singular slaughtering of the cattle and lamb.',
'Fat covering the belly and all fat on it are named again. Propose upon it for the opening prepositional phrase: the displayed Greek has epi, not apo. The preceding altar is a plausible referent for it, but the candidate leaves the pronoun unresolved rather than inserting altar. The selected preposition must not be silently assimilated to the from-phrases in 3:3 and 3:9.',
'Both kidneys and all their fat by the thighs precede the liver lobe, with removal alongside the kidneys. All is explicit before the fat in this goat list and is retained. The anatomical description remains distinct from a general command to offer every organ.',
'The priest offers the listed portions on the altar, followed by the aroma formula and the separate statement that all the fat belongs to the Lord. Preserve the ownership statement as a distinct clause and read its scope with the surrounding ritual instructions.',
'The enduring statute extends through generations and every dwelling place, with a plural prohibition on eating any fat or blood. Both objects and the repeated totality remain. Its application must be examined within the wider legal context rather than expanded here into a modern dietary ruling.'
]
}
CLOSE = {
'1:3': 'If his gift is a whole burnt offering from the cattle, he shall bring an unblemished male; at the door of the Tent of Testimony he shall present it, acceptable before the Lord.',
'1:6': 'And having skinned the whole burnt offering, they shall divide it according to its limbs.',
'1:9': 'But they shall wash the entrails and the feet with water; and the priests shall place everything upon the altar. It is an offering, a sacrifice, a pleasing aroma to the Lord.',
'2:1': 'And if a person brings a gift as a sacrifice unto the Lord, his gift shall be fine flour; and he shall pour oil upon it, and put frankincense upon it. It is a sacrifice.',
'2:2': 'And he shall bring it unto the sons of Aaron, the priests; and the priest, having taken from it a full handful of fine flour with the oil and all its frankincense, shall place its memorial portion upon the altar: a sacrifice, a sweet savour unto the Lord.',
'2:3': 'And the remainder from the sacrifice belongs to Aaron and his sons: a most holy thing from the sacrifices of the Lord.',
'2:12': 'As a gift of firstfruits you shall bring them unto the Lord; but they shall not be brought up upon the altar for a sweet savour unto the Lord.',
'3:1': 'And if his gift unto the Lord is a sacrifice of well-being, if he brings it from his cattle, whether male or female, he shall bring it unblemished before the Lord.',
}
OPEN = {
'1:4': ['Referents of the two for-him phrases; exact atonement construction.'],
'1:14': ['Second-to-third-person shift; preserve rather than silently regularize.'],
'1:15': ['Precise ritual force of removing the head and implicit object of placing.'],
'1:16': ['Crop/feather terminology and ancient ritual handling.'],
'1:17': ['Technical distinction between opening by the wings and dividing.'],
'2:2': ['Subject of the taking participle and the precise memorial-portion construction.'],
'2:5': ['Ancient cooking utensil identification.'],
'2:7': ['Hearth/grill versus a different cooking vessel; no specialist lookup completed.'],
'2:8': ['Agent of the approaching participle across the verse boundary.'],
'2:12': ['Antecedent of the altar prohibition; a singular Greek verb does not distinguish a neuter singular from a neuter plural subject. Exact scope of the firstfruits exception.'],
'2:14': ['Prepared-grain terminology and the relation of the modifiers.'],
'3:1': ['Contextual deliverance/well-being/peace-offering terminology; specialist lexical review pending.'],
'3:4': ['Precise anatomical identification of the liver lobe and adjacent fat.'],
'3:9': ['Loin, unblemished/whole and lower-back-muscle terminology; preserve selected source distinctions.'],
'3:14': ['Referent of upon it, with the preceding altar a plausible antecedent; independent syntax review pending.'],
'3:17': ['Legal scope of fat/blood prohibition in the surrounding sacrificial legislation.'],
}

raw = subprocess.check_output(['git', '-C', str(ROOT), 'show', BASELINE+':leviticus/verses.json'])
assert (ROOT/'leviticus/verses.json').read_bytes().replace(b'\r\n',b'\n') == raw.replace(b'\r\n',b'\n')
verses = [v for v in json.loads(raw) if v['chapter'] <= 3]
assert len(verses) == 50
records = []
for v in verses:
    c = v['chapter']
    n = int(v['ref'].split(':')[1])
    text = v['text']
    candidate = text.replace('And from it he shall offer up', 'And upon it he shall offer up') if v['ref']=='3:14' else text
    records.append({
        'record_type': 'focused_running_text_comparison', 'review_id': 'OT-015-leviticus-'+v['ref'].replace(':','-'),
        'book_id': 'leviticus', 'reference': 'Leviticus '+v['ref'], 'verse_anchor': v['id'], 'reading_section_id': str(c),
        'baseline_commit': BASELINE, 'baseline_text': text, 'candidate_text': candidate,
        'candidate_sha256': hashlib.sha256(candidate.encode()).hexdigest(), 'decision': 'propose_revision' if candidate!=text else 'retain_provisionally',
        'source': {'edition':'Rahlfs–Hanhart 2006','url':f'https://www.die-bibel.de/en/bible/LXX/LEV.{c}',
                   'accessed_on':'2026-11-12','running_text_read':True,'apparatus_consulted':False},
        'drafts': {'close':CLOSE.get(v['ref'],candidate),'spoken':candidate,'literary':candidate},
        'draft_policy': 'Retain identical stages where the focused comparison supports the inherited wording; close alternatives expose selected constructions and terminology. These are AI stages, not human read-aloud results.',
        'analysis': NOTES[c][n-1], 'unresolved_questions': OPEN.get(v['ref'],[]),
        'review': {'reviewer':'OpenAI Codex assistant','type':'AI','scope':'Individual running-text comparison; ritual vocabulary and full token alignment remain pending.',
                   'all_tokens_accounted_for':False,'independent_greek':None,'human_read_aloud':None,'editorial_acceptance':None},
        'benchmark_change':False,'publication':{'staging':None,'production':None}
    })
assert [len([v for v in verses if v['chapter']==c]) for c in NOTES] == [len(NOTES[c]) for c in NOTES]
assert len({r['verse_anchor'] for r in records}) == len(records)
assert all(all(isinstance(r['drafts'][s],str) and r['drafts'][s].strip() for s in ('close','spoken','literary')) and r['drafts']['literary']==r['candidate_text'] for r in records)
def write(name, data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
write('focused-reviews.json',{'batch_id':'OT-015','scope':'Leviticus 1–3','records':records})
write('sources.json',{'date':'2026-11-12','edition':'Rahlfs–Hanhart 2006','publisher':'Deutsche Bibelgesellschaft',
    'scope':[{'chapter':c,'url':f'https://www.die-bibel.de/en/bible/LXX/LEV.{c}','complete_displayed_running_text_read':True} for c in NOTES],
    'apparatus_consulted':False,'specialist_lexicon_consulted':False,'independent_human_review':False,
    'limits':'This batch reproduces no full critical Greek corpus; source locators and original English analysis identify the actual reading scope.'})
write('validation.json',{'status':'passed','units':50,'retained':49,'proposed':1,'accepted':0,
    'chapter_counts':{'1':17,'2':16,'3':17},'checks':['Exact original text matches frozen baseline','All three chapters have a note per stored unit','Unique stable anchors','Three nonempty draft stages per unit; literary matches candidate'],
    'limits':'Structural validation and provisional AI source comparisons; not complete token, apparatus or independent human review.'})
print('Leviticus 1–3: 50 focused comparisons, 49 retained and one proposal; eight distinct close alternatives.')
