# Saints Modern English — Fidelity Review against the Saints Greek Critical Text (24 November 2026)

- **Status:** `provisional_source_checked_ai_review`. These are AI-made corrections that still need Vince's editorial decisions and an independent human Greek review and read-aloud review, as `TRANSLATION-STANDARD.md` requires.
- **Scope:** the whole Saints Modern English edition: all 70 books, 34,150 verses, 6,135 notes and 58 additional (`unplaced`) items. The NT was reviewed first, then the OT.
- **Source authority:** the Saints Greek Critical Text as held in this repository (`Saints-Greek-Critical-Text/`). Where the Greek has an unusual reading, the English translates it as it stands. Nothing was harmonized to NA28, Rahlfs, the Byzantine text, the Hebrew or the Latin.
- **Target:** *literal-smooth*, as defined in `STYLE.md`: formal-equivalent English, smoothed only as far as natural modern English requires.
- **Files:**
  - `README.md` (this file): method, results, structural fixes, settled renderings and open items.
  - `wording-changes.jsonl`: every applied wording and note change in canonical order, one JSON object per line with `ref`, `field` (`verse` or `note`), `category`, `old`, `new` and `reason`.

## Method

1. **Verse alignment.** Each English verse was aligned against its Greek verse using a statistical word-alignment model trained on the edition itself, plus a verse-by-verse alignment pass. This found verses that had been merged into a neighbour, shifted by one, or placed in a different order from the Greek (see *Structural fixes* below).
2. **Rule checks.** Automated checks covered banned archaisms, the divine-name house style (no `LORD`/`Yahweh`), preservation of the ⟦ ⟧ brackets, names supplied without a Greek basis (`Jesus`, `God`, `Christ`, `the Lord`), quotation-mark balance, and notes that make false claims about the Greek.
3. **Verse-by-verse review.** Every verse and note was read against its Greek by parallel reviewers working from one brief. The brief looked for:
   - **additions**: interpretive words, intensifiers or supplied titles that have no basis in the Greek;
   - **omissions**: Greek words that carry meaning but were dropped, including logical particles;
   - **meaning errors**: wrong tense, voice, mood, person, number, referent or negation, or a statement turned into a question;
   - **harmonization**: English that follows another edition or a familiar English Bible instead of this Greek;
   - **doctrinal bias**: wording or capitalization that quietly settles a disputed reading;
   - **consistency**: the same Greek rendered differently without a reason in context;
   - **notes**: notes that are doctrinal or devotional, describe other translations, or are false for this Greek.
4. **Central validation.** Before any change was applied, its `old` text had to match the edition exactly. Changes were rejected automatically if they added an archaism, broke the divine-name style or changed the ⟦ ⟧ brackets. Changes that altered the quotation-mark count or the verse length sharply were flagged for review. Every change in the *meaning*, *harmonization*, *doctrinal* and *referent* categories was checked by hand before it went in.
5. **Global consistency passes.** Some terms recur across books that different reviewers covered. These were standardized edition-wide in a final pass (see *Edition-wide renderings settled*).
6. **Final QA.**
   - The alignment and rule checks were run again.
   - All 1,291 chapter markdown files were regenerated from the JSON: **0 mismatches**.
   - Edition counts were updated in the root, NT, OT and division READMEs.
   - The only remaining QA flags are deliberate:
     - speeches that continue across a chapter break (Leviticus 25–26, Daniel 11–12);
     - the name *Bar-Jesus* in Acts 13:6, which is in the Greek.

## Results

**1,819 changes:** 1,441 to verse text (1,408 distinct verses) and 378 to notes. The NT had 528 changes and the OT 1,291. Philemon, 2 John and 3 John were reviewed and needed no change.

| Category | Changes | What it covers |
| :--- | ---: | :--- |
| consistency | 1,050 | Same Greek, same English (within a book first, then edition-wide) |
| note | 355 | Notes corrected: false claims about this Greek, doctrinal/devotional comment, `LORD` in notes, claims about other translations |
| harmonization | 124 | English that followed the Hebrew, Rahlfs/NA28 or familiar English Bibles instead of this Greek |
| addition | 97 | Words with no Greek basis removed (supplied names, intensifiers, interpretive expansions) |
| meaning | 59 | Wrong sense, tense, voice, mood, person, number or relation |
| grammar | 51 | Greek syntax misrepresented (conditions, participles, subordination) |
| doctrinal | 25 | Wording or capitalization that silently decided a disputed referent |
| omission | 24 | Greek words with meaning that were not represented |
| clarity | 18 | Smoothing where the English was unclear without changing the sense |
| referent | 13 | Wrong subject or object, or a pronoun capitalized for the wrong person |
| negation | 3 | Negation lost, added or misplaced |

