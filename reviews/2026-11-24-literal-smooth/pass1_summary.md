# Stage 2 Pass 1 — Independent Greek-Only Source-Language Fidelity Review Summary

## 1. Provenance, Scope & Isolation Invariant
- **Edition Reviewed:** `Greek-Translation` (`Modern-English-OT` [43 books] + `Modern-English-NT` [27 books])
- **Branch:** `review/2026-11-24-literal-smooth`
- **Pinned Base Commit (`GRC_BASE_SHA`):** `278767fbb0a64a8af6abb343b835c39e791d4a05`
- **Adopted Source Critical Text (`CTS_SHA`):** `Saints-Greek-Critical-Text` (Studio v10 Stage 1, `a0d022c1`)
- **Strict Language Isolation:** **100% Greek-only.** Zero Hebrew or Latin critical texts, English translations, or review files were accessed or referenced.
- **Pass 1 Read-Only Rule:** **0 tracked Modern English JSON or Markdown files modified** (all proposed changes recorded exclusively in `reviews/2026-11-24-literal-smooth/` for Pass 2 independent second source-language verification).
- **Note on CT README Metadata:** `Saints-Greek-Critical-Text/README.md` line 3 still reports `34,210 verses` (pre-Stage-1 count prior to removal of 12 phantom/duplicate verses); the actual adopted TSV corpus at `278767fb` contains exactly **34,198 verses** across **70 books / 1,291 chapters**.

### Book-Level Adopted Source Witness Provenance (Rule 1)
| Scope | Books | Orthographic Base | Versification Anchor | Admitted Witnesses |
|---|---:|---|---|---|
| Greek OT (Standard) | 41 | Swete-Amicarelli | Sixtine/Brenton | `Swete-Amicarelli`, `1st1K-LXX`, `Swete (B/A/א)`, `Sixtine/Brenton` |
| Ecclesiastes | 1 | Swete-Amicarelli | Sixtine/Brenton | `Swete-Amicarelli`, `Sixtine/Brenton` |
| Isaiah | 1 | Swete-Amicarelli | Sixtine/Brenton | `Swete-Amicarelli`, `1st1K-LXX`, `Sixtine/Brenton` |
| Greek NT (Standard) | 22 | SBLGNT | SBLGNT | `SRGNT`, `SBLGNT`, `BHP`, `Nestle1904`, `RP2018 (Byz)`, `TR (KJTR)`, `B (03)`, `א (01)` |
| Greek NT (B Lacunose: 1–2 Tim, Titus, Phlm, Rev) | 5 | SBLGNT | SBLGNT | `SRGNT`, `SBLGNT`, `BHP`, `Nestle1904`, `RP2018 (Byz)`, `TR (KJTR)`, `א (01)` |

## 2. Corpus Coverage & Exact Parity Reconciliation (Rule 0)
- **Adopted Greek Critical Text Total (`source_total`):** **34,198 verses** across **70 books** / **1,291 chapters** (**26,238** OT across 43 books / 1,031 chapters; **7,960** NT across 27 books / 260 chapters).
- **Coverage Breakdown (`verified + disputed + unverified == source_total`):**
  - **`verified`:** **34,000** (26,096 OT + 7,904 NT)
  - **`disputed`:** **198** (142 OT + 56 NT — exact count of distinct adopted source verses covered by open Pass 1 proposals, expanding the 3 merged Sirach CT pairs to their 6 underlying source verses and excluding the 12 Stage 1 removed verses that are absent from `source_total`)
  - **`unverified`:** **0** (every book underwent full programmatic structural, Stage 1 diff, length-outlier, negation, numeral, divine-name, bracket, lexeme, and manuscript-citation auditing, complemented by full paragraph-in-context reading of **155 OT chapters + Sirach Prologue + Esther Additions A–F + 4,839 NT verses across all 27 NT books + all 514 non-consistency Claude OT/NT edits + all 18 NT bracketed unplaced verses**).
