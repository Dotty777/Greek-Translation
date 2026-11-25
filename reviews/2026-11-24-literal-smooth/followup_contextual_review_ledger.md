# Reconciled Revision-Pinned Greek (LXX OT + NT) Evidence & Contextual-Review Ledger (v2.0 — Strict 5-Tier Taxonomy)

- **Date:** 2026-11-25 (Evidence & Reporting Reconciliation; **0** Bible verse-text, note, mapping, or Studio changes)
- **Adopted Source Corpus:** Saints-Greek-Critical-Text (Studio v10 Stage 1 `a0d022c1`, 70 books / 1,291 ch / 34,198 native vv)
- **Pinned Text / Mapping Commit SHA:** `6ea0be9f7aa43f6f66fe3e617f03d54e7fa478ab`
- **Revision Chain Audited:** `df7abd10` → `278767fb` → `53ec61b9` → `1379708f` → `d307f8f7` → `4615526d` → `acef6069` → `fea550e4` → `6ea0be9f` (0 Bible text/note/mapping changes in evidence reconciliation)
- **Studio DB Snapshot:** `data/studio.db` (`seed_version = 10`, SHA-256 `23f39dbdcbc4599b1ed783bfce8a0b6268610e5dde6c200e114057798e64761d`)
- **Machine-Readable Ledgers:** `followup_contextual_review_ledger.json` & `scratch/followup/greek_contextual_ledger.jsonl` (`13,426` deduplicated citations retained after removing `1` exact duplicates)

## 1. Strict 5-Tier Evidence Totals (Each Native Reference Counted Once at Strongest Level)

> **Standard Applied Uniformly Across All Three Editions:** A passage is credited as `full_source_in_context_read` **only** where surviving evidence proves the reviewer compared its English against the adopted source in the surrounding paragraph, speech, or literary unit. Note checks, mapping checks, and isolated wording checks are classified under `targeted_evidence` (with explicit subtype counts and overlap). Batch scans, zero-change book claims, and unexpanded multi-verse issue-title ranges are strictly excluded. An earlier read supports the final revision **only** after programmatically confirming that the reviewed source text, English text, and relevant surrounding context (`±2` native verses / exact Pass 3.5 blind packet context) match final `HEAD` byte-for-byte.

| Strongest Documented Evidence Level | Distinct Native Verses | Share | Supports Final Revision (`true`) | Historical Only (`false`) | Strict Whole-Chapter Final Match |
|---|---:|---:|---:|---:|---:|
| **`full_source_in_context_read`** | **8,693** | **25.42%** | **8,597** | **96** | 7,952 |
| **`targeted_evidence`** *(note / mapping / isolated wording)* | **1,177** | **3.44%** | **1,174** | **3** | — |
| **`english_only_read`** *(Pass 3 standalone English)* | **243** | **0.71%** | **239** | **4** | — |
| **`automated_screening_only`** | **24,085** | **70.43%** | 24,085 | 0 | — |
| **`insufficient_evidence`** | **0** | **0.00%** | 0 | 0 | — |
| **TOTAL (`source_total` — exact partition)** | **34,198** | **100.00%** | — | — | — |

*Separate Editorial Status (NEVER merged with evidence depth): `verified` = **34,036**, `disputed` / `awaiting_human_signoff` = **162**, `unverified` = **0** (`34,036 + 162 = 34,198`).*

### Targeted Evidence Breakdown & Subtype Overlap

| Disjoint Targeted-Tier Subset | Distinct Native Verses | Share of Targeted Tier |
|---|---:|---:|
| `note_check` only | 173 | 14.70% |
| `mapping_check` only | 54 | 4.59% |
| `isolated_wording_check` only | 746 | 63.38% |
| `note_check` + `mapping_check` | 42 | 3.57% |
| `note_check` + `isolated_wording_check` | 123 | 10.45% |
| `mapping_check` + `isolated_wording_check` | 14 | 1.19% |
| `note_check` + `mapping_check` + `isolated_wording_check` | 25 | 2.12% |
| **TOTAL (`targeted_evidence` strongest tier)** | **1,177** | **100.00%** |

- **Targeted-tier check totals (non-disjoint across subtypes):** `note_check = 363`, `mapping_check = 135`, `isolated_wording_check = 908`, **multi-subtype overlap (`2+` subtypes) = `204`** (of which `note ∩ map = 67`).
- **Gross corpus-wide checks (including overlaps on `full_source_in_context_read` passages):** `note_check = 669` (`306` also in full), `mapping_check = 420` (`285` also in full), `isolated_wording_check = 1,366` (`458` also in full), `english_only_read = 1,353` (`1,079` also in full, `31` also in targeted).

