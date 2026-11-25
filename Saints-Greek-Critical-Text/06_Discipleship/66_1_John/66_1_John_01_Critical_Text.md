# 1 John 01 — Saints Greek Critical Text

**Division:** `06_Discipleship` · **Language:** `Greek` · **Engine:** `Textual Analysis Brain (Claude-designed · internal evidence · offline)` · **Updated:** `2026-11-25T00:07:49Z`

**Versification:** Septuagint numbering as in Brenton/eBible (the Saints.Bible numbering) for the OT; standard numbering for the NT. Witnesses that number differently (e.g. Swete in Joel and Malachi) are re-aligned by content. Proverbs is numbered as Saints.Bible numbers it: Hebrew chapter and verse numbers in the Greek order (24:1–22e, 30:1–14, 24:23–34, 30:15–33, 31:1–9, 25–29, 31:10–31), not as the Brenton e-text runs 30:1–31:9 on as 24:22–62. Numbering anchor for this chapter: `SBLGNT`. Spelling and punctuation follow `SBLGNT` where it attests the adopted reading.

**Sigla in the text:** `⟦ ⟧` = verse absent from (or bracketed by) witnesses that outweigh those containing it — printed for reference, probably not original. `(…)` before a Hebrew word = ketiv, followed by the qere.

---

## Section I — Admitted Witnesses & Gatekeeper Quarantine Declaration

### Admitted Collation Witnesses (Open-Source Tiers 1–4)
| Siglum | Witness Title | Tier | Weight | License | Text-Type |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **SRGNT** | Statistical Restoration Greek New Testament (CNTR 2022) | Tier 1 | `0.95` | CC BY 4.0 | Earliest-Manuscript Statistical Critical Edition |
| **SBLGNT** | SBL Greek New Testament & Apparatus (Holmes 2010) | Tier 1 | `0.94` | CC BY 4.0 | Reasoned Eclectic Critical Edition |
| **BHP** | Bunning Heuristic Prototype GNT (CNTR) | Tier 1 | `0.88` | CC BY 4.0 | Algorithmic Alexandrian/Early Witness Reconstruction |
| **Nestle1904** | Eberhard Nestle Greek New Testament (1904) | Tier 2 | `0.90` | Public Domain | Tischendorf / Westcott-Hort / Weymouth Consensus |
| **RP2018 (Byz)** | Robinson–Pierpont Byzantine Textform (2018) | Tier 3 | `0.72` | Public Domain / Unlicense | Byzantine / Majority Ecclesiastical Tradition |
| **TR (KJTR)** | Textus Receptus (CNTR KJTR Collation) | Tier 3 | `0.60` | CC BY 4.0 | Reformation Textus Receptus Tradition |
| **B (03)** | Codex Vaticanus Direct Transcription (CNTR Early MSS) | Tier 4 | `0.98` | CC BY-SA 4.0 | Premier Alexandrian Uncial |
| **א (01)** | Codex Sinaiticus Direct Transcription (CNTR Early MSS) | Tier 4 | `0.96` | CC BY-SA 4.0 | Alexandrian / Western Mixed Uncial |

### Apparatus Witnesses (Additional Editions & Direct Manuscripts — recorded, not voting)
Collated against the adopted text and listed in the apparatus wherever they differ in substance; they do not vote on the text.

