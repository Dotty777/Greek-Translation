# Complete Old Testament — provisional reading draft

**43 books · 1,037 reading sections · 26,580 stored units · 7 attached continuation paragraphs · 12 November 2026**

The entire inherited Saints English Old Testament is assembled here. New focused Greek comparisons cover **7126 units**, including **121 unaccepted wording proposals**. The other **19,454 units remain inherited drafts without a new comparison in this batch**. This is a complete reading manuscript, not a completed fresh translation, exhaustive Greek audit or accepted release.

- [Read the Old Testament](Saints-English-Old-Testament.html) — standalone offline HTML with book selection, every reading section and expandable proposal comparisons. Download and open locally; all text remains available without JavaScript.
- [Plain-text edition](Saints-English-Old-Testament.txt) and [structured edition](old-testament.json).
- [Readable proposal ledger](PROPOSED-CHANGES.md), [machine-readable changes](changes.json), [manifest and book inventory](manifest.json), [validation](validation.json) and [file hashes](checksums.json).
- [Inherited source histories](source-history.json); these are preserved historical records, not newly certified review claims.

## Review boundaries

The working source remains Rahlfs–Hanhart 2006 subject to the book-specific histories; Daniel uses Old Greek. Fresh evidence resides in the dated OT batch directories listed in the manifest. Of the compared units, 1 have explicit token accounting (19 source tokens); these are a subset of the comparison total. Three working draft stages are recorded for 7029 units and may deliberately agree. These statuses do not imply critical-apparatus collation or resolved interpretation. Independent human Greek review, human read-aloud review, editorial acceptance and publication remain pending. No New Testament work is included or altered.

Each proposed wording change is visibly marked in the reader and plain text. The JSON retains the exact original unit, including display text and metadata, alongside its candidate. Genesis 1–11's accepted historical benchmark remains intact in the original book archive. Proposed corrections do not silently change that status.

## Exceptional units and reading order

Preserved: Psalm 151; all Greek Esther additions and six attached continuation paragraphs; the additional continuation at 1 Kings 8:53a; Daniel's separate chapter-five preface, furnace material, Susanna and Bel and the Dragon; Sirach's translator's prologue; all 34 Proverbs sections in the inherited reading order. Stored units and attached continuations are counted separately. Lettered/grouped references and meaningful gaps remain unchanged.

All 4,008 inherited display-text differences remain available in `inherited_unit`; escaped line breaks are rendered as line breaks. The 32 Genesis/Exodus units whose JSON recorded only a break count recover their exact breaks from matching inherited HTML; normalized wording is checked against the JSON before use. Existing poetry is preserved. Explicit AI-proposed lineation for retained wording is identified in its passage evidence; normalized words must still match the candidate exactly.

## Rebuild and verification

Run `python tools/build_ot_reading_draft.py --require-reviews` from the repository root. The script reads baseline `39a2bb990f252f9c867879f14942b200c4a86aa5`, verifies unchanged original Scripture and source histories, and overlays a review only when book, anchor, full reference, inherited text and candidate hash agree exactly. Duplicate or unmatched reviews stop the build.

The build checks source identity (allowing Git's Windows checkout line-ending conversion), every scoped passage ID/order, candidate hashes, all special units, full JSON round-trip and exact HTML/TXT text round-trips including continuations. Source hashes use canonical baseline Git bytes. It checks that the existing NT book directories and NT review editions have no tracked differences from the baseline. These are structural checks, not scholarly approval. Browser visual checks, if performed, are recorded separately.

The reader preserves each original anchor in JSON while using book-and-section-qualified DOM IDs to avoid cross-book collisions. Source locators remain in the inherited metadata; this compilation creates no new website routes. The flat source schemas for Leviticus, Numbers and Deuteronomy are grouped by their existing chapter order without changing any unit.

## Provenance and recovery

Baseline: `39a2bb990f252f9c867879f14942b200c4a86aa5`. The original book files are untouched. `manifest.json` records source SHA-256 hashes and review-input hashes; `checksums.json` covers all generated files except itself. To return to inherited wording, use each unit's `inherited_unit`, or omit this dated edition. `changes.json` records every before/after proposal. No staging or production deployment was made.

## Browser verification

[Browser checks](browser-validation.json) record 36 passing checks in local headless Chrome at desktop and phone widths, tied to the current reader's SHA-256. [Visual inspection](visual-verification.json) records the scope of the AI screenshot inspection. No human read-aloud, real-phone or assistive-technology review is implied. `verify-browser.cjs` reproduces the browser checks with configurable runtime paths.