## 2. Recovered Greek Pass 1 Helper Reading Records (`helper_ot_notes.md` & `helper_nt_notes.md`)

- **OT Helper (`grc-ot-reader`):** `C:/Users/penna/.gemini/antigravity/brain/c0bae784-da10-4a32-8e56-6a49b88cd34d/scratch/helpers/helper_ot_notes.md` (`L14–L38, L46–L57`; Pass 1; source `a0d022c1`, English `278767fb`)
  - Reconstructed directly from pinned source: **`3,892` distinct native rows across `154` native chapters** (helper counted `155` display chapters because `Deuteronomy 28:69–32:43` spans `5` display chapters `28[v.69], 29, 30, 31, 32[1–43]` but resolves in native Greek `a0d022c1` to `4` native chapters `29:1–29, 30, 31, 32:1–43`, with `Deuteronomy 32` ending strictly at verse **`43`** [excluding `32:44–52`]; `Sirach Prologue` is embedded in native `Sirach 1:1`; `Sirach 30–36` is verified 100% closed under transposition).
- **NT Helper (`grc-nt-reader`):** `C:/Users/penna/.gemini/antigravity/brain/c0bae784-da10-4a32-8e56-6a49b88cd34d/scratch/helpers/helper_nt_notes.md` (`L28–L31, L40–L45`; Pass 1; source `a0d022c1`, English `278767fb`)
  - Named discourse-context ranges (`L29–L31`): **`4,778` distinct native rows** across `160` full chapters + `1` partial chapter (`John 7:53` from `⟦7:53–8:11⟧`).
  - Separately listed **18 bracketed unplaced NT passages (`L40–L44`):** **`8` overlaps** with the named NT chapters (`Acts 15:34, Luke 23:17, Mark 15:28, Mark 9:44, Mark 9:46, Romans 14:24, Romans 14:25, Romans 14:26`) + **`10` net new** (`Acts 24:7, Acts 28:29, Acts 8:37, John 5:4, Luke 17:36, Mark 11:26, Mark 7:16, Matthew 17:21, Matthew 18:11, Matthew 23:14`) = **`4,788` distinct NT rows** (`4,778 + 18 − 8 = 4,788`). Under the strict Part 2 standard, the `4,778` continuous-discourse rows are classified as `full_source_in_context_read`, while the `10` non-overlapping isolated unplaced bracketed verses (audited in §4 against Stage 1 Greek and adjacent placed-verse notes without reading their chapters in context) are classified as `targeted_evidence` (`isolated_wording_check + note_check`), and the `8` overlapping bracketed rows hold both `full_source_in_context_read` and targeted check flags.
  - **Exact Reconciliation with Earlier `4,839` Summary & `4,860` Helper Subtotals:**

| NT Metric | Verse Count | Delta vs. `4,778` Named | Disposition |
|---|---:|---:|---|
| Named NT discourse-context ranges (`L29–L31`, pinned source recount) | **4,778** | 0 | Assigned to `full_source_in_context_read` |
| + 18 separately listed bracketed NT passages (`L40–L44`; `8` overlaps removed, `+10` net new) | **4,788** | +10 | `8` overlap full-context; `10` net new assigned to `targeted_evidence` |
| Earlier summary total (`helper_nt_notes.md#L28` & `pass1_coverage.json`) | 4,839 | +61 *(+51 vs 4,788)* | Unsupported excess (`+61` / `+51`) kept **strictly unassigned** |
| Sum of helper's 12 printed NT subtotals (`L29–L31`) | 4,860 | +82 *(+21 vs 4,839)* | **100% of `+82` is localized in John** (reported `515` vs `433` actual; all other 11 NT book-groups match with `0` diff). Kept **strictly unassigned** (`unresolved_excess`). |

### Recovered Range-by-Range Provenance Table (`grc-ot-reader` & `grc-nt-reader`)

