# Greek Source and Access Register

**Initial register · 12 November 2026 · No new collation claimed**

This is the programme-level register. Before translating a batch, add its book/section-specific edition, actual access, scope and review evidence. The [tracker](../review-progress.json) links the existing source records for every book.

## Recorded sources and intended use

| ID | Source | Status supported by inspected records | Next evidence needed |
| --- | --- | --- | --- |
| LXX-RH2006 | Rahlfs–Hanhart, Septuaginta, 2006 | Recorded provisional OT base, with book-level exceptions to reconcile. Representative Genesis, Esther, Daniel and Sirach records identify the publisher's running text and bounded checks. | Exact book/textual form, accessed passages, source locator and date; full token and syntax coverage for each new batch. |
| LXX-GOTT | Göttingen Septuaginta, specific volume/edition | Intended critical comparison. Relevant volumes appear in the official catalogue; complete project access and collation are not established by this plan. | Author/editor, volume, edition/year, text form, access, passage/apparatus locators and actual comparison. |
| NT-NA28 | Nestle–Aland 28 | Governing NT base recorded in README and the 9 November review. Existing progress also acknowledges earlier draft histories, including SBLGNT. | Book-level provenance reconciliation and exact scoped source comparisons. |
| NT-UBS6 | UBS6/GNT6, sixth edition | Preferred next NT base in existing progress. Publisher description verified; the older access record says the full preferred text had not been obtained. Current full-text access has not been established in this planning pass. | Verify actual current possession/access, permission scope, source version and complete affected-passage collation before migration. |
| NT-ECM | Editio Critica Maior, specific volume | Intended deeper textual comparison; do not assume every NT book has the same publication/access status. | Relevant volume and publication details, access, passage-level use and reasons for any adopted difference. |

UBS6/GNT6 refers to the sixth-edition UBS Greek New Testament; do not count these labels as two independent Greek witnesses. Critical editions themselves must also be distinguished from manuscript witnesses.

## Scope cautions already supported by the archive

- **Genesis:** 1–11 is the accepted English benchmark. Its acceptance does not constitute a fresh complete Greek collation. Later source-check entries describe selected checks and outstanding Göttingen/apparatus work.
- **Daniel:** the declared provisional base is **Old Greek**, not Theodotion. Preserve the 12 numbered chapters, Susanna, Bel and the Dragon, the furnace prayer/song and the distinct chapter-five preface. Do not silently substitute the familiar alternate Greek form.
- **Esther:** preserve the Greek additions and six existing continuation paragraphs; audit their identity and placement rather than forcing a Hebrew-only structure.
- **Sirach:** retain the translator's prologue and all 51 chapters as distinct reading sections. Its source record's full running-text reading with focused comparisons does not claim exhaustive apparatus verification.
- **Psalms, Jeremiah and Proverbs:** numbering, arrangement and split sections require explicit mappings. Validate passage content, not merely matching labels.
- **Ezra/Nehemiah and other book exceptions:** reconcile the source's book naming and scope with the existing project records before assigning an edition globally.

## Required fields for each book or special section

Record book and section IDs; base edition and textual form; editor, year and revision; actual source locator; access date and permitted uses; source snapshot/hash where appropriate and permitted; previous edition provenance; comparison witnesses; source/check scope; textual decisions; numbering map; translator/reviewer identities and dates; unresolved issues and decision evidence.

Use distinct statuses:

1. **Declared** — an edition is named.
2. **Accessed** — the relevant text or apparatus was actually available and read.
3. **Collated** — the stated passage was compared and differences recorded.
4. **Language reviewed** — lexical and syntactic decisions were checked within a recorded scope.
5. **Independently reviewed** — a qualified independent reviewer completed and signed the identified scope.

Never advance one status solely because another exists.

## Access and permissions

The owner previously reported permission for UBS6/GNT6 use. Retain that as an owner-reported fact until its evidence and scope are attached to the controlled project record. Avoid publishing private correspondence. Record separately whether the permission covers website display, excerpts, downloadable editions and repository redistribution; do not infer one from another.