| Siglum | Witness Title | Tier | License | Text-Type |
| :--- | :--- | :---: | :--- | :--- |
| **NA28 (TAGNT)** | Nestle–Aland 28th Edition Word-Stream (STEPBible TAGNT CC BY 4.0) | Tier 1 | CC BY 4.0 (STEPBible.org / Tyndale House) | Modern Standard Eclectic Critical Edition (NA28) |
| **THGNT** | Tyndale House Greek New Testament (STEPBible TAGNT CC BY 4.0) | Tier 1 | CC BY 4.0 (STEPBible.org / Tyndale House Cambridge) | Documentarily-Grounded Modern Critical Edition (THGNT) |
| **WH1881** | Westcott & Hort Greek New Testament (1881, CNTR Unicode) | Tier 2 | Public Domain / CC BY-SA 4.0 | Neutral / Alexandrian Critical Edition (Westcott–Hort) |
| **Tisch8** | Tischendorf 8th Edition Greek New Testament (1869–1872, OSIS v2.8) | Tier 2 | Public Domain | Sinaiticus-Weighted Critical Edition (Tischendorf 8th) |
| **TCGNT (Byz)** | The Text-Critical Greek New Testament: Byzantine Text (Robert Adam Boyd) | Tier 3 | Public Domain | Byzantine Majority Manuscript Collation (TuT / ECM / Hoskier) |
| **PT1904 (Byz)** | 1904 Ecumenical Patriarchal Greek New Testament (Basileios Antoniades) | Tier 3 | Public Domain | Constantinopolitan Lectionary & Byzantine Ecclesiastical Majority |
| **TR-Scrivener (1894)** | Scrivener Textus Receptus (Cambridge 1894 Polytonic Edition) | Tier 3 | Public Domain / GPL-3.0 | Beza 1598 / KJV-Underlying Textus Receptus |
| **TR-Boyd (Elz/Scr/Steph)** | Polytonic Textus Receptus (Stephanus 1550 / Elzevir 1624 / Scrivener 1894) | Tier 3 | Public Domain | Reformation Printed Textus Receptus |
| **TR-Stephanus (1550)** | Stephanus Editio Regia Textus Receptus (Paris 1550, CNTR Unicode) | Tier 3 | Public Domain / CC BY-SA 4.0 | Reformation Printed Textus Receptus (Stephanus 1550) |
| **TR-Elzevir (1624)** | Elzevir Textus Receptus (1624 Leiden Edition, Robinson .UEL) | Tier 3 | Public Domain | Classic Elzevir Textus Receptus |
| **A (02)** | Codex Alexandrinus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Byzantine (Gospels) / Premier Alexandrian (Acts, Epistles, Revelation) |
| **C (04)** | Codex Ephraemi Rescriptus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Mixed Alexandrian / Early Eclectic Palimpsest |
| **Ψ (044)** | Codex Athous Laurensis (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 (INTF / IGNTP) | Alexandrian-Allied Uncial (Mark, Gospels, Acts, Catholics, Paul) |

### Disregarded / Quarantined Sources (Excluded by AI Gatekeeper)
| Source | Status | Reason Excluded from Open Critical Text |
| :--- | :---: | :--- |
| Pickering-f35 | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-ND (Tier 5 — Owner-Authorized Apparatus)) — held in local Studio only; excluded from public open-licence exports. |
| Tregelles (1879) | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-SA 3.0 (Owner-Authorized Apparatus Witness)) — held in local Studio only; excluded from public open-licence exports. |

---

## Section II — Continuous Greek Critical Text