| Range ID | Helper | File & Lines | Source / English Rev | Reported Range | Native Chs | Native Rows | Reported Sub. | Status |
|---|---|---|---|---|---:|---:|---:|---|
| `GRC-HOT-01` | `grc-ot-reader` | `helper_ot_notes.md#L17` | `a0d022c1` / `278767fb` | Genesis 1–4, 22, 48–49 | 7 | 185 | — | `resolved` |
| `GRC-HOT-02` | `grc-ot-reader` | `helper_ot_notes.md#L18,L46` | `a0d022c1` / `278767fb` | Exodus 20, 32, 36–40 | 7 | 201 | — | `resolved` |
| `GRC-HOT-03` | `grc-ot-reader` | `helper_ot_notes.md#L19` | `a0d022c1` / `278767fb` | Leviticus 16 | 1 | 34 | — | `resolved` |
| `GRC-HOT-04` | `grc-ot-reader` | `helper_ot_notes.md#L20` | `a0d022c1` / `278767fb` | Numbers 6, 22–24 | 4 | 123 | — | `resolved` |
| `GRC-HOT-05` | `grc-ot-reader` | `helper_ot_notes.md#L21,L47` | `a0d022c1` / `278767fb` | Deuteronomy 5–6, 28:69–32:43 | 6 | 180 | — | `resolved` |
| `GRC-HOT-06` | `grc-ot-reader` | `helper_ot_notes.md#L22` | `a0d022c1` / `278767fb` | Joshua 24 | 1 | 33 | — | `resolved` |
| `GRC-HOT-07` | `grc-ot-reader` | `helper_ot_notes.md#L22` | `a0d022c1` / `278767fb` | Judges 5 | 1 | 31 | — | `resolved` |
| `GRC-HOT-08` | `grc-ot-reader` | `helper_ot_notes.md#L22` | `a0d022c1` / `278767fb` | 1 Samuel 1–2 | 2 | 64 | — | `resolved` |
| `GRC-HOT-09` | `grc-ot-reader` | `helper_ot_notes.md#L22` | `a0d022c1` / `278767fb` | 2 Samuel 7 | 1 | 29 | — | `resolved` |
| `GRC-HOT-10` | `grc-ot-reader` | `helper_ot_notes.md#L22` | `a0d022c1` / `278767fb` | 1 Kings 8 | 1 | 64 | — | `resolved` |
| `GRC-HOT-11` | `grc-ot-reader` | `helper_ot_notes.md#L23,L48` | `a0d022c1` / `278767fb` | Esther 1–10 including Additions A–F | 10 | 164 | — | `resolved` |
| `GRC-HOT-12` | `grc-ot-reader` | `helper_ot_notes.md#L24` | `a0d022c1` / `278767fb` | 1 Maccabees 1–2 | 2 | 134 | — | `resolved` |
| `GRC-HOT-13` | `grc-ot-reader` | `helper_ot_notes.md#L24` | `a0d022c1` / `278767fb` | 2 Maccabees 7 | 1 | 42 | — | `resolved` |
| `GRC-HOT-14` | `grc-ot-reader` | `helper_ot_notes.md#L25` | `a0d022c1` / `278767fb` | Job 1–3, 19, 38–42 | 9 | 236 | — | `resolved` |
| `GRC-HOT-15` | `grc-ot-reader` | `helper_ot_notes.md#L27,L49` | `a0d022c1` / `278767fb` | Psalms 1–2, 21–22, 44, 50, 109, 117, 151 | 9 | 138 | — | `resolved` |
| `GRC-HOT-16` | `grc-ot-reader` | `helper_ot_notes.md#L28,L50` | `a0d022c1` / `278767fb` | Proverbs 8, 24–31 | 9 | 271 | — | `resolved` |
| `GRC-HOT-17` | `grc-ot-reader` | `helper_ot_notes.md#L29` | `a0d022c1` / `278767fb` | Ecclesiastes 1, 3, 12 | 3 | 54 | — | `resolved` |
| `GRC-HOT-18` | `grc-ot-reader` | `helper_ot_notes.md#L30` | `a0d022c1` / `278767fb` | Song of Songs 1–8 | 8 | 117 | — | `resolved` |
| `GRC-HOT-19` | `grc-ot-reader` | `helper_ot_notes.md#L31` | `a0d022c1` / `278767fb` | Wisdom of Solomon 1–2, 7 | 3 | 70 | — | `resolved` |
| `GRC-HOT-20` | `grc-ot-reader` | `helper_ot_notes.md#L32,L51` | `a0d022c1` / `278767fb` | Sirach Prologue + Sirach 1, 24, 30–36, 51 | 10 | 273 | — | `resolved` |
| `GRC-HOT-21` | `grc-ot-reader` | `helper_ot_notes.md#L34` | `a0d022c1` / `278767fb` | Isaiah 7, 9, 11, 32, 40, 42, 49, 52–53, 61, 63 | 11 | 220 | — | `resolved` |
| `GRC-HOT-22` | `grc-ot-reader` | `helper_ot_notes.md#L35,L52` | `a0d022c1` / `278767fb` | Jeremiah 1, 23, 25–32, 38 | 11 | 356 | — | `resolved` |
| `GRC-HOT-23` | `grc-ot-reader` | `helper_ot_notes.md#L36` | `a0d022c1` / `278767fb` | Ezekiel 1–3, 8, 11, 20–21, 36–37, 43 | 10 | 279 | — | `resolved` |
| `GRC-HOT-24` | `grc-ot-reader` | `helper_ot_notes.md#L37,L53-L57` | `a0d022c1` / `278767fb` | Daniel 2–5, 7, 9 | 6 | 264 | — | `resolved` |
| `GRC-HOT-25` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Hosea 1–2, 11 | 3 | 45 | — | `resolved` |
| `GRC-HOT-26` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Joel 2–3 | 2 | 32 | — | `resolved` |
| `GRC-HOT-27` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Amos 5, 9 | 2 | 42 | — | `resolved` |
| `GRC-HOT-28` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Jonah 1–4 | 4 | 48 | — | `resolved` |
| `GRC-HOT-29` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Micah 5 | 1 | 14 | — | `resolved` |
| `GRC-HOT-30` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Habakkuk 2–3 | 2 | 39 | — | `resolved` |
| `GRC-HOT-31` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Zechariah 3, 6, 9, 12–14 | 6 | 86 | — | `resolved` |
| `GRC-HOT-32` | `grc-ot-reader` | `helper_ot_notes.md#L38` | `a0d022c1` / `278767fb` | Malachi 3 | 1 | 24 | — | `resolved` |
| `GRC-HNT-01` | `grc-nt-reader` | `helper_nt_notes.md#L29` | `a0d022c1` / `278767fb` | Matt 1, 5–7, 13, 16, 22, 24–28 | 12 | 526 | 526 | `resolved` |
| `GRC-HNT-02` | `grc-nt-reader` | `helper_nt_notes.md#L29` | `a0d022c1` / `278767fb` | Mark 1, 4, 8–10, 12–16 incl. ⟦16:9–20⟧ | 10 | 446 | 446 | `resolved` |
| `GRC-HNT-03` | `grc-nt-reader` | `helper_nt_notes.md#L29` | `a0d022c1` / `278767fb` | Luke 1–2, 4, 6, 10, 15, 22–24 | 9 | 479 | 479 | `resolved` |
| `GRC-HNT-04` | `grc-nt-reader` | `helper_nt_notes.md#L29` | `a0d022c1` / `278767fb` | John 1, 3, 6, ⟦7:53–8:11⟧, 8, 10, 14–17, 20–21 | 12 | 433 | 515 | `resolved_with_unassigned_subtotal_excess` |
| `GRC-HNT-05` | `grc-nt-reader` | `helper_nt_notes.md#L29` | `a0d022c1` / `278767fb` | Acts 2, 7, 10, 13, 15, 17, 20, 26 | 8 | 352 | 352 | `resolved` |
| `GRC-HNT-06` | `grc-nt-reader` | `helper_nt_notes.md#L30` | `a0d022c1` / `278767fb` | Romans 1, 3–9, 11–12, 14–16 | 13 | 372 | 372 | `resolved` |
| `GRC-HNT-07` | `grc-nt-reader` | `helper_nt_notes.md#L30` | `a0d022c1` / `278767fb` | 1 Cor 1, 7, 11–15 & 2 Cor 3–5, 12 | 11 | 325 | 325 | `resolved` |
| `GRC-HNT-08` | `grc-nt-reader` | `helper_nt_notes.md#L30` | `a0d022c1` / `278767fb` | Galatians 1–6, Ephesians 1–6, Philippians 1–4, Colossians 1–4 (full) | 20 | 503 | 503 | `resolved` |
| `GRC-HNT-09` | `grc-nt-reader` | `helper_nt_notes.md#L30` | `a0d022c1` / `278767fb` | 1–2 Thessalonians, 1–2 Timothy, Titus, Philemon (full) | 22 | 403 | 403 | `resolved` |
| `GRC-HNT-10` | `grc-nt-reader` | `helper_nt_notes.md#L31` | `a0d022c1` / `278767fb` | Hebrews 1–2, 4, 7–13 | 10 | 250 | 250 | `resolved` |
| `GRC-HNT-11` | `grc-nt-reader` | `helper_nt_notes.md#L31` | `a0d022c1` / `278767fb` | James 1–5, 1–2 Peter, 1–3 John, Jude (full) | 21 | 432 | 432 | `resolved` |
| `GRC-HNT-12` | `grc-nt-reader` | `helper_nt_notes.md#L31` | `a0d022c1` / `278767fb` | Revelation 1–5, 12–14, 16, 19–22 | 13 | 257 | 257 | `resolved` |
| `GRC-HNT-BRK18` | `grc-nt-reader` | `helper_nt_notes.md#L40-L44` | `a0d022c1` / `278767fb` | Matt 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28; Luke 17:36, 23:17; John 5:4; Acts 8:37, 15:34, 24:7, 28:29; Rom 14:24-26 | 13 | 18 | — | `resolved` |