- **Missing Passages:** `missing_in_studio = 0`, `missing_in_english = 0`.
- **Exact Arithmetic Reconciliation (`34,198` CT vs `34,208` ME entries = `34,150` placed + `58` unplaced):**
  - `+1`: **Sirach Prologue** is embedded inside CT `1:1` and cleanly separated in ME into `unplaced` (`Prologue`) + placed `1:1` (`Πᾶσα σοφία...`).
  - `-3`: **Sirach 30–36** uses restored Saints.Bible parallel chapter numbering and merges 3 short consecutive CT verse pairs into 3 ME verses with zero omitted Greek words (`CT 32:4+32:5 → ME 35:4`, `CT 33:1+33:2 → ME 36:1`, `CT 33:11+36:16 → ME 36:10`).
  - `+12`: **12 Stage 1 removed phantom/duplicate verses** (`Numbers 16:44`, `1 Samuel 20:43`, `Psalms 25:22, 27:14, 71:24, 102:29, 114:26, 116:10, 136:26, 149:14, 150:9`, `Ezekiel 20:45`) were deleted from Studio in `a0d022c1` but still persist in ME `unplaced`; all 12 are proposed for deletion.
  - Check: `34,198 + 1 - 3 + 12 = 34,208` (`100%` accounted for; `Deuteronomy 29:1–29` maps 1:1 to ME `28:69` + `29:1–28`, already documented at `28:69`).
- **Out-of-Canon Scope (Explicitly Classified, Not Missing):** Greek Daniel additions **Susanna** (64 vv Theodotion / 60 vv OG) and **Bel and the Dragon** (42 vv) are absent from both Studio's 12-chapter Theodotion Daniel (which retains Prayer of Azariah & Song of the Three at `3:24–90`) and `Modern-English-OT`. Documented under `out_of_canon_scope` in `pass1_coverage.json` and `GRC-HQ-009`.

## 3. Pass 1 Proposals Overview (`pass1_proposals.jsonl`)
- **Total Proposals:** **207** (`GRC-P1-001` through `GRC-P1-207`; **151** OT + **56** NT)
  - Verse-text changes: **105** | Note changes: **133** | Both text & note: **31**
  - Flagged `needs_human_editor: true`: **59** (38 OT + 21 NT) | Pass-2 auto-verifiable (`false`): **148**
  - Validation status: **PASS (0 errors)** — every `current_english`, `current_note`, and non-removed `source_phrase` verified byte-for-byte against `GRC_BASE_SHA = 278767fb`.

| Proposal Category | Count |
|---|---:|
| `rule4_ambiguity_note` | 42 |
| `stage1_drift_text` | 34 |
| `rule2_order_and_mapping_note` | 25 |
| `rule4_sperma_echo` | 18 |
| `stage1_drift_removed_verse` | 12 |
| `stage1_drift_text_and_note` | 12 |
| `stage1_drift_note` | 10 |
| `fidelity_grammar` | 8 |
| `note_neutrality` | 8 |
| `note_factual_error` | 7 |
| `stage1_drift_proper_name` | 6 |
| `stale_note` | 6 |
| `fidelity_meaning` | 4 |
| `fidelity_wording` | 4 |
| `lexical_consistency` | 4 |
| `broken_manuscript_citation` | 2 |
| `fidelity_note` | 2 |
| `fidelity_negation` | 1 |
| `fidelity_omission` | 1 |
| `fidelity_referent` | 1 |

## 4. Stage 1 Critical-Text Drift Audit (`HEAD~1` vs `HEAD`, `a0d022c1`)
Programmatic diff across all 1,291 TSVs identified **979 modified TSVs** containing **12 removed verses**, **0 added verses**, **100 substantive text diffs**, **0 bracket diffs**, and **43 diacritic/punctuation/case diffs**. Auditing every single diff against current Modern English and notes yielded **74 Stage 1 drift proposals** (while confirming all orthographic/numeral/punctuation cleanups in `Exod 30:23`, `Num 2:31, 17:21, 29:15–26`, `Judg 20:25`, `1 Kgs 12:24`, `Ezra 2:37–38`, `Neh 7:26, 27, 41, 70`, `Matt 4:18–19, 25:16, 28:10`, `Mark 1, 8, 9, 12`, `Luke 3, 22, 24`, `John 18:17`, `Acts 6:9`, `Rom 6:8, 14:25, 15:19, 16:1`, `1 Cor 1:20`, `2 Cor 7:3`, `2 Thess 2:13`, `Heb 12:15, 13:21`, `Jas 2:3` are already clean in ME):