Where full Greek reproduction is not permitted, store source locators and allowed excerpts/analysis instead. A public publisher page or sample is evidence of availability of that page/sample, not the full edition. If the desired edition cannot be accessed, continue useful work against an explicitly declared authorized provisional base and keep the deeper review open.

## External references checked on 12 November 2026

- [German Bible Society: sixth edition of the Greek New Testament](https://www.die-bibel.de/en/the-sixth-edition-of-the-greek-new-testament-ubs6) — publisher overview, including ECM-related changes.
- [Göttingen Septuaginta publication catalogue](https://septuaginta.uni-goettingen.de/publications/septuaginta/) — book-level bibliographic reference.
- [Existing Genesis source checks](../genesis/source-checks.json), [Esther source checks](../esther/source-checks.json), [Daniel record](../daniel/README.md), [Sirach record](../sirach/README.md), [NT access history](../progress.json), and [9 November review](../review-2026-11-09.md).

This register records the limits of this planning inspection. It is not a newly verified rights grant, a complete bibliography, an imported critical text or a substitute for examining the Greek.

## 12 November 2026 — Old Testament assignment and opening comparisons

The latest owner instruction limits new work to all 43 OT books. The [OT manuscript manifest](../editions/2026-11-12-ot-reading-draft/manifest.json) inventories the inherited text at commit `39a2bb990f252f9c867879f14942b200c4a86aa5`, including attached continuation paragraphs and special sections. Its preserved source histories are historical records, not freshly certified collations.

The publisher's complete displayed running text was actually read for [Genesis 1](https://www.die-bibel.de/en/bible/LXX/GEN.1), [Genesis 2](https://www.die-bibel.de/en/bible/LXX/GEN.2), [Genesis 3](https://www.die-bibel.de/en/bible/LXX/GEN.3), and [Jonah 1](https://www.die-bibel.de/en/bible/LXX/JON.1), [2](https://www.die-bibel.de/en/bible/LXX/JON.2), [3](https://www.die-bibel.de/en/bible/LXX/JON.3), [4](https://www.die-bibel.de/en/bible/LXX/JON.4) on 12 November 2026. Each page identifies Rahlfs–Hanhart 2006, Deutsche Bibelgesellschaft. The three dated OT review folders contain 128 focused verse comparisons; Genesis 1 also supplies 31 close drafts. These are AI analyses, without full token-accounting claims. No full Greek text is redistributed, and no new rights grant is inferred from public access.

No critical apparatus, Göttingen volume or specialist Septuagint lexicon was consulted for these opening records. The general Middle Liddell entry for *pheidomai* was read for the provisional Jonah 4:10–11 proposal; the exact locator and limits appear in the [Jonah record](../reviews/2026-11-12-OT-003-jonah/README.md). Textual/source differences are preserved within the selected running text; they are not claimed as freshly collated manuscript variants. Independent human Greek review, human reading aloud, acceptance and website publication remain open. The benchmark's original Genesis files remain unchanged; candidate changes are explicit proposals in the dated working edition.

## GT-003 — John 1:1–18, 12 November 2026

[Batch evidence](../reviews/2026-11-12-GT-003-john-1-1-18/sources.json) records actual access to the publisher’s NA28 running text for all eighteen verses and 252 tokens. The bounded lexical sequence was compared with the openly licensed SBLGNT; punctuation differences are recorded. MorphGNT supplies openly licensed morphology, with its John 1:9 participle tag explicitly distinguished from the candidate’s selected parse. The SBL edition-comparison apparatus was read only at 1:15, 1:16 and 1:18. It is not the NA28 manuscript apparatus.

Two general lexical entries and a partial monogenēs headword lookup inform preliminary notes; the partial lookup is not credited as a completed specialist study. Full NA28 apparatus, UBS6/GNT6, independent Greek and human read-aloud review remain open. Reproduced token forms come from the attributed SBLGNT witness; no full NA28 corpus or private rights correspondence is redistributed. See [attribution](../reviews/2026-11-12-GT-003-john-1-1-18/ATTRIBUTION.md).


## 12 November 2026 — complete NT reading draft and additional comparisons

[Edition manifest](../editions/2026-11-12-nt-reading-draft/manifest.json) records the 27-book, 260-chapter, 7,943-unit inherited manuscript at commit `7ba61929f083d8e10e1702f2a7f7e3c9ac46b300`. All source histories were retrieved and preserved in the edition's source-history.json; this does not newly certify their historical coverage. Publisher NA28 running text was read for John 1:19–51, Romans 3:21–31, James 2:14–26, Philemon, 2 John, 3 John and Jude, with 135 focused verse comparisons. These records do not claim exhaustive word accounting or apparatus collation. Middle Liddell δικαιόω was consulted for a preliminary James 2:24 study; specialist lexical review remains open. UBS6/GNT6 and ECM migration/comparison status is unchanged. The complete reading manuscript includes inherited text and seven John proposals, not 7,943 newly certified translations.

## 12 November 2026 — continuation from Genesis 4

Following the continuation instruction, the complete displayed Rahlfs–Hanhart running text was read for Genesis 4–50, Exodus 1–40 and Leviticus 1–3. The [continuation report](../reviews/2026-11-12-OT-CONTINUATION.md) links the dated records and exact counts. Each unit identifies its publisher chapter URL and access date. Exodus 28–40 also has a [numbering and order record](../reviews/2026-11-12-OT-014-exodus-28-40/structure.json), preserving lettered units, gaps and the Greek arrangement of the tabernacle material.

Genesis 4:7 has an explicit 19-token ledger, with morphology and English realizations. Its pronoun antecedents and the time supplied for a verbless clause remain unresolved. All other new records are focused comparisons with working draft stages, not complete token ledgers. The stages may retain identical wording when the comparison supports it. No source-access entry alone is credited as independent review or acceptance.

For Genesis 34:27, the root assistant read the general [LSJ entry for traumatias, senses I–II](https://atlas.perseus.tufts.edu/dictionaries/entry/urn%3Acite2%3Ascaife-viewer%3Adictionaries.v1%3Alsj-n104589/). The dead-casualty sense and the immediate killing context support retaining slain. This was one bounded lexicon consultation; the entry’s cited examples were not independently collated, and no complete specialist Septuagint lexicon review is claimed. [Scoped second AI checks](../reviews/2026-11-12-OT-CONTINUATION-QA.json) identify what was checked and corrected.

No critical apparatus or Göttingen volume was consulted for these continuation batches. Technical animal, ritual, gemstone, anatomical and material terms retain explicit review questions. The [selected name register](OT-NAME-DECISIONS.json) is provisional and incomplete. Full specialist, independent human Greek and human read-aloud review remain open. Original Scripture and source-history files are preserved.

## 13 November 2026 — Numbers completed in the provisional comparison pass

Complete selected Greek running text and exact inherited English were read for Numbers 15–36, following the earlier Numbers 1–14 work. Dated batches OT-031 through OT-040 contain 739 additional authored unit comparisons and six proposals; Numbers now has 1,287 focused comparison records. The [continuation report](../reviews/2026-11-12-OT-CONTINUATION.md) and edition manifest carry the cumulative counts. The whole Old Testament assignment remains active, with Deuteronomy next.

The publisher’s English-interface Numbers 21 page timed out; the [German-interface page](https://www.die-bibel.de/bibel/LXX/NUM.21) supplied the complete same-edition Greek chapter actually read. Other chapter URLs and access dates are recorded per batch.

For Numbers 25:8, the [bounded lexical record](../reviews/2026-11-13-OT-036-numbers-25-26/lexical-checks.json) identifies the LSJ entry and scholarly review actually consulted in proposing kiln. The competing alcove sense and the limits of access remain explicit. Cited papyri and other scholarly works were not independently consulted. This proposal does not represent settled specialist consensus.

The census, offerings and spoil records preserve manually read quantities and separately label arithmetic. Both itinerary movements in 33:36, difficult boundary wording and selected legal clauses remain intact. No full Greek corpus, apparatus collation, independent human review or editorial acceptance is claimed.