## 3. Reclassification Audit (Previous Follow-Up Ledger → Strict 5-Tier Ledger)

| Previous Ledger Class → Reconciled 5-Tier Class | Distinct Native Verses | Explanation |
|---|---:|---|
| `old_auto_only -> automated_screening_only` | 23,917 | Unchanged automated screening only |
| `old_auto_only -> full_source_in_context_read` | 6,717 | Newly recovered from surviving Greek helper notes (`helper_ot_notes.md` / `helper_nt_notes.md`) |
| `old_auto_only -> targeted_evidence` | 28 | Newly captured from follow-up verified mapping/note audit or net-new Greek NT bracketed audit |
| `old_doc_src_ctx -> automated_screening_only` | 168 | Pruned batch scan reconstruction, zero-change prose claim, or unexpanded issue-title range |
| `old_doc_src_ctx -> full_source_in_context_read` | 1,006 | Confirmed genuine full source-in-context read (Pass 3.5 blind review or recovered Greek helper range) |
| `old_doc_src_ctx -> targeted_evidence` | 1,149 | Reclassified from undifferentiated prior bucket into targeted note / mapping / isolated wording check |
| `old_p3_eng_only -> english_only_read` | 243 | Retained as Pass 3 standalone English-only read |
| `old_p3_eng_only -> full_source_in_context_read` | 970 | Upgraded via recovered Greek Pass 1 helper full-context chapter reads |

