# Jude 01 — Saints Greek Critical Text

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
| **𝔓72** | Papyrus 72 — Bodmer VII–VIII (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Earliest Complete Witness to 1–2 Peter & Jude |
| **A (02)** | Codex Alexandrinus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Byzantine (Gospels) / Premier Alexandrian (Acts, Epistles, Revelation) |
| **C (04)** | Codex Ephraemi Rescriptus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Mixed Alexandrian / Early Eclectic Palimpsest |
| **33** | Minuscule 33 — Queen of the Cursives (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 | Premier Alexandrian Minuscule (Gospels, Acts, Epistles) |
| **Ψ (044)** | Codex Athous Laurensis (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 (INTF / IGNTP) | Alexandrian-Allied Uncial (Mark, Gospels, Acts, Catholics, Paul) |

### Disregarded / Quarantined Sources (Excluded by AI Gatekeeper)
| Source | Status | Reason Excluded from Open Critical Text |
| :--- | :---: | :--- |
| Pickering-f35 | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-ND (Tier 5 — Owner-Authorized Apparatus)) — held in local Studio only; excluded from public open-licence exports. |
| Tregelles (1879) | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-SA 3.0 (Owner-Authorized Apparatus Witness)) — held in local Studio only; excluded from public open-licence exports. |

---

## Section II — Continuous Greek Critical Text

**1** Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
**2** ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
**3** Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
**4** παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
**5** Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
**6** ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
**7** ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
**8** Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
**9** ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν· Ἐπιτιμήσαι σοι κύριος.
**10** οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
**11** οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
**12** οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
**13** κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
**14** Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· Ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
**15** ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
**16** οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
**17** Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
**18** ὅτι ἔλεγον ὑμῖν· Ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
**19** οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
**20** ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
**21** ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
**22** καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
**23** οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
**24** Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει
**25** μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### Jude 1:1
- **Apparatus:** `ἠγαπημένοις` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ἡγιασμένοις** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **χυ̅ (= χριστοῦ)** Ψ (044)
- **Apparatus:** `Χριστῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **om.** Ψ (044)
- *Disregarded Surface Variant:* kept `Ἰούδας` over `ιουδασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ` over `χυ̅`, `χριστοῦ` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `δοῦλος,` over `δουλοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφὸς` over `αδελφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰακώβου,` over `ιακωβου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ` over `θω̅`, `Θεῷ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `πατρὶ` over `πατρι`, `Πατρὶ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστῷ` over `χω̅`, `χριστῷ` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `τετηρημένοις` over `τετηρημενοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κλητοῖς·` over `κλητοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:2
- *Disregarded Surface Variant:* kept `ἔλεος` over `ελεοσ`, `Ἔλεος` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνη` over `ειρηνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγάπη` over `αγαπη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πληθυνθείη.` over `πληθυνθειη`, `πληθυνθιη` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### Jude 1:3
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **του** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἡμῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **και ζωησ** א (01) Ψ (044) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `γράψαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **γραφιν** א (01) Ψ (044) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐπαγωνίζεσθαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **επαγωνιζεσθε** A (02) 𝔓72
- **Apparatus:** `παραδοθείσῃ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **παραοθειση πειστι** 𝔓72
- **Apparatus:** `πίστει.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- *Disregarded Surface Variant:* kept `Ἀγαπητοί,` over `αγαπητοι`, `ἀγαπητοί,` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶσαν` over `πασαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σπουδὴν` over `σπουδην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιούμενος` over `ποιουμενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γράφειν` over `γραφειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κοινῆς` over `κοινησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σωτηρίας` over `σωτηριασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνάγκην` over `αναγκην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔσχον` over `εσχον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρακαλῶν` over `παρακαλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπαγωνίζεσθαι` over `επαγωνιζεσθαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἅπαξ` over `απαξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραδοθείσῃ` over `παραδοθειση` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁγίοις` over `αγιοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστει.` over `πιστει`, `πιστι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### Jude 1:4
- **Apparatus:** `παρεισέδυσαν` א (01) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT BHP A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Ψ (044) 𝔓72 **]** **παρεισεδύησαν** B (03) Nestle1904 C (04) WH1881 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **και** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τὸ κρίμα,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κρισμα** 𝔓72 ; **το κηρυγμα** Ψ (044)
- **Apparatus:** `κρίμα, ἀσεβεῖς,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κηρυγμα ασεβειν** Ψ (044) ; **ασεβεισ** 𝔓72
- **Apparatus:** `τὴν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **τη** 𝔓72
- **Apparatus:** `χάριτα` B (03) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 𝔓72 **]** **χάριν** א (01) RP2018 (Byz) TR (KJTR) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Ψ (044) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `μόνον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **νομον ημων** 𝔓72
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) PT1904 (Byz) THGNT Tisch8 WH1881 𝔓72 **]** **θεὸν** RP2018 (Byz) TR (KJTR) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Ψ (044) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἡμῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ημων** 𝔓72
- *Disregarded Surface Variant:* kept `γάρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τινες` over `τινεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωποι,` over `ανθρωποι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάλαι` over `παλαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προγεγραμμένοι` over `προγεγραμμενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦτο` over `τουτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίμα,` over `κριμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀσεβεῖς,` over `ασεβεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετατιθέντες` over `μετατιθεντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀσέλγειαν` over `ασελγειαν`, `ασελγιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μόνον` over `μονον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεσπότην` over `δεσποτην`, `Δεσπότην` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κύριον` over `κν̅`, `Κύριον` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦν` over `ιν̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστὸν` over `χν̅`, `χριστὸν` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἀρνούμενοι.` over `αρνουμενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:5
- **Apparatus:** `Ὑπομνῆσαι δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **υπομνησει ουν** C (04) ; **υπομνησαι ουν** Ψ (044) ; **υπομνησε δε** 𝔓72
- **Apparatus:** `Ὑπομνῆσαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **υπομνησε** 𝔓72 ; **υπομνησει** C (04)
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **ουν** Ψ (044) C (04)
- **Apparatus:** `ὑμᾶς` B (03) א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) **]** **om.** Nestle1904 A (02) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): modern critical editions.
- **Apparatus:** `ἅπαξ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **om.** א (01) Ψ (044) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `πάντα` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **τοῦτο** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **παντασ** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `Ἰησοῦς` B (03) SRGNT SBLGNT BHP A (02) NA28 (TAGNT) THGNT **]** **ὁ κύριος** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **κσ̅ απαξ (= κύριοσ απαξ)** א (01) Ψ (044) ; **Κύριος** Nestle1904 Tisch8 WH1881 ; **ο απαξ** C (04) ; **θσ̅ χρσ̅ (= θεὸσ χριστὸσ)** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `ἐκ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εγ** 𝔓72
- **Apparatus:** `γῆς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **της** Ψ (044)
- **Apparatus:** `Αἰγύπτου` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εγυπτου** 𝔓72
- **Apparatus:** `πιστεύσαντας` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 Ψ (044) 𝔓72 **]** **πιστεύσαντες** Tisch8
- *Disregarded Surface Variant:* kept `Ὑπομνῆσαι` over `υπομνησαι`, `ὑπομνῆσαι` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμᾶς` over `υμασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βούλομαι,` over `βουλομαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰδότας` over `ειδοτασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαὸν` over `λαον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γῆς` over `γησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Αἰγύπτου` over `αιγυπτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σώσας` over `σωσασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεύτερον` over `δευτερον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πιστεύσαντας` over `πιστευσαντασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπώλεσεν,` over `απωλεσεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:6
- **Apparatus:** `τε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **δε** A (02)
- **Apparatus:** `οἰκητήριον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **κατοικητηριον** Ψ (044)
- *Disregarded Surface Variant:* kept `ἀγγέλους` over `αγγελουσ`, `Ἀγγέλους` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τηρήσαντας` over `τηρησαντασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτῶν` over `εαυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀρχὴν` over `αρχην`, `ἀρχήν,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπολιπόντας` over `απολιποντασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἴδιον` over `ιδιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἰκητήριον` over `οικητηριον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίσιν` over `κρισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεγάλης` over `μεγαλησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέρας` over `ημερασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεσμοῖς` over `δεσμοισ`, `Δεσμοῖς` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀϊδίοις` over `αιδιοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζόφον` over `ζοφον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τετήρηκεν·` over `τετηρηκεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / αλλ` (C (04), NA28 (TAGNT), Ψ (044)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### Jude 1:7
- **Apparatus:** `αἱ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ε** 𝔓72
- **Apparatus:** `τρόπον τούτοις` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 𝔓72 **]** **τούτοις τρόπον** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **τροπον αυτοις** Ψ (044) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐκπορνεύσασαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εκπορνευσασθαι** 𝔓72
- **Apparatus:** `ἀπελθοῦσαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **απελθουσε** 𝔓72
- **Apparatus:** `ἑτέρας, πρόκεινται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **τερασ προσκειντε** 𝔓72
- **Apparatus:** `δεῖγμα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **δε διγμα** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αἰωνίου` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εωνιου** 𝔓72
- **Apparatus:** `ὑπέχουσαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ουκ εχουσιν** א (01) ; **υπερεχουσαι** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ`, `Ὡς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Σόδομα` over `σοδομα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Γόμορρα` over `γομορρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἱ` over `αι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὰς` over `αυτασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλεις,` over `πολεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅμοιον` over `ομοιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκπορνεύσασαι` over `εκπορνευσασαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπελθοῦσαι` over `απελθουσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀπίσω` over `οπισω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σαρκὸς` over `σαρκοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑτέρας,` over `ετερασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρόκεινται` over `προκεινται`, `προκινται` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `πυρὸς` over `πυροσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰωνίου` over `αιωνιου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίκην` over `δικην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `Γόμορρα / γομορα` (𝔓72) — *Apparatus witness, not a variant: Single / double consonant spelling (Ἰωάνης / Ἰωάννης type)*

### Jude 1:8
- **Apparatus:** `Ὁμοίως` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ομωσ** A (02)
- **Apparatus:** `μὲν μιαίνουσιν,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **μειενουσιν** 𝔓72
- **Apparatus:** `κυριότητα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **κυριοτητασ** א (01) Ψ (044) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `βλασφημοῦσιν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **βασφημουσιν** 𝔓72
- *Disregarded Surface Variant:* kept `Ὁμοίως` over `ομοιωσ`, `ὁμοίως` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέντοι` over `μεντοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτοι` over `ουτοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐνυπνιαζόμενοι` over `ενυπνιαζομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σάρκα` over `σαρκα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὲν` over `μεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μιαίνουσιν,` over `μιαινουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀθετοῦσιν,` over `αθετουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξας` over `δοξασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βλασφημοῦσιν.` over `βλασφημουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:9
- **Apparatus:** `ὁ δὲ Μιχαὴλ` א (01) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **οτε μειχαηλ** B (03) ; **ο δε μιχαησ** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ὅτε` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **τοτε** B (03) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `διακρινόμενος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **διεκρινομενοσ** A (02)
- **Apparatus:** `Μωϋσέως` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Μωσέως** A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Ψ (044) ; **μουσεωσ** 𝔓72
- **Apparatus:** `Μωϋσέως σώματος, οὐκ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Μωσέως σώματος—οὐκ** A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Ψ (044) ; **μουσεωσ σωματοσ ουκ** 𝔓72
- **Apparatus:** `ἐπενεγκεῖν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **υπενεγκειν** Ψ (044)
- **Apparatus:** `Ἐπιτιμήσαι` SRGNT SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) BHP A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **επιτειμησαι εν** B (03) ; **επιτιμησε** א (01) ; **εν** Ψ (044) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κύριος` B (03) SRGNT Nestle1904 BHP TR (KJTR) SBLGNT RP2018 (Byz) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ο θσ̅ (= ο θσ)** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀρχάγγελος,` over `αρχαγγελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διαβόλῳ` over `διαβολω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διακρινόμενος` over `διακρεινομενοσ`, `διακρινομενοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `διελέγετο` over `διελεγετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μωϋσέως` over `μωυσεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σώματος,` over `σωματοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐτόλμησεν` over `ετολμησεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίσιν` over `κρισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπενεγκεῖν` over `επενεγκειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βλασφημίας,` over `βλασφημιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα`, `αλλ`, `ἀλλ’`, `ἀλλʼ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Elision (κατὰ / κατ’ type)*
- *Disregarded Surface Variant:* kept `εἶπεν·` over `ειπεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλʼ` (C (04), NA28 (TAGNT), PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### Jude 1:10
- **Apparatus:** `οἴδασιν βλασφημοῦσιν,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **υδασιν βασφημουσιν** 𝔓72
- **Apparatus:** `φθείρονται.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **διαφθειρονται** Ψ (044)
- *Disregarded Surface Variant:* kept `οὗτοι` over `ουτοι`, `Οὗτοι` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅσα` over `οσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὲν` over `μεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἴδασιν` over `οιδασιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βλασφημοῦσιν,` over `βλασφημουσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅσα` over `οσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυσικῶς` over `φυσικωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄλογα` over `αλογα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζῷα` over `ζωα`, `ζῶα` (B (03), TR (KJTR), א (01)) — *Non-morphological iota-subscript convention (αἴρω aorist / κἀγώ / ἀθῷος / ζῷον / ᾠδή / σῴζω)*
- *Disregarded Surface Variant:* kept `ἐπίστανται,` over `επιστανται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τούτοις` over `τουτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φθείρονται.` over `φθειρονται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:11
- **Apparatus:** `αὐτοῖς,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αυτοι** 𝔓72
- **Apparatus:** `Βαλαὰμ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **βαλαακ** 𝔓72
- *Disregarded Surface Variant:* kept `οὐαὶ` over `ουαι`, `Οὐαὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς,` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι`, `Ὅτι` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁδῷ` over `οδω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Κάϊν` over `καιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπορεύθησαν,` over `επορευθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλάνῃ` over `πλανη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Βαλαὰμ` over `βαλααμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μισθοῦ` over `μισθου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξεχύθησαν,` over `εξεχυθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀντιλογίᾳ` over `αντιλογια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Κόρε` over `κορε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπώλοντο.` over `απωλοντο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:12
- **Apparatus:** `οἱ` B (03) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **γογγυσται μεμψιμυροι κα τασ επιθυμιασ αυτων πορευομενοι** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἐν ταῖς ἀγάπαις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **απαταισ** C (04) ; **εν ταισ απαταισ** A (02)
- **Apparatus:** `ἀγάπαις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **απαταισ** A (02)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ὑμῖν** TR (KJTR) C (04) TR-Scrivener (1894) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἑαυτοὺς ποιμαίνοντες, νεφέλαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αυτουσ πυμενοντεσ νεφελε** 𝔓72 ; **εαυτουσ ποιμενοντεσ νεφελαι** C (04)
- **Apparatus:** `ποιμαίνοντες,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ποιμενοντεσ** C (04) ; **πυμενοντεσ** 𝔓72
- **Apparatus:** `ὑπὸ ἀνέμων` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **παντι ανεμω** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `παραφερόμεναι` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **παραφερομενοι** B (03) Ψ (044) 𝔓72 ; **περιφερόμεναι** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `φθινοπωρινὰ` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) RP2018 (Byz) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **φθινοπωρικα** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `οὗτοί` over `ουτοι`, `Οὗτοί` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσιν` over `εισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγάπαις` over `αγαπαισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σπιλάδες` over `σπιλαδεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συνευωχούμενοι,` over `συνευωχουμενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀφόβως` over `αφοβωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτοὺς` over `εαυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιμαίνοντες,` over `ποιμαινοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νεφέλαι` over `νεφελαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνυδροι` over `ανυδροι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δένδρα` over `δενδρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄκαρπα` over `ακαρπα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὶς` over `δισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποθανόντα` over `αποθανοντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκριζωθέντα,` over `εκριζωθεντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:13
- **Apparatus:** `κύματα ἄγρια` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **αγρια κυματα** א (01) ; **κυματα αγια** C (04) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `θαλάσσης ἐπαφρίζοντα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **θαλασησ απαφριζοντα** 𝔓72 C (04)
- **Apparatus:** `ἐπαφρίζοντα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **απαφριζοντα** C (04) 𝔓72
- **Apparatus:** `πλανῆται οἷς ὁ ζόφος τοῦ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πλανητεσ οισ ζοφοσ** B (03) ; **πλανητε οισ ο ζοφοσ του** A (02) ; **πλανιται οις ο ζοφος του** Ψ (044) ; **πλανητε οισ ζοφοσ του** 𝔓72 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **τὸν** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550)
- **Apparatus:** `αἰῶνα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αιωνας** Ψ (044) ; **εωνα** 𝔓72
- **Apparatus:** `αἰῶνα τετήρηται.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εωνα τετηρητε** 𝔓72 ; **αιωνας τετηρηται** Ψ (044)
- *Disregarded Surface Variant:* kept `θαλάσσης` over `θαλασσησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπαφρίζοντα` over `επαφριζοντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτῶν` over `εαυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰσχύνας,` over `αισχυνασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀστέρες` over `αστερεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σκότους` over `σκοτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰῶνα` over `αιωνα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τετήρηται.` over `τετηρηται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:14
- **Apparatus:** `Ἐπροφήτευσεν` B (03) SRGNT Nestle1904 BHP Tisch8 WH1881 𝔓72 **]** **Προεφήτευσεν** SBLGNT RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Ψ (044) ; **προεπροφητευσεν** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ο** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **μυριάσιν** TR (KJTR) C (04) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'μυριάσιν' together form one word-order variant (TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἁγίαις` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** א (01) ; **αγιων αγγελων** 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `μυριάσιν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **om.** TR (KJTR) C (04) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'μυριάσιν' together form one word-order variant (TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `αὐτοῦ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αγιων αγγελων** א (01) ; **αγγελων** Ψ (044) ; **om.** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τούτοις` over `τουτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἕβδομος` over `εβδομοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἀδὰμ` over `αδαμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἑνὼχ` over `ενωχ`, `Ἐνώχ,` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `λέγων·` over `λεγων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰδοὺ` over `ιδου`, `“ἰδοὺ,`, `Ἰδού,` (B (03), BHP, RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦλθεν` over `ηλθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κύριος` over `κσ̅`, `Κύριος` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:15
- **Apparatus:** `ἐλέγξαι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 Ψ (044) **]** **ἐξελέγξαι** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ελεγξε** 𝔓72
- **Apparatus:** `πάντας τοὺς ἀσεβεῖς` B (03) SRGNT SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) A (02) C (04) THGNT WH1881 Ψ (044) **]** **πᾶσαν ψυχὴν** א (01) BHP NA28 (TAGNT) 𝔓72 ; **πάντας τοὺς ἀσεβεῖς αὐτῶν** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT WH1881 Ψ (044) 𝔓72 **]** **αὐτῶν** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 𝔓72 ; **των εργων αυτων ων ησεβησαν και περι παντων των** C (04) ; **των ασεβειων αυτων ων ησεβησαν και περι παντων των** Ψ (044)
- **Apparatus:** `ἀσεβείας αὐτῶν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** א (01) 𝔓72 ; **αυτων** C (04) Ψ (044) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 Ψ (044) 𝔓72 **]** **λογων** א (01) C (04) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ποιῆσαι` over `ποιησαι`, `Ποιῆσαι` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κρίσιν` over `κρισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντων` over `παντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλέγξαι` over `ελεγξαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντων` over `παντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργων` over `εργων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὧν` over `ων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἠσέβησαν` over `ησεβησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντων` over `παντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σκληρῶν` over `σκληρων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὧν` over `ων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλάλησαν` over `ελαλησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατʼ` over `κατ`, `κατ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτωλοὶ` over `αμαρτωλοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀσεβεῖς.` over `ασεβεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:16
- **Apparatus:** `γογγυσταί,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **γογγυστε** 𝔓72
- **Apparatus:** `μεμψίμοιροι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **μεμψιμυροι** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72 ; **κατὰ τὰς ἐπιθυμίας ἑαυτῶν πορευόμενοι,** C (04) NA28 (TAGNT)
- **Apparatus:** `αὐτῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ἑαυτῶν** C (04) NA28 (TAGNT) ; **om.** 𝔓72
- **Apparatus:** `τὸ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- **Apparatus:** `αὐτῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **αυτω** A (02)
- *Disregarded Surface Variant:* kept `οὗτοί` over `ουτοι`, `Οὗτοί` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσιν` over `εισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γογγυσταί,` over `γογγυσται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιθυμίας` over `επιθυμιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πορευόμενοι,` over `πορευομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στόμα` over `στομα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαλεῖ` over `λαλει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπέρογκα,` over `υπερογκα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θαυμάζοντες` over `θαυμαζοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρόσωπα` over `προσωπα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὠφελείας` over `ωφελιασ`, `ωφελειασ`, `ὠφελίας` (B (03), BHP, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `χάριν.` over `χαριν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:17
- **Apparatus:** `Ὑμεῖς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **υμει** 𝔓72
- **Apparatus:** `ἀγαπητοί,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αγαπητοισ** 𝔓72
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **προειρημενων** A (02)
- **Apparatus:** `τῶν προειρημένων` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **om.** A (02)
- *Disregarded Surface Variant:* kept `Ὑμεῖς` over `υμεισ`, `ὑμεῖς` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δέ,` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπητοί,` over `αγαπητοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μνήσθητε` over `μνησθητε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥημάτων` over `ρηματων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προειρημένων` over `προειρημενων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποστόλων` over `αποστολων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ·` over `χυ̅`, `χριστοῦ·` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### Jude 1:18
- **Apparatus:** `Ἐπ ἐσχάτου` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT WH1881 Ψ (044) 𝔓72 **]** **ὅτι ἐν** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **επ εσχατου του** A (02) Tisch8 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 Ψ (044) 𝔓72 **]** **τοῦ** א (01) Nestle1904 A (02) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `χρόνου` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ἐσχάτῳ χρόνῳ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἔσονται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **αναστησονται** Ψ (044) ; **ελευσονται** A (02)
- **Apparatus:** `ἐμπαῖκται` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εμπεκται** א (01) A (02) C (04) ; **εμπεκτε** 𝔓72 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἑαυτῶν ἐπιθυμίας` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επιθυμιασ αυτων** א (01) ; **αυτων επιθυμιας** Ψ (044) ; **εαυτω επειθυμιασ** 𝔓72 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι`, `Ὅτι` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔλεγον` over `ελεγον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν·` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔσονται` over `εσονται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πορευόμενοι` over `πορευομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀσεβειῶν.` over `ασεβειων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:19
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ἑαυτούς** TR (KJTR) C (04) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `οὗτοί` over `ουτοι`, `Οὗτοί` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσιν` over `εισιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποδιορίζοντες,` over `αποδιοριζοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ψυχικοί,` over `ψυχικοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεῦμα` over `πνευμα`, `πνα̅`, `Πνεῦμα` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔχοντες.` over `εχοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:20
- **Apparatus:** `ὑμεῖς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ημεισ** C (04)
- **Apparatus:** `ἐποικοδομοῦντες ἑαυτοὺς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **om.** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) 𝔓72
- **Apparatus:** `ἁγιωτάτῃ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αγιοτατη** A (02) C (04) ; **εαυτων** 𝔓72
- **Apparatus:** `ἁγιωτάτῃ ὑμῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αγιοτατη ημων** C (04) ; **εαυτων αγιοτητι** 𝔓72 ; **αγιοτατη υμων** A (02)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **ἐποικοδομοῦντες ἑαυτούς** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ανυκοδομεισθαι** 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `προσευχόμενοι,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **προσεχομενοι εαυτοισ** 𝔓72
- *Disregarded Surface Variant:* kept `ὑμεῖς` over `υμεισ`, `Ὑμεῖς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δέ,` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπητοί,` over `αγαπητοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐποικοδομοῦντες ἑαυτοὺς` over `om.` (RP2018 (Byz), TR (KJTR)) — *Not counted as omitting 'εποικοδομουντεσ εαυτουσ': RP2018 (Byz), TR (KJTR) have these words in a neighbouring unit where the alignment put them (not an omission)*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁγιωτάτῃ` over `αγιωτατη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστει,` over `πιστει`, `πιστι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεύματι` over `πνευματι`, `πνι̅`, `Πνεύματι` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Ἁγίῳ` over `ἁγίῳ`, `αγιω`, `Ἁγίω` (B (03), RP2018 (Byz), SBLGNT, TR (KJTR), א (01)) — *Spelling variant pooled before the vote with the reading 'Ἁγίῳ' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `προσευχόμενοι,` over `προσευχομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:21
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **του** Ψ (044)
- **Apparatus:** `τηρήσατε` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τηρησωμεν** B (03) Ψ (044) 𝔓72 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εισ ζοην** 𝔓72
- **Apparatus:** `εἰς ζωὴν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- *Disregarded Surface Variant:* kept `ἑαυτοὺς` over `εαυτουσ`, `Ἑαυτοὺς` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγάπῃ` over `αγαπη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `προσδεχόμενοι` over `προσδεχομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔλεος` over `ελεοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ` over `χυ̅`, `χριστοῦ` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωὴν` over `ζωην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰώνιον.` over `αιωνιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:22
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- **Apparatus:** `ἐλεᾶτε` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) WH1881 Ψ (044) **]** **ἐλεεῖτε** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ελεγχεται** A (02) ; **ελεγχετε** C (04) THGNT Tisch8 ; **εκ πυροσ αρπασατε** 𝔓72 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `διακρινομένους` א (01) SRGNT SBLGNT Nestle1904 BHP B (03) A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **διακρινόμενοι** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὓς` over `ουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὲν` over `μεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διακρινομένους` over `διακρινομενουσ`, `διακρεινομενουσ` (B (03), א (01)) — *Spelling variant pooled before the vote with the reading 'διακρινομένους' (same word, different spelling); whether that reading was adopted is shown in the apparatus*

### Jude 1:23
- **Apparatus:** `οὓς δὲ` א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) THGNT Tisch8 Ψ (044) **]** **om.** B (03) Nestle1904 WH1881 ; **οὓς δὲ ἐν φόβῳ** PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **δε** 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **ἐν φόβῳ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) A (02) C (04) NA28 (TAGNT) TCGNT (Byz) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **τοῦ** TR (KJTR) PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἁρπάζοντες` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αρπαζετεσ** א (01) ; **om.** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `οὓς δὲ ἐλεᾶτε ἐν φόβῳ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ουσ δε ελεαται εν φοβω** A (02) ; **εν φοβω** C (04) 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐσπιλωμένον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εσπειλωμενοι** 𝔓72
- *Disregarded Surface Variant:* kept `σῴζετε` over `σωζετε`, `σώζετε` (B (03), TR (KJTR), א (01)) — *Non-morphological iota-subscript convention (αἴρω aorist / κἀγώ / ἀθῷος / ζῷον / ᾠδή / σῴζω)*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πυρὸς` over `πυροσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μισοῦντες` over `μεισουντεσ`, `μισουντεσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σαρκὸς` over `σαρκοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐσπιλωμένον` over `εσπιλωμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χιτῶνα.` over `χιτωνα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Jude 1:24
- **Apparatus:** `φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 Ψ (044) **]** **στηριξαι ασπειλουσ αμωμουσ αγνευομενουσ απεναντι** 𝔓72 ; **φυλαξαι ημασ απταιστουσ και στησαι κατενωπιον** A (02) ; **φυλαξαι υμασ απταιστουσ και απιλουσ στησαι ενωπιον** C (04) ; **φυλάξαι αὐτοὺς ἀπταίστους καὶ στῆσαι κατενώπιον** PT1904 (Byz) TCGNT (Byz) TR-Stephanus (1550)
- **Apparatus:** `ὑμᾶς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) C (04) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 WH1881 Ψ (044) **]** **αὐτοὺς** RP2018 (Byz) PT1904 (Byz) TCGNT (Byz) TR-Stephanus (1550) ; **ημασ** A (02) ; **ασπειλουσ** 𝔓72 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἀπταίστους` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **απτεστουσ** א (01) ; **αμωμουσ** 𝔓72 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **απιλουσ** C (04)
- **Apparatus:** `κατενώπιον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ενωπιον** C (04) ; **om.** 𝔓72
- **Apparatus:** `ἀμώμους` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **αμεμπτουσ** A (02) ; **om.** 𝔓72
- *Disregarded Surface Variant:* kept `Τῷ` over `τω`, `τῷ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δυναμένῳ` over `δυναμενω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυλάξαι` over `φυλαξαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στῆσαι` over `στησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατενώπιον` over `κατενωπιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξης` over `δοξησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀμώμους` over `αμωμουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαλλιάσει` over `αγαλλιασει`, `αγαλλιασι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### Jude 1:25
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **σοφῷ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `σωτῆρι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **om.** 𝔓72
- **Apparatus:** `διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν` B (03) א (01) SRGNT Nestle1904 BHP SBLGNT A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **δια ιηυ̅ χρυ̅ του κυ̅ ω ημων αυτω (= δια ἰησοῦ χριστοῦ του κυρίου ω ημων αυτω)** 𝔓72 *(omission / addition)*
  - *transcriptional: homoeoteleuton:* The omission in RP2018 (Byz), TR (KJTR) is explicable by eye-skip between the two occurrences of 'ημων' (between such common short words a possibility only; the vote is unchanged).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **ω** א (01) ; **αυτω** 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) 𝔓72 **]** **καὶ** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 𝔓72 **]** **om.** Ψ (044)