### By book

| Book | Verse edits | Note edits |
| :--- | ---: | ---: |
| Genesis | 58 | 11 |
| Exodus | 95 | 18 |
| Leviticus | 83 | 9 |
| Numbers | 103 | 6 |
| Deuteronomy | 40 | 14 |
| Joshua | 9 | 4 |
| Judges | 10 | 1 |
| Ruth | 6 | 1 |
| 1 Samuel | 32 | 6 |
| 2 Samuel | 26 | 4 |
| 1 Kings | 22 | 5 |
| 2 Kings | 49 | 5 |
| 1 Chronicles | 14 | 3 |
| 2 Chronicles | 22 | 6 |
| Ezra | 3 | 1 |
| Nehemiah | 6 | 1 |
| Esther | 6 | 1 |
| 1 Maccabees | 29 | 6 |
| 2 Maccabees | 14 | 1 |
| Job | 33 | 5 |
| Psalms | 75 | 21 |
| Proverbs | 8 | 5 |
| Ecclesiastes | 10 | 3 |
| Song of Songs | 18 | 2 |
| Lamentations | 8 | 1 |
| Wisdom of Solomon | 3 | 6 |
| Sirach | 28 | 10 |
| Isaiah | 60 | 26 |
| Jeremiah | 40 | 11 |
| Ezekiel | 63 | 5 |
| Daniel | 26 | 10 |
| Hosea | 5 | 0 |
| Joel | 3 | 2 |
| Amos | 20 | 2 |
| Obadiah | 1 | 0 |
| Jonah | 3 | 0 |
| Micah | 2 | 0 |
| Nahum | 3 | 1 |
| Habakkuk | 0 | 1 |
| Zephaniah | 1 | 0 |
| Haggai | 6 | 0 |
| Zechariah | 24 | 6 |
| Malachi | 3 | 1 |
| Matthew | 72 | 18 |
| Mark | 26 | 9 |
| Luke | 27 | 15 |
| John | 57 | 28 |
| Acts | 42 | 21 |
| Romans | 21 | 5 |
| 1 Corinthians | 16 | 9 |
| 2 Corinthians | 8 | 3 |
| Galatians | 5 | 2 |
| Ephesians | 5 | 3 |
| Philippians | 1 | 0 |
| Colossians | 7 | 4 |
| 1 Thessalonians | 2 | 0 |
| 2 Thessalonians | 2 | 1 |
| 1 Timothy | 6 | 3 |
| 2 Timothy | 2 | 1 |
| Titus | 4 | 0 |
| Philemon | 0 | 0 |
| Hebrews | 14 | 6 |
| James | 3 | 2 |
| 1 Peter | 2 | 0 |
| 2 Peter | 2 | 0 |
| 1 John | 1 | 6 |
| 2 John | 0 | 0 |
| 3 John | 0 | 0 |
| Jude | 5 | 1 |
| Revelation | 41 | 20 |

## Structural fixes

Most were made in commit `b7edf3b`. The last item below, and a leftover copy of the 5:25 text in Daniel 5:17, were cleaned up during the wording review. Where the critical-text verse has a slot in the Hebrew or Latin editions, it was restored as a regular verse. Otherwise it was added as an additional verse (`unplaced`, reason `no-site-verse`). Deuteronomy 28:69–29:28 and Sirach 30–36 keep the parallel numbering they share with the Hebrew and Latin editions; this is documented in the OT README.