### Pruned Batch Scans, Zero-Change Prose Claims & Issue-Title Ranges

- `claude_readme_range_or_open_item_scope`: **95** rows removed from per-verse credit
- `claude_zero_change_books_no_per_verse_log`: **53** rows removed from per-verse credit
- `pass1_all_151_psalm_superscriptions_batch_sweep`: **151** rows removed from per-verse credit
- `pass35_grc_exp1_103_psalter_batch_scan`: **103** rows removed from per-verse credit
- `pass35_grc_exp2_67_epicheir_batch_scan`: **67** rows removed from per-verse credit

## 4. Unique Native Verses by Pass & Evidence Class

| Pass | Evidence Class | Unique Native Verses |
|---|---|---:|
| `followup_mapping_audit` | `targeted_evidence` | 375 |
| `followup_note_audit` | `targeted_evidence` | 13 |
| `pass1_grc_fidelity` | `targeted_evidence` | 776 |
| `pass1_grc_nt_helper` | `full_source_in_context_read` | 4,778 |
| `pass1_grc_nt_helper_bracketed` | `targeted_evidence` | 18 |
| `pass1_grc_nt_helper_notes` | `targeted_evidence` | 15 |
| `pass1_grc_ot_helper` | `full_source_in_context_read` | 3,892 |
| `pass2_grc_peer` | `targeted_evidence` | 295 |
| `pass35_response_grc_peer` | `targeted_evidence` | 15 |
| `pass3_bounceback_grc_peer` | `targeted_evidence` | 6 |
| `pass4_reconciliation` | `targeted_evidence` | 117 |
| `pre_stage2_claude_fidelity` | `targeted_evidence` | 1,429 |
| `stage2_pass35_blind_ai_peer_review` | `full_source_in_context_read` | 40 |
| `stage2_pass3_standalone_flow` | `english_only_read` | 1,353 |

## 5. Unassigned Aggregate Claims & Batch Scans (`0` Verses Assigned)