**1** Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς—
**2** καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν—
**3** ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
**4** καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
**5** Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
**6** ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
**7** ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
**8** ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
**9** ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
**10** ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### 1 John 1:1
- **Apparatus:** `ἑωράκαμεν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εορακαμεν** B (03) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Ὃ` over `ο`, `ὃ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπʼ` over `απ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀρχῆς,` over `αρχησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκηκόαμεν,` over `ακηκοαμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀφθαλμοῖς` over `οφθαλμοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν,` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐθεασάμεθα` over `εθεασαμεθα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἱ` over `αι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χεῖρες` over `χειρεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐψηλάφησαν,` over `εψηλαφησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγου` over `λογου`, `Λόγου` (B (03), Nestle1904, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωῆς—` over `ζωησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:2
- **Apparatus:** `ἑωράκαμεν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ο εορακαμεν** B (03) ; **εορακαμεν** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ`, `(Καὶ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωὴ` over `ζωη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐφανερώθη,` over `εφανερωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μαρτυροῦμεν` over `μαρτυρουμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπαγγέλλομεν` over `απαγγελλομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωὴν` over `ζωην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰώνιον` over `αιωνιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἥτις` over `ητισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατέρα` over `πατερα`, `Πατέρα,`, `Πατέρα` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐφανερώθη` over `εφανερωθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν—` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:3
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ακηκοαμεν και** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἑωράκαμεν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εορακαμεν** B (03) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀκηκόαμεν ἀπαγγέλλομεν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **απαγγελλομεν ι** א (01) *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `καὶ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἔχητε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εχηται** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** C (04)
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **υμων** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὃ` over `ο`, `Ὃ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν,` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵνα` over `ινα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμεῖς` over `υμεισ`, `υμισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `κοινωνίαν` over `κοινωνιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεθʼ` over `μεθ`, `μεθ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ἡμῶν·` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κοινωνία` over `κοινωνια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμετέρα` over `ημετερα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετὰ` over `μετα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατρὸς` over `πατροσ`, `Πατρὸς,`, `Πατρὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετὰ` over `μετα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `υἱοῦ` over `υιου`, `Υἱοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ·` over `χυ̅`, `χριστοῦ·` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### 1 John 1:4
- **Apparatus:** `ἡμεῖς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **ὑμῖν** RP2018 (Byz) TR (KJTR) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἡμῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ὑμῶν** TR (KJTR) A (02) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῦτα` over `ταυτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γράφομεν` over `γραφομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵνα` over `ινα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαρὰ` over `χαρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ᾖ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πεπληρωμένη.` over `πεπληρωμενη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:5
- **Apparatus:** `ἔστιν αὕτη` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) C (04) NA28 (TAGNT) TCGNT (Byz) THGNT Tisch8 WH1881 Ψ (044) **]** **αὕτη ἔστιν** TR (KJTR) A (02) PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἀγγελία` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Scrivener (1894) Tisch8 WH1881 **]** **απαγγελιασ** א (01) ; **επαγγελια** C (04) PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Stephanus (1550) ; **αγαπη της επαγγελιας** Ψ (044) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀναγγέλλομεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αναγελλομεν** A (02) ; **αναγγελλομεν εν** C (04)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εν** C (04)
- **Apparatus:** `om.` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Ψ (044) **]** **ουκ εστιν** B (03) WH1881 *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'οὐκ ἔστιν' together form one word-order variant (B (03) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `οὐκ ἔστιν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Ψ (044) **]** **om.** B (03) WH1881 *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'οὐκ ἔστιν' together form one word-order variant (B (03) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἣν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκηκόαμεν` over `ακηκοαμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπʼ` over `απ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀναγγέλλομεν` over `αναγγελλομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν,` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸς` over `θσ̅`, `Θεὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `φῶς` over `φωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν`, `ἐστίν,` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σκοτία` over `σκοτια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῷ` over `αυτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐδεμία.` over `ουδεμια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:6
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **γαρ** A (02)
- **Apparatus:** `τῷ σκότει` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τη σκοτια** Ψ (044)
- **Apparatus:** `ποιοῦμεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ποιωμεν** A (02)
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴπωμεν` over `ειπωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κοινωνίαν` over `κοινωνιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχομεν` over `εχομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετʼ` over `μετ`, `μετ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σκότει` over `σκοτει`, `σκοτι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `περιπατῶμεν,` over `περιπατωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ψευδόμεθα` over `ψευδομεθα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιοῦμεν` over `ποιουμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλήθειαν·` over `αληθειαν`, `αληθιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### 1 John 1:7
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** NA28 (TAGNT) Ψ (044)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **χριστοῦ** RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *scribal tendency: expansion of a sacred name or title:* 'χριστοῦ' is a typical scribal expansion of a sacred name or title; such additions are more likely than omissions.
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φωτὶ` over `φωτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περιπατῶμεν` over `περιπατωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτός` over `αυτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φωτί,` over `φωτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κοινωνίαν` over `κοινωνιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχομεν` over `εχομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετʼ` over `μετ`, `μετ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ἀλλήλων` over `αλληλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἷμα` over `αιμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `υἱοῦ` over `υιου`, `υυ̅`, `Υἱοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθαρίζει` over `καθαριζει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμᾶς` over `ημασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάσης` over `πασησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίας.` over `αμαρτιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:8
- **Apparatus:** `ἑαυτοὺς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εαυτοισ** C (04)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ἐν ἡμῖν** A (02) C (04)
- **Apparatus:** `ἐν ἡμῖν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** A (02) C (04)
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴπωμεν` over `ειπωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίαν` over `αμαρτιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχομεν,` over `εχομεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτοὺς` over `εαυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλανῶμεν` over `πλανωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλήθεια` over `αληθεια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν.` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:9
- **Apparatus:** `ἐστιν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ημων** א (01) C (04) Ψ (044) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `καθαρίσῃ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **καθαρισει** A (02)
- **Apparatus:** `ἡμᾶς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** C (04)
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁμολογῶμεν` over `ομολογωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίας` over `αμαρτιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν,` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πιστός` over `πιστοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίκαιος` over `δικαιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵνα` over `ινα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀφῇ` over `αφη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίας` over `αμαρτιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθαρίσῃ` over `καθαριση` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμᾶς` over `ημασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάσης` over `πασησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδικίας.` over `αδικιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### 1 John 1:10
- **Apparatus:** `οὐχ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ουκ** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἡμῖν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υμιν** Ψ (044)
- *Disregarded Surface Variant:* kept `ἐὰν` over `εαν`, `Ἐὰν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴπωμεν` over `ειπωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμαρτήκαμεν,` over `ημαρτηκαμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ψεύστην` over `ψευστην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιοῦμεν` over `ποιουμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον`, `αὐτόν,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγος` over `λογοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν.` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς—
  - `SRGNT`: Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς–
  - `SBLGNT`: Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς—
  - `BHP`: ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς–
  - `Nestle1904`: Ὃ ἦν ἀπ’ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ Λόγου τῆς ζωῆς,—
  - `RP2018 (Byz)`: Ὃ ἦν ἀπ’ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς.
  - `TR (KJTR)`: Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ Λόγου τῆς ζωῆς·
  - `B (03)`: ο ην απ αρχησ ο ακηκοαμεν ο εορακαμεν τοισ οφθαλμοισ ημων ο εθεασαμεθα και αι χειρεσ ημων εψηλαφησαν περι του λογου τησ ζωησ
  - `א (01)`: ο ην απ αρχησ ο ακηκοαμεν ο εωρακαμεν τοισ οφθαλμοισ ημων ο εθεασαμεθα και αι χειρεσ ημων εψηλαφησαν περι του λογου τησ ζωησ
  - `NA28 (TAGNT)`: Ὃ ἦν ἀπ᾽ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς·
  - `THGNT`: Ὃ ἦν ἀπ᾽ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς·
  - `WH1881`: Ὃ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς,–
  - `Tisch8`: Ὃ ἦν ἀπ’ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς
  - `TCGNT (Byz)`: Ὃ ἦν ἀπ᾽ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς—
  - `PT1904 (Byz)`: Ὃ ἦν ἀπ᾽ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν, περὶ τοῦ λόγου τῆς ζωῆς· —
  - `TR-Scrivener (1894)`: Ὃ ἦν ἀπ᾽ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς
  - `TR-Boyd (Elz/Scr/Steph)`: Ὃ ἦν ἀπ᾿ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς.
  - `TR-Stephanus (1550)`: Ὁ ἦν ἀπʼ ἀρχῆς, ὃ ἀκηκόαμεν, ὃ ἑωράκαμεν τοῖς ὀφθαλμοῖς ἡμῶν, ὃ ἐθεασάμεθα, καὶ αἱ χεῖρες ἡμῶν ἐψηλάφησαν περὶ τοῦ λόγου τῆς ζωῆς,
  - `TR-Elzevir (1624)`: ο ην απ αρχης ο ακηκοαμεν ο εωρακαμεν τοις οφθαλμοις ημων ο εθεασαμεθα και αι χειρες ημων εψηλαφησαν περι του λογου της ζωης
  - `A (02)`: ο ην απ αρχησ ο ακηκοαμεν ο εωρακαμεν τοισ οφθαλμοισ ημων ο εθεασαμεθα και αι χειρεσ ημων εψηλαφησαν περι του λογου τησ ζωησ
  - `C (04)`: ο ην απ αρχησ ο ακηκοαμεν ο εωρακαμεν …
  - `Ψ (044)`: ο ην απ αρχης ο ακηκοαμεν ο εωρακαμεν τοις οφθαλμοις ημων ο εθεασαμεθα και αι χειρες ημων εψηλαφησαν περι του λογου της ζωης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἑωράκαμεν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over εορακαμεν (B (03)). Also normalised 22 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 2 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν—
  - `SRGNT`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν, τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν Πατέρα, καὶ ἐφανερώθη ἡμῖν–
  - `SBLGNT`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν—
  - `BHP`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν, τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν Πατέρα, καὶ ἐφανερώθη ἡμῖν–
  - `Nestle1904`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν Πατέρα καὶ ἐφανερώθη ἡμῖν,—
  - `RP2018 (Byz)`: Καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα, καὶ ἐφανερώθη ἡμῖν.
  - `TR (KJTR)`: (Καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν Πατέρα, καὶ ἐφανερώθη ἡμῖν·)
  - `B (03)`: και η ζωη εφανερωθη και ο εορακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητισ ην προσ τον πατερα και εφανερωθη ημιν
  - `א (01)`: και η ζωη εφανερωθη και εωρακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητισ ην προσ τον πατερα και εφανερωθη ημιν
  - `NA28 (TAGNT)`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν·
  - `THGNT`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν·
  - `WH1881`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν,–
  - `Tisch8`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν
  - `TCGNT (Byz)`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν—
  - `PT1904 (Byz)`: καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν καὶ μαρτυροῦμεν καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα καὶ ἐφανερώθη ἡμῖν· —
  - `TR-Scrivener (1894)`: (καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα, καὶ ἐφανερώθη ἡμῖν)·
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἡ ζωὴ ἐφανερώθη, καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα, καὶ ἐφανερώθη ἡμῖν.
  - `TR-Stephanus (1550)`: (καὶ ἡ ζωὴ ἐφανερώθη· καὶ ἑωράκαμεν, καὶ μαρτυροῦμεν, καὶ ἀπαγγέλλομεν ὑμῖν τὴν ζωὴν τὴν αἰώνιον, ἥτις ἦν πρὸς τὸν πατέρα, καὶ ἐφανερώθη ἡμῖν·)
  - `TR-Elzevir (1624)`: και η ζωη εφανερωθη και εωρακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητις ην προς τον πατερα και εφανερωθη ημιν
  - `A (02)`: και η ζωη εφανερωθη και εορακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητισ ην προσ τον πρα̅ και εφανερωθη ημιν
  - `C (04)`: … εωρακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητισ ην προσ τον πρα̅ και εφανερωθη ημιν
  - `Ψ (044)`: και η ζωη εφανερωθη και εωρακαμεν και μαρτυρουμεν και απαγγελλομεν υμιν την ζωην την αιωνιον ητις ην προς τον πρα̅ και εφανερωθη ημιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἑωράκαμεν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over ο εορακαμεν (B (03)). Also normalised 22 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `94.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
  - `SRGNT`: ὃ ἑωράκαμεν, καὶ ἀκηκόαμεν, ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ Πατρὸς, καὶ μετὰ τοῦ Υἱοῦ αὐτοῦ, Ἰησοῦ Χριστοῦ.
  - `SBLGNT`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
  - `BHP`: ὃ ἑωράκαμεν, καὶ ἀκηκόαμεν, ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ Πατρὸς, καὶ μετὰ τοῦ Υἱοῦ αὐτοῦ, Ἰησοῦ Χριστοῦ.
  - `Nestle1904`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ’ ἡμῶν. καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ Πατρὸς καὶ μετὰ τοῦ Υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `RP2018 (Byz)`: Ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ’ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ χριστοῦ·
  - `TR (KJTR)`: Ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν: καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ Πατρὸς, καὶ μετὰ τοῦ Υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `B (03)`: ο εορακαμεν και ακηκοαμεν απαγγελλομεν και υμιν ινα και υμεισ κοινωνιαν εχητε μεθ ημων και η κοινωνια δε η ημετερα μετα του πατροσ και μετα του υιου αυτου ιυ̅ χυ̅
  - `א (01)`: ο ακηκοαμεν και εωρακαμεν και απαγγελλομεν ι και υμιν ινα και υμισ κοινωνιαν εχηται μεθ ημων και η κοινωνια δε η ημετερα υμων μετα του πατροσ και μετα του υιου αυτου ιυ̅ χυ̅
  - `NA28 (TAGNT)`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν καὶ ὑμῖν ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾽ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `THGNT`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν καὶ ὑμῖν ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾽ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `WH1881`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
  - `Tisch8`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν καὶ ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ’ ἡμῶν. καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `TCGNT (Byz)`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾽ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `PT1904 (Byz)`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾽ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `TR-Scrivener (1894)`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾽ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
  - `TR-Boyd (Elz/Scr/Steph)`: Ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθ᾿ ἡμῶν· καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ·
  - `TR-Stephanus (1550)`: ὃ ἑωράκαμεν καὶ ἀκηκόαμεν, ἀπαγγέλλομεν ὑμῖν, ἵνα καὶ ὑμεῖς κοινωνίαν ἔχητε μεθʼ ἡμῶν, καὶ ἡ κοινωνία δὲ ἡ ἡμετέρα μετὰ τοῦ πατρὸς καὶ μετὰ τοῦ υἱοῦ αὐτοῦ Ἰησοῦ Χριστοῦ.
  - `TR-Elzevir (1624)`: ο εωρακαμεν και ακηκοαμεν απαγγελλομεν υμιν ινα και υμεις κοινωνιαν εχητε μεθ ημων και η κοινωνια δε η ημετερα μετα του πατρος και μετα του υιου αυτου ιησου χριστου
  - `A (02)`: ο εωρακαμεν και ακηκοαμεν απαγγελλομεν και υμιν ινα και υμεισ κοινωνιαν εχητε μεθ ημων και η κοινωνια δε η ημετερα μετα του πρσ̅ και μετα του υυ̅ αυτου ιυ̅ χυ̅
  - `C (04)`: ο εωρακαμεν και ακηκοαμεν απαγγελλομεν και υμιν ινα και υμεισ κοινωνιαν εχητε μεθ ημων και η κοινωνια η ημετερα μετα του πρσ̅ και μετα του υιου αυτου ιυ̅ χυ̅
  - `Ψ (044)`: ο εωρακαμεν και ακηκοαμεν απαγγελλομεν και υμιν ινα και υμεις κοινωνιαν εχητε μεθ ημων και η κοινωνια δε η ημετερα μετα του πρς̅ και μετα του υυ̅ αυτου ιυ̅ χυ̅
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ακηκοαμεν και (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἑωράκαμεν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over εορακαμεν (B (03)). [Variation unit spanning several words] Adopted 'ἀκηκόαμεν ἀπαγγέλλομεν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απαγγελλομεν ι (א (01)). [Omission in some witnesses] Adopted 'καὶ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἔχητε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εχηται (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over υμων (א (01)). Reference apparatus (SBLGNT): καὶ WH Treg NA28 ] – RP Reference apparatus (SBLGNT): Ἰησοῦ WH Treg NA28 ] + Χριστοῦ RP Also normalised 25 orthographic/surface variation(s).
- *confidence:* Verse confidence 94% = product of 6 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `SRGNT`: Καὶ ταῦτα γράφομεν ἡμεῖς, ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `SBLGNT`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `BHP`: καὶ ταῦτα γράφομεν ἡμεῖς, ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `Nestle1904`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `RP2018 (Byz)`: καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `TR (KJTR)`: Καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ὑμῶν ᾖ πεπληρωμένη.
  - `B (03)`: και ταυτα γραφομεν ημεισ ινα η χαρα ημων η πεπληρωμενη
  - `א (01)`: και ταυτα γραφομεν ημεισ ινα η χαρα ημων η πεπληρωμενη
  - `NA28 (TAGNT)`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `THGNT`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `WH1881`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `Tisch8`: καὶ ταῦτα γράφομεν ἡμεῖς ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `TCGNT (Byz)`: καὶ ταῦτα γράφομεν ὑμῖν ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `PT1904 (Byz)`: καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `TR-Scrivener (1894)`: καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ὑμῶν ᾖ πεπληρωμένη.
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ὑμῶν ᾖ πεπληρωμένη.
  - `TR-Stephanus (1550)`: καὶ ταῦτα γράφομεν ὑμῖν, ἵνα ἡ χαρὰ ἡμῶν ᾖ πεπληρωμένη.
  - `TR-Elzevir (1624)`: και ταυτα γραφομεν υμιν ινα η χαρα υμων η πεπληρωμενη
  - `A (02)`: και ταυτα γραφομεν ημεισ ινα η χαρα υμων η πεπληρωμενη
  - `C (04)`: και ταυτα γραφομεν υμιν ινα η χαρα ημων η πεπληρωμενη
  - `Ψ (044)`: και ταυτα γραφομεν ημεις ινα η χαρα ημων η πεπληρωμενη
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἡμεῖς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ὑμῖν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἡμῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over ὑμῶν (TR (KJTR)). Also normalised 8 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `SRGNT`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστιν, καὶ σκοτία ἐν αὐτῷ, οὐκ ἔστιν οὐδεμία.
  - `SBLGNT`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `BHP`: καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστιν, καὶ σκοτία ἐν αὐτῷ, οὐκ ἔστιν οὐδεμία.
  - `Nestle1904`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ’ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `RP2018 (Byz)`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ’ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστίν, καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TR (KJTR)`: Καὶ αὕτη ἔστιν ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ, καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστιν, καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `B (03)`: και εστιν αυτη η αγγελια ην ακηκοαμεν απ αυτου και αναγγελλομεν υμιν οτι ο θσ̅ φωσ εστιν και σκοτια ουκ εστιν εν αυτω ουδεμια
  - `א (01)`: και εστιν αυτη η απαγγελιασ ην ακηκοαμεν απ αυτου και αναγγελλομεν υμιν οτι ο θσ̅ φωσ εστιν και σκοτια εν αυτω ουκ εστιν ουδεμια
  - `NA28 (TAGNT)`: καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ᾽ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `THGNT`: καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ᾽ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `WH1881`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστὶν καὶ σκοτία οὐκ ἔστιν ἐν αὐτῷ οὐδεμία.
  - `Tisch8`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ’ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ θεὸς φῶς ἐστιν καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TCGNT (Byz)`: Καὶ ἔστιν αὕτη ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ᾽ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστι καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `PT1904 (Byz)`: Καὶ αὕτη ἐστὶν ἡ ἐπ αγγελία ἣν ἀκηκόαμεν ἀπ᾽ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστι καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TR-Scrivener (1894)`: Καὶ αὕτη ἐστὶν ἡ ἀγγελία ἣν ἀκηκόαμεν ἀπ᾽ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστί, καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ αὕτη ἐστίν ἡ ἐπαγγελία ἣν ἀκηκόαμεν ἀπ᾿ αὐτοῦ καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστί, καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TR-Stephanus (1550)`: Καὶ αὕτη ἐστὶν ἡ ἐπαγγελία ἣν ἀκηκόαμεν ἀπʼ αὐτοῦ, καὶ ἀναγγέλλομεν ὑμῖν, ὅτι ὁ Θεὸς φῶς ἐστι, καὶ σκοτία ἐν αὐτῷ οὐκ ἔστιν οὐδεμία.
  - `TR-Elzevir (1624)`: και αυτη εστιν η επαγγελια ην ακηκοαμεν απ αυτου και αναγγελλομεν υμιν οτι ο θεος φως εστιν και σκοτια εν αυτω ουκ εστιν ουδεμια
  - `A (02)`: και αυτη εστιν η αγγελια ην ακηκοαμεν απ αυτου και αναγελλομεν υμιν οτι ο θσ̅ φωσ εστιν και σκοτια εν αυτω ουκ εστιν ουδεμια
  - `C (04)`: και εστιν αυτη η επαγγελια ην ακηκοαμεν απ αυτου και αναγγελλομεν εν υμιν οτι ο θσ̅ φωσ εστιν και σκοτια εν αυτω ουκ εστιν ουδεμια
  - `Ψ (044)`: και εστιν αυτη η αγαπη της επαγγελιας ην ακηκοαμεν απ αυτου και αναγγελλομεν υμιν οτι ο θς̅ φως εστιν και σκοτια εν αυτω ουκ εστιν ουδεμια
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἔστιν αὕτη' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over αὕτη ἔστιν (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἀγγελία' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απαγγελιασ (א (01)). [Addition / omission between witnesses] Adopted 'om.' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.07, confidence 99%) over ουκ εστιν (B (03)). [Variation unit spanning several words] Adopted 'οὐκ ἔστιν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `SRGNT`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν.
  - `SBLGNT`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `BHP`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν.
  - `Nestle1904`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ’ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `RP2018 (Byz)`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ’ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα, καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TR (KJTR)`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα, καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν:
  - `B (03)`: εαν ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τω σκοτει περιπατωμεν ψευδομεθα και ου ποιουμεν την αληθειαν
  - `א (01)`: εαν ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τω σκοτι περιπατωμεν ψευδομεθα και ου ποιουμεν την αληθιαν
  - `NA28 (TAGNT)`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾽ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `THGNT`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾽ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `WH1881`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `Tisch8`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ’ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TCGNT (Byz)`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾽ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `PT1904 (Byz)`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾽ αὐτοῦ καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TR-Scrivener (1894)`: ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾽ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα, καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετ᾿ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα, καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TR-Stephanus (1550)`: Ἐὰν εἴπωμεν ὅτι κοινωνίαν ἔχομεν μετʼ αὐτοῦ, καὶ ἐν τῷ σκότει περιπατῶμεν, ψευδόμεθα, καὶ οὐ ποιοῦμεν τὴν ἀλήθειαν·
  - `TR-Elzevir (1624)`: εαν ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τω σκοτει περιπατωμεν ψευδομεθα και ου ποιουμεν την αληθειαν
  - `A (02)`: εαν γαρ ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τω σκοτει περιπατωμεν ψευδομεθα και ου ποιωμεν την αληθειαν
  - `C (04)`: εαν ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τω σκοτει περιπατωμεν ψευδομεθα και ου ποιουμεν την αληθειαν
  - `Ψ (044)`: εαν ειπωμεν οτι κοινωνιαν εχομεν μετ αυτου και εν τη σκοτια περιπατωμεν ψευδομεθα και ου ποιουμεν την αληθειαν
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 18 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Punctuation / spacing difference only).

### Verse 7 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `SRGNT`: Ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ τοῦ Υἱοῦ αὐτοῦ, καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `SBLGNT`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `BHP`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ τοῦ Υἱοῦ αὐτοῦ, καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `Nestle1904`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ’ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ Υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `RP2018 (Byz)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ’ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TR (KJTR)`: Ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ Υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `B (03)`: εαν δε εν τω φωτι περιπατωμεν ωσ αυτοσ εστιν εν τω φωτι κοινωνιαν εχομεν μετ αλληλων και το αιμα ιυ̅ του υιου αυτου καθαριζει ημασ απο πασησ αμαρτιασ
  - `א (01)`: εαν δε εν τω φωτι περιπατωμεν ωσ αυτοσ εστιν εν τω φωτι κοινωνιαν εχομεν μετ αλληλων και το αιμα ιυ̅ του υυ̅ αυτου καθαριζει ημασ απο πασησ αμαρτιασ
  - `NA28 (TAGNT)`: ἐὰν ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾽ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `THGNT`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾽ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `WH1881`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτὸς ἔστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετʼ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `Tisch8`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ’ ἀλλήλων καὶ τὸ αἷμα Ἰησοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TCGNT (Byz)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾽ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `PT1904 (Byz)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾽ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TR-Scrivener (1894)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾽ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TR-Boyd (Elz/Scr/Steph)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτί, κοινωνίαν ἔχομεν μετ᾿ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TR-Stephanus (1550)`: ἐὰν δὲ ἐν τῷ φωτὶ περιπατῶμεν, ὡς αὐτός ἐστιν ἐν τῷ φωτὶ, κοινωνίαν ἔχομεν μετʼ ἀλλήλων, καὶ τὸ αἷμα Ἰησοῦ Χριστοῦ τοῦ υἱοῦ αὐτοῦ καθαρίζει ἡμᾶς ἀπὸ πάσης ἁμαρτίας.
  - `TR-Elzevir (1624)`: εαν δε εν τω φωτι περιπατωμεν ως αυτος εστιν εν τω φωτι κοινωνιαν εχομεν μετ αλληλων και το αιμα ιησου χριστου του υιου αυτου καθαριζει ημας απο πασης αμαρτιας
  - `A (02)`: εαν δε εν τω φωτι περιπατωμεν ωσ αυτοσ εστιν εν τω φωτι κοινωνιαν εχομεν μετ … και το αιμα ιυ̅ χυ̅ του υιου αυτου καθαριζει ημασ απο πασησ αμαρτιασ
  - `C (04)`: εαν δε εν τω φωτι περιπατωμεν ωσ αυτοσ εστιν εν τω φωτι κοινωνιαν εχομεν μετ αλληλων και το αιμα ιυ̅ του υιου αυτου καθαριζει ημασ απο πασησ αμαρτιασ
  - `Ψ (044)`: εαν εν τω φωτι περιπατωμεν ως αυτος εστιν εν τω φωτι κοινωνιαν εχομεν μετ αλληλων και το αιμα ιυ̅ του υυ̅ αυτου καθαριζει ημας απο πασης αμαρτιας
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over χριστοῦ (RP2018 (Byz), TR (KJTR)). Also normalised 28 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 8 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `SRGNT`: Ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `SBLGNT`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `BHP`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `Nestle1904`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `RP2018 (Byz)`: Ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν, καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `TR (KJTR)`: Ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν, καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `B (03)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτουσ πλανωμεν και η αληθεια ουκ εστιν εν ημιν
  - `א (01)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτουσ πλανωμεν και η αληθεια ουκ εστιν εν ημιν
  - `NA28 (TAGNT)`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `THGNT`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `WH1881`: Ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `Tisch8`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `TCGNT (Byz)`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `PT1904 (Byz)`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Scrivener (1894)`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν, καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν, καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Stephanus (1550)`: ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν, ἑαυτοὺς πλανῶμεν, καὶ ἡ ἀλήθεια οὐκ ἔστιν ἐν ἡμῖν·
  - `TR-Elzevir (1624)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτους πλανωμεν και η αληθεια ουκ εστιν εν ημιν
  - `A (02)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτουσ πλανωμεν και η αληθεια εν ημιν ουκ εστιν
  - `C (04)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτοισ πλανωμεν και η αληθεια εν ημιν ουκ εστιν
  - `Ψ (044)`: εαν ειπωμεν οτι αμαρτιαν ουκ εχομεν εαυτους πλανωμεν και η αληθεια ουκ εστιν εν ημιν
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 15 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 9 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `SRGNT`: Ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος, ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `SBLGNT`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `BHP`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος, ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `Nestle1904`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος, ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `RP2018 (Byz)`: Ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `TR (KJTR)`: Ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `B (03)`: εαν ομολογωμεν τασ αμαρτιασ ημων πιστοσ εστιν και δικαιοσ ινα αφη ημιν τασ αμαρτιασ και καθαριση ημασ απο πασησ αδικιασ
  - `א (01)`: εαν ομολογωμεν τασ αμαρτιασ ημων πιστοσ και δικαιοσ ινα αφη ημιν τασ αμαρτιασ ημων και καθαριση ημασ απο πασησ αδικιασ
  - `NA28 (TAGNT)`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `THGNT`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `WH1881`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `Tisch8`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστιν καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `TCGNT (Byz)`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστι καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `PT1904 (Byz)`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστι καὶ δίκαιος, ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `TR-Scrivener (1894)`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστι καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστι καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας.
  - `TR-Stephanus (1550)`: ἐὰν ὁμολογῶμεν τὰς ἁμαρτίας ἡμῶν, πιστός ἐστι καὶ δίκαιος ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας, καὶ καθαρίσῃ ἡμᾶς ἀπὸ πάσης ἀδικίας·
  - `TR-Elzevir (1624)`: εαν ομολογωμεν τας αμαρτιας ημων πιστος εστιν και δικαιος ινα αφη ημιν τας αμαρτιας και καθαριση ημας απο πασης αδικιας
  - `A (02)`: εαν ομολογωμεν τασ αμαρτιασ ημων πιστοσ εστιν και δικαιοσ ινα αφη ημιν τασ αμαρτιασ και καθαρισει ημασ απο πασησ αδικειασ
  - `C (04)`: εαν ομολογωμεν τασ αμαρτιασ ημων πιστοσ εστιν και δικαιοσ ινα αφη ημιν τασ αμαρτιασ ημων και καθαριση απο πασησ αδικιασ
  - `Ψ (044)`: εαν ομολογωμεν τας αμαρτιας ημων πιστος εστιν και δικαιος ινα αφη ημιν τας αμαρτιας ημων και καθαριση ημας απο πασης αδικιας
- **Philological Rationale:** [Omission in some witnesses] Adopted 'ἐστιν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ημων (א (01)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `SRGNT`: Ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `SBLGNT`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `BHP`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `Nestle1904`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `RP2018 (Byz)`: Ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτόν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TR (KJTR)`: Ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `B (03)`: εαν ειπωμεν οτι ουχ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογοσ αυτου ουκ εστιν εν ημιν
  - `א (01)`: εαν ειπωμεν οτι ουκ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογοσ αυτου ουκ εστιν εν ημιν
  - `NA28 (TAGNT)`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτόν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `THGNT`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `WH1881`: Ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `Tisch8`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TCGNT (Byz)`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `PT1904 (Byz)`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτόν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Scrivener (1894)`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτόν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτόν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Stephanus (1550)`: ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν, ψεύστην ποιοῦμεν αὐτὸν, καὶ ὁ λόγος αὐτοῦ οὐκ ἔστιν ἐν ἡμῖν.
  - `TR-Elzevir (1624)`: εαν ειπωμεν οτι ουχ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογος αυτου ουκ εστιν εν ημιν
  - `A (02)`: εαν ειπωμεν οτι ουχ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογοσ αυτου ουκ εστιν εν ημιν
  - `C (04)`: εαν ειπωμεν οτι ουχ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογοσ αυτου ουκ εστιν εν ημιν
  - `Ψ (044)`: εαν ειπωμεν οτι ουχ ημαρτηκαμεν ψευστην ποιουμεν αυτον και ο λογος αυτου ουκ εστιν εν υμιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'οὐχ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ουκ (א (01)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