1. **12 Removed Phantom/Duplicate `unplaced` Verses:** `Num 16:44`, `1 Sam 20:43`, `Ps 25:22, 27:14, 71:24, 102:29, 114:26, 116:10, 136:26, 149:14, 150:9`, `Ezek 20:45`.
2. **Exodus 39:14–16 (3 proposals):** Restored ark/poles clause in `39:14`; fixed misallocated `40:8` corruption and obsolete note in `39:15`; removed moved altar clause from `39:16`.
3. **Leviticus 8:19–20, 8:28–30 (5 proposals):** Realigned washing clause `8:20 → 8:19`; removed duplicated sprinkling clause in `8:28`; deleted now-false note on `8:29`; restored full sanctification clause and deleted false note in `8:30`.
4. **Numbers 21:18–21 & 27:5–7 (7 proposals):** Realigned itinerary phrase `21:18 → 21:19`; removed duplicate envoys clause in `21:21` and obsolete note on `21:20`; moved `λέγων` `27:5 → 27:6`; removed duplicate closing clause from `27:6` and obsolete note on `27:7`.
5. **1 Kings 6:17 (1 proposal):** Removed duplicated closing clause (now solely in `6:19`).
6. **1 Chronicles 1, 5, 6, 7, 9, 12 (23 proposals):** Removed misplaced chiefs from `1:48` → `1:51` and updated stale note at `1:47`; fixed `6:8 ↔ 6:11` swap; fixed displaced Levitical city lists in `6:43, 6:54, 6:58` and stale notes at `6:42, 6:54`; repaired `7:26` from misallocated Gedson text to Ladan/Amioueid/Eleimasai; removed `12:4` duplication of `12:5` (unplaced) and updated `12:5` spellings/note; added missing `Καινὰ` in `12:7`; removed dropped `καί` in `6:3` and `9:44`; flagged Swete/B proper-name shifts (`5:31, 5:35, 6:15, 6:19, 6:25, 6:28, 6:36, 6:37`) and `6:32` omitted `υἱοῦ` for human editor review.
7. **Nehemiah 12:8, 12:15 (note), 12:17–19 (5 proposals):** Removed duplicate closing phrase in `12:8` (now solely in `12:9`); realigned priestly pairings across `12:17–19` and updated stale note on `12:15`.
8. **Job 41:1–3 (3 proposals):** Removed duplicated questions in `41:1` and `41:3`, synced `οὐδὲ` in `41:2`, deleted obsolete duplication note on `41:1`, and relocated the `'prepared for/by Me'` note to `41:2`.
9. **Psalms 12:4–5 & 123:1, 130:1, 132:1 (5 proposals):** Removed duplicated clause in `12:5` and obsolete note on `12:4`; restored `τῷ Δαυίδ` (`For David.`) in superscriptions of `123:1, 130:1, 132:1`.
10. **Sirach 41:23–24 (2 proposals):** Removed duplicate line from `41:24` (unplaced), deleted obsolete duplication note on `41:23`, and relocated the `deuteroseos kai logou akoes` hendiadys note from `41:24` to `41:23`.
11. **Ezekiel 12:8 & 21:24–27 (5 proposals):** Restored `τὸ πρωί` (`in the morning`) in `12:8`; removed duplicate clause from `21:24` and obsolete first sentence from `21:25` note; moved `ἐκ δεξιῶν αὐτοῦ.` (`on his right.`) from end of `21:26` to opening of `21:27`.
12. **NT Stage 1 Drift (2 proposals):** `1 Corinthians 14:37` (removed stray raised dot `κυρίου ἐστίν· ἐντολή` → unified predicate `are a command of the Lord` + updated note); `Revelation 16:3` (`πᾶσα ψυχὴ ζῶσα` → `πᾶσα ψυχὴ ζωῆς`, restoring `"every soul of life"` + Semitic genitive-of-quality explanation and correcting false `pasa psyche zosa` citation in note).