- **Genesis:** 47:4 restored as its own verse (was merged into 47:5); note corrected.
- **Exodus:** 39:4-39:20 re-paired to the Greek verse divisions; 39:14 restored; 39:15 translated from the critical text; 39:21 added as an additional verse.
- **Leviticus:** 8:19-8:30 re-paired to the Greek verse divisions (8:19 restored); 11:15 restored; notes corrected.
- **Numbers:** 6:23-27 put back in the Greek order (6:27 after the blessing, as an additional verse); 21:19-20 and 27:4-8 re-paired to the Greek verse divisions.
- **Deuteronomy:** 5:17-18 put back in the Greek order (murder, then adultery); 28:69 versification note corrected.
- **1 Kings:** "And Solomon built Gezer" moved from 5:14 back to its Greek position (4:33, additional verse).
- **Nehemiah:** 12:17-19 re-paired to the Greek verse divisions (12:18 restored).
- **Psalms:** Psalm 12:1-4 re-paired to the Greek verse divisions (12:1 restored).
- **Proverbs:** 15:5 and 31:24 restored; 15:5-6 and 31:24-28 re-paired to the Greek verse divisions.
- **Wisdom of Solomon:** 4:18 restored; 17:10-17:21 re-paired to the Greek verse divisions (17:21 as an additional verse).
- **Sirach:** 6:2, 23:16, 29:18, 41:18 and 41:22 restored; 5:15, 23:16-17, 29:16-18 and 41:18-24 re-paired to the Greek verse divisions; 51:11 added as an additional verse; 30-36 versification documented.
- **Jeremiah:** 10:5 and 23:40 restored (23:8 content moved to 23:40); 25:20 added as an additional verse.
- **Daniel:** 3:54-55, 3:58-59 and 3:77-78 put back in the Greek order; greeting and doxology moved from 4:37 to 4:1-3 (additional verses); 5:25 added as an additional verse.
- **Amos:** 8:1 restored (was merged into 8:2).
- **Exodus/Numbers/Psalms:** removed the now-redundant additional-verse copies of Exod 39:15, Num 21:20 and Ps 12:4, which are now in their own verse slots.

## Edition-wide renderings settled

Most of these terms had two or more renderings, usually because different parts of a book had been drafted separately. In each case the rendering already used most often in the edition was kept, unless the Greek required otherwise.

| Greek | Rendering | Notes |
| :--- | :--- | :--- |
| σπέρμα (OT) | "seed" | Replaces "offspring"/"descendants" where the Greek is σπέρμα; the NT is not yet uniform (see open items) |
| κάρπωμα | "fire offering" | Pentateuch and beyond; replaces "sacrificial offering" |
| σκηνὴ (σκήνωμα) τοῦ μαρτυρίου | "tent of testimony" | |
| καταπέτασμα | "curtain" | OT and NT; replaces "veil" |
| ἐπωμίς | "shoulder-garment" | |
| νόμιμον αἰώνιον | "eternal statute" | `πρόσταγμα διὰ παντός` (Ezek 46:14) stays "perpetual statute" because it is different Greek |
| προσήλυτος (OT) | "resident alien" where the sense is legal residence | |
| τῷ Δαυίδ (Psalm headings) | "for David" | Psalter-wide |
| τάδε λέγει (prophetic formula) | "Thus says" | Revelation 2–3 keeps its established "This is what … says" |
| Kings regnal formula (τὰ λοιπὰ τῶν λόγων … βιβλίῳ λόγων τῶν ἡμερῶν) | "the rest of the matters of … the book of the records of the days" | 1–2 Kings |
| ἀμὴν λέγω ὑμῖν | "Truly I say to you" | `ἀληθῶς λέγω ὑμῖν` (Luke 21:3) stays "Truly I tell you" because it is different Greek |
| ὁ νόμος | "law" in lower case, except where the edition already consistently writes "the Law" for the Mosaic Law | Hebrews 7–9 brought into line with Hebrews 10 and James |
| ἀδελφιδός (Song of Songs) | "kinsman" | Chapters 5–6 and 8:5 brought into line with the rest of the book and the note at 1:13 |
| Βαλτασάρ (Daniel) | "Baltasar" | One Greek form for both Daniel's Babylonian name and the king, as in the critical text |

## Open items for the editor

1. **Capitalized pronouns for OT figures whose identity is disputed.** The house style capitalizes pronouns for God and for Jesus. In some OT passages the referent is disputed, and the Translation Standard says capitalization must not decide it. Examples: Isaiah 7:14–16, 9:5–6, 11:1–5 and 11:10; Psalm 2; Psalm 109:1. The edition already writes several of these in lower case and others in capitals. This review changed only the places that were inconsistent *within their own passage*:
   - Isaiah 53:2–12, lowered to match the servant in 52:13–15;
   - Isaiah 61:1, lowered to match the first-person servant speeches in 49:1–6, 50:4–9 and 61:10;
   - Daniel 7:14, lowered to match "one like a son of man" in 7:13.

   Everything else is left as it was. A single edition-wide rule is needed. Each set above is listed in `wording-changes.jsonl` (category `doctrinal`) and can be reversed as a unit.