- **`UNATTR-CLAUDE-01`** (`reviews/2026-11-24-ME-GREEK-FIDELITY/README.md & wording-changes.jsonl`, claimed `34,150`): Global reading prose claim with no per-verse log for unedited verses (incl. 53 zero-change verses in Philemon/2 John/3 John, now independently recovered via helper_nt_notes.md) plus 351 edition/division-wide automated consistency batch rows.
- **`UNATTR-P1-NT-JOHN-EXCESS`** (`helper_nt_notes.md#L28-L31 & pass1_coverage.json`, claimed `82`): Helper NT subtotals sum to 4,860 vs 4,778 actual distinct native rows (+82 localized entirely in John: reported 515 vs 433 actual). Earlier 4,839 summary sits +61 above 4,778 named rows (+51 above 4,788 named+18 bracketed) and -21 below 4,860. All unsupported excess remains strictly unassigned.
- **`UNATTR-P1-PSALM-SUPERSCRIPTIONS`** (`reviews/2026-11-24-literal-smooth/pass1_coverage.json`, claimed `151`): Aggregate list label "All 151 Psalm superscriptions" without per-verse log; 9 full Psalms are recovered via helper_ot_notes.md and specifically cited superscriptions (Ps 121:1, 123:1, 130:1, 132:1, etc.) are credited individually.
- **`UNATTR-P35-EXP-1-2`** (`reviews/2026-11-24-literal-smooth/pass35_ai_peer_review_response.jsonl#GRC-P35-EXP-1,GRC-P35-EXP-2`, claimed `170`): Batch pattern-expansion scans (103 Psalter person-dative superscriptions + 67 OT epi+cheir matches) reporting aggregate counts without enumerating unedited matches; only explicitly named fixes/anchors (14 verses) receive targeted_evidence credit.

## 6. Complete Per-Book 5-Tier Evidence Breakdown (70 Books, Summing to `34,198`)