- **Apparatus:** `πρὸ παντὸς τοῦ αἰῶνος` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 Ψ (044) **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) 𝔓72 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `πάντας` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) 𝔓72 **]** **om.** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τοὺς αἰῶνας·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ψ (044) **]** **εωνασ** 𝔓72
- *Disregarded Surface Variant:* kept `μόνῳ` over `μονω`, `Μόνῳ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ` over `θω̅`, `Θεῷ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `σωτῆρι` over `σωτηρι`, `Σωτῆρι` (B (03), BHP, Nestle1904, SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῶν` over `ημων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξα` over `δοξα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεγαλωσύνη` over `μεγαλωσυνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κράτος` over `κρατοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξουσία` over `εξουσια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νῦν` over `νυν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰῶνας·` over `αιωνασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀμήν.` over `αμην`, `Ἀμήν!`, `Ἀμήν.` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `SRGNT`: Ἰούδας, Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ Πατρὶ ἠγαπημένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς:
  - `SBLGNT`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `BHP`: Ἰούδας, Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου· τοῖς ἐν Θεῷ Πατρὶ ἠγαπημένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς:
  - `Nestle1904`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ Πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς.
  - `RP2018 (Byz)`: Ἰούδας Ἰησοῦ χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἡγιασμένοις, καὶ Ἰησοῦ χριστῷ τετηρημένοις, κλητοῖς·
  - `TR (KJTR)`: Ἰούδας, Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ Πατρὶ ἠγίασμένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις, κλητοῖς:
  - `B (03)`: ιουδασ ιυ̅ χυ̅ δουλοσ αδελφοσ δε ιακωβου τοισ εν θω̅ πατρι ηγαπημενοισ και ιυ̅ χω̅ τετηρημενοισ κλητοισ
  - `א (01)`: ιουδασ ιυ̅ χυ̅ δουλοσ αδελφοσ δε ιακωβου τοισ εν θω̅ πατρι ηγαπημενοισ και ιυ̅ χω̅ τετηρημενοισ κλητοισ
  - `NA28 (TAGNT)`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `THGNT`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `WH1881`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `Tisch8`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν θεῷ πατρὶ ἠγαπημένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `TCGNT (Byz)`: Ἰούδας, Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ πατρὶ ἡγιασμένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις, κλητοῖς·
  - `PT1904 (Byz)`: Ἰούδας, Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφός δὲ Ἰακώβου, τοῖς ἐν Θεῷ πατρὶ ἡγιασμένοις καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `TR-Scrivener (1894)`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ πατρὶ ἡγιασμένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις, κλητοῖς·
  - `TR-Boyd (Elz/Scr/Steph)`: Ἰούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ πατρὶ ἡγιασμένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις, κλητοῖς·
  - `TR-Stephanus (1550)`: Ιούδας Ἰησοῦ Χριστοῦ δοῦλος, ἀδελφὸς δὲ Ἰακώβου, τοῖς ἐν Θεῷ πατρὶ ἡγιασμένοις, καὶ Ἰησοῦ Χριστῷ τετηρημένοις κλητοῖς·
  - `TR-Elzevir (1624)`: ιουδας ιησου χριστου δουλος αδελφος δε ιακωβου τοις εν θεω πατρι ηγιασμενοις και ιησου χριστω τετηρημενοις κλητοις
  - `𝔓72`: ιουδασ ιηυ̅ χρυ̅ δουλοσ αδελφοσ δε ιακωβου τοισ εν θω̅ πρι̅ ηγαπημενοισ και ιηυ̅ χρω̅ τετηρημενοισ κλητοισ
  - `A (02)`: ιουδασ ιυ̅ χυ̅ δουλοσ αδελφοσ δε ιακωβου τοισ εν θω̅ πρι̅ ηγαπημενοισ και ιυ̅ χω̅ τετηρημενοισ κλητοισ
  - `33`: ιουδας ιυ̅ χυ̅ δουλος αδελφος δε […] […] […] […] […] […] […] […] […] […] κλητοις
  - `Ψ (044)`: ιουδας ιυ̅ χυ̅ δουλος αδελφος δε ιακωβου τοις εν θω̅ πρι̅ ηγαπημενοις και χυ̅ ιυ̅ τετηρημενοις κλητοις
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἠγαπημένοις' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἡγιασμένοις (RP2018 (Byz), TR (KJTR)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 2 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `SRGNT`: ἔλεος ὑμῖν, καὶ εἰρήνη, καὶ ἀγάπη πληθυνθείη.
  - `SBLGNT`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `BHP`: ἔλεος ὑμῖν, καὶ εἰρήνη, καὶ ἀγάπη πληθυνθείη.
  - `Nestle1904`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `RP2018 (Byz)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TR (KJTR)`: Ἔλεος ὑμῖν, καὶ εἰρήνη, καὶ ἀγάπη, πληθυνθείη.
  - `B (03)`: ελεοσ υμιν και ειρηνη και αγαπη πληθυνθειη
  - `א (01)`: ελεοσ υμιν και ειρηνη και αγαπη πληθυνθιη
  - `NA28 (TAGNT)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `THGNT`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `WH1881`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `Tisch8`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TCGNT (Byz)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `PT1904 (Byz)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TR-Scrivener (1894)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TR-Boyd (Elz/Scr/Steph)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TR-Stephanus (1550)`: ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη πληθυνθείη.
  - `TR-Elzevir (1624)`: ελεος υμιν και ειρηνη και αγαπη πληθυνθειη
  - `𝔓72`: ελεοσ υμιν και ειρηνη και αγαπη πληθυνθιη
  - `A (02)`: ελεοσ υμιν και ειρηνη και αγαπη πληθυνθειη
  - `33`: ελεος υμιν και […] […] […] […]
  - `Ψ (044)`: ελεος υμιν και ειρηνη και αγαπη πληθυνθειη
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 7 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 3 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `SRGNT`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `SBLGNT`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `BHP`: ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `Nestle1904`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `RP2018 (Byz)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `TR (KJTR)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `B (03)`: αγαπητοι πασαν σπουδην ποιουμενοσ γραφειν υμιν περι τησ κοινησ ημων σωτηριασ αναγκην εσχον γραψαι υμιν παρακαλων επαγωνιζεσθαι τη απαξ παραδοθειση τοισ αγιοισ πιστει
  - `א (01)`: αγαπητοι πασαν σπουδην ποιουμενοσ του γραφειν υμιν περι τησ κοινησ ημων σωτηριασ και ζωησ αναγκην εσχον γραφιν υμιν παρακαλων επαγωνιζεσθαι τη απαξ παραδοθειση τοισ αγιοισ πιστι
  - `NA28 (TAGNT)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `THGNT`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `WH1881`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `Tisch8`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `TCGNT (Byz)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `PT1904 (Byz)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `TR-Scrivener (1894)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας, ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
  - `TR-Stephanus (1550)`: Ἀγαπητοὶ, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν, παρακαλῶν ἐπαγωνίζεσθαι τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει·
  - `TR-Elzevir (1624)`: αγαπητοι πασαν σπουδην ποιουμενος γραφειν υμιν περι της κοινης σωτηριας αναγκην εσχον γραψαι υμιν παρακαλων επαγωνιζεσθαι τη απαξ παραδοθειση τοις αγιοις πιστει
  - `𝔓72`: αγαπητοι πασαν σπουδην ποιησαμενοσ του γραφιν υμιν περει τησ κοινησ ημων σωτηριασ αναγκην εσχον γραψαι υμιν παρακαλων επαγωνιζεσθε τη απαξ παραοθειση πειστι τοισ αγιοισ
  - `A (02)`: αγαπητοι πασαν σπουδην ποιουμενοσ γραφειν υμιν περι τησ κοινησ ημων σωτηριασ αναγκην εσχον γραψαι υμιν παρακαλων επαγωνιζεσθε τη απαξ παραδοθειση τοισ αγιοισ πιστει
  - `C (04)`: αγαπητοι πασαν σπουδην ποιουμενοσ γραφειν υμιν περι τησ κοινησ ημων σωτηριασ αναγκην εσχον γραψαι υμιν παρακαλων επαγωνιζεσθαι τη απαξ παραδοθειση τοισ αγιοισ πιστει
  - `33`: […] […] […] ποιουμενος γραφειν […] […] […] […] […] […] […] […] […] […] …
  - `Ψ (044)`: αγαπητοι πασαν σπουδην ποιουμενοι του γραφειν υμιν περι της κοινης ημων σριας̅ και ζωης αναγκην εσχον γραφειν υμιν παρακαλων επαγωνιζεσθαι τη απαξ παραδοθειση τοις αγιοις πιστει
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over του (א (01)). [Omission in some witnesses] Adopted 'ἡμῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over και ζωησ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'γράψαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over γραφιν (א (01)). Also normalised 21 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `92.7%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `SRGNT`: Παρεισέδυσαν γάρ τινες ἄνθρωποι οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον Δεσπότην καὶ Κύριον ἡμῶν, Ἰησοῦν Χριστὸν, ἀρνούμενοι.
  - `SBLGNT`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `BHP`: παρεισέδυσαν γάρ τινες ἄνθρωποι οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον Δεσπότην καὶ Κύριον ἡμῶν, Ἰησοῦν Χριστὸν, ἀρνούμενοι.
  - `Nestle1904`: παρεισεδύησαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον Δεσπότην καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `RP2018 (Byz)`: Παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον δεσπότην θεὸν καὶ κύριον ἡμῶν Ἰησοῦν χριστὸν ἀρνούμενοι.
  - `TR (KJTR)`: Παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον Δεσπότην Θεόν, καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `B (03)`: παρεισεδυησαν γαρ τινεσ ανθρωποι οι παλαι προγεγραμμενοι εισ τουτο το κριμα ασεβεισ την του θυ̅ ημων χαριτα μετατιθεντεσ εισ ασελγειαν και τον μονον δεσποτην και κν̅ ημων ιν̅ χν̅ αρνουμενοι
  - `א (01)`: παρεισεδυσαν γαρ τινεσ ανθρωποι οι και παλαι προγεγραμμενοι εισ τουτο το κριμα ασεβεισ την του θυ̅ ημων χαριν μετατιθεντεσ εισ ασελγιαν και τον μονον δεσποτην και κν̅ ημων ιν̅ χν̅ αρνουμενοι
  - `NA28 (TAGNT)`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `THGNT`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `WH1881`: παρεισεδύησαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `Tisch8`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ θεοῦ ἡμῶν χάριτα μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `TCGNT (Byz)`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην Θεὸν καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `PT1904 (Byz)`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρῖμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν καὶ τὸν μόνον δεσπότην καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `TR-Scrivener (1894)`: παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον δεσπότην Θεόν, καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `TR-Boyd (Elz/Scr/Steph)`: Παρεισέδυσαν γάρ τινες ἄνθρωποι, οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρίμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον δεσπότην Θεὸν καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `TR-Stephanus (1550)`: παρεισέδυσαν γάρ τινες ἄνθρωποι οἱ πάλαι προγεγραμμένοι εἰς τοῦτο τὸ κρῖμα, ἀσεβεῖς, τὴν τοῦ Θεοῦ ἡμῶν χάριν μετατιθέντες εἰς ἀσέλγειαν, καὶ τὸν μόνον δεσπότην Θεὸν, καὶ Κύριον ἡμῶν Ἰησοῦν Χριστὸν ἀρνούμενοι.
  - `TR-Elzevir (1624)`: παρεισεδυσαν γαρ τινες ανθρωποι οι παλαι προγεγραμμενοι εις τουτο το κριμα ασεβεις την του θεου ημων χαριν μετατιθεντες εις ασελγειαν και τον μονον δεσποτην θεον και κυριον ημων ιησουν χριστον αρνουμενοι
  - `𝔓72`: παρεισεδυσαν γαρ τινεσ ανοι̅ οι παλε προγεγραμενοι εισ τουτο κρισμα ασεβεισ τη του θυ̅ ημων χαρειτα μετατιθεντεσ εισ ασελγειαν και τον νομον ημων δεσποτην και κν̅ ιην̅ χρν̅ ημων αρνουμενοι
  - `A (02)`: παρεισεδυσαν γαρ τινεσ ανοι̅ οι παλαι προγεγραμμενοι εισ τουτο το κριμα ασεβεισ την του θυ̅ ημων χαριτα μετατιθεντεσ εισ ασελγειαν και τον μονον δεσποτην και κν̅ ημων ιν̅ χν̅ αρνουμενοι
  - `C (04)`: παρεισεδυησαν γαρ τινεσ ανθρωποι οι παλαι προγεγραμμενοι εισ τουτο το κριμα ασεβεισ την του θυ̅ ημων χαριν μετατιθεντεσ εισ ασελγειαν και τον μονον δεσποτην και κν̅ ημων ιν̅ χν̅ αρνουμενοι
  - `Ψ (044)`: παρεισεδυσαν γαρ τινες ανοι̅ οι παλαι προγεγραμμενοι εις τουτο το κηρυγμα ασεβειν την του θυ̅ ημων χαριν μετατιθεντες εις ασελγειαν και τον μονον δεσποτην θν̅ και κν̅ ημων ιν̅ χν̅ αρνουμενοι
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'παρεισέδυσαν' [א (01), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, BHP] (weight 5.05, confidence 97%) over παρεισεδύησαν (B (03), Nestle1904). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over και (א (01)). [Lexical, morphological, or word-order variant] Adopted 'χάριτα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over χάριν (א (01), RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over θεὸν (RP2018 (Byz), TR (KJTR)). Also normalised 28 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `93.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
  - `SRGNT`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `SBLGNT`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
  - `BHP`: ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `Nestle1904`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ἅπαξ πάντα, ὅτι Κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
  - `RP2018 (Byz)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ κύριος, λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `TR (KJTR)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος, λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `B (03)`: υπομνησαι δε υμασ βουλομαι ειδοτασ υμασ απαξ παντα οτι ισ̅ λαον εκ γησ αιγυπτου σωσασ το δευτερον τουσ μη πιστευσαντασ απωλεσεν
  - `א (01)`: υπομνησαι δε υμασ βουλομαι ειδοτασ υμασ παντα οτι κσ̅ απαξ λαον εκ γησ αιγυπτου σωσασ το δευτερον τουσ μη πιστευσαντασ απωλεσεν
  - `NA28 (TAGNT)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ πάντα, ὅτι ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `THGNT`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ἅπαξ πάντα, ὅτι ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `WH1881`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ἅπαξ πάντα, ὅτι Κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
  - `Tisch8`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ἅπαξ πάντα, ὅτι κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας τὸ δεύτερον τοὺς μὴ πιστεύσαντες ἀπώλεσεν,
  - `TCGNT (Byz)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `PT1904 (Byz)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν,
  - `TR-Scrivener (1894)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος, λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος, λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν.
  - `TR-Stephanus (1550)`: ὑπομνῆσαι δὲ ὑμᾶς βούλομαι, εἰδότας ὑμᾶς ἅπαξ τοῦτο, ὅτι ὁ Κύριος λαὸν ἐκ γῆς Αἰγύπτου σώσας, τὸ δεύτερον τοὺς μὴ πιστεύσαντας ἀπώλεσεν·
  - `TR-Elzevir (1624)`: υπομνησαι δε υμας βουλομαι ειδοτας υμας απαξ τουτο οτι ο κυριος λαον εκ γης αιγυπτου σωσας το δευτερον τους μη πιστευσαντας απωλεσεν
  - `𝔓72`: υπομνησε δε υμασ βουλομαι ειδοτασ απαξ παντασ οτι θσ̅ χρσ̅ λαον εγ γησ εγυπτου σωσασ το δευτερον τουσ μη πειστευσαντασ απωλεσεν
  - `A (02)`: υπομνησαι δε υμασ βουλομαι ειδοτασ απαξ παντα οτι ισ̅ λαον εκ γησ αιγυπτου σωσασ το δευτερον τουσ μη πιστευσαντασ απωλεσεν
  - `C (04)`: υπομνησει ουν υμασ βουλομαι ειδοτασ παντα οτι ο … απαξ λαον εκ γησ αιγυπτου σωσασ το δευτερον τουσ μη πιστευσαντασ απωλεσεν
  - `Ψ (044)`: υπομνησαι ουν υμας βουλομαι ειδοτας παντα οτι κς̅ απαξ λαον εκ της αιγυπτου σωσας το δευτερον τους μη πιστευσαντας απωλεσεν