2. **Other reversible sets.** If the editor prefers the other choice, these sets in `wording-changes.jsonl` can be reversed as a unit:
   - Song of Songs "kinsman" (chapters 5–6 and 8:5);
   - Daniel "Baltasar" (1:7, 2:26, 7:1, 8:1, 10:1).
3. **Hebrew-form proper names.** Many names still use their familiar Hebrew/English form rather than the Greek form (for example "Nun" for Ναυή). This review did not change name forms, except where a note contradicted its verse.
4. **Manuscript citations in notes.** A few notes name specific witnesses or sigla (for example Codex A at Genesis 8:2 and 18:7, and Psalm 41:9 and 44:14). These citations were not verified against the critical text's apparatus.
5. **Quotation marks across chapter breaks.** Leviticus 25–26 and Daniel 11–12 contain speeches that run across a chapter break, so the quotation marks balance only across the two chapters, not within each one. This is deliberate.
6. **σπέρμα in the NT.** The NT renders σπέρμα "offspring" 24 times and "seed" 12 times. The OT was standardized to "seed"; the NT was left for the editor to decide, because "offspring" reads naturally in the levirate passages (Matthew 22, Mark 12, Luke 20), while "seed" keeps the link to the OT promise texts that the NT quotes.
7. **Minor variation left as is.** Some renderings still vary where the context arguably allows it: λῃστής "robber"/"bandit"; ἀρχισυνάγωγος; οἰκονόμος "steward"/"manager"; μύρον "perfume"/"ointment"; ἑορτή "feast"/"festival". John 6:31 and 6:45 keep "it stands written" for the periphrastic ἐστιν γεγραμμένον.

## Critical-text anomalies for the Studio

The English translates these as they stand. Each has a short factual note in the edition.

| Reference | Anomaly |
| :--- | :--- |
| Exodus 39:15 | The critical text adopts wording identical to 40:8 at this point (verse confidence 8%). |
| Leviticus 8:28–30 | The sprinkling of oil and blood is given twice (end of 8:28 and in full in 8:29), and 8:30 repeats only the closing phrase of 8:29. 8:29 also has the misspelling `προσέῤῥνεν` for `προσέρρανεν`. |
| Numbers 21:20 | The sending of messengers to Sihon appears here and again at the opening of 21:21. The verse also has the misspelling `πρέαβεις` for `πρέσβεις`. |
| Numbers 27:7 | Repeats the closing clause of 27:6 ("And you shall speak to the sons of Israel"). |
| Psalm 12:4 | The same clause appears here (optative εἴποι) and again at the opening of 12:5 (subjunctive εἴπῃ). |
| Sirach 41:23 | The same line appears here and again at the opening of 41:24. |
| 1 Kings 12:24 | In the long additional account, `Ἵωα` and `ἄπτους` stand for `ἵνα` and `ἄρτους`. |
| Romans 15:19 | Stray raised dot in `ἐν δυνάμει πνεύματος· Θεοῦ·`, probably left over from converting the brackets. |

Two passages were re-paired to this repository's critical text: Nehemiah 12:17–19 and 1 Chronicles 6:54. Their verse division here differs from the Studio's current version. The Studio repository was not available to this review, so any difference between the Studio's current text and this repository's copy should be checked there.

## Commits

This review is in the following commits on branch `ccr-46393f40-vccvrn`:

- `b7edf3b`: structural re-pairing to the critical text
- `f1ee137`: NT wording, Matthew–James
- `6e22403`: NT wording, 1 Peter–Revelation, plus the NT consistency pass
- `731c4d1`, `c3edaee`, `102fb85`, `32f7f26`: OT wording from Genesis through Isaiah 24, including the whole Wisdom division
- final commit:
  - OT wording for Isaiah 25–66, Jeremiah, Ezekiel, Daniel and the Twelve;
  - OT-wide consistency passes, which also touch earlier books;
  - edition counts;
  - this review record.
