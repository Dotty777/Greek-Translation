# Genesis 5–11: Greek-led Saints English working review

**OT-005 · 12 November 2026 · Provisional AI draft; no acceptance or publication**

All **193 existing stored units** in Genesis 5–11 were compared with the complete displayed Rahlfs–Hanhart 2006 running text on the German Bible Society chapter pages. Chapter coverage is 32, 22, 24, 22, 29, 32 and 32 units. The original accepted Genesis benchmark remains unchanged at baseline commit `39a2bb990f252f9c867879f14942b200c4a86aa5`.

The [comparison records](focused-reviews.json) include exact baseline references, anchors and text; an authored close draft; spoken and literary candidates; passage-specific analysis; unresolved questions; source locators; and candidate SHA-256 checksums. Spoken and literary drafts sometimes agree because no further wording change was warranted after comparison. They have not received human reading aloud.

**Thirteen revisions are proposed; 180 units retain the inherited wording provisionally.** The proposals remain separate from the benchmark:

| Passage | Proposed change | Source reason |
| --- | --- | --- |
| 6:5 | “intently devised evil in his heart every day” | Distinguish diligence/intentness from the separate daily-time expression. |
| 6:20 | “according to their kind” | Preserve singular kind with a plural possessive. |
| 6:21 | “some of every kind of food that you shall eat” | Preserve the partitive taking and future plural eating clause. |
| 7:9, 7:15 | “came into the ark to Noah” | Preserve Noah as the person approached. |
| 7:19 | “exceedingly, exceedingly” | Represent the paired intensifying expressions; cadence remains for human review. |
| 8:3 | “continued to recede and diminish” | Retain the imperfect recession after 150 days. |
| 8:19 | “according to their kind” | Preserve the singular source form. |
| 9:21 | “was uncovered” | Avoid adding a lying posture. |
| 9:24 | “became sober” | Preserve recovery from intoxication rather than infer waking from sleep. |
| 10:9 | “therefore they shall say” | Retain the future active reporting verb. |
| 11:7 | “may not understand” | Remove the separate no-longer assertion. |
| 11:9 | “the speech of the whole earth” | Render the plural lips metaphor without requiring pre-existing multiple languages. |

The [number audit](number-audit.json) preserves every displayed genealogical age checked in chapters 5 and 11 and the main flood dates. All chapter-five stated lifespans equal their stated intervals. A conventional sequential sum nevertheless puts Methuselah's death fourteen years after the flood year. This is explicitly an **arithmetic tension**, not a resolved historical chronology or an apparatus finding. The displayed 167/802/969 figures remain unchanged.

Other source-specific details retained include the twenty-seventh-day flood dates; tenth and eleventh months in 8:5; summer and spring in 8:22; house in 9:21; the repeated Elishah and Cainan placements in chapter 10; and the name Confusion in 11:9. The whole Cainan passage stays inside **v11-13**, including Arphaxad's 430 later years, Cainan's 130 before Shelah and 330 afterward. No new verse IDs are invented. Country of the Chaldeans remains in 11:28 and 11:31 without inserting Ur. The two references to Harran and the 205-year wording in 11:32 remain despite their chronological difficulty.

Open issues include the sons of God in 6:2–4; the 120 years in 6:3; ark construction in 6:16; the clean-animal sevens; the olive leaf/stalk in 8:11; the person/blood syntax in 9:6; the pronouns in 9:26–27; name-authority mappings; and the genealogical tensions. Retention does not certify these as settled translations.

[Source-access evidence](sources.json) lists the seven publisher pages and actual scope. Only running text was consulted; no full Greek text is redistributed. Full token accounting, specialist lexical evidence, apparatus/Göttingen comparison, independent qualified Greek review, human reading aloud, editorial acceptance and website publication remain pending. No New Testament material was touched.

[Validation](validation.json) checks all 193 identities, ordering, exact baseline text, candidate hashes, draft presence, number calculations, and grouped Cainan preservation. Run `python reviews/2026-11-12-OT-005-genesis-5-11/build_reviews.py` from the repository root to reproduce these files from the pinned benchmark and authored observations. The builder does not automatically retrieve or translate Greek.