- **Philological Rationale:** [Omission in some witnesses] Adopted 'ὑμᾶς' [B (03), א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.03, confidence 99%) over om. (Nestle1904). [Omission in some witnesses] Adopted 'ἅπαξ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Lexical, morphological, or word-order variant] Adopted 'πάντα' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over τοῦτο (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'Ἰησοῦς' [B (03), SRGNT, SBLGNT, BHP] (weight 3.75, confidence 96%) over ὁ κύριος (RP2018 (Byz), TR (KJTR)); κσ̅ απαξ (= κύριοσ απαξ) (א (01)); Κύριος (Nestle1904). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `SRGNT`: Ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας, δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν.
  - `SBLGNT`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `BHP`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας, δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `Nestle1904`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `RP2018 (Byz)`: Ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχήν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν.
  - `TR (KJTR)`: Ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας. Δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν
  - `B (03)`: αγγελουσ τε τουσ μη τηρησαντασ την εαυτων αρχην αλλα απολιποντασ το ιδιον οικητηριον εισ κρισιν μεγαλησ ημερασ δεσμοισ αιδιοισ υπο ζοφον τετηρηκεν
  - `א (01)`: αγγελουσ τε τουσ μη τηρησαντασ την εαυτων αρχην αλλα απολιποντασ το ιδιον οικητηριον εισ κρισιν μεγαλησ ημερασ δεσμοισ αιδιοισ υπο ζοφον τετηρηκεν
  - `NA28 (TAGNT)`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλ᾽ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `THGNT`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `WH1881`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `Tisch8`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `TCGNT (Byz)`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχήν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `PT1904 (Byz)`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχήν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `TR-Scrivener (1894)`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχήν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχήν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν.
  - `TR-Stephanus (1550)`: ἀγγέλους τε τοὺς μὴ τηρήσαντας τὴν ἑαυτῶν ἀρχὴν, ἀλλὰ ἀπολιπόντας τὸ ἴδιον οἰκητήριον, εἰς κρίσιν μεγάλης ἡμέρας, δεσμοῖς ἀϊδίοις ὑπὸ ζόφον τετήρηκεν·
  - `TR-Elzevir (1624)`: αγγελους τε τους μη τηρησαντας την εαυτων αρχην αλλα απολιποντας το ιδιον οικητηριον εις κρισιν μεγαλης ημερας δεσμοις αιδιοις υπο ζοφον τετηρηκεν
  - `𝔓72`: αγγελουσ τε τουσ μη τηρησαντασ την εαυτων αρχην αλλα απολειποντασ το ιδιον οικητηριον εισ κρισιν μεγαλησ ημερασ δεσμοισ αειδειοισ υπο ζοφον τετηρηκεν
  - `A (02)`: αγγελουσ δε τουσ μη τηρησαντασ την εαυτων αρχην αλλα απολιποντασ το ιδιον οικητηριον εισ κρισιν μεγαλησ ημερασ δεσμοισ αιδιοισ υπο ζοφον τετηρηκεν
  - `C (04)`: αγγελουσ τε τουσ μη τηρησαντασ την εαυτων αρχην αλλ απολιποντασ το ιδιον οικητηριον εισ κρισιν μεγαλησ ημερασ δεσμοισ αιδιοισ υπο ζοφον τετηρηκεν
  - `Ψ (044)`: αγγελους τε τους μη τηρησαντας την εαυτων αρχην αλλ απολιπόντας το ιδιον κατοικητηριον εις κρισιν μεγαλης ημερας δεσμοις αιδιοις υπο ζοφον τετηρηκεν
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 21 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 7 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `SRGNT`: Ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `SBLGNT`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `BHP`: ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `Nestle1904`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `RP2018 (Byz)`: Ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TR (KJTR)`: Ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις τὸν ὅμοιον τούτοις τρόπον, ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `B (03)`: ωσ σοδομα και γομορρα και αι περι αυτασ πολεισ τον ομοιον τροπον τουτοισ εκπορνευσασαι και απελθουσαι οπισω σαρκοσ ετερασ προκεινται δειγμα πυροσ αιωνιου δικην υπεχουσαι
  - `א (01)`: ωσ σοδομα και γομορρα και αι περι αυτασ πολεισ τον ομοιον τροπον τουτοισ εκπορνευσασαι και απελθουσαι οπισω σαρκοσ ετερασ προκινται δε διγμα πυροσ αιωνιου δικην ουκ εχουσιν
  - `NA28 (TAGNT)`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `THGNT`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `WH1881`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `Tisch8`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τρόπον τούτοις ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TCGNT (Byz)`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `PT1904 (Byz)`: ὡς Σόδομα καὶ Γόμορρα καὶ αἱ περὶ αὐτὰς πόλεις τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TR-Scrivener (1894)`: ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὡς Σόδομα καὶ Γόμορρα, καὶ αἱ περὶ αὐτὰς πόλεις, τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TR-Stephanus (1550)`: ὡς Σόδομα καὶ Γόμοῤῥα, καὶ αἱ περὶ αὐτὰς πόλεις τὸν ὅμοιον τούτοις τρόπον ἐκπορνεύσασαι, καὶ ἀπελθοῦσαι ὀπίσω σαρκὸς ἑτέρας, πρόκεινται δεῖγμα, πυρὸς αἰωνίου δίκην ὑπέχουσαι.
  - `TR-Elzevir (1624)`: ως σοδομα και γομορρα και αι περι αυτας πολεις τον ομοιον τουτοις τροπον εκπορνευσασαι και απελθουσαι οπισω σαρκος ετερας προκεινται δειγμα πυρος αιωνιου δικην υπεχουσαι
  - `𝔓72`: ωσ σοδομα και γομορα και ε περει αυτασ πολεισ τον ομοιον τροπον τουτοισ εκπορνευσασθαι και απελθουσε οπισω σαρκοσ τερασ προσκειντε διγμα πυροσ εωνιου δικην υπεχουσαι
  - `A (02)`: ωσ σοδομα και γομορρα και αι περι αυτασ πολεισ τον ομοιον τροπον τουτοισ εκπορνευσασαι και απελθουσαι οπισω σαρκοσ ετερασ προκεινται διγμα πυροσ αιωνιου δικην υπερεχουσαι
  - `C (04)`: ωσ σοδομα … αι περι αυτασ πολεισ τον ομοιον τροπον τουτοισ εκπορνευσασαι και απελθουσαι οπισω σαρκοσ ετερασ προκεινται δειγμα πυροσ αιωνιου δικην υπεχουσαι
  - `Ψ (044)`: ως σοδομα και γομορρα και αι περι αυτας πολεις τον ομοιον τροπον αυτοις εκπορνευσασαι και απελθουσαι οπισω σαρκος ετερας προκεινται δειγμα πυρος αιωνιου δικην υπεχουσαι
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'τρόπον τούτοις' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over τούτοις τρόπον (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'δεῖγμα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over δε διγμα (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ὑπέχουσαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ουκ εχουσιν (א (01)). Also normalised 21 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 8 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `SRGNT`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι, σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `SBLGNT`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `BHP`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι, σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `Nestle1904`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `RP2018 (Byz)`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `TR (KJTR)`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `B (03)`: ομοιωσ μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσιν κυριοτητα δε αθετουσιν δοξασ δε βλασφημουσιν
  - `א (01)`: ομοιωσ μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσιν κυριοτητασ δε αθετουσιν δοξασ δε βλασφημουσιν
  - `NA28 (TAGNT)`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `THGNT`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `WH1881`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `Tisch8`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσιν, κυριότητα δὲ ἀθετοῦσιν, δόξας δὲ βλασφημοῦσιν.
  - `TCGNT (Byz)`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσι, κυριότητα δὲ ἀθετοῦσι, δόξας δὲ βλασφημοῦσιν.
  - `PT1904 (Byz)`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσι, κυριότητα δὲ ἀθετοῦσι, δόξας δὲ βλασφημοῦσιν.
  - `TR-Scrivener (1894)`: ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσι, κυριότητα δὲ ἀθετοῦσι, δόξας δὲ βλασφημοῦσιν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσι, κυριότητα δὲ ἀθετοῦσι, δόξας δὲ βλασφημοῦσιν.
  - `TR-Stephanus (1550)`: Ὁμοίως μέντοι καὶ οὗτοι ἐνυπνιαζόμενοι σάρκα μὲν μιαίνουσι, κυριότητα δὲ ἀθετοῦσι, δόξας δὲ βλασφημοῦσιν.
  - `TR-Elzevir (1624)`: ομοιως μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσιν κυριοτητα δε αθετουσιν δοξας δε βλασφημουσιν
  - `𝔓72`: ομοιωσ μεντοι και ουτοι ενυπνιαζομενοι σαρκα μειενουσιν κυριοτητα δε αθετουσι δοξασ δε βασφημουσιν
  - `A (02)`: ομωσ μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσιν κυριοτητα δε αθετουσιν δοξασ δε βλασφημουσιν
  - `C (04)`: ομοιωσ μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσι κυριοτητα δε αθετουσιν δοξασ δε βλασφημουσιν
  - `Ψ (044)`: ομοιως μεντοι και ουτοι ενυπνιαζομενοι σαρκα μεν μιαινουσι κυριοτητας δε αθετουσι δοξας δε βλασφημουσιν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'κυριότητα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over κυριοτητασ (א (01)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 9 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν· Ἐπιτιμήσαι σοι κύριος.
  - `SRGNT`: Ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος, διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν, “Ἐπιτιμήσαι σοι Κύριος.”
  - `SBLGNT`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν· Ἐπιτιμήσαι σοι κύριος.
  - `BHP`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος, διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν, “ἐπιτιμήσαι σοι Κύριος.”
  - `Nestle1904`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν Ἐπιτιμήσαι σοι Κύριος.
  - `RP2018 (Byz)`: Ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλ’ εἶπεν, Ἐπιτιμήσαι σοι κύριος.
  - `TR (KJTR)`: Ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλʼ εἶπεν, Ἐπιτιμήσαι σοι Κύριος.
  - `B (03)`: οτε μειχαηλ ο αρχαγγελοσ τοτε τω διαβολω διακρεινομενοσ διελεγετο περι του μωυσεωσ σωματοσ ουκ ετολμησεν κρισιν επενεγκειν βλασφημιασ αλλα ειπεν επιτειμησαι εν σοι κσ̅
  - `א (01)`: ο δε μιχαηλ ο αρχαγγελοσ οτε τω διαβολω διακρινομενοσ διελεγετο περι του μωυσεωσ σωματοσ ουκ ετολμησεν κρισιν επενεγκειν βλασφημιασ αλλ ειπεν επιτιμησε σοι ο θσ̅
  - `NA28 (TAGNT)`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας ἀλλ᾽ εἶπεν· ἐπιτιμήσαι σοι κύριος.
  - `THGNT`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας ἀλλὰ εἶπεν· ἐπιτιμήσαι σοι κύριος.
  - `WH1881`: Ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωυσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν Ἐπιτιμήσαι σοι Κύριος.
  - `Tisch8`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωϋσέως σώματος, οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν, ἐπιτιμήσαι σοι κύριος.
  - `TCGNT (Byz)`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωσέως σώματος, οὐκ ἐτόλμησε κρίσιν ἐπενεγκεῖν βλασφημίας ἀλλ᾽ εἶπεν, Ἐπιτιμήσαι σοι Κύριος.
  - `PT1904 (Byz)`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωσέως σώματος, οὐκ ἐτόλμησε κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλ᾽ εἶπεν· ἐπιτιμήσαι σοι Κύριος .
  - `TR-Scrivener (1894)`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωσέως σώματος, οὐκ ἐτόλμησε κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλ᾽ εἶπεν, Ἐπιτιμήσαι σοι Κύριος.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος, ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωσέως σώματος, οὐκ ἐτόλμησε κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλ᾿ εἶπεν, Ἐπιτιμήσαι σοι Κύριος.
  - `TR-Stephanus (1550)`: ὁ δὲ Μιχαὴλ ὁ ἀρχάγγελος ὅτε τῷ διαβόλῳ διακρινόμενος διελέγετο περὶ τοῦ Μωσέως σώματος, οὐκ ἐτόλμησε κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλʼ εἶπεν, Ἐπιτιμήσαι σοι Κύριος.
  - `TR-Elzevir (1624)`: ο δε μιχαηλ ο αρχαγγελος οτε τω διαβολω διακρινομενος διελεγετο περι του μωσεως σωματος ουκ ετολμησεν κρισιν επενεγκειν βλασφημιας αλλ ειπεν επιτιμησαι σοι κυριος
  - `𝔓72`: ο δε μιχαησ ο αρχαγγελοσ οτε τω διαβολω διακρινομενοσ διελεγετο περι του μουσεωσ σωματοσ ουκ ετολμησεν κρισιν επενεγκειν βλασφημιασ αλλα ειπεν επειτειμησαι σοι κσ̅
  - `A (02)`: ο δε μιχαηλ ο αρχαγγελοσ οτε τω διαβολω διεκρινομενοσ διελεγετο περι του μωσεωσ σωματοσ ουκ ετολμησεν κρισιν επενεγκειν βλασφημειασ αλλα ειπεν επιτιμησαι σοι κσ̅
  - `C (04)`: ο δε μιχαηλ ο αρχαγγελοσ οτε τω διαβολω διακρινομενοσ διελεγετο περι του μωυσεωσ σωματοσ ουκ ετολμησεν κρισιν επενεγκειν βλασφημιασ αλλ ειπεν επιτιμησαι σοι κσ̅
  - `Ψ (044)`: ο δε μιχαηλ ο αρχαγγελος οτε τω διαβολω διακρινομενος διελεγετο περι του μωσεως σωματος ουκ ετολμησεν κρισιν υπενεγκειν βλασφημιας αλλα ειπενεπιτιμησαι εν σοι κς̅
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ὁ δὲ Μιχαὴλ' [א (01), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP] (weight 5.95, confidence 99%) over οτε μειχαηλ (B (03)). [Lexical, morphological, or word-order variant] Adopted 'ὅτε' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over τοτε (B (03)). [Lexical, morphological, or word-order variant] Adopted 'Ἐπιτιμήσαι' [SRGNT, SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR), BHP] (weight 4.99, confidence 99%) over επιτειμησαι εν (B (03)); επιτιμησε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'κύριος' [B (03), SRGNT, Nestle1904, BHP, TR (KJTR), SBLGNT, RP2018 (Byz)] (weight 5.97, confidence 99%) over ο θσ̅ (= ο θσ) (א (01)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `SRGNT`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `SBLGNT`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `BHP`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `Nestle1904`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `RP2018 (Byz)`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν· ὅσα δὲ φυσικῶς, ὡς τὰ ἄλογα ζῷα, ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TR (KJTR)`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν: ὅσα δὲ φυσικῶς, ὡς τὰ ἄλογα ζῶα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `B (03)`: ουτοι δε οσα μεν ουκ οιδασιν βλασφημουσιν οσα δε φυσικωσ ωσ τα αλογα ζωα επιστανται εν τουτοισ φθειρονται
  - `א (01)`: ουτοι δε οσα μεν ουκ οιδασιν βλασφημουσιν οσα δε φυσικωσ ωσ τα αλογα ζωα επιστανται εν τουτοισ φθειρονται
  - `NA28 (TAGNT)`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν· ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `THGNT`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν· ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῶα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `WH1881`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `Tisch8`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασιν βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TCGNT (Byz)`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασι βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `PT1904 (Byz)`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασι βλασφημοῦσιν, ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῷα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TR-Scrivener (1894)`: οὗτοι δὲ ὅσα μὲν οὐκ οἴδασι βλασφημοῦσιν· ὅσα δὲ φυσικῶς, ὡς τὰ ἄλογα ζῶα, ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασι βλασφημοῦσιν· ὅσα δὲ φυσικῶς, ὡς τὰ ἄλογα ζῷα, ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TR-Stephanus (1550)`: Οὗτοι δὲ ὅσα μὲν οὐκ οἴδασι, βλασφημοῦσιν· ὅσα δὲ φυσικῶς ὡς τὰ ἄλογα ζῶα ἐπίστανται, ἐν τούτοις φθείρονται.
  - `TR-Elzevir (1624)`: ουτοι δε οσα μεν ουκ οιδασιν βλασφημουσιν οσα δε φυσικως ως τα αλογα ζωα επιστανται εν τουτοις φθειρονται
  - `𝔓72`: ουτοι δε οσα μεν ουκ υδασιν βασφημουσιν οσα δε φυσικωσ ωσ τα αλογα ζωα επειστανται εν τουτοισ φθιρονται
  - `A (02)`: ουτοι δε οσα μεν ουκ οιδασιν βλασφημουσιν οσα δε φυσικωσ ωσ τα αλογα ζωα επιστανται εν τουτοισ φθειρονται
  - `C (04)`: ουτοι δε οσα μεν ουκ οιδασιν βλασφημουσιν οσα δε φυσικωσ ωσ τα αλογα ζωα επιστανται εν τουτοισ φθειρονται
  - `Ψ (044)`: ουτοι δε οσα μεν ουκ οιδασι βλασφημουσιν οσα δε φυσικως ως τα αλογα ζωα επιστανται εν τουτοις διαφθειρονται
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 18 surface variation(s) (Accentuation / capitalisation / breathing convention; Non-morphological iota-subscript convention (αἴρω aorist / κἀγώ / ἀθῷος / ζῷον / ᾠδή / σῴζω)).

### Verse 11 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `SRGNT`: Οὐαὶ αὐτοῖς! Ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `SBLGNT`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `BHP`: οὐαὶ αὐτοῖς! ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `Nestle1904`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `RP2018 (Byz)`: Οὐαὶ αὐτοῖς· ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `TR (KJTR)`: Οὐαὶ αὐτοῖς! ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `B (03)`: ουαι αυτοισ οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν και τη αντιλογια του κορε απωλοντο
  - `א (01)`: ουαι αυτοισ οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν και τη αντιλογια του κορε απωλοντο
  - `NA28 (TAGNT)`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `THGNT`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν καὶ τῇ ἀντιλογίᾳ τοῦ κορὲ ἀπώλοντο.
  - `WH1881`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Καὶν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κορὲ ἀπώλοντο.
  - `Tisch8`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `TCGNT (Byz)`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κορὲ ἀπώλοντο.
  - `PT1904 (Byz)`: οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κορὲ ἀπώλοντο.
  - `TR-Scrivener (1894)`: οὐαὶ αὐτοῖς· ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κορὲ ἀπώλοντο.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὐαὶ αὐτοῖς· ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κόρε ἀπώλοντο.
  - `TR-Stephanus (1550)`: Οὐαὶ αὐτοῖς, ὅτι τῇ ὁδῷ τοῦ Κάϊν ἐπορεύθησαν, καὶ τῇ πλάνῃ τοῦ Βαλαὰμ μισθοῦ ἐξεχύθησαν, καὶ τῇ ἀντιλογίᾳ τοῦ Κορὲ ἀπώλοντο.
  - `TR-Elzevir (1624)`: ουαι αυτοις οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν και τη αντιλογια του κορε απωλοντο
  - `𝔓72`: ουαι αυτοι οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλαακ μεισθου εξεχυθησαν και τη αντιλογεια του κορε απωλοντο
  - `A (02)`: ουαι αυτοισ οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν και τη αντιλογια του κορε απωλοντο
  - `C (04)`: ουαι αυτοισ οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν …
  - `Ψ (044)`: ουαι αυτοις οτι τη οδω του καιν επορευθησαν και τη πλανη του βαλααμ μισθου εξεχυθησαν και τη αντιλογια του κορε απωλοντο
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 21 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 12 (Confidence: `95.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `SRGNT`: Οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν, σπιλάδες συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `SBLGNT`: οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `BHP`: οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν, σπιλάδες συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `Nestle1904`: Οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `RP2018 (Byz)`: Οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων παραφερόμεναι· δένδρα φθινοπωρινά, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `TR (KJTR)`: Οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι ὑμῖν, ἀφόβως ἑαυτοὺς ποιμαίνοντες: νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων περιφερόμεναι· δένδρα φθινοπωρινὰ, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `B (03)`: ουτοι εισιν οι εν ταισ αγαπαισ υμων σπιλαδεσ συνευωχουμενοι αφοβωσ εαυτουσ ποιμαινοντεσ νεφελαι ανυδροι υπο ανεμων παραφερομενοι δενδρα φθινοπωρινα ακαρπα δισ αποθανοντα εκριζωθεντα
  - `א (01)`: ουτοι εισιν γογγυσται μεμψιμυροι κα τασ επιθυμιασ αυτων πορευομενοι εν ταισ αγαπαισ υμων σπιλαδεσ συνευωχουμενοι αφοβωσ εαυτουσ ποιμαινοντεσ νεφελαι ανυδροι παντι ανεμω παραφερομεναι δενδρα φθινοπωρικα ακαρπα δισ αποθανοντα εκριζωθεντα
  - `NA28 (TAGNT)`: Οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `THGNT`: Οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `WH1881`: οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `Tisch8`: Οὗτοί εἰσιν οἱ ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινὰ ἄκαρπα δὶς ἀποθανόντα ἐκριζωθέντα,
  - `TCGNT (Byz)`: οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι· δένδρα φθινοπωρινά, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `PT1904 (Byz)`: Οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι ἀφόβως, ἑαυτοὺς ποιμαίνοντες, νεφέλαι ἄνυδροι ὑπὸ ἀνέμων παραφερόμεναι, δένδρα φθινοπωρινά, ἄκαρπα, δίς ἀποθανόντα, ἐκριζωθέντα,
  - `TR-Scrivener (1894)`: οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι ὑμῖν, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων περιφερόμεναι· δένδρα φθινοπωρινά, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `TR-Boyd (Elz/Scr/Steph)`: Οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν σπιλάδες, συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων περιφερόμεναι· δένδρα φθινοπωρινά, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `TR-Stephanus (1550)`: οὗτοί εἰσιν ἐν ταῖς ἀγάπαις ὑμῶν, σπιλάδες, συνευωχούμενοι, ἀφόβως ἑαυτοὺς ποιμαίνοντες· νεφέλαι ἄνυδροι, ὑπὸ ἀνέμων περιφερόμεναι, δένδρα φθινοπωρινὰ, ἄκαρπα, δὶς ἀποθανόντα, ἐκριζωθέντα·
  - `TR-Elzevir (1624)`: ουτοι εισιν εν ταις αγαπαις υμων σπιλαδες συνευωχουμενοι αφοβως εαυτους ποιμαινοντες νεφελαι ανυδροι υπο ανεμων περιφερομεναι δενδρα φθινοπωρινα ακαρπα δις αποθανοντα εκριζωθεντα
  - `𝔓72`: ουτοι εισιν οι εν ταισ αγαπαισ υμων σπειλαδεσ συνευχομενοι αφοβωσ αυτουσ πυμενοντεσ νεφελε ανυδροι υπο ανεμων παραφερομενοι δενδρα φθινοπωρινα ακαρπα δισ αποθανοντα εκριζωθεντα
  - `A (02)`: ουτοι εισιν οι εν ταισ απαταισ υμων σπιλαδεσ συνευωχουμενοι αφοβωσ εαυτουσ ποιμαινοντεσ νεφελαι ανυδροι υπο ανεμων παραφερομεναι δενδρα φθινοπωρινα ακαρπα δισ αποθανοντα εκριζωθεντα
  - `C (04)`: … οι … απαταισ υμων σπιλαδεσ συνευωχουμενοι υμιν αφοβωσ εαυτουσ ποιμενοντεσ νεφελαι ανυδροι υπο ανεμων παραφερομεναι δενδρα φθινοπωρινα ακαρπα … αποθανοντα εκριζωθεντα
  - `Ψ (044)`: ουτοι εισιν οι εν ταις αγαπαις υμων σπιλαδες συνευωχουμενοι αφοβως εαυτους ποιμαινοντες νεφελαι ανυδροι υπο ανεμων παραφερομενοι δενδρα φθινοπωρινα ακαρπα δις αποθανοντα εκριζωθεντα
- **Philological Rationale:** [Omission in some witnesses] Adopted 'οἱ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)); γογγυσται μεμψιμυροι κα τασ επιθυμιασ αυτων πορευομενοι (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over ὑμῖν (TR (KJTR)). [Variation unit spanning several words] Adopted 'ὑπὸ ἀνέμων' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over παντι ανεμω (א (01)). [Lexical, morphological, or word-order variant] Adopted 'παραφερόμεναι' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 5.35, confidence 99%) over παραφερομενοι (B (03)); περιφερόμεναι (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'φθινοπωρινὰ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR), RP2018 (Byz)] (weight 5.97, confidence 99%) over φθινοπωρικα (א (01)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 95% = product of 5 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 13 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `SRGNT`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `SBLGNT`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `BHP`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `Nestle1904`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `RP2018 (Byz)`: κύματα ἄγρια θαλάσσης, ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας· ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `TR (KJTR)`: Κύματα ἄγρια θαλάσσης, ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας· ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `B (03)`: κυματα αγρια θαλασσησ επαφριζοντα τασ εαυτων αισχυνασ αστερεσ πλανητεσ οισ ζοφοσ σκοτουσ εισ αιωνα τετηρηται
  - `א (01)`: αγρια κυματα θαλασσησ επαφριζοντα τασ εαυτων αισχυνασ αστερεσ πλανηται οισ ο ζοφοσ του σκοτουσ εισ αιωνα τετηρηται
  - `NA28 (TAGNT)`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `THGNT`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `WH1881`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `Tisch8`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται οἷς ὁ ζόφος τοῦ σκότους εἰς αἰῶνα τετήρηται.
  - `TCGNT (Byz)`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας· ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς τὸν αἰῶνα τετήρηται.
  - `PT1904 (Byz)`: κύματα ἄγρια θαλάσσης ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς τὸν αἰῶνα τετήρηται.
  - `TR-Scrivener (1894)`: κύματα ἄγρια θαλάσσης, ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας· ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς τὸν αἰῶνα τετήρηται.
  - `TR-Boyd (Elz/Scr/Steph)`: κύματα ἄγρια θαλάσσης, ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας· ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς τὸν αἰῶνα τετήρηται.
  - `TR-Stephanus (1550)`: κύματα ἄγρια θαλάσσης, ἐπαφρίζοντα τὰς ἑαυτῶν αἰσχύνας, ἀστέρες πλανῆται, οἷς ὁ ζόφος τοῦ σκότους εἰς τὸν αἰῶνα τετήρηται.
  - `TR-Elzevir (1624)`: κυματα αγρια θαλασσης επαφριζοντα τας εαυτων αισχυνας αστερες πλανηται οις ο ζοφος του σκοτους εις τον αιωνα τετηρηται
  - `𝔓72`: κυματα κυματα αγρια θαλασησ απαφριζοντα τασ εαυτων αισχυνασ αστερσ πλανητε οισ ζοφοσ του σκοτουσ εισ εωνα τετηρητε
  - `A (02)`: κυματα αγρια θαλασσησ επαφριζοντα τασ εαυτων αισχυνασ αστερεσ πλανητε οισ ο ζοφοσ του σκοτουσ εισ αιωνα τετηρηται
  - `C (04)`: κυματα αγια θαλασσησ απαφριζοντα τασ εαυτων αισχυνασ αστερεσ πλανηται οισ ο ζοφοσ του σκοτουσ εισ αιωνα τετηρηται
  - `Ψ (044)`: κυματα αγρια θαλασσης επαφριζοντα τας εαυτων αισχυνας αστερες πλανιται οις ο ζοφος του σκοτους εις αιωνας τετηρηται
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'κύματα ἄγρια' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αγρια κυματα (א (01)). [Variation unit spanning several words] Adopted 'πλανῆται οἷς ὁ ζόφος τοῦ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over πλανητεσ οισ ζοφοσ (B (03)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 14 (Confidence: `89.8%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· Ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `SRGNT`: Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ, Ἑνὼχ, λέγων, “Ἰδοὺ, ἦλθεν Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `SBLGNT`: Προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· Ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `BHP`: ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ, Ἑνὼχ, λέγων, “ἰδοὺ, ἦλθεν Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `Nestle1904`: Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων Ἰδοὺ ἦλθεν Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `RP2018 (Byz)`: Προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἐνώχ, λέγων, Ἰδού, ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `TR (KJTR)`: Προεφήτευσεν δὲ καὶ τούτοις, ἕβδομος ἀπὸ Ἀδὰμ, Ἑνὼχ, λέγων, Ἰδοὺ, ἦλθεν Κύριος ἐν μυριάσιν ἁγίαις αὐτοῦ,
  - `B (03)`: επροφητευσεν δε και τουτοισ εβδομοσ απο αδαμ ενωχ λεγων ιδου ηλθεν κσ̅ εν αγιαισ μυριασιν αυτου
  - `א (01)`: προεπροφητευσεν δε και τουτοισ εβδομοσ απο αδαμ ενωχ λεγων ιδου ηλθεν ο κσ̅ εν μυριασιν αγιων αγγελων
  - `NA28 (TAGNT)`: προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ
  - `THGNT`: προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ ἐνὼχ λέγων· ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ
  - `WH1881`: Ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων Ἰδοὺ ἦλθεν Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `Tisch8`: ἐπροφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων, ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `TCGNT (Byz)`: Προεφήτευσε δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἐνὼχ λέγων, Ἰδού, ἦλθε Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ
  - `PT1904 (Byz)`: προεφήτευσε δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἐνὼχ λέγων· ἰδοὺ ἦλθε Κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ,
  - `TR-Scrivener (1894)`: προεφήτευσε δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἐνώχ, λέγων, Ἰδού, ἦλθε Κύριος ἐν μυριάσιν ἁγίαις αὐτοῦ,
  - `TR-Boyd (Elz/Scr/Steph)`: Προεφήτευσε δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἐνώχ, λέγων, Ἰδού, ἦλθε Κύριος ἐν μυριάσιν ἁγίαις αὐτοῦ,
  - `TR-Stephanus (1550)`: προεφήτευσε δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ, λέγων, Ἰδοὺ ἦλθε Κύριος ἐν μυριάσιν ἁγίαις αὑτοῦ,
  - `TR-Elzevir (1624)`: προεφητευσεν δε και τουτοις εβδομος απο αδαμ ενωχ λεγων ιδου ηλθεν κυριος εν μυριασιν αγιαις αυτου
  - `𝔓72`: επροφητευσεν δε και τουτοισ εβδομοσ απο αδαμ ενωχ λεγων ιδου ηλθεν κσ̅ εν αγιων αγγελων μυριασιν
  - `A (02)`: προεφητευσεν και τουτοισ εβδομοσ απο αδαμ ενωχ λεγων ιδου ηλθεν κσ̅ εν αγιαισ μυριασιν αυτου
  - `C (04)`: προεφητευσεν δε και τουτοισ εβδομοσ απο αδαμ ενωχ λεγων ιδου ηλθεν κσ̅ εν μυριασιν αγιαισ αυτου
  - `Ψ (044)`: προεφητευσεν δε και τουτοις εβδομος απο αδαμ ενωχ λεγων ιδου ηλθεν κς̅ εν αγιαις μυριασιν αγγελων
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Ἐπροφήτευσεν' [B (03), SRGNT, Nestle1904, BHP] (weight 3.71, confidence 94%) over Προεφήτευσεν (SBLGNT, RP2018 (Byz), TR (KJTR)); προεπροφητευσεν (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ο (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over μυριάσιν (TR (KJTR)). [Omission in some witnesses] Adopted 'ἁγίαις' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Omission in some witnesses] Adopted 'μυριάσιν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over om. (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'αὐτοῦ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αγιων αγγελων (א (01)). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 90% = product of 5 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `94.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `SRGNT`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν, ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν, ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.”
  - `SBLGNT`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `BHP`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐλέγξαι πᾶσαν ψυχὴν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν, ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν, ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.”
  - `Nestle1904`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ’ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `RP2018 (Byz)`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ’ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `TR (KJTR)`: Ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `B (03)`: ποιησαι κρισιν κατα παντων και ελεγξαι παντασ τουσ ασεβεισ περι παντων των εργων ασεβειασ αυτων ων ησεβησαν και περι παντων των σκληρων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεισ
  - `א (01)`: ποιησαι κρισιν κατα παντων και ελεγξαι πασαν ψυχην περι παντων των εργων ων ησεβησαν και περι παντων των σκληρων λογων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεισ
  - `NA28 (TAGNT)`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πᾶσαν ψυχὴν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `THGNT`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `WH1881`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `Tisch8`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν λόγων ὧν ἐλάλησαν κατ’ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `TCGNT (Byz)`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `PT1904 (Byz)`: ποιῆσαι κρίσιν κατὰ πάντων καὶ ἐλέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς .
  - `TR-Scrivener (1894)`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐξελέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾽ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `TR-Boyd (Elz/Scr/Steph)`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐξελέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν περὶ πάντων τῶν ἔργων ἀσεβείας αὐτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατ᾿ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `TR-Stephanus (1550)`: ποιῆσαι κρίσιν κατὰ πάντων, καὶ ἐξελέγξαι πάντας τοὺς ἀσεβεῖς αὐτῶν, περὶ πάντων τῶν ἔργων ἀσεβείας αὑτῶν ὧν ἠσέβησαν, καὶ περὶ πάντων τῶν σκληρῶν ὧν ἐλάλησαν κατʼ αὐτοῦ ἁμαρτωλοὶ ἀσεβεῖς.
  - `TR-Elzevir (1624)`: ποιησαι κρισιν κατα παντων και εξελεγξαι παντας τους ασεβεις αυτων περι παντων των εργων ασεβειας αυτων ων ησεβησαν και περι παντων των σκληρων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεις
  - `𝔓72`: ποιησαι κρισιν κατα παντων και ελεγξε πασαν ψυχην περει παντων σκληρων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεισ
  - `A (02)`: ποιησαι κρισιν κατα παντων και ελεγξαι παντασ τουσ ασεβεισ περι παντων των εργων ασεβειασ αυτων ων ησεβησαν και περι παντων των σκληρων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεισ
  - `C (04)`: ποιησαι κρισιν κατα παντων και ελεγξαι παντασ τουσ ασεβεισ περι παντων των εργων αυτων ων ησεβησαν και περι παντων των σκληρων λογων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεισ
  - `Ψ (044)`: ποιησαι κρισιν κατα παντων και ελεγξαι παντας τους ασεβεις περι παντων των ασεβειων αυτων ων ησεβησαν και περι παντων των σκληρων ων ελαλησαν κατ αυτου αμαρτωλοι ασεβεις
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'πάντας τοὺς ἀσεβεῖς' [B (03), SRGNT, SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR)] (weight 5.09, confidence 97%) over πᾶσαν ψυχὴν (א (01), BHP). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over αὐτῶν (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'ἀσεβείας αὐτῶν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over λογων (א (01)). Also normalised 23 orthographic/surface variation(s).
- *confidence:* Verse confidence 94% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 16 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `SRGNT`: Οὗτοί εἰσιν γογγυσταί μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `SBLGNT`: οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `BHP`: οὗτοί εἰσιν γογγυσταί μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελίας χάριν.
  - `Nestle1904`: Οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `RP2018 (Byz)`: Οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `TR (KJTR)`: Οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι· καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `B (03)`: ουτοι εισιν γογγυσται μεμψιμοιροι κατα τασ επιθυμιασ αυτων πορευομενοι και το στομα αυτων λαλει υπερογκα θαυμαζοντεσ προσωπα ωφελιασ χαριν
  - `א (01)`: ουτοι εισιν γογγυσται μεμψιμυροι κατα τασ επιθυμιασ αυτων πορευομενοι και το στομα αυτων λαλει υπερογκα θαυμαζοντεσ προσωπα ωφελειασ χαριν
  - `NA28 (TAGNT)`: οὗτοί εἰσιν γογγυσταὶ μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας ἑαυτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `THGNT`: οὗτοί εἰσιν γογγυσταὶ μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `WH1881`: Οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελίας χάριν.
  - `Tisch8`: οὗτοί εἰσιν γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `TCGNT (Byz)`: οὗτοί εἰσι γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `PT1904 (Byz)`: Οὗτοί εἰσι γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `TR-Scrivener (1894)`: οὗτοί εἰσι γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὗτοί εἰσι γογγυσταί, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὐτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα ὠφελείας χάριν.
  - `TR-Stephanus (1550)`: οὗτοί εἰσι γογγυσταὶ, μεμψίμοιροι, κατὰ τὰς ἐπιθυμίας αὑτῶν πορευόμενοι, καὶ τὸ στόμα αὐτῶν λαλεῖ ὑπέρογκα, θαυμάζοντες πρόσωπα, ὠφελείας χάριν.
  - `TR-Elzevir (1624)`: ουτοι εισιν γογγυσται μεμψιμοιροι κατα τας επιθυμιας αυτων πορευομενοι και το στομα αυτων λαλει υπερογκα θαυμαζοντες προσωπα ωφελειας χαριν
  - `𝔓72`: ουτοι εισιν γογγυστε μεμψιμοιροι και στομα αυτων λαλει υπερογκα θαυμαζοντεσ προσωπα ωφελιασ χαρειν
  - `A (02)`: ουτοι εισι γογγυσται μεμψιμυροι κατα τασ επιθυμιασ αυτων πορευομενοι και το στομα αυτω λαλει υπερογκα θαυμαζοντεσ προσωπα ωφελειασ χαριν
  - `C (04)`: ουτοι εισιν γογγυσται μεμψιμοιροι κατα τασ επιθυμιασ εαυτων πορευομενοι και το στομα αυτων λαλει υπερογκα θαυμαζοντεσ προσωπα ωφελειασ χαριν
  - `Ψ (044)`: ουτοι εισι γογγυσται μεμψιμοιροι κατα τας επιθυμιας αυτων πορευομενοι και το στομα αυτων λαλει υπερογκα θαυμαζοντες προσωπα ωφελειας χαριν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'μεμψίμοιροι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over μεμψιμυροι (א (01)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `SRGNT`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ,
  - `SBLGNT`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `BHP`: ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ,
  - `Nestle1904`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `RP2018 (Byz)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ χριστοῦ·
  - `TR (KJTR)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `B (03)`: υμεισ δε αγαπητοι μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυ̅ ημων ιυ̅ χυ̅
  - `א (01)`: υμεισ δε αγαπητοι μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυ̅ ημων ιυ̅ χυ̅
  - `NA28 (TAGNT)`: Ὑμεῖς δέ ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `THGNT`: Ὑμεῖς δὲ ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `WH1881`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `Tisch8`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `TCGNT (Byz)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `PT1904 (Byz)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `TR-Scrivener (1894)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `TR-Boyd (Elz/Scr/Steph)`: Ὑμεῖς δέ, ἀγαπητοί, μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ·
  - `TR-Stephanus (1550)`: Ὑμεῖς δὲ ἀγαπητοὶ μνήσθητε τῶν ῥημάτων τῶν προειρημένων ὑπὸ τῶν ἀποστόλων τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ,
  - `TR-Elzevir (1624)`: υμεις δε αγαπητοι μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυριου ημων ιησου χριστου
  - `𝔓72`: υμει δε αγαπητοισ μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυ̅ ημων ιηυ̅ χρυ̅
  - `A (02)`: υμεισ δε αγαπητοι μνησθητε των προειρημενων ρηματων υπο των αποστολων του κυ̅ ημων ιυ̅ χυ̅
  - `C (04)`: υμεισ δε αγαπητοι μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυ̅ ημων ιυ̅ χυ̅
  - `Ψ (044)`: υμεις δε αγαπητοι μνησθητε των ρηματων των προειρημενων υπο των αποστολων του κυ̅ ημων ιυ̅ χυ̅
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 16 surface variation(s) (Accentuation / capitalisation / breathing convention; Nomen sacrum (contracted sacred name) for the full word).

### Verse 18 (Confidence: `92.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅτι ἔλεγον ὑμῖν· Ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `SRGNT`: ὅτι ἔλεγον ὑμῖν, “Ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.”
  - `SBLGNT`: ὅτι ἔλεγον ὑμῖν· Ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `BHP`: ὅτι ἔλεγον ὑμῖν, “ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.”
  - `Nestle1904`: ὅτι ἔλεγον ὑμῖν Ἐπ’ ἐσχάτου τοῦ χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `RP2018 (Byz)`: ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται, κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TR (KJTR)`: Ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται, κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `B (03)`: οτι ελεγον υμιν επ εσχατου χρονου εσονται εμπαικται κατα τασ εαυτων επιθυμιασ πορευομενοι των ασεβειων
  - `א (01)`: οτι ελεγον υμιν επ εσχατου του χρονου εσονται εμπεκται κατα τασ επιθυμιασ αυτων πορευομενοι των ασεβειων
  - `NA28 (TAGNT)`: ὅτι ἔλεγον ὑμῖν ἐπ᾽ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `THGNT`: ὅτι ἔλεγον ὑμῖν ὅτι ἐπ᾽ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `WH1881`: ὅτι ἔλεγον ὑμῖν Ἐπʼ ἐσχάτου χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `Tisch8`: ὅτι ἔλεγον ὑμῖν· ἐπ’ ἐσχάτου τοῦ χρόνου ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TCGNT (Byz)`: ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `PT1904 (Byz)`: ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TR-Scrivener (1894)`: ὅτι ἔλεγον ὑμῖν, ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται, κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TR-Boyd (Elz/Scr/Steph)`: ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται, κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TR-Stephanus (1550)`: ὅτι ἔλεγον ὑμῖν ὅτι ἐν ἐσχάτῳ χρόνῳ ἔσονται ἐμπαῖκται, κατὰ τὰς ἑαυτῶν ἐπιθυμίας πορευόμενοι τῶν ἀσεβειῶν.
  - `TR-Elzevir (1624)`: οτι ελεγον υμιν οτι εν εσχατω χρονω εσονται εμπαικται κατα τας εαυτων επιθυμιας πορευομενοι των ασεβειων
  - `𝔓72`: οτι ελεγον υμιν οτι επ εσχατου χρονου εσονται εμπεκτε κατα τασ εαυτω επειθυμιασ πορευομενοι των ασεβιων
  - `A (02)`: οτι ελεγον υμιν οτι επ εσχατου του χρονου ελευσονται εμπεκται κατα τασ εαυτων επιθυμιασ πορευομενοι των ασεβειων
  - `C (04)`: οτι ελεγον υμιν οτι επ εσχατου χρονου εσονται εμπεκται κατα τασ εαυτων επιθυμιασ πορευομενοι των ασεβειων
  - `Ψ (044)`: οτι ελεγον υμιν επ εσχατου χρονου αναστησονται εμπαικται κατα τας αυτων επιθυμιας πορευομενοι των ασεβειων
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'Ἐπ ἐσχάτου' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ὅτι ἐν (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.19, confidence 97%) over τοῦ (א (01), Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'χρόνου' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἐσχάτῳ χρόνῳ (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐμπαῖκται' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εμπεκται (א (01)). [Variation unit spanning several words] Adopted 'ἑαυτῶν ἐπιθυμίας' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επιθυμιασ αυτων (א (01)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 5 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 19 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `SRGNT`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `SBLGNT`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `BHP`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `Nestle1904`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `RP2018 (Byz)`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `TR (KJTR)`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες ἑαυτούς, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `B (03)`: ουτοι εισιν οι αποδιοριζοντεσ ψυχικοι πνευμα μη εχοντεσ
  - `א (01)`: ουτοι εισιν οι αποδιοριζοντεσ ψυχικοι πνα̅ μη εχοντεσ
  - `NA28 (TAGNT)`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `THGNT`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `WH1881`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `Tisch8`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `TCGNT (Byz)`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `PT1904 (Byz)`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `TR-Scrivener (1894)`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες ἑαυτούς, ψυχικοί, Πνεῦμα μὴ ἔχοντες.
  - `TR-Boyd (Elz/Scr/Steph)`: Οὗτοί εἰσιν οἱ ἀποδιορίζοντες ἑαυτούς, ψυχικοί, πνεῦμα μὴ ἔχοντες.
  - `TR-Stephanus (1550)`: οὗτοί εἰσιν οἱ ἀποδιορίζοντες, ψυχικοὶ, πνεῦμα μὴ ἔχοντες.
  - `TR-Elzevir (1624)`: ουτοι εισιν οι αποδιοριζοντες εαυτους ψυχικοι πνευμα μη εχοντες
  - `𝔓72`: ουτοι εισιν οι αποδιωριζοντεσ ψυχικοι πνα̅ μη εχοντεσ
  - `A (02)`: ουτοι εισιν οι αποδιοριζοντεσ ψυχικοι πνα̅ μη εχοντεσ
  - `C (04)`: ουτοι εισιν οι αποδιοριζοντεσ εαυτουσ ψυχικοι πνευμα μη εχοντεσ
  - `Ψ (044)`: ουτοι εισιν οι αποδιοριζοντες ψυχικοι πνα̅ μη εχοντες
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over ἑαυτούς (TR (KJTR)). Also normalised 8 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 20 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `SRGNT`: Ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι.
  - `SBLGNT`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `BHP`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι.
  - `Nestle1904`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι,
  - `RP2018 (Byz)`: Ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτούς, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `TR (KJTR)`: Ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτοὺς, ἐν Πνεύματι Ἁγίω προσευχόμενοι,
  - `B (03)`: υμεισ δε αγαπητοι εποικοδομουντεσ εαυτουσ τη αγιωτατη υμων πιστει εν πνευματι αγιω προσευχομενοι
  - `א (01)`: υμεισ δε αγαπητοι εποικοδομουντεσ εαυτουσ τη αγιωτατη υμων πιστι εν πνι̅ αγιω προσευχομενοι
  - `NA28 (TAGNT)`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `THGNT`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `WH1881`: Ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `Tisch8`: ὑμεῖς δέ, ἀγαπητοί, ἐποικοδομοῦντες ἑαυτοὺς τῇ ἁγιωτάτῃ ὑμῶν πίστει, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `TCGNT (Byz)`: ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτούς, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι,
  - `PT1904 (Byz)`: Ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτούς, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι,
  - `TR-Scrivener (1894)`: ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτούς, ἐν Πνεύματι Ἁγίῳ προσευχόμενοι,
  - `TR-Boyd (Elz/Scr/Steph)`: Ὑμεῖς δέ, ἀγαπητοί, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτούς, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `TR-Stephanus (1550)`: Ὑμεῖς δὲ, ἀγαπητοὶ, τῇ ἁγιωτάτῃ ὑμῶν πίστει ἐποικοδομοῦντες ἑαυτοὺς, ἐν πνεύματι ἁγίῳ προσευχόμενοι,
  - `TR-Elzevir (1624)`: υμεις δε αγαπητοι τη αγιωτατη υμων πιστει εποικοδομουντες εαυτους εν πνευματι αγιω προσευχομενοι
  - `𝔓72`: υμισ δε αγαπητοι τη εαυτων αγιοτητι πειστι ανυκοδομεισθαι εν πντι̅ αγιω προσεχομενοι εαυτοισ
  - `A (02)`: υμεισ δε αγαπητοι εποικοδομουντεσ εαυτουσ τη αγιοτατη υμων πιστει εν πνι̅ αγιω προσευχομενοι
  - `C (04)`: ημεισ δε αγαπητοι εποικοδομουντεσ εαυτουσ τη αγιοτατη ημων πιστει εν πνι̅ αγιω προσευχομενοι
  - `Ψ (044)`: υμεις δε αγαπητοι εποικοδομουντες εαυτους τη αγιωτατη υμων πιστει εν πνι̅ αγιω προσευχομενοι
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἐποικοδομοῦντες ἑαυτούς (RP2018 (Byz), TR (KJTR)). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 21 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `SRGNT`: Ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ, εἰς ζωὴν αἰώνιον.
  - `SBLGNT`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `BHP`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν, Ἰησοῦ Χριστοῦ, εἰς ζωὴν αἰώνιον.
  - `Nestle1904`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `RP2018 (Byz)`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ χριστοῦ εἰς ζωὴν αἰώνιον.
  - `TR (KJTR)`: Ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `B (03)`: εαυτουσ εν αγαπη θυ̅ τηρησωμεν προσδεχομενοι το ελεοσ του κυ̅ ημων ιυ̅ χυ̅ εισ ζωην αιωνιον
  - `א (01)`: εαυτουσ εν αγαπη θυ̅ τηρησατε προσδεχομενοι το ελεοσ του κυ̅ ημων ιυ̅ χυ̅ εισ ζωην αιωνιον
  - `NA28 (TAGNT)`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `THGNT`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `WH1881`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `Tisch8`: ἑαυτοὺς ἐν ἀγάπῃ θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `TCGNT (Byz)`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `PT1904 (Byz)`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ, εἰς ζωὴν αἰώνιον.
  - `TR-Scrivener (1894)`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `TR-Boyd (Elz/Scr/Steph)`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ εἰς ζωὴν αἰώνιον.
  - `TR-Stephanus (1550)`: ἑαυτοὺς ἐν ἀγάπῃ Θεοῦ τηρήσατε, προσδεχόμενοι τὸ ἔλεος τοῦ Κυρίου ἡμῶν Ἰησοῦ Χριστοῦ, εἰς ζωὴν αἰώνιον·
  - `TR-Elzevir (1624)`: εαυτους εν αγαπη θεου τηρησατε προσδεχομενοι το ελεος του κυριου ημων ιησου χριστου εις ζωην αιωνιον
  - `𝔓72`: εαυτουσ εν αγαπη θυ̅ τηρησωμεν προσδεχομενοι το ελεοσ του κυ̅ εισ ζοην ημων ιηυ̅ χρυ̅ αιωνιον
  - `A (02)`: εαυτουσ εν αγαπη θυ̅ τηρησατε προσδεχομενοι το ελεοσ του κυ̅ ημων ιυ̅ χυ̅ εισ ζωην αιωνιον
  - `C (04)`: εαυτουσ εν αγαπη … τηρησωμεν προσδεχομενοι το ελεοσ του κυ̅ ημων ιυ̅ χυ̅ εισ ζωην αιωνιον
  - `Ψ (044)`: εαυτους εν αγαπη του θυ̅ τηρησωμεν προσδεχομενοι το ελεος του κυ̅ ημων ιυ̅ χυ̅ εις ζωην αιωνιον
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'τηρήσατε' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over τηρησωμεν (B (03)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 22 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
  - `SRGNT`: Καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
  - `SBLGNT`: καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
  - `BHP`: καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
  - `Nestle1904`: καὶ οὓς μὲν ἐλεᾶτε διακρινομένους
  - `RP2018 (Byz)`: Καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι·
  - `TR (KJTR)`: Καὶ οὓς μὲν ἐλεεῖτε, διακρινομένοι:
  - `B (03)`: και ουσ μεν ελεατε διακρεινομενουσ
  - `א (01)`: και ουσ μεν ελεατε διακρινομενουσ
  - `NA28 (TAGNT)`: καὶ οὓς μὲν ἐλεᾶτε διακρινομένους,
  - `THGNT`: καὶ οὓς μὲν ἐλέγχετε διακρινομένους,
  - `WH1881`: Καὶ οὓς μὲν ἐλεᾶτε διακρινομένους
  - `Tisch8`: καὶ οὓς μὲν ἐλέγχετε διακρινομένους,
  - `TCGNT (Byz)`: καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι,
  - `PT1904 (Byz)`: καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι,
  - `TR-Scrivener (1894)`: καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι·
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι·
  - `TR-Stephanus (1550)`: καὶ οὓς μὲν ἐλεεῖτε διακρινόμενοι,
  - `TR-Elzevir (1624)`: και ους μεν ελεειτε διακρινομενοι
  - `𝔓72`: ουσ μεν εκ πυροσ αρπασατε διακρινομενουσ
  - `A (02)`: και ουσ μεν ελεγχεται διακρινομενουσ
  - `C (04)`: και ουσ μεν ελεγχετε διακρινομενουσ
  - `Ψ (044)`: και ους μεν ελεατε διακρινομενους
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐλεᾶτε' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἐλεεῖτε (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'διακρινομένους' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, B (03)] (weight 5.61, confidence 99%) over διακρινόμενοι (RP2018 (Byz), TR (KJTR)). Also normalised 4 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 23 (Confidence: `92.8%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `SRGNT`: οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `SBLGNT`: οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `BHP`: οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `Nestle1904`: σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `RP2018 (Byz)`: οὓς δὲ ἐν φόβῳ σῴζετε, ἐκ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TR (KJTR)`: Οὓς δὲ ἐν φόβῳ, σώζετε ἐκ τοῦ πυρὸς ἁρπάζοντες· μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `B (03)`: σωζετε εκ πυροσ αρπαζοντεσ ουσ δε ελεατε εν φοβω μεισουντεσ και τον απο τησ σαρκοσ εσπιλωμενον χιτωνα
  - `א (01)`: ουσ δε σωζετε εκ πυροσ αρπαζετεσ ουσ δε ελεατε εν φοβω μισουντεσ και τον απο τησ σαρκοσ εσπιλωμενον χιτωνα
  - `NA28 (TAGNT)`: οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `THGNT`: οὓς δὲ σώζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `WH1881`: σώζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `Tisch8`: οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες, οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TCGNT (Byz)`: οὓς δὲ ἐν φόβῳ σῴζετε, ἐκ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `PT1904 (Byz)`: οὓς δὲ ἐν φόβῳ σῴζετε, ἐκ τοῦ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TR-Scrivener (1894)`: οὓς δὲ ἐν φόβῳ σώζετε, ἐκ τοῦ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TR-Boyd (Elz/Scr/Steph)`: οὓς δὲ ἐν φόβῳ σώζετε, ἐκ τοῦ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TR-Stephanus (1550)`: οὓς δὲ ἐν φόβῳ σώζετε, ἐκ τοῦ πυρὸς ἁρπάζοντες, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα.
  - `TR-Elzevir (1624)`: ους δε εν φοβω σωζετε εκ του πυρος αρπαζοντες μισουντες και τον απο της σαρκος εσπιλωμενον χιτωνα
  - `𝔓72`: δε ελεειτε εν φοβω μεισουντεσ και τον απο τησ σαρκοσ εσπειλωμενοι χιτωνα
  - `A (02)`: ουσ δε σωζετε εκ πυροσ αρπαζοντεσ ουσ δε ελεαται εν φοβω μεισουντεσ και τον απο τησ σαρκοσ εσπιλωμενον χιτωνα
  - `C (04)`: ουσ δε σωζετε εκ πυροσ αρπαζοντεσ εν φοβω μισουντεσ και τον απο τησ σαρκοσ εσπιλωμενον χιτωνα
  - `Ψ (044)`: ους δε σωζετε εκ πυρος αρπαζοντες ους δε ελεατε εν φοβω μισουντες και τον απο της σαρκος εσπιλωμενον χιτωνα
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'οὓς δὲ' [א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.05, confidence 97%) over om. (B (03), Nestle1904). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἐν φόβῳ (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over τοῦ (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἁρπάζοντες' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αρπαζετεσ (א (01)). [Variation unit spanning several words] Adopted 'οὓς δὲ ἐλεᾶτε ἐν φόβῳ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 93% = product of 5 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 24 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει
  - `SRGNT`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `SBLGNT`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει
  - `BHP`: τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `Nestle1904`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `RP2018 (Byz)`: Τῷ δὲ δυναμένῳ φυλάξαι αὐτοὺς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TR (KJTR)`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `B (03)`: τω δε δυναμενω φυλαξαι υμασ απταιστουσ και στησαι κατενωπιον τησ δοξησ αυτου αμωμουσ εν αγαλλιασει
  - `א (01)`: τω δε δυναμενω φυλαξαι υμασ απτεστουσ και στησαι κατενωπιον τησ δοξησ αυτου αμωμουσ εν αγαλλιασι
  - `NA28 (TAGNT)`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `THGNT`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `WH1881`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει
  - `Tisch8`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TCGNT (Byz)`: Τῷ δὲ δυναμένῳ φυλάξαι αὐτοὺς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `PT1904 (Byz)`: Τῷ δὲ δυναμένῳ φυλάξαι αὐτοὺς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TR-Scrivener (1894)`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TR-Boyd (Elz/Scr/Steph)`: Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TR-Stephanus (1550)`: Τῷ δὲ δυναμένῳ φυλάξαι αὐτοὺς ἀπταίστους, καὶ στῆσαι κατενώπιον τῆς δόξης αὑτοῦ ἀμώμους ἐν ἀγαλλιάσει,
  - `TR-Elzevir (1624)`: τω δε δυναμενω φυλαξαι υμας απταιστους και στησαι κατενωπιον της δοξης αυτου αμωμους εν αγαλλιασει
  - `𝔓72`: τω δε δυναμενω στηριξαι ασπειλουσ αμωμουσ αγνευομενουσ απεναντι τησ δοξησ αυτου εν αγαλλιασι
  - `A (02)`: τω δε δυναμενω φυλαξαι ημασ απταιστουσ και στησαι κατενωπιον τησ δοξησ αυτου αμεμπτουσ εν αγαλλιασει
  - `C (04)`: τω δε δυναμενω φυλαξαι υμασ απταιστουσ και απιλουσ στησαι ενωπιον τησ δοξησ αυτου αμωμουσ εν αγαλλιασει
  - `Ψ (044)`: τω δε δυναμενω φυλαξαι υμας απταιστους και στησαι κατενωπιον της δοξης αυτου αμωμους εν αγαλλιασει
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ὑμᾶς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over αὐτοὺς (RP2018 (Byz)). [Lexical, morphological, or word-order variant] Adopted 'ἀπταίστους' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απτεστουσ (א (01)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 25 (Confidence: `94.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `SRGNT`: μόνῳ Θεῷ Σωτῆρι ἡμῶν, διὰ Ἰησοῦ Χριστοῦ τοῦ Κυρίου ἡμῶν, δόξα, μεγαλωσύνη, κράτος, καὶ ἐξουσία, πρὸ παντὸς τοῦ αἰῶνος, καὶ νῦν, καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν!
  - `SBLGNT`: μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `BHP`: μόνῳ Θεῷ Σωτῆρι ἡμῶν, διὰ Ἰησοῦ Χριστοῦ τοῦ Κυρίου ἡμῶν, δόξα, μεγαλωσύνη, κράτος, καὶ ἐξουσία, πρὸ παντὸς τοῦ αἰῶνος, καὶ νῦν, καὶ εἰς πάντας τοὺς αἰῶνας. ἀμήν!
  - `Nestle1904`: μόνῳ Θεῷ Σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ Κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `RP2018 (Byz)`: μόνῳ σοφῷ θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν.
  - `TR (KJTR)`: Μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν.
  - `B (03)`: μονω θω̅ σωτηρι ημων δια ιυ̅ χυ̅ του κυ̅ ημων δοξα μεγαλωσυνη κρατοσ και εξουσια προ παντοσ του αιωνοσ και νυν και εισ παντασ τουσ αιωνασ αμην
  - `א (01)`: μονω θω̅ σωτηρι ημων δια ιυ̅ χυ̅ του κυ̅ ημων ω δοξα μεγαλωσυνη κρατοσ και εξουσια προ παντοσ του αιωνοσ και νυν και εισ τουσ αιωνασ αμην
  - `NA28 (TAGNT)`: μόνῳ θεῷ σωτῆρι ἡμῶν, διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν, δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας, ἀμήν.
  - `THGNT`: μόνῳ θεῷ σωτῆρι ἡμῶν, διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν, δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας, ἀμήν.
  - `WH1881`: μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `Tisch8`: μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `TCGNT (Byz)`: μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν.
  - `PT1904 (Byz)`: μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
  - `TR-Scrivener (1894)`: μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. ἀμήν.
  - `TR-Boyd (Elz/Scr/Steph)`: μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν, δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν.
  - `TR-Stephanus (1550)`: μόνῳ σοφῷ Θεῷ σωτῆρι ἡμῶν δόξα καὶ μεγαλωσύνη, κράτος καὶ ἐξουσία, καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας. Ἀμήν.
  - `TR-Elzevir (1624)`: μονω σοφω θεω σωτηρι ημων δοξα και μεγαλωσυνη κρατος και εξουσια και νυν και εις παντας τους αιωνας αμην
  - `𝔓72`: μονω θω̅ ημων αυτω δοξα κρατοσ τιμη δια ιηυ̅ χρυ̅ του κυ̅ ω ημων αυτω δοξα και μεγαλοσυνη και νυν και εισ τουσ παντασ εωνασ αμην
  - `A (02)`: μονω θω̅ σρι̅ ημων δια ιυ̅ χυ̅ του κυ̅ ημων δοξα μεγαλωσυνη κρατοσ και εξουσια προ παντοσ του αιωνοσ και νυν και εισ παντασ τουσ αιωνασ αμην
  - `C (04)`: μονω θω̅ σρι̅ ημων δια ιυ̅ χυ̅ του κυ̅ ημων δοξα μεγαλωσυνη κρατοσ και εξουσια προ παντοσ του αιωνοσ και νυν και εισ παντασ τουσ αιωνασ αμην
  - `Ψ (044)`: μονω θω̅ σρι̅ ημων δια ιυ̅ χυ̅ του κυ̅ ημων δοξα μεγαλωσυνη κρατος εξουσια προ παντος του αιωνος και νυν και εις παντας τους αιωνας αμην
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over σοφῷ (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν' [B (03), א (01), SRGNT, Nestle1904, BHP, SBLGNT] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ω (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'πρὸ παντὸς τοῦ αἰῶνος' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'πάντας' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 94% = product of 6 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