## 5. Full-Corpus Fidelity, Manuscript Citations & Claude Checklist Audit
- **Mechanical & Hygiene Checks (All 34,198 verses):** **0** archaisms, **0** bracket `⟦ ⟧` mismatches (across all placed and 18 unplaced NT bracketed verses), **0** orphan notes, **0** true negation flips (outside `Ezek 24:17`'s elliptical omission of `will be`), **0** numeral errors, **0** disallowed proper names, **0** `LORD`/`YHWH` in verse text.
- **Broken Manuscript Citations Audited & Fixed:**
  - Verified accurate: `Gen 8:2` (`ἀπεκαλύφθησαν`, Swete/A), `Gen 18:7` (`ἔλαβον`, Swete/A), `Ps 41:9` (`δηλώσει`, B + א).
  - **Fixed (`broken_manuscript_citation`, 2 proposals):** `Psalms 44:14` (note falsely credited Alexandrinus `A` with `Ἑσεβών` → corrected to **Codex Vaticanus `B` + Codex Sinaiticus `א`**, noting `A` reads `ἔσωθεν`); `Psalms 115:4` (note falsely cited Vaticanus `B` inside its Psalms `105:27–137:6` lacuna → corrected to **Sinaiticus `א` and Alexandrinus `A`**).
  - **Fixed (`note_factual_error`, 7 NT proposals):** `John 5:3` and `Acts 8:36` notes falsely claimed `John 5:4` / `Acts 8:37` are *not included* in SGCT (both appear in `⟦ ⟧` and ME `unplaced`); `Mark 9:43` omitted `⟦ ⟧` notice; `Matt 17:20`, `Matt 18:10`, `John 1:51`, and `Acts 15:33` misquoted their own rendered English verses.
  - **Fixed (`note_neutrality`, 8 NT proposals):** Removed evaluative phrases (`most reliable`, `best manuscripts`, `better attested`, `traditional English translations`) in `Mark 16:8`, `Luke 15:21`, `Acts 16:7`, `Rom 16:24`, `Gal 2:19`, `1 John 5:7`, `Rev 8:13`, `Rev 20:9` (0 evaluative manuscript phrases found across all 43 OT books).
- **Substantive Paragraph-in-Context Fidelity Findings (OT + NT):**
  - **OT (18 verse fixes + 6 stale notes + 2 syntax notes):** `Exod 10:17` (`pardon my sin`), `Num 14:18` (`clear the guilty`), `1 Sam 13:13` (`would have established`), `2 Sam 18:12` (counterfactual `Even if I were weighing out...`), `2 Chr 25:27` (preventing self-murder misreading of Amaziah), `Ezra 1:4` (`support him`), `1 Macc 1:61` (resuming `put to death` from `1:60`), `2 Macc 1:19` (restoring omitted `τάξιν`), `2 Macc 9:15` (`ὡς` not `οὕς`, removing added `but`), `Isa 35:4` (`Take comfort`), `Isa 44:5` (`inscribe on his hand` + note), `Ezek 24:17` (restoring `will be` outside negation scope), `Dan 5:22` (rhetorical question `did you not know all these things?` + note), `Mic 3:8` (separating genitives of filling + note), `Zech 1:6` (`which` + antecedent note), `Gen 48:19` (sole OT `σπέρμα` → `seed` holdout), `Ps 121:1` (sole `τῷ Δαυίδ` → `For David.` holdout), `1 Kgs 8:66` (`good heart` wordplay matching `2 Chr 7:10`), `Jer 28:59` (sole `Μαασαίου` → `Maaseiah` holdout), plus 6 stale notes (`Gen 24:7`, `Exod 40:8`, `Num 21:30`, `Num 23:10`, `1 Sam 2:31`, `1 Kgs 1:48`) and 2 explanatory notes (`Song 1:16`, `Jer 27:18`).
  - **NT (4 verse fixes):** `Mark 14:22` and `Luke 24:30` (objectless `εὐλογέω` harmonized to `saying/said a blessing` matching `Matt 26:26`), `Luke 4:11` (`μήποτε` → `so that You do not strike` matching `Matt 4:6`), `1 Cor 15:24` (standalone `τῷ θεῷ καὶ πατρί` → `to God the Father` matching `Eph 5:20` & `Jas 1:27`).
- **Claude Checklist Audit (`reviews/2026-11-24-ME-GREEK-FIDELITY/`):** All 235 OT rows and all 279 non-consistency NT rows audited against Stage 1 Greek. The overwhelming majority of Claude's edits are sound; 34 concrete follow-up fixes (29 OT + 5 NT) were captured above, and all open editorial sets (Messianic capitals, Song of Songs `kinsman`, Daniel `Baltasar`, Hebrew vs. Greek OT proper names, minor lexical variation `μύρον`/`οἰκονόμος`/OT `λῃστής`) are explicitly verified and escalated in `pass1_human_queue.jsonl` (note: NT `λῃστής` [100% `robber`], `ἀρχισυνάγωγος` [100% `synagogue ruler`], and `ἑορτή` [100% `feast`] are verified already 100% consistent).

## 6. Rule 2 (Native Order & Saints.Bible Mapping) & Rule 4 (Ambiguity Preservation) Test Results
### Rule 2 — Native Order, Skipped-Verse & Mapping Notes (`25` proposals)
- Verified existing accurate notes at `Exod 20:13`, `Num 6:27`, `Deut 28:69`, `Sir 30:25`, `Sir 33:17`, `Esth` Additions A–F, `Ps 151`, and `Dan 3–5`.
- Added concise reader notes preventing perceived omissions at: **`Deut 5:17`** (Greek Decalogue order variation vs `Exod 20:13–15` and Swete B), **`1 Kgs 5:9, 6:15, 6:19, 6:34`**, **`Neh 12:7, 12:42`**, **`Prov 16:2, 19:3, 24:23`** (clarifying Studio standard chapter sequence vs Rahlfs/Vaticanus arrangement), **`Sir 26:28`** (GII `26:19–27`), **`Sir 35:4, 35:12, 35:21, 35:24, 36:1, 36:10, 36:18`** (documenting all 3 merged CT pairs and all skipped parallel verse slots), and **`Jer 26:2, 27:1, 28:1, 29:1, 38:1, 52:4, 52:31`** (completing LXX↔MT chapter correspondence and absent-verse notes).

### Rule 4 — Mandatory Ambiguity Preservation Tests (`60` proposals: `42` notes + `18` NT `σπέρμα` policy proposals)
1. **`πίστις Ἰησοῦ Χριστοῦ` (`faith of` vs `faith in`):** Verified existing notes at `Mark 11:22`, `Rom 3:22`, `Gal 2:16`, `Gal 3:22`, `Eph 3:12`, `Phil 3:9`, `Rev 2:13`, `Rev 14:12`. Added missing standalone notes at **`Rom 3:26`**, **`Gal 2:20`**, **`Col 2:12`**, and expanded **`Jas 2:1`** (which preserves natural English ambiguity `the faith of`). Escalated edition-wide policy to `GRC-HQ-002`.
2. **`πνεῦμα` Capitalization (`spirit` vs `Spirit`):** Added alternate-reading footnotes across **all 9 Ezekiel visionary loci** (`Ezek 2:2, 3:12, 3:14` [articular `τὸ πνεῦμα`], `3:24, 8:3, 11:1, 11:5, 11:24, 43:5`), **`Isa 32:15`** (lowercase `a spirit`), **`Isa 63:14`**, **`Gen 41:38`**, **`Job 27:3`**, and **10 NT `πνεῦμα` loci** (`John 4:23`, `Rom 8:15, 12:11`, `1 Cor 14:2, 15:45`, `2 Cor 3:6`, `Eph 1:17`, `1 Tim 3:16`, `1 John 4:6`, `Rev 1:10` [cross-referenced by `4:2` & `17:3` yet missing its own note]). Escalated Ezekiel/Isaiah capitalization policy to `GRC-HQ-003`.
3. **Contextual `σπέρμα` (`seed` vs `offspring`):** OT fixed to 226/226 non-idiomatic `seed` via `Gen 48:19` (5 `κοίτη σπέρματος` idioms remain appropriately idiomatic). In NT (40 `σπέρμα` occurrences), 7 botanical + 2 biological are `seed` and 7 levirate marriage passages naturally remain `offspring`; the **18 OT-promise/covenant/Gen-3:15 echo verses** currently reading `offspring` (`Luke 1:55`, `John 7:42, 8:33, 8:37`, `Acts 3:25, 7:5, 7:6, 13:23`, `Rom 4:13, 4:16, 4:18, 9:7, 9:8, 9:29`, `2 Cor 11:22`, `2 Tim 2:8`, `Heb 2:16`, `Rev 12:17`) are proposed as `seed` with `needs_human_editor: true` (`GRC-HQ-004`) to eliminate intra-book and parallel-quote clashes (e.g., `Rom 9:7` vs `Heb 11:18`, `Rom 4 & 9` vs `Rom 1:3 & 11:1`, `2 Tim 2:8` vs `Rom 1:3`, `Rev 12:17` vs `Gen 3:15`).
4. **Additional OT Messianic & NT Grammatical Ambiguities:** Added neutral Rule 4 notes for **12 OT Messianic/royal capitalization anchors** (`Gen 49:24`, `Ps 2:7, 109:1`, `Isa 7:14, 9:5, 11:2, 11:10`, `Lam 4:20`, `Dan 7:14`, `Mic 5:1`, `Zech 9:9, 12:10` → `GRC-HQ-001`) and **3 NT grammatical ambiguities** (`Matt 5:39`, `2 Cor 5:19`, `Col 1:20`).

## 7. Human Editorial Queue (`pass1_human_queue.jsonl` — 14 Items)
| ID | Category | Topic |
|---|---|---|
| `GRC-HQ-001` | `doctrinal_capitalization_policy` | Messianic Pronoun Capitalization Policy in Greek OT |
| `GRC-HQ-002` | `doctrinal_genitive_ambiguity` | πίστις Ἰησοῦ Χριστοῦ (Objective vs. Subjective Genitive) Policy |
| `GRC-HQ-003` | `doctrinal_capitalization_policy` | πνεῦμα Capitalization in Ezekiel Visionary Formulas & Isaiah 32:15 / 63:14 |
| `GRC-HQ-004` | `lexical_intertextual_policy` | Contextual σπέρμα ('seed' vs. 'offspring') Policy Across OT & NT Echoes |
| `GRC-HQ-005` | `proper_name_policy` | OT Proper-Name Transliteration Policy (Traditional English/Hebrew vs. Greek LXX Forms) |
| `GRC-HQ-006` | `reversible_lexical_choice` | Song of Songs ἀδελφιδός ('kinsman' vs. 'beloved') |
| `GRC-HQ-007` | `proper_name_policy` | Daniel Βαλτασάρ ('Baltasar' for both Belteshazzar and Belshazzar) |
| `GRC-HQ-008` | `minor_lexical_variation` | Minor Lexical Variation in NT/OT (μύρον, οἰκονόμος/οἰκονομία, OT λῃστής) |
| `GRC-HQ-009` | `canon_scope_and_base_text` | Out-of-Canon Greek Daniel Additions (Susanna; Bel and the Dragon) & Old Greek vs. Theodotion Scope |
| `GRC-HQ-010` | `critical_text_witness_divergence` | Low-Confidence Stage 1 Critical Text Loci & Codex B/Swete Structural Divergences (1 Chr 5-7, 1 Kgs 12:24, etc.) |
| `GRC-HQ-011` | `note_style_policy` | References to 'YHWH' and 'GOD' Inside Comparative OT Notes |
| `GRC-HQ-012` | `greek_syntax_judgment_call` | Isaiah 44:5 Bare Dative After Compound ἐπιγράφω ('inscribe on his hand' vs. 'write with his hand') |
| `GRC-HQ-013` | `editorial_punctuation_judgment_call` | Daniel 5:22 Punctuation of οὐ πάντα ταῦτα ἔγνως (Rhetorical Question vs. Statement) |
| `GRC-HQ-014` | `greek_syntax_judgment_call` | Micah 3:8 Dual Grammatical Attachment of κρίματος καὶ δυναστείας & Anarthrous πνεύματι |

## 8. Complete 70-Book Coverage Table (`GRC_BASE_SHA = 278767fb`, `CTS_SHA = a0d022c1`)
| # | Book | Test. | Ch. | Source Total | Verified | Disputed | Unverified | ME Placed | ME Unpl. | S1 Extra | Proposals | Human Ed. | Context Ch. |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Genesis | OT | 50 | 1531 | 1527 | 4 | 0 | 1531 | 0 | 0 | 4 | 2 | 7 |
| 2 | Exodus | OT | 40 | 1163 | 1158 | 5 | 0 | 1162 | 1 | 0 | 5 | 0 | 7 |
| 3 | Leviticus | OT | 27 | 859 | 854 | 5 | 0 | 859 | 0 | 0 | 5 | 0 | 1 |
| 4 | Numbers | OT | 36 | 1288 | 1278 | 10 | 0 | 1287 | 2 | 1 | 11 | 0 | 4 |
| 5 | Deuteronomy | OT | 34 | 958 | 957 | 1 | 0 | 958 | 0 | 0 | 1 | 0 | 7 |
| 6 | Joshua | OT | 24 | 643 | 643 | 0 | 0 | 643 | 0 | 0 | 0 | 0 | 1 |
| 7 | Judges | OT | 21 | 618 | 618 | 0 | 0 | 618 | 0 | 0 | 0 | 0 | 1 |
| 8 | Ruth | OT | 4 | 85 | 85 | 0 | 0 | 85 | 0 | 0 | 0 | 0 | 0 |
| 9 | 1 Samuel | OT | 31 | 772 | 770 | 2 | 0 | 772 | 1 | 1 | 3 | 0 | 2 |
| 10 | 2 Samuel | OT | 24 | 694 | 693 | 1 | 0 | 694 | 0 | 0 | 1 | 0 | 1 |
| 11 | 1 Kings | OT | 22 | 755 | 748 | 7 | 0 | 754 | 1 | 0 | 7 | 0 | 1 |
| 12 | 2 Kings | OT | 25 | 719 | 719 | 0 | 0 | 718 | 1 | 0 | 0 | 0 | 0 |
| 13 | 1 Chronicles | OT | 29 | 930 | 906 | 24 | 0 | 929 | 1 | 0 | 24 | 10 | 0 |
| 14 | 2 Chronicles | OT | 36 | 820 | 819 | 1 | 0 | 820 | 0 | 0 | 1 | 0 | 0 |
| 15 | Ezra | OT | 10 | 280 | 279 | 1 | 0 | 280 | 0 | 0 | 1 | 0 | 0 |
| 16 | Nehemiah | OT | 13 | 388 | 381 | 7 | 0 | 388 | 0 | 0 | 7 | 0 | 0 |
| 17 | Esther | OT | 10 | 164 | 164 | 0 | 0 | 164 | 0 | 0 | 0 | 0 | 10 |
| 18 | 1 Maccabees | OT | 16 | 924 | 923 | 1 | 0 | 924 | 0 | 0 | 1 | 0 | 2 |
| 19 | 2 Maccabees | OT | 15 | 555 | 553 | 2 | 0 | 555 | 0 | 0 | 2 | 0 | 1 |
| 20 | Job | OT | 42 | 1068 | 1064 | 4 | 0 | 1068 | 0 | 0 | 4 | 1 | 9 |
| 21 | Psalms | OT | 151 | 2533 | 2523 | 10 | 0 | 2533 | 9 | 9 | 19 | 2 | 9 |
| 22 | Proverbs | OT | 31 | 889 | 886 | 3 | 0 | 889 | 0 | 0 | 3 | 0 | 9 |
| 23 | Ecclesiastes | OT | 12 | 222 | 222 | 0 | 0 | 222 | 0 | 0 | 0 | 0 | 3 |
| 24 | Song of Songs | OT | 8 | 117 | 116 | 1 | 0 | 117 | 0 | 0 | 1 | 0 | 8 |
| 25 | Lamentations | OT | 5 | 150 | 149 | 1 | 0 | 150 | 0 | 0 | 1 | 1 | 0 |
| 26 | Wisdom of Solomon | OT | 19 | 436 | 436 | 0 | 0 | 435 | 1 | 0 | 0 | 0 | 3 |
| 27 | Sirach | OT | 51 | 1357 | 1344 | 13 | 0 | 1352 | 3 | 0 | 10 | 0 | 10 |
| 28 | Isaiah | OT | 66 | 1289 | 1281 | 8 | 0 | 1289 | 0 | 0 | 8 | 7 | 11 |
| 29 | Jeremiah | OT | 52 | 1296 | 1287 | 9 | 0 | 1295 | 1 | 0 | 9 | 0 | 11 |
| 30 | Ezekiel | OT | 48 | 1265 | 1250 | 15 | 0 | 1265 | 1 | 1 | 16 | 9 | 10 |
| 31 | Daniel | OT | 12 | 420 | 418 | 2 | 0 | 402 | 18 | 0 | 2 | 2 | 6 |
| 32 | Hosea | OT | 14 | 197 | 197 | 0 | 0 | 197 | 0 | 0 | 0 | 0 | 3 |
| 33 | Joel | OT | 4 | 73 | 73 | 0 | 0 | 73 | 0 | 0 | 0 | 0 | 2 |
| 34 | Amos | OT | 9 | 146 | 146 | 0 | 0 | 146 | 0 | 0 | 0 | 0 | 2 |
| 35 | Obadiah | OT | 1 | 21 | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 0 | 0 |
| 36 | Jonah | OT | 4 | 48 | 48 | 0 | 0 | 48 | 0 | 0 | 0 | 0 | 4 |
| 37 | Micah | OT | 7 | 105 | 103 | 2 | 0 | 105 | 0 | 0 | 2 | 2 | 1 |
| 38 | Nahum | OT | 3 | 47 | 47 | 0 | 0 | 47 | 0 | 0 | 0 | 0 | 0 |
| 39 | Habakkuk | OT | 3 | 56 | 56 | 0 | 0 | 56 | 0 | 0 | 0 | 0 | 2 |
| 40 | Zephaniah | OT | 3 | 53 | 53 | 0 | 0 | 53 | 0 | 0 | 0 | 0 | 0 |
| 41 | Haggai | OT | 2 | 38 | 38 | 0 | 0 | 38 | 0 | 0 | 0 | 0 | 0 |
| 42 | Zechariah | OT | 14 | 211 | 208 | 3 | 0 | 211 | 0 | 0 | 3 | 2 | 6 |
| 43 | Malachi | OT | 3 | 55 | 55 | 0 | 0 | 55 | 0 | 0 | 0 | 0 | 1 |
| 44 | Matthew | NT | 28 | 1071 | 1068 | 3 | 0 | 1068 | 3 | 0 | 3 | 0 | 11 |
| 45 | Mark | NT | 16 | 678 | 675 | 3 | 0 | 673 | 5 | 0 | 3 | 0 | 10 |
| 46 | Luke | NT | 24 | 1151 | 1147 | 4 | 0 | 1149 | 2 | 0 | 4 | 1 | 9 |
| 47 | John | NT | 21 | 879 | 873 | 6 | 0 | 878 | 1 | 0 | 6 | 3 | 11 |
| 48 | Acts | NT | 28 | 1006 | 999 | 7 | 0 | 1002 | 4 | 0 | 7 | 4 | 8 |
| 49 | Romans | NT | 16 | 436 | 426 | 10 | 0 | 433 | 3 | 0 | 10 | 7 | 12 |
| 50 | 1 Corinthians | NT | 16 | 437 | 433 | 4 | 0 | 437 | 0 | 0 | 4 | 0 | 7 |
| 51 | 2 Corinthians | NT | 13 | 256 | 253 | 3 | 0 | 256 | 0 | 0 | 3 | 1 | 4 |
| 52 | Galatians | NT | 6 | 149 | 147 | 2 | 0 | 149 | 0 | 0 | 2 | 1 | 6 |
| 53 | Ephesians | NT | 6 | 155 | 154 | 1 | 0 | 155 | 0 | 0 | 1 | 0 | 6 |
| 54 | Philippians | NT | 4 | 104 | 104 | 0 | 0 | 104 | 0 | 0 | 0 | 0 | 4 |
| 55 | Colossians | NT | 4 | 95 | 93 | 2 | 0 | 95 | 0 | 0 | 2 | 0 | 4 |
| 56 | 1 Thessalonians | NT | 5 | 89 | 89 | 0 | 0 | 89 | 0 | 0 | 0 | 0 | 5 |
| 57 | 2 Thessalonians | NT | 3 | 47 | 47 | 0 | 0 | 47 | 0 | 0 | 0 | 0 | 3 |
| 58 | 1 Timothy | NT | 6 | 113 | 112 | 1 | 0 | 113 | 0 | 0 | 1 | 0 | 6 |
| 59 | 2 Timothy | NT | 4 | 83 | 82 | 1 | 0 | 83 | 0 | 0 | 1 | 1 | 4 |
| 60 | Titus | NT | 3 | 46 | 46 | 0 | 0 | 46 | 0 | 0 | 0 | 0 | 3 |
| 61 | Philemon | NT | 1 | 25 | 25 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 1 |
| 62 | Hebrews | NT | 13 | 303 | 302 | 1 | 0 | 303 | 0 | 0 | 1 | 1 | 10 |
| 63 | James | NT | 5 | 108 | 107 | 1 | 0 | 108 | 0 | 0 | 1 | 1 | 5 |
| 64 | 1 Peter | NT | 5 | 105 | 105 | 0 | 0 | 105 | 0 | 0 | 0 | 0 | 5 |
| 65 | 2 Peter | NT | 3 | 61 | 61 | 0 | 0 | 61 | 0 | 0 | 0 | 0 | 3 |
| 66 | 1 John | NT | 5 | 105 | 103 | 2 | 0 | 105 | 0 | 0 | 2 | 0 | 5 |
| 67 | 2 John | NT | 1 | 13 | 13 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 1 |
| 68 | 3 John | NT | 1 | 15 | 15 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 1 |
| 69 | Jude | NT | 1 | 25 | 25 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 1 |
| 70 | Revelation | NT | 22 | 405 | 400 | 5 | 0 | 405 | 0 | 0 | 5 | 1 | 13 |
| — | **OT Subtotal (43 books)** | OT | **1031** | **26,238** | **26,096** | **142** | **0** | **26,208** | **40** | **12** | **151** | **38** | **155** |
| — | **NT Subtotal (27 books)** | NT | **260** | **7,960** | **7,904** | **56** | **0** | **7,942** | **18** | **0** | **56** | **21** | **158** |
| — | **GRAND TOTAL (70 books)** | ALL | **1291** | **34,198** | **34,000** | **198** | **0** | **34,150** | **58** | **12** | **207** | **59** | **313** |

*All 70 books satisfy `verified + disputed + unverified == source_total` (`34,000 + 198 + 0 == 34,198`). Out-of-canon Greek Daniel additions (Susanna; Bel and the Dragon) are explicitly excluded by canonical scope (`GRC-HQ-009`).*
