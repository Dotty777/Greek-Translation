# OT-012 · Exodus 3–15

Provisional Greek-led comparison of **all 368 stored units** in Exodus 3–15 against the publisher's complete Rahlfs–Hanhart 2006 running Greek, accessed and read on **12 November 2026**. This is an AI focused comparison, not a fully reviewed translation release or exhaustive token alignment.

The inherited English is retained provisionally in **360 units**, with **eight proposed revisions**. Every unit has its exact baseline, stable identity, source locator, individual Greek rationale, close/spoken/literary working drafts, candidate SHA-256, and pending review status. Drafts agree when the scoped comparison supports the same wording; agreement does not certify an unresolved passage.

| Chapter | Units |
| --- | ---: |
| 3 | 22 |
| 4 | 31 |
| 5 | 23 |
| 6 | 30 |
| 7 | 29 |
| 8 | 28 |
| 9 | 35 |
| 10 | 29 |
| 11 | 10 |
| 12 | 51 |
| 13 | 22 |
| 14 | 31 |
| 15 | 27 |
| **Total** | **368** |

## Proposals

| Reference | Proposed change | Source-led reason |
| --- | --- | --- |
| 4:28 | The words the Lord had sent | The relative pronoun agrees with words, the object of sent; inherited with which He had sent him supplies an instrumental relation and personal object. |
| 8:4 | I will let the people go | Restores the explicit people when Pharaoh moves from his own Egyptian people to those to be released, avoiding an ambiguous them. |
| 9:17 | Yet you still act against My people… | Follows the selected edition's statement punctuation. This is an editorial punctuation choice, not proof that a Greek indicative cannot form a rhetorical question or a claim of a manuscript variant. The uncommon verb remains under review. |
| 10:7 | Let the people go | Preserves the general human-group noun in the attendants' request, distinct from Pharaoh's explicit male-only restriction in 10:11. |
| 12:3, 12:4, 12:5, 12:21 | An animal from the flock | Avoids restricting the Passover animal to sheep when 12:5 expressly permits both lambs and young goats. The recurring noun's scope follows that immediate context. |

All eight proposals are prose. The **18 units with recorded poetic breaks**, all in Exodus 15, retain their original wording. No source book, verse identifier, original HTML line break, shared tracker or shared builder was changed. The main reading builder must continue recovering retained poetry layout from the original HTML. The batch builder fails if a future proposed change touches a poetic unit without a separate reviewed display implementation.

## Important retained readings and open questions

The records preserve the selected Greek's distinctive wording: the angel and cessation-of-blood speech in 4:24–26; your covenant in 6:5; Kohath's 130 and Amram's 132 years in 6:18/20; the 29/28-unit chapter 7/8 division; south winds in 10:13 and 14:21; Egypt **and Canaan** within the 430 years in 12:40; six days followed by the seventh-day feast in 13:6; redemption rather than a neck-breaking instruction in 13:13; fifth generation in 13:18; bound axles in 14:25; and the Song's shattering wars, righteousness, angry nations and hastening Edomite leaders.

Difficult readings remain marked for review, including the pronouns in 4:24–26; speech and sensory descriptions in 4:10–11 and 6:12; insect and grain identifications; 5:19 speech attribution; 9:14/17 syntax; 10:10 and 10:17 idioms; Passover status terminology in 12:43–49; the vigil construction in 12:42; the causal demonstrative in 13:8; 14:16's awkward raising-with-the-staff construction; the force/difficulty nuance in 14:25; holy ones versus holy things/places in 15:11; and comfort/encouragement toward the holy dwelling in 15:13. Retention is provisional even where the inherited wording remains awkward. No uncertainty was settled by silently importing another textual tradition.

## Evidence and reproducibility

- `notes.tsv`: 368 manually authored, passage-specific analyses, one per stored unit.
- `build-review.py`: deterministic record assembly from the frozen original and authored notes; this does not generate or validate Greek analysis automatically.
- `focused-reviews.json`: complete proposed review records and three working draft fields.
- `sources.json`: all 13 actually read publisher chapter URLs and access limits.
- `validation.json`: structural checks, counts and the retained poetic-unit list.

Rebuild from the repository root:

```powershell
python reviews/2026-11-12-OT-012-exodus-3-15/build-review.py
```

The builder compares the original Exodus JSON with commit `39a2bb990f252f9c867879f14942b200c4a86aa5`, verifies complete ordered coverage and unique anchors, checks candidate hashes, requires prose display text for changes, and writes UTF-8 with LF. It writes only this review folder. No critical-text corpus is redistributed; Greek evidence is represented through precise passage locators and limited linguistic discussion.

No specialist lexicon, printed apparatus, Göttingen collation or manuscript was consulted for this batch. Complete token accounting, apparatus work, independent human Greek review, human read-aloud, editorial acceptance and publication remain pending. AI review cannot fill those human stages. No New Testament work is included.