| # | Book | Test. | Ch | `source_total` | `full_src_ctx` *(fin / hist)* | `targeted` *(fin / hist)* | `tgt_note` | `tgt_map` | `tgt_word` | `tgt_ov2+` | `eng_only` | `auto_only` | `insuff_ev` | Ed. `verified` / `disputed` *(sep.)* |
|---:|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Genesis | OT | 50 | 1,531 | 186 (176/10) | 49 (49/0) | 15 | 2 | 40 | 8 | 3 | 1,293 | 0 | 1,529 / 2 |
| 2 | Exodus | OT | 40 | 1,163 | 202 (190/12) | 54 (54/0) | 18 | 2 | 44 | 10 | 0 | 907 | 0 | 1,163 / 0 |
| 3 | Leviticus | OT | 27 | 859 | 34 (34/0) | 92 (92/0) | 18 | 17 | 76 | 15 | 93 | 640 | 0 | 859 / 0 |
| 4 | Numbers | OT | 36 | 1,288 | 123 (119/4) | 65 (65/0) | 17 | 16 | 51 | 16 | 2 | 1,098 | 0 | 1,288 / 0 |
| 5 | Deuteronomy | OT | 34 | 958 | 180 (180/0) | 37 (37/0) | 12 | 0 | 27 | 2 | 0 | 741 | 0 | 958 / 0 |
| 6 | Joshua | OT | 24 | 643 | 33 (33/0) | 10 (10/0) | 6 | 0 | 9 | 5 | 0 | 600 | 0 | 643 / 0 |
| 7 | Judges | OT | 21 | 618 | 31 (31/0) | 16 (16/0) | 3 | 0 | 15 | 2 | 0 | 571 | 0 | 618 / 0 |
| 8 | Ruth | OT | 4 | 85 | 0 (0/0) | 5 (5/0) | 1 | 0 | 5 | 1 | 21 | 59 | 0 | 85 / 0 |
| 9 | 1 Samuel | OT | 31 | 772 | 65 (65/0) | 33 (33/0) | 8 | 0 | 28 | 3 | 0 | 674 | 0 | 772 / 0 |
| 10 | 2 Samuel | OT | 24 | 694 | 31 (31/0) | 25 (25/0) | 5 | 0 | 23 | 3 | 0 | 638 | 0 | 694 / 0 |
| 11 | 1 Kings | OT | 22 | 755 | 64 (61/3) | 31 (31/0) | 14 | 11 | 17 | 10 | 0 | 660 | 0 | 755 / 0 |
| 12 | 2 Kings | OT | 25 | 719 | 1 (1/0) | 30 (30/0) | 5 | 2 | 25 | 2 | 0 | 688 | 0 | 719 / 0 |
| 13 | 1 Chronicles | OT | 29 | 930 | 1 (1/0) | 48 (47/1) | 11 | 5 | 43 | 9 | 2 | 879 | 0 | 919 / 11 |
| 14 | 2 Chronicles | OT | 36 | 820 | 1 (1/0) | 26 (26/0) | 9 | 0 | 23 | 6 | 0 | 793 | 0 | 820 / 0 |
| 15 | Ezra | OT | 10 | 280 | 1 (0/1) | 5 (5/0) | 2 | 0 | 5 | 2 | 0 | 274 | 0 | 280 / 0 |
| 16 | Nehemiah | OT | 13 | 388 | 0 (0/0) | 23 (23/0) | 11 | 7 | 20 | 12 | 0 | 365 | 0 | 388 / 0 |
| 17 | Esther | OT | 10 | 164 | 164 (164/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 164 / 0 |
| 18 | 1 Maccabees | OT | 16 | 924 | 134 (129/5) | 35 (35/0) | 4 | 0 | 32 | 1 | 0 | 755 | 0 | 924 / 0 |
| 19 | 2 Maccabees | OT | 15 | 555 | 42 (42/0) | 12 (12/0) | 3 | 0 | 12 | 3 | 0 | 501 | 0 | 555 / 0 |
| 20 | Job | OT | 42 | 1,068 | 237 (227/10) | 31 (31/0) | 6 | 0 | 31 | 6 | 15 | 785 | 0 | 1,067 / 1 |
| 21 | Psalms | OT | 151 | 2,533 | 141 (140/1) | 74 (74/0) | 28 | 6 | 56 | 15 | 6 | 2,312 | 0 | 2,429 / 104 |
| 22 | Proverbs | OT | 31 | 889 | 271 (271/0) | 16 (16/0) | 8 | 4 | 9 | 5 | 0 | 602 | 0 | 889 / 0 |
| 23 | Ecclesiastes | OT | 12 | 222 | 54 (54/0) | 12 (11/1) | 2 | 0 | 10 | 0 | 1 | 155 | 0 | 222 / 0 |
| 24 | Song of Songs | OT | 8 | 117 | 117 (117/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 117 / 0 |
| 25 | Lamentations | OT | 5 | 150 | 1 (1/0) | 9 (9/0) | 2 | 0 | 9 | 2 | 0 | 140 | 0 | 149 / 1 |
| 26 | Wisdom of Solomon | OT | 19 | 436 | 71 (71/0) | 21 (21/0) | 7 | 15 | 2 | 3 | 0 | 344 | 0 | 436 / 0 |
| 27 | Sirach | OT | 51 | 1,357 | 274 (269/5) | 58 (58/0) | 17 | 27 | 28 | 12 | 2 | 1,023 | 0 | 1,357 / 0 |
| 28 | Isaiah | OT | 66 | 1,289 | 221 (221/0) | 50 (50/0) | 18 | 0 | 38 | 6 | 7 | 1,011 | 0 | 1,282 / 7 |
| 29 | Jeremiah | OT | 52 | 1,296 | 356 (351/5) | 43 (43/0) | 12 | 5 | 32 | 6 | 2 | 895 | 0 | 1,296 / 0 |
| 30 | Ezekiel | OT | 48 | 1,265 | 281 (271/10) | 34 (34/0) | 10 | 4 | 29 | 9 | 7 | 943 | 0 | 1,256 / 9 |
| 31 | Daniel | OT | 12 | 420 | 265 (265/0) | 14 (13/1) | 4 | 1 | 11 | 2 | 54 | 87 | 0 | 418 / 2 |
| 32 | Hosea | OT | 14 | 197 | 45 (45/0) | 5 (5/0) | 0 | 0 | 5 | 0 | 0 | 147 | 0 | 197 / 0 |
| 33 | Joel | OT | 4 | 73 | 32 (32/0) | 1 (1/0) | 0 | 0 | 1 | 0 | 0 | 40 | 0 | 73 / 0 |
| 34 | Amos | OT | 9 | 146 | 42 (42/0) | 7 (7/0) | 3 | 2 | 3 | 1 | 0 | 97 | 0 | 146 / 0 |
| 35 | Obadiah | OT | 1 | 21 | 0 (0/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 21 | 0 | 21 / 0 |
| 36 | Jonah | OT | 4 | 48 | 48 (48/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 48 / 0 |
| 37 | Micah | OT | 7 | 105 | 14 (14/0) | 2 (2/0) | 1 | 0 | 2 | 1 | 0 | 89 | 0 | 103 / 2 |
| 38 | Nahum | OT | 3 | 47 | 0 (0/0) | 2 (2/0) | 1 | 0 | 2 | 1 | 0 | 45 | 0 | 47 / 0 |
| 39 | Habakkuk | OT | 3 | 56 | 39 (39/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 56 / 0 |
| 40 | Zephaniah | OT | 3 | 53 | 0 (0/0) | 1 (1/0) | 0 | 0 | 1 | 0 | 0 | 52 | 0 | 53 / 0 |
| 41 | Haggai | OT | 2 | 38 | 0 (0/0) | 1 (1/0) | 0 | 0 | 1 | 0 | 0 | 37 | 0 | 38 / 0 |
| 42 | Zechariah | OT | 14 | 211 | 86 (86/0) | 11 (11/0) | 5 | 0 | 9 | 3 | 0 | 114 | 0 | 209 / 2 |
| 43 | Malachi | OT | 3 | 55 | 24 (24/0) | 3 (3/0) | 1 | 0 | 2 | 0 | 0 | 28 | 0 | 55 / 0 |
| 44 | Matthew | NT | 28 | 1,071 | 526 (526/0) | 43 (43/0) | 18 | 3 | 30 | 5 | 26 | 476 | 0 | 1,071 / 0 |
| 45 | Mark | NT | 16 | 678 | 446 (441/5) | 10 (10/0) | 6 | 2 | 7 | 3 | 0 | 222 | 0 | 678 / 0 |
| 46 | Luke | NT | 24 | 1,151 | 479 (469/10) | 27 (27/0) | 12 | 1 | 19 | 4 | 0 | 645 | 0 | 1,150 / 1 |
| 47 | John | NT | 21 | 879 | 435 (435/0) | 28 (28/0) | 13 | 1 | 17 | 2 | 2 | 414 | 0 | 876 / 3 |
| 48 | Acts | NT | 28 | 1,006 | 353 (353/0) | 38 (38/0) | 12 | 2 | 30 | 4 | 0 | 615 | 0 | 1,002 / 4 |
| 49 | Romans | NT | 16 | 436 | 372 (372/0) | 3 (3/0) | 1 | 0 | 2 | 0 | 0 | 61 | 0 | 429 / 7 |
| 50 | 1 Corinthians | NT | 16 | 437 | 247 (237/10) | 10 (10/0) | 4 | 0 | 7 | 1 | 0 | 180 | 0 | 437 / 0 |
| 51 | 2 Corinthians | NT | 13 | 256 | 78 (78/0) | 5 (5/0) | 0 | 0 | 5 | 0 | 0 | 173 | 0 | 255 / 1 |
| 52 | Galatians | NT | 6 | 149 | 149 (149/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 148 / 1 |
| 53 | Ephesians | NT | 6 | 155 | 155 (155/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 155 / 0 |
| 54 | Philippians | NT | 4 | 104 | 104 (104/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 104 / 0 |
| 55 | Colossians | NT | 4 | 95 | 95 (95/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 95 / 0 |
| 56 | 1 Thessalonians | NT | 5 | 89 | 89 (89/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 89 / 0 |
| 57 | 2 Thessalonians | NT | 3 | 47 | 47 (47/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 47 / 0 |
| 58 | 1 Timothy | NT | 6 | 113 | 113 (113/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 113 / 0 |
| 59 | 2 Timothy | NT | 4 | 83 | 83 (83/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 82 / 1 |
| 60 | Titus | NT | 3 | 46 | 46 (46/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 46 / 0 |
| 61 | Philemon | NT | 1 | 25 | 25 (25/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 / 0 |
| 62 | Hebrews | NT | 13 | 303 | 250 (250/0) | 2 (2/0) | 1 | 0 | 2 | 1 | 0 | 51 | 0 | 302 / 1 |
| 63 | James | NT | 5 | 108 | 108 (108/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 107 / 1 |
| 64 | 1 Peter | NT | 5 | 105 | 105 (105/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 105 / 0 |
| 65 | 2 Peter | NT | 3 | 61 | 61 (61/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 61 / 0 |
| 66 | 1 John | NT | 5 | 105 | 105 (105/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 105 / 0 |
| 67 | 2 John | NT | 1 | 13 | 13 (13/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 / 0 |
| 68 | 3 John | NT | 1 | 15 | 15 (15/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 / 0 |
| 69 | Jude | NT | 1 | 25 | 25 (25/0) | 0 (0/0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 / 0 |
| 70 | Revelation | NT | 22 | 405 | 257 (252/5) | 20 (20/0) | 9 | 0 | 13 | 2 | 0 | 128 | 0 | 404 / 1 |
| — | **TOTAL (70 books)** | — | **1,291** | **34,198** | **8,693** (8,597/96) | **1,177** (1,174/3) | **363** | **135** | **908** | **204** | **243** | **24,085** | **0** | **34,036 / 162** |
