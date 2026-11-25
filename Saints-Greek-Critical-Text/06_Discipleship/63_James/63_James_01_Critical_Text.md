# James 01 — Saints Greek Critical Text

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
| **33** | Minuscule 33 — Queen of the Cursives (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 | Premier Alexandrian Minuscule (Gospels, Acts, Epistles) |

### Disregarded / Quarantined Sources (Excluded by AI Gatekeeper)
| Source | Status | Reason Excluded from Open Critical Text |
| :--- | :---: | :--- |
| Pickering-f35 | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-ND (Tier 5 — Owner-Authorized Apparatus)) — held in local Studio only; excluded from public open-licence exports. |
| Tregelles (1879) | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-SA 3.0 (Owner-Authorized Apparatus Witness)) — held in local Studio only; excluded from public open-licence exports. |

---

## Section II — Continuous Greek Critical Text

**1** Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
**2** Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
**3** γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
**4** ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
**5** Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ·
**6** αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος, ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ·
**7** μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου
**8** ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
**9** Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
**10** ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
**11** ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
**12** Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
**13** μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
**14** ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
**15** εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
**16** μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
**17** Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
**18** βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
**19** Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν,
**20** ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
**21** διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
**22** Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
**23** ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ,
**24** κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
**25** ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
**26** Εἴ τις δοκεῖ θρησκὸς εἶναι μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
**27** θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### James 1:1
- *Disregarded Surface Variant:* kept `Ἰάκωβος` over `ιακωβοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Ἰησοῦ` over `ιυ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `Χριστοῦ` over `χυ̅`, `χριστοῦ` (B (03), RP2018 (Byz), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `δοῦλος` over `δουλοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δώδεκα` over `δωδεκα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυλαῖς` over `φυλαισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διασπορᾷ` over `διασπορα`, `Διασπορᾷ` (B (03), Nestle1904, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαίρειν.` over `χαιρειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:2
- **Apparatus:** `ἡγήσασθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ηγησασθαι** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `περιπέσητε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **περιπεσηται** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ποικίλοις,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πυκιλοισ** A (02) ; **ποικιλαισ** C (04)
- *Disregarded Surface Variant:* kept `Πᾶσαν` over `πασαν`, `πᾶσαν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαρὰν` over `χαραν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μου,` over `μου` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ὅταν` over `οταν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πειρασμοῖς` over `πειρασμοισ`, `πιρασμοισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ποικίλοις,` over `ποικιλοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:3
- **Apparatus:** `κατεργάζεται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κατεργαζετε** A (02)
- *Disregarded Surface Variant:* kept `γινώσκοντες` over `γεινωσκοντεσ`, `γινωσκοντεσ`, `Γινώσκοντες,` (B (03), TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοκίμιον` over `δοκιμιον`, `δοκιμειον` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστεως` over `πιστεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατεργάζεται` over `κατεργαζεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπομονήν·` over `υπομονην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:4
- *Disregarded Surface Variant:* kept `ἡ` over `η`, `Ἡ` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπομονὴ` over `υπομονη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργον` over `εργον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τέλειον` over `τελειον`, `τελιον` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐχέτω,` over `εχετω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἵνα` over `ινα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦτε` over `ητε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τέλειοι` over `τελειοι`, `τελιοι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁλόκληροι,` over `ολοκληροι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μηδενὶ` over `μηδενι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λειπόμενοι.` over `λειπομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:5
- **Apparatus:** `λείπεται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **λειπετε** A (02)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **θυ̅ του (= θεοῦ του)** A (02)
- **Apparatus:** `θεοῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** A (02)
- **Apparatus:** `μὴ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) A (02) C (04) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **οὐκ** RP2018 (Byz) PT1904 (Byz) TCGNT (Byz) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Εἰ` over `ει`, `εἰ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δέ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τις` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λείπεται` over `λειπεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοφίας,` over `σοφιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰτείτω` over `αιτειτω`, `αιτιτω` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `παρὰ` over `παρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διδόντος` over `διδοντοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ,`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `πᾶσιν` over `πασιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁπλῶς` over `απλωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀνειδίζοντος,` over `ονειδιζοντοσ`, `ονιδιζοντοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοθήσεται` over `δοθησεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῷ·` over `αυτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:6
- *Disregarded Surface Variant:* kept `αἰτείτω` over `αιτειτω`, `Αἰτείτω` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πίστει,` over `πιστει`, `πιστι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `μηδὲν` over `μηδεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διακρινόμενος,` over `διακρεινομενοσ`, `διακρινομενοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διακρινόμενος` over `διακρεινομενοσ`, `διακρινομενοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἔοικεν` over `εοικε`, `εοικεν` (B (03), א (01)) — *Euphonic movable-nu (-ν) variation*
- *Disregarded Surface Variant:* kept `κλύδωνι` over `κλυδωνι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θαλάσσης` over `θαλασσησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνεμιζομένῳ` over `ανεμιζομενω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥιπιζομένῳ·` over `ρειπιζομενω`, `ριπιζομενω` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### James 1:7
- **Apparatus:** `λήμψεταί` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **λημψετε** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `μὴ` over `μη`, `Μὴ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἰέσθω` over `οιεσθω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωπος` over `ανθρωποσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκεῖνος` over `εκεινοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λήμψεταί` over `λημψεται`, `λήψεταί` (B (03), RP2018 (Byz), TR (KJTR)) — *Spelling variant pooled before the vote with the reading 'λήμψεταί' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `παρὰ` over `παρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου,`, `Κυρίου.` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### James 1:8
- *Disregarded Surface Variant:* kept `ἀνὴρ` over `ανηρ`, `Ἀνὴρ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίψυχος,` over `διψυχοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκατάστατος` over `ακαταστατοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάσαις` over `πασαισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁδοῖς` over `οδοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ.` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:9
- **Apparatus:** `ὁ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Καυχάσθω` over `καυχασθω`, `καυχάσθω` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφὸς` over `αδελφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταπεινὸς` over `ταπεινοσ`, `ταπινοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὕψει` over `υψει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ,` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:10
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλούσιος` over `πλουσιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταπεινώσει` over `ταπεινωσι`, `ταπινωσει` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτοῦ,` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθος` over `ανθοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χόρτου` over `χορτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρελεύσεται.` over `παρελευσεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:11
- **Apparatus:** `αὐτοῦ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτοῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εαυτου** C (04)
- *Disregarded Surface Variant:* kept `ἀνέτειλεν` over `ανετειλεν`, `ανετιλεν`, `Ἀνέτειλεν` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἥλιος` over `ηλιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σὺν` over `συν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καύσωνι` over `καυσωνι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξήρανεν` over `εξηρανε`, `εξηρανεν` (B (03), א (01)) — *Euphonic movable-nu (-ν) variation*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χόρτον,` over `χορτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθος` over `ανθοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξέπεσεν` over `εξεπεσεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐπρέπεια` over `ευπρεπεια`, `ευπρεπια` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προσώπου` over `προσωπου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπώλετο·` over `απωλετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὕτως` over `ουτωσ`, `Οὕτως` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλούσιος` over `πλουσιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πορείαις` over `πορειαισ`, `ποριαισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μαρανθήσεται.` over `μαρανθησεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω`, `οὕτως / οὕτω` (PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Movable final sigma (οὕτω/οὕτως type)*

### James 1:12
- **Apparatus:** `ἀνὴρ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ανοσ̅ (= ανοσ)** A (02)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ὁ κύριος** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **κσ̅ (= κύριοσ)** C (04) *(omission / addition)*
  - *scribal tendency: expansion of a sacred name or title:* 'ὁ κύριος' is a typical scribal expansion of a sacred name or title; such additions are more likely than omissions.
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Μακάριος` over `μακαριοσ`, `μακάριος` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνὴρ` over `ανηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃς` over `οσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπομένει` over `υπομενει`, `υπομενι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `πειρασμόν,` over `πειρασμον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόκιμος` over `δοκιμοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γενόμενος` over `γενομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λήμψεται` over `λημψεται`, `λήψεται`, `λήψεταί` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Nasal spelling (λημψ- / ληψ-)*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στέφανον` over `στεφανον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ζωῆς,` over `ζωησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃν` over `ον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπηγγείλατο` over `επηγγειλατο`, `επηγγιλατο` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπῶσιν` over `αγαπωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτόν.` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `λήμψεται / ληψεται`, `λήμψεται / λήψεται`, `λήμψεται / λήψεται`, `λήμψεται / λήψεται`, `λήμψεται / λήψεται`, `λήμψεται / ληψεται`, `λήμψεται / λήψεται`, `λήμψεται / λήψεται` (C (04), PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Nasal spelling (λημψ- / ληψ-)*

### James 1:13
- **Apparatus:** `Ἀπὸ` B (03) SRGNT SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) BHP A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 WH1881 **]** **υπο** א (01) ; **Ἀπὸ τοῦ** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `μηδεὶς` over `μηδεισ`, `μηδισ`, `Μηδεὶς` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `πειραζόμενος` over `πειραζομενοσ`, `πιραζομενοσ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `λεγέτω` over `λεγετω`, `Λεγέτω,` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `πειράζομαι·` over `πειραζομαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸς` over `θσ̅`, `Θεὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἀπείραστός` over `απειραστοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κακῶν,` over `κακων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πειράζει` over `πειραζει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸς` over `αυτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐδένα.` over `ουδενα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:14
- **Apparatus:** `πειράζεται` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πιραζετε** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἕκαστος` over `εκαστοσ`, `Ἕκαστος` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰδίας` over `ιδιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιθυμίας` over `επιθυμιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξελκόμενος` over `εξελκομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δελεαζόμενος·` over `δελεαζομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:15
- *Disregarded Surface Variant:* kept `εἶτα` over `ειτα`, `Εἶτα` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιθυμία` over `επιθυμια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συλλαβοῦσα` over `συλλαβουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τίκτει` over `τικτει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτίαν,` over `αμαρτιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁμαρτία` over `αμαρτια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποτελεσθεῖσα` over `αποτελεσθεισα`, `αποτελεσθισα` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἀποκύει` over `αποκυει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θάνατον.` over `θανατον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:16
- **Apparatus:** `πλανᾶσθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **πλανασθαι** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `μὴ` over `μη`, `Μὴ` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπητοί.` over `αγαπητοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:17
- **Apparatus:** `καταβαῖνον` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **καταβενον** א (01) ; **καταβαινων** A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἔνι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εστιν** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀποσκίασμα` SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αποσκιασματοσ** B (03) א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Πᾶσα` over `πασα`, `πᾶσα` (B (03), BHP, Nestle1904, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόσις` over `δοσισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαθὴ` over `αγαθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶν` over `παν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δώρημα` over `δωρημα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τέλειον` over `τελειον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνωθέν` over `ανωθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν,` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατρὸς` over `πατροσ`, `Πατρὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φώτων,` over `φωτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρʼ` over `παρ`, `παρ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ᾧ` over `ω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραλλαγὴ` over `παραλλαγη`, `παραλλαγή,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τροπῆς` over `τροπησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:18
- **Apparatus:** `αὐτοῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εαυτου** A (02) C (04)
- *Disregarded Surface Variant:* kept `βουληθεὶς` over `βουληθεισ`, `βουληθισ`, `Βουληθεὶς,`, `Βουληθεὶς` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἀπεκύησεν` over `απεκυησεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμᾶς` over `ημασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγῳ` over `λογω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀληθείας,` over `αληθειασ`, `αληθιασ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶναι` over `ειναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμᾶς` over `ημασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπαρχήν` over `απαρχην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κτισμάτων.` over `κτισματων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:19
- **Apparatus:** `Ἴστε` B (03) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **Ὥστε** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ιστω** א (01) ; **ιστε δε** A (02) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `δὲ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **εστωσ** A (02) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ἀδελφοί` over `αδελφοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγαπητοί.` over `αγαπητοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔστω` over `εστω`, `Ἔστω` (B (03), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶς` over `πασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωπος` over `ανθρωποσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταχὺς` over `ταχυσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκοῦσαι,` over `ακουσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βραδὺς` over `βραδυσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαλῆσαι,` over `λαλησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βραδὺς` over `βραδυσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀργήν,` over `οργην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:20
- **Apparatus:** `οὐκ ἐργάζεται` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP THGNT Tisch8 WH1881 **]** **οὐ κατεργάζεται** RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ουκ εργαζετε** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `ὀργὴ` over `οργη`, `Ὀργὴ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνδρὸς` over `ανδροσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δικαιοσύνην` over `δικαιοσυνην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### James 1:21
- **Apparatus:** `περισσείαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **περισσευμα** A (02)
- **Apparatus:** `ἐν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εμ** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δέξασθε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δεξασθαι** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `διὸ` over `διο`, `Διὸ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποθέμενοι` over `αποθεμενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶσαν` over `πασαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥυπαρίαν` over `ρυπαριαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περισσείαν` over `περισσειαν`, `περισσιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `κακίας` over `κακιασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πραΰτητι` over `πραυτητι`, `πρᾳΰτητι` (B (03), RP2018 (Byz), א (01)) — *Spelling variant pooled before the vote with the reading 'πραΰτητι' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔμφυτον` over `εμφυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγον` over `λογον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δυνάμενον` over `δυναμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σῶσαι` over `σωσαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ψυχὰς` over `ψυχασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῶν.` over `υμων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἔμφυτον / ενφυτον` (A (02)) — *Apparatus witness, not a variant: Prefix assimilation spelling (συνπ-/συμπ-, ἐνκ-/ἐγκ-, συνζ-/συζ-, Κενχρ-/Κεγχρ- type)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `περισσείαν / περισειαν` (C (04)) — *Apparatus witness, not a variant: Single / double consonant spelling (Ἰωάνης / Ἰωάννης type)*

### James 1:22
- **Apparatus:** `Γίνεσθε` SRGNT SBLGNT RP2018 (Byz) TR (KJTR) Nestle1904 BHP B (03) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γεινεσθαι** א (01) A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `μόνον ἀκροαταὶ` א (01) SRGNT BHP TR (KJTR) RP2018 (Byz) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **ἀκροαταὶ μόνον** B (03) SBLGNT Nestle1904 WH1881 ; **μονον ακροται** A (02) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- *Disregarded Surface Variant:* kept `Γίνεσθε` over `γίνεσθε`, `γεινεσθε` (B (03), BHP, Nestle1904) — *Spelling variant pooled before the vote with the reading 'Γίνεσθε' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιηταὶ` over `ποιηται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγου` over `λογου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραλογιζόμενοι` over `παραλογιζομενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτούς.` over `εαυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:23
- **Apparatus:** `ὅτι εἴ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **η** A (02)
- **Apparatus:** `κατανοοῦντι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κατανοουντεσ** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι`, `Ὅτι` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἴ` over `ει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τις` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκροατὴς` over `ακροατησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λόγου` over `λογου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστὶν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιητής,` over `ποιητησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτος` over `ουτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔοικεν` over `εοικεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνδρὶ` over `ανδρι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρόσωπον` over `προσωπον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γενέσεως` over `γενεσεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐσόπτρῳ,` over `εσοπτρω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:24
- *Disregarded Surface Variant:* kept `κατενόησεν` over `κατενοησεν`, `Κατενόησεν` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτὸν` over `εαυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπελήλυθεν` over `απεληλυθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐθέως` over `ευθεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπελάθετο` over `επελαθετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁποῖος` over `οποιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν.` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:25
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **οὗτος** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐπιλησμονῆς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επιλισμονης** 33
- **Apparatus:** `ἀλλὰ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **αλλ ακροατης νομου και** 33
- *Disregarded Surface Variant:* kept `ὁ` over `ο`, `Ὁ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρακύψας` over `παρακυψασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τέλειον` over `τελειον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλευθερίας` over `ελευθεριασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παραμείνας,` over `παραμεινασ`, `παραμινασ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκροατὴς` over `ακροατησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιλησμονῆς` over `επιλησμονησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γενόμενος` over `γενομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιητὴς` over `ποιητησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔργου,` over `εργου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτος` over `ουτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μακάριος` over `μακαριοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιήσει` over `ποιησει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔσται.` over `εσται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### James 1:26
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **δε** 33 C (04)
- **Apparatus:** `θρησκὸς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **θρισκος** 33
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 WH1881 **]** **ἐν ὑμῖν** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `χαλιναγωγῶν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **χαλινων** B (03) ; **χαλιναγων** C (04) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτοῦ` א (01) SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **ἑαυτοῦ** B (03) SRGNT Nestle1904 WH1881 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `αὐτοῦ` א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **ἑαυτοῦ** B (03) Nestle1904 C (04) WH1881 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `τούτου` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **του** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `θρησκεία.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **θρισκια** 33
- *Disregarded Surface Variant:* kept `Εἴ` over `ει`, `εἴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τις` over `τισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοκεῖ` over `δοκει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θρησκὸς` over `θρησκοσ`, `θρῆσκος` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `εἶναι` over `ειναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γλῶσσαν` over `γλωσσαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλὰ` over `αλλα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπατῶν` over `απατων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρδίαν` over `καρδιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μάταιος` over `ματαιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θρησκεία.` over `θρησκεια`, `θρησκια` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / ἀλλ᾿`, `ἀλλὰ / αλλ`, `ἀλλὰ / ἀλλ᾽`, `ἀλλὰ / ἀλλʼ` (NA28 (TAGNT), PT1904 (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### James 1:27
- **Apparatus:** `θρησκεία` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 33 ; **θρησκεια γαρ** A (02)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **γαρ** A (02)
- **Apparatus:** `καὶ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **κι** B (03) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τῷ` B (03) SRGNT SBLGNT Nestle1904 BHP 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) WH1881 **]** **om.** א (01) RP2018 (Byz) TR (KJTR) TCGNT (Byz) Tisch8 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **τω** A (02)
- **Apparatus:** `ἐπισκέπτεσθαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **επισκεπτεσθε** א (01) 33 *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `χήρας` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **χειρας** 33
- **Apparatus:** `ἑαυτὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **σεαυτον** A (02)
- **Apparatus:** `ἀπὸ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **εκ** C (04)
- *Disregarded Surface Variant:* kept `θρησκεία` over `θρησκεια`, `θρησκια`, `Θρησκεία` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καθαρὰ` over `καθαρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀμίαντος` over `αμιαντοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρὰ` over `παρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ` over `θω̅`, `Θεῷ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατρὶ` over `πατρι`, `Πατρὶ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὕτη` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστίν,` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀρφανοὺς` over `ορφανουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χήρας` over `χηρασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θλίψει` over `θλειψει`, `θλιψει` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτῶν,` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄσπιλον` over `ασπιλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑαυτὸν` over `εαυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τηρεῖν` over `τηρειν`, `τηριν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κόσμου.` over `κοσμου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `SRGNT`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ, δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ: χαίρειν.
  - `SBLGNT`: Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `BHP`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ, δοῦλος· ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ: χαίρειν.
  - `Nestle1904`: Ἰάκωβος Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ Διασπορᾷ χαίρειν.
  - `RP2018 (Byz)`: Ἰάκωβος, θεοῦ καὶ κυρίου Ἰησοῦ χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ, χαίρειν.
  - `TR (KJTR)`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ, χαίρειν.
  - `B (03)`: ιακωβοσ θυ̅ και κυ̅ ιυ̅ χυ̅ δουλοσ ταισ δωδεκα φυλαισ ταισ εν τη διασπορα χαιρειν
  - `א (01)`: ιακωβοσ θυ̅ και κυ̅ ιυ̅ χυ̅ δουλοσ ταισ δωδεκα φυλαισ ταισ εν τη διασπορα χαιρειν
  - `NA28 (TAGNT)`: Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `THGNT`: Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `WH1881`: Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `Tisch8`: Ἰάκωβος θεοῦ καὶ κυρίου Ἰησοῦ Χριστοῦ δοῦλος ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `TCGNT (Byz)`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `PT1904 (Byz)`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ χαίρειν.
  - `TR-Scrivener (1894)`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ, χαίρειν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἰάκωβος, Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ, χαίρειν.
  - `TR-Stephanus (1550)`: Ιάκωβος Θεοῦ καὶ Κυρίου Ἰησοῦ Χριστοῦ δοῦλος, ταῖς δώδεκα φυλαῖς ταῖς ἐν τῇ διασπορᾷ, χαίρειν.
  - `TR-Elzevir (1624)`: ιακωβος θεου και κυριου ιησου χριστου δουλος ταις δωδεκα φυλαις ταις εν τη διασπορα χαιρειν
  - `A (02)`: ιακωβοσ θυ̅ και κυ̅ ιυ̅ χυ̅ δουλοσ ταισ δωδεκα φυλαισ ταισ εν τη διασπορα χαιρειν
  - `C (04)`: ιακωβοσ … ιυ̅ χυ̅ δουλοσ ταισ δωδεκα φυλαισ … εν … χαιρειν
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 15 surface variation(s) (Accentuation / capitalisation / breathing convention; Nomen sacrum (contracted sacred name) for the full word).

### Verse 2 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `SRGNT`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `SBLGNT`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `BHP`: πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `Nestle1904`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `RP2018 (Byz)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TR (KJTR)`: Πᾶσαν χαρὰν ἡγήσασθε ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις·
  - `B (03)`: πασαν χαραν ηγησασθε αδελφοι μου οταν πειρασμοισ περιπεσητε ποικιλοισ
  - `א (01)`: πασαν χαραν ηγησασθαι αδελφοι μου οταν πιρασμοισ περιπεσηται ποικιλοισ
  - `NA28 (TAGNT)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `THGNT`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `WH1881`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `Tisch8`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TCGNT (Byz)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `PT1904 (Byz)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TR-Scrivener (1894)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TR-Boyd (Elz/Scr/Steph)`: Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TR-Stephanus (1550)`: Πᾶσαν χαρὰν ἡγήσασθε ἀδελφοί μου, ὅταν πειρασμοῖς περιπέσητε ποικίλοις,
  - `TR-Elzevir (1624)`: πασαν χαραν ηγησασθε αδελφοι μου οταν πειρασμοις περιπεσητε ποικιλοις
  - `A (02)`: πασαν χαραν ηγησασθε αδελφοι μου οταν πειρασμοισ περιπεσητε πυκιλοισ
  - `C (04)`: πασαν … αδελφοι … πειρασμοισ περιπεσητε ποικιλαισ
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἡγήσασθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ηγησασθαι (א (01)). [Lexical, morphological, or word-order variant] Adopted 'περιπέσητε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over περιπεσηται (א (01)). Also normalised 7 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `SRGNT`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν.
  - `SBLGNT`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `BHP`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν.
  - `Nestle1904`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν.
  - `RP2018 (Byz)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `TR (KJTR)`: Γινώσκοντες, ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν.
  - `B (03)`: γεινωσκοντεσ οτι το δοκιμιον υμων τησ πιστεωσ κατεργαζεται υπομονην
  - `א (01)`: γινωσκοντεσ οτι το δοκιμειον υμων τησ πιστεωσ κατεργαζεται υπομονην
  - `NA28 (TAGNT)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `THGNT`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `WH1881`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `Tisch8`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν.
  - `TCGNT (Byz)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `PT1904 (Byz)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `TR-Scrivener (1894)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `TR-Boyd (Elz/Scr/Steph)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `TR-Stephanus (1550)`: γινώσκοντες ὅτι τὸ δοκίμιον ὑμῶν τῆς πίστεως κατεργάζεται ὑπομονήν·
  - `TR-Elzevir (1624)`: γινωσκοντες οτι το δοκιμιον υμων της πιστεως κατεργαζεται υπομονην
  - `A (02)`: γινωσκοντεσ οτι το δοκιμιον υμων τησ πιστεωσ κατεργαζετε υπομονην
  - `C (04)`: γινωσκοντεσ οτι το δοκιμιον υμων τησ πιστεωσ κατεργαζεται υπομονην
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 9 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 4 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `SRGNT`: Ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `SBLGNT`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `BHP`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `Nestle1904`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `RP2018 (Byz)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TR (KJTR)`: Ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `B (03)`: η δε υπομονη εργον τελειον εχετω ινα ητε τελειοι και ολοκληροι εν μηδενι λειπομενοι
  - `א (01)`: η δε υπομονη εργον τελιον εχετω ινα ητε τελιοι και ολοκληροι εν μηδενι λειπομενοι
  - `NA28 (TAGNT)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι ἐν μηδενὶ λειπόμενοι.
  - `THGNT`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι ἐν μηδενὶ λειπόμενοι.
  - `WH1881`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `Tisch8`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TCGNT (Byz)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `PT1904 (Byz)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TR-Scrivener (1894)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TR-Boyd (Elz/Scr/Steph)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TR-Stephanus (1550)`: ἡ δὲ ὑπομονὴ ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι, ἐν μηδενὶ λειπόμενοι.
  - `TR-Elzevir (1624)`: η δε υπομονη εργον τελειον εχετω ινα ητε τελειοι και ολοκληροι εν μηδενι λειπομενοι
  - `A (02)`: η δε υπομονη εργον τελειον εχετω ινα ητε τελειοι και ολοκληροι εν μηδενι λειπομενοι
  - `C (04)`: η δε υπομονη εργον τελειον εχετω ινα ητε τελειοι και ολοκληροι εν μηδενι λειπομενοι
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 14 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 5 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ·
  - `SRGNT`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος, Θεοῦ, πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `SBLGNT`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ·
  - `BHP`: εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος, Θεοῦ, πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `Nestle1904`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `RP2018 (Byz)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς, καὶ οὐκ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `TR (KJTR)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος· καὶ δοθήσεται αὐτῷ.
  - `B (03)`: ει δε τισ υμων λειπεται σοφιασ αιτειτω παρα του διδοντοσ θυ̅ πασιν απλωσ και μη ονειδιζοντοσ και δοθησεται αυτω
  - `א (01)`: ει δε τισ υμων λειπεται σοφιασ αιτιτω παρα του διδοντοσ θυ̅ πασιν απλωσ και μη ονιδιζοντοσ και δοθησεται αυτω
  - `NA28 (TAGNT)`: εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `THGNT`: εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `WH1881`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ·
  - `Tisch8`: εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος θεοῦ πᾶσιν ἁπλῶς καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `TCGNT (Byz)`: εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς καὶ οὐκ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `PT1904 (Byz)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς καὶ οὐκ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ·
  - `TR-Scrivener (1894)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `TR-Boyd (Elz/Scr/Steph)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος, καὶ δοθήσεται αὐτῷ.
  - `TR-Stephanus (1550)`: Εἰ δέ τις ὑμῶν λείπεται σοφίας, αἰτείτω παρὰ τοῦ διδόντος Θεοῦ πᾶσιν ἁπλῶς, καὶ μὴ ὀνειδίζοντος· καὶ δοθήσεται αὐτῷ.
  - `TR-Elzevir (1624)`: ει δε τις υμων λειπεται σοφιας αιτειτω παρα του διδοντος θεου πασιν απλως και μη ονειδιζοντος και δοθησεται αυτω
  - `A (02)`: ει δε τισ υμων λειπετε σοφιασ αιτειτω παρα του θυ̅ του διδοντοσ πασιν απλωσ και μη ονιδιζοντοσ και δοθησεται αυτω
  - `C (04)`: ει δε τισ υμων λειπεται σοφειασ αιτειτω παρα του διδοντοσ θυ̅ πασιν απλωσ και μη ονειδιζοντοσ και δοθησεται αυτω
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'μὴ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR)] (weight 6.21, confidence 99%) over οὐκ (RP2018 (Byz)). Reference apparatus (SBLGNT): μὴ WH Treg NA28 ] οὐκ RP Reference apparatus (SBLGNT): δὲ WH Treg NA28 ] – RP Reference apparatus (SBLGNT): αὐτοῦ Treg NA28 RP ] ἑαυτοῦ WH Reference apparatus (SBLGNT): αὐτοῦ Treg NA28 RP ] ἑαυτοῦ WH Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος, ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ·
  - `SRGNT`: Αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος, ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης, ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `SBLGNT`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος, ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ·
  - `BHP`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης, ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `Nestle1904`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `RP2018 (Byz)`: Αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TR (KJTR)`: Αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος. Ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `B (03)`: αιτειτω δε εν πιστει μηδεν διακρεινομενοσ ο γαρ διακρεινομενοσ εοικε κλυδωνι θαλασσησ ανεμιζομενω και ρειπιζομενω
  - `א (01)`: αιτειτω δε εν πιστι μηδεν διακρινομενοσ ο γαρ διακρινομενοσ εοικεν κλυδωνι θαλασσησ ανεμιζομενω και ριπιζομενω
  - `NA28 (TAGNT)`: αἰτείτω δὲ ἐν πίστει μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `THGNT`: αἰτείτω δὲ ἐν πίστει μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `WH1881`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος, ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ·
  - `Tisch8`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικεν κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TCGNT (Byz)`: αἰτείτω δὲ ἐν πίστει μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικε κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `PT1904 (Byz)`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικε κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TR-Scrivener (1894)`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικε κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TR-Boyd (Elz/Scr/Steph)`: Αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικε κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TR-Stephanus (1550)`: αἰτείτω δὲ ἐν πίστει, μηδὲν διακρινόμενος· ὁ γὰρ διακρινόμενος ἔοικε κλύδωνι θαλάσσης ἀνεμιζομένῳ καὶ ῥιπιζομένῳ.
  - `TR-Elzevir (1624)`: αιτειτω δε εν πιστει μηδεν διακρινομενος ο γαρ διακρινομενος εοικεν κλυδωνι θαλασσης ανεμιζομενω και ριπιζομενω
  - `A (02)`: αιτειτω δε εν πιστει μηδεν διακρινομενοσ ο γαρ διακρινομενοσ εοικεν κλυδωνι θαλασσησ ανεμιζομενω και ριπιζομενω
  - `C (04)`: αιτειτω δε εν πιστι μηδεν διακρινομενοσ ο γαρ διακρινομενοσ εοικε … θαλασσησ ανεμιζομενω και ριπιζομενω
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 15 surface variation(s) (Accentuation / capitalisation / breathing convention; Euphonic movable-nu (-ν) variation; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 7 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου
  - `SRGNT`: Μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ Κυρίου,
  - `SBLGNT`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου
  - `BHP`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ Κυρίου,
  - `Nestle1904`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ Κυρίου,
  - `RP2018 (Byz)`: Μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ κυρίου.
  - `TR (KJTR)`: Μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου.
  - `B (03)`: μη γαρ οιεσθω ο ανθρωποσ εκεινοσ οτι λημψεται τι παρα του κυ̅
  - `א (01)`: μη γαρ οιεσθω ο ανθρωποσ εκεινοσ οτι λημψετε παρα του κυ̅
  - `NA28 (TAGNT)`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου·
  - `THGNT`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου·
  - `WH1881`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου
  - `Tisch8`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήμψεταί τι παρὰ τοῦ κυρίου,
  - `TCGNT (Byz)`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου.
  - `PT1904 (Byz)`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου.
  - `TR-Scrivener (1894)`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου.
  - `TR-Boyd (Elz/Scr/Steph)`: Μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου.
  - `TR-Stephanus (1550)`: μὴ γὰρ οἰέσθω ὁ ἄνθρωπος ἐκεῖνος ὅτι λήψεταί τι παρὰ τοῦ Κυρίου·
  - `TR-Elzevir (1624)`: μη γαρ οιεσθω ο ανθρωπος εκεινος οτι ληψεται τι παρα του κυριου
  - `A (02)`: μη γαρ οιεσθω ο ανοσ̅ εκεινοσ οτι λημψεται τι παρα του …
  - `C (04)`: μη γαρ οιεσθω ο ανοσ̅ εκεινοσ … του κυ̅
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'λήμψεταί' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over λημψετε (א (01)). [Omission in some witnesses] Adopted 'τι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 8 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `SRGNT`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `SBLGNT`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `BHP`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `Nestle1904`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `RP2018 (Byz)`: Ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `TR (KJTR)`: Ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `B (03)`: ανηρ διψυχοσ ακαταστατοσ εν πασαισ ταισ οδοισ αυτου
  - `א (01)`: ανηρ διψυχοσ ακαταστατοσ εν πασαισ ταισ οδοισ αυτου
  - `NA28 (TAGNT)`: ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `THGNT`: ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `WH1881`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `Tisch8`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `TCGNT (Byz)`: ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `PT1904 (Byz)`: ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `TR-Scrivener (1894)`: ἀνὴρ δίψυχος ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὐτοῦ.
  - `TR-Stephanus (1550)`: ἀνὴρ δίψυχος, ἀκατάστατος ἐν πάσαις ταῖς ὁδοῖς αὑτοῦ.
  - `TR-Elzevir (1624)`: ανηρ διψυχος ακαταστατος εν πασαις ταις οδοις αυτου
  - `A (02)`: ανηρ διψυχοσ ακαταστατοσ εν πασαισ ταισ οδοισ αυτου
  - `C (04)`: ανηρ διψυχοσ ακαταστατοσ εν πασαισ ταισ οδοισ αυτου
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 8 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 9 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `SRGNT`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς, ἐν τῷ ὕψει αὐτοῦ,
  - `SBLGNT`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `BHP`: καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς, ἐν τῷ ὕψει αὐτοῦ·
  - `Nestle1904`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `RP2018 (Byz)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ·
  - `TR (KJTR)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ:
  - `B (03)`: καυχασθω δε αδελφοσ ο ταπεινοσ εν τω υψει αυτου
  - `א (01)`: καυχασθω δε ο αδελφοσ ο ταπινοσ εν τω υψει αυτου
  - `NA28 (TAGNT)`: καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `THGNT`: καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `WH1881`: Καυχάσθω δὲ [ὁ] ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `Tisch8`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `TCGNT (Byz)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `PT1904 (Byz)`: καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ,
  - `TR-Scrivener (1894)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ·
  - `TR-Boyd (Elz/Scr/Steph)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὐτοῦ·
  - `TR-Stephanus (1550)`: Καυχάσθω δὲ ὁ ἀδελφὸς ὁ ταπεινὸς ἐν τῷ ὕψει αὑτοῦ·
  - `TR-Elzevir (1624)`: καυχασθω δε ο αδελφος ο ταπεινος εν τω υψει αυτου
  - `A (02)`: καυχασθω δε ο αδελφοσ ο ταπεινοσ εν τω υψει αυτου
  - `C (04)`: καυχασθω δε ο αδελφοσ ο ταπεινοσ εν τω υψει αυτου
- **Philological Rationale:** [Omission in some witnesses] Adopted 'ὁ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `SRGNT`: ὁ δὲ πλούσιος, ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `SBLGNT`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `BHP`: ὁ δὲ πλούσιος, ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `Nestle1904`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `RP2018 (Byz)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ· ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `TR (KJTR)`: Ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ: ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `B (03)`: ο δε πλουσιοσ εν τη ταπεινωσι αυτου οτι ωσ ανθοσ χορτου παρελευσεται
  - `א (01)`: ο δε πλουσιοσ εν τη ταπινωσει αυτου οτι ωσ ανθοσ χορτου παρελευσεται
  - `NA28 (TAGNT)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `THGNT`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `WH1881`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `Tisch8`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `TCGNT (Byz)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `PT1904 (Byz)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `TR-Scrivener (1894)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ· ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `TR-Boyd (Elz/Scr/Steph)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ· ὅτι ὡς ἄνθος χόρτου παρελεύσεται.
  - `TR-Stephanus (1550)`: ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὑτοῦ, ὅτι ὡς ἄνθος χόρτου παρελεύσεται·
  - `TR-Elzevir (1624)`: ο δε πλουσιος εν τη ταπεινωσει αυτου οτι ως ανθος χορτου παρελευσεται
  - `A (02)`: ο δε πλουσιοσ εν τη ταπεινωσει αυτου οτι ωσ ανθοσ χορτου παρελευσεται
  - `C (04)`: ο δε πλουσιοσ εν τη ταπεινωσει αυτου οτι ωσ ανθοσ χορτου παρελευσεται
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 12 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 11 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `SRGNT`: Ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο. Οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `SBLGNT`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `BHP`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο. οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `Nestle1904`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `RP2018 (Byz)`: Ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `TR (KJTR)`: Ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο: οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `B (03)`: ανετειλεν γαρ ο ηλιοσ συν τω καυσωνι και εξηρανε τον χορτον και το ανθοσ αυτου εξεπεσεν και η ευπρεπεια του προσωπου απωλετο ουτωσ και ο πλουσιοσ εν ταισ πορειαισ αυτου μαρανθησεται
  - `א (01)`: ανετιλεν γαρ ο ηλιοσ συν τω καυσωνι και εξηρανεν τον χορτον και το ανθοσ αυτου εξεπεσεν και η ευπρεπια του προσωπου αυτου απωλετο ουτωσ και ο πλουσιοσ εν ταισ ποριαισ αυτου μαρανθησεται
  - `NA28 (TAGNT)`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `THGNT`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `WH1881`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `Tisch8`: ἀνέτειλεν γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανεν τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσεν καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτως καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `TCGNT (Byz)`: ἀνέτειλε γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανε τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτω καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `PT1904 (Byz)`: ἀνέτειλε γὰρ ὁ ἥλιος σὺν τῷ καύσωνι καὶ ἐξήρανε τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο. οὕτω καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `TR-Scrivener (1894)`: ἀνέτειλε γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανε τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτω καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀνέτειλε γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανε τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτω καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὐτοῦ μαρανθήσεται.
  - `TR-Stephanus (1550)`: ἀνέτειλε γὰρ ὁ ἥλιος σὺν τῷ καύσωνι, καὶ ἐξήρανε τὸν χόρτον, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε, καὶ ἡ εὐπρέπεια τοῦ προσώπου αὐτοῦ ἀπώλετο· οὕτω καὶ ὁ πλούσιος ἐν ταῖς πορείαις αὑτοῦ μαρανθήσεται.
  - `TR-Elzevir (1624)`: ανετειλεν γαρ ο ηλιος συν τω καυσωνι και εξηρανεν τον χορτον και το ανθος αυτου εξεπεσεν και η ευπρεπεια του προσωπου αυτου απωλετο ουτως και ο πλουσιος εν ταις πορειαις αυτου μαρανθησεται
  - `A (02)`: ανετειλεν γαρ ο ηλιοσ συν τω καυσωνι και εξηρανεν τον χορτον και το ανθοσ αυτου εξεπεσεν και η ευπρεπεια του προσωπου αυτου απωλετο ουτωσ και ο πλουσιοσ εν ταισ ποριαισ αυτου μαρανθησεται
  - `C (04)`: ανετειλεν γαρ ο ηλιοσ συν τω καυσωνι και εξηρανεν τον χορτον και το ανθοσ αυτου εξεπεσεν και η ευπρεπεια του προσωπου αυτου απωλετο ουτωσ και ο πλουσιοσ εν ταισ πορειαισ εαυτου μαρανθησεται
- **Philological Rationale:** [Omission in some witnesses] Adopted 'αὐτοῦ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). Also normalised 31 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 12 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `SRGNT`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος, λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `SBLGNT`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `BHP`: μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος, λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `Nestle1904`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `RP2018 (Byz)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν· ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `TR (KJTR)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν: ὅτι δόκιμος γενόμενος, λήψεταί τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `B (03)`: μακαριοσ ανηρ οσ υπομενει πειρασμον οτι δοκιμοσ γενομενοσ λημψεται τον στεφανον τησ ζωησ ον επηγγειλατο τοισ αγαπωσιν αυτον
  - `א (01)`: μακαριοσ ανηρ οσ υπομενι πειρασμον οτι δοκιμοσ γενομενοσ λημψεται τον στεφανον τησ ζωησ ον επηγγιλατο τοισ αγαπωσιν αυτον
  - `NA28 (TAGNT)`: μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `THGNT`: μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `WH1881`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `Tisch8`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήμψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο τοῖς ἀγαπῶσιν αὐτόν.
  - `TCGNT (Byz)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν, ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `PT1904 (Byz)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν· ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `TR-Scrivener (1894)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν· ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `TR-Boyd (Elz/Scr/Steph)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν· ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὐτόν.
  - `TR-Stephanus (1550)`: Μακάριος ἀνὴρ ὃς ὑπομένει πειρασμὸν, ὅτι δόκιμος γενόμενος λήψεται τὸν στέφανον τῆς ζωῆς, ὃν ἐπηγγείλατο ὁ Κύριος τοῖς ἀγαπῶσιν αὑτόν.
  - `TR-Elzevir (1624)`: μακαριος ανηρ ος υπομενει πειρασμον οτι δοκιμος γενομενος ληψεται τον στεφανον της ζωης ον επηγγειλατο ο κυριος τοις αγαπωσιν αυτον
  - `A (02)`: μακαριοσ ανοσ̅ οσ υπομενει πειρασμον οτι δοκιμοσ γενομενοσ λημψεται τον στεφανον τησ ζωησ ον επηγγειλατο τοισ αγαπωσιν αυτον
  - `C (04)`: μακαριοσ ανηρ οσ … πειρασμον οτι δοκιμοσ γενομενοσ ληψεται τον στεφανον τησ ζωησ ον επηγγειλατο κσ̅ τοισ αγαπωσιν αυτον
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ὁ κύριος (RP2018 (Byz), TR (KJTR)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 13 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `SRGNT`: Μηδεὶς πειραζόμενος λεγέτω, ὅτι “Ἀπὸ Θεοῦ πειράζομαι.” Ὁ γὰρ Θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `SBLGNT`: μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `BHP`: μηδεὶς πειραζόμενος λεγέτω, ὅτι “ἀπὸ Θεοῦ πειράζομαι.” ὁ γὰρ Θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `Nestle1904`: Μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `RP2018 (Byz)`: Μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα·
  - `TR (KJTR)`: Μηδεὶς πειραζόμενος Λεγέτω, ὅτι Ἀπὸ Θεοῦ πειράζομαι: ὁ γὰρ Θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα:
  - `B (03)`: μηδεισ πειραζομενοσ λεγετω οτι απο θυ̅ πειραζομαι ο γαρ θσ̅ απειραστοσ εστιν κακων πειραζει δε αυτοσ ουδενα
  - `א (01)`: μηδισ πιραζομενοσ λεγετω οτι υπο θυ̅ πειραζομαι ο γαρ θσ̅ απειραστοσ εστιν κακων πειραζει δε αυτοσ ουδενα
  - `NA28 (TAGNT)`: Μηδεὶς πειραζόμενος λεγέτω ὅτι ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα·
  - `THGNT`: Μηδεὶς πειραζόμενος λεγέτω ὅτι ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα·
  - `WH1881`: μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `Tisch8`: μηδεὶς πειραζόμενος λεγέτω ὅτι ἀπὸ θεοῦ πειράζομαι· ὁ γὰρ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `TCGNT (Byz)`: μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστι κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `PT1904 (Byz)`: Μηδεὶς πειραζόμενος λεγέτω ὅτι ἀπὸ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστι κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `TR-Scrivener (1894)`: μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ τοῦ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστι κακῶν, πειράζει δὲ αὐτὸς οὐδένα·
  - `TR-Boyd (Elz/Scr/Steph)`: Μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ τοῦ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστι κακῶν, πειράζει δὲ αὐτὸς οὐδένα·
  - `TR-Stephanus (1550)`: Μηδεὶς πειραζόμενος λεγέτω, ὅτι ἀπὸ τοῦ Θεοῦ πειράζομαι· ὁ γὰρ Θεὸς ἀπείραστός ἐστι κακῶν, πειράζει δὲ αὐτὸς οὐδένα.
  - `TR-Elzevir (1624)`: μηδεις πειραζομενος λεγετω οτι απο του θεου πειραζομαι ο γαρ θεος απειραστος εστιν κακων πειραζει δε αυτος ουδενα
  - `A (02)`: μηδεισ πειραζομενοσ λεγετω οτι απο θυ̅ πειραζομαι ο γαρ θσ̅ απειραστοσ εστιν κακων πειραζει δε αυτοσ ουδενα
  - `C (04)`: μηδεισ πειραζομενοσ λεγετω οτι απο θυ̅ πειραζομαι ο γαρ θσ̅ απειραστοσ εστιν κακων πειραζει δε αυτοσ ουδενα
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Ἀπὸ' [B (03), SRGNT, SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR), BHP] (weight 5.97, confidence 99%) over υπο (א (01)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 14 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `SRGNT`: Ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας, ἐξελκόμενος καὶ δελεαζόμενος.
  - `SBLGNT`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `BHP`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας, ἐξελκόμενος καὶ δελεαζόμενος·
  - `Nestle1904`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `RP2018 (Byz)`: ἕκαστος δὲ πειράζεται, ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος.
  - `TR (KJTR)`: Ἕκαστος δὲ πειράζεται, ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος, καὶ δελεαζόμενος.
  - `B (03)`: εκαστοσ δε πειραζεται υπο τησ ιδιασ επιθυμιασ εξελκομενοσ και δελεαζομενοσ
  - `א (01)`: εκαστοσ δε πιραζετε υπο τησ ιδιασ επιθυμιασ εξελκομενοσ και δελεαζομενοσ
  - `NA28 (TAGNT)`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `THGNT`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `WH1881`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `Tisch8`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `TCGNT (Byz)`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος.
  - `PT1904 (Byz)`: ἕκαστος δὲ πειράζεται ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `TR-Scrivener (1894)`: ἕκαστος δὲ πειράζεται, ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος.
  - `TR-Boyd (Elz/Scr/Steph)`: ἕκαστος δὲ πειράζεται, ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος.
  - `TR-Stephanus (1550)`: ἕκαστος δὲ πειράζεται, ὑπὸ τῆς ἰδίας ἐπιθυμίας ἐξελκόμενος καὶ δελεαζόμενος·
  - `TR-Elzevir (1624)`: εκαστος δε πειραζεται υπο της ιδιας επιθυμιας εξελκομενος και δελεαζομενος
  - `A (02)`: εκαστοσ δε πειραζεται υπο τησ ιδιασ επιθυμιασ εξελκομενοσ και δελεαζομενοσ
  - `C (04)`: εκαστοσ δε πειραζεται υπο τησ ιδιασ επιθυμιασ εξελκομενοσ και δελεαζομενοσ
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'πειράζεται' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over πιραζετε (א (01)). Also normalised 9 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `SRGNT`: Εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα, ἀποκύει θάνατον.
  - `SBLGNT`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `BHP`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα, ἀποκύει θάνατον.
  - `Nestle1904`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `RP2018 (Byz)`: Εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν· ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TR (KJTR)`: Εἶτα ἡ ἐπιθυμία συλλαβοῦσα, τίκτει ἁμαρτίαν: ἡ δὲ ἁμαρτία, ἀποτελεσθεῖσα, ἀποκύει θάνατον.
  - `B (03)`: ειτα η επιθυμια συλλαβουσα τικτει αμαρτιαν η δε αμαρτια αποτελεσθεισα αποκυει θανατον
  - `א (01)`: ειτα η επιθυμια συλλαβουσα τικτει αμαρτιαν η δε αμαρτια αποτελεσθισα αποκυει θανατον
  - `NA28 (TAGNT)`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `THGNT`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `WH1881`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκυεῖ θάνατον.
  - `Tisch8`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TCGNT (Byz)`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `PT1904 (Byz)`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TR-Scrivener (1894)`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν· ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TR-Boyd (Elz/Scr/Steph)`: Εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν· ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TR-Stephanus (1550)`: εἶτα ἡ ἐπιθυμία συλλαβοῦσα τίκτει ἁμαρτίαν, ἡ δὲ ἁμαρτία ἀποτελεσθεῖσα ἀποκύει θάνατον.
  - `TR-Elzevir (1624)`: ειτα η επιθυμια συλλαβουσα τικτει αμαρτιαν η δε αμαρτια αποτελεσθεισα αποκυει θανατον
  - `A (02)`: ειτα η επιθυμια συλλαβουσα τικτει αμαρτιαν η δε αμαρτια αποτελεσθεισα αποκυει θανατον
  - `C (04)`: ειτα η επιθυμια συλλαβουσα τικτει αμαρτιαν η δε αμαρτια αποτελεσθεισα αποκυει θανατον
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 12 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 16 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `SRGNT`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `SBLGNT`: μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `BHP`: μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `Nestle1904`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `RP2018 (Byz)`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `TR (KJTR)`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `B (03)`: μη πλανασθε αδελφοι μου αγαπητοι
  - `א (01)`: μη πλανασθαι αδελφοι μου αγαπητοι
  - `NA28 (TAGNT)`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί·
  - `THGNT`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί·
  - `WH1881`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `Tisch8`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `TCGNT (Byz)`: μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `PT1904 (Byz)`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί·
  - `TR-Scrivener (1894)`: μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `TR-Boyd (Elz/Scr/Steph)`: Μὴ πλανᾶσθε, ἀδελφοί μου ἀγαπητοί.
  - `TR-Stephanus (1550)`: Μὴ πλανᾶσθε ἀδελφοί μου ἀγαπητοί·
  - `TR-Elzevir (1624)`: μη πλανασθε αδελφοι μου αγαπητοι
  - `A (02)`: μη πλανασθε αδελφοι μου αγαπητοι
  - `C (04)`: μη πλανασθε αδελφοι μου αγαπητοι
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'πλανᾶσθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over πλανασθαι (א (01)). Also normalised 3 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `94.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `SRGNT`: Πᾶσα δόσις ἀγαθὴ, καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ Πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `SBLGNT`: Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `BHP`: πᾶσα δόσις ἀγαθὴ, καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ Πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `Nestle1904`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν καταβαῖνον ἀπὸ τοῦ Πατρὸς τῶν φώτων, παρ’ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `RP2018 (Byz)`: Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ’ ᾧ οὐκ ἔνι παραλλαγή, ἢ τροπῆς ἀποσκίασμα.
  - `TR (KJTR)`: Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ Πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ, ἢ τροπῆς ἀποσκίασμα.
  - `B (03)`: πασα δοσισ αγαθη και παν δωρημα τελειον ανωθεν εστιν καταβαινον απο του πατροσ των φωτων παρ ω ουκ ενι παραλλαγη η τροπησ αποσκιασματοσ
  - `א (01)`: πασα δοσισ αγαθη και παν δωρημα τελειον ανωθεν εστιν καταβενον απο του πατροσ των φωτων παρ ω ουκ εστιν παραλλαγη η τροπησ αποσκιασματοσ
  - `NA28 (TAGNT)`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων παρ᾽ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `THGNT`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων παρ᾽ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `WH1881`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `Tisch8`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστιν, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ’ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `TCGNT (Byz)`: Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστι καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ᾽ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `PT1904 (Byz)`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστι καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ᾽ ᾧ οὐκ ἔνι παραλλαγὴ ἢ τροπῆς ἀποσκίασμα.
  - `TR-Scrivener (1894)`: πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστι, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ᾽ ᾧ οὐκ ἔνι παραλλαγή, ἢ τροπῆς ἀποσκίασμα.
  - `TR-Boyd (Elz/Scr/Steph)`: Πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστι, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρ᾿ ᾧ οὐκ ἔνι παραλλαγή, ἢ τροπῆς ἀποσκίασμα.
  - `TR-Stephanus (1550)`: πᾶσα δόσις ἀγαθὴ, καὶ πᾶν δώρημα τέλειον ἄνωθέν ἐστι, καταβαῖνον ἀπὸ τοῦ πατρὸς τῶν φώτων, παρʼ ᾧ οὐκ ἔνι παραλλαγὴ, ἢ τροπῆς ἀποσκίασμα.
  - `TR-Elzevir (1624)`: πασα δοσις αγαθη και παν δωρημα τελειον ανωθεν εστιν καταβαινον απο του πατρος των φωτων παρ ω ουκ ενι παραλλαγη η τροπης αποσκιασμα
  - `A (02)`: πασα δοσισ αγαθη και παν δωρημα τελειον ανωθεν εστιν καταβαινων απο του πρσ̅ των φωτων παρ ω ουκ ενι παραλλαγη η τροπησ αποσκιασμα
  - `C (04)`: πασα δοσισ αγαθη και παν δωρημα τελειον ανωθεν εστιν καταβαινον απο του πρσ̅ των φωτων παρ ω ουκ ενι παραλλαγη η τροπησ αποσκιασμα
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'καταβαῖνον' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over καταβενον (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἔνι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εστιν (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἀποσκίασμα' [SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.99, confidence 96%) over αποσκιασματοσ (B (03), א (01)). Also normalised 20 orthographic/surface variation(s).
- *confidence:* Verse confidence 94% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 18 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `SRGNT`: Βουληθεὶς, ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `SBLGNT`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `BHP`: βουληθεὶς, ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `Nestle1904`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `RP2018 (Byz)`: Βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `TR (KJTR)`: Βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `B (03)`: βουληθεισ απεκυησεν ημασ λογω αληθειασ εισ το ειναι ημασ απαρχην τινα των αυτου κτισματων
  - `א (01)`: βουληθισ απεκυησεν ημασ λογω αληθιασ εισ το ειναι ημασ απαρχην τινα των αυτου κτισματων
  - `NA28 (TAGNT)`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `THGNT`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `WH1881`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `Tisch8`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `TCGNT (Byz)`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `PT1904 (Byz)`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `TR-Scrivener (1894)`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `TR-Boyd (Elz/Scr/Steph)`: Βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὐτοῦ κτισμάτων.
  - `TR-Stephanus (1550)`: βουληθεὶς ἀπεκύησεν ἡμᾶς λόγῳ ἀληθείας, εἰς τὸ εἶναι ἡμᾶς ἀπαρχήν τινα τῶν αὑτοῦ κτισμάτων.
  - `TR-Elzevir (1624)`: βουληθεις απεκυησεν ημας λογω αληθειας εις το ειναι ημας απαρχην τινα των αυτου κτισματων
  - `A (02)`: βουληθεισ απεκυησεν ημασ λογω αληθειασ εισ το ειναι ημασ απαρχην τινα των εαυτου κτισματων
  - `C (04)`: βουληθεισ απεκυησεν ημασ λογω αληθειασ εισ το ειναι ημασ απαρχην τινα των εαυτου κτισματων
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 13 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 19 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν,
  - `SRGNT`: Ἴστε, ἀδελφοί μου ἀγαπητοί. Ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν,
  - `SBLGNT`: Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν,
  - `BHP`: ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `Nestle1904`: Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `RP2018 (Byz)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TR (KJTR)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν:
  - `B (03)`: ιστε αδελφοι μου αγαπητοι εστω δε πασ ανθρωποσ ταχυσ εισ το ακουσαι βραδυσ εισ το λαλησαι βραδυσ εισ οργην
  - `א (01)`: ιστω αδελφοι μου αγαπητοι εστω δε πασ ανθρωποσ ταχυσ εισ το ακουσαι βραδυσ εισ το λαλησαι βραδυσ εισ οργην
  - `NA28 (TAGNT)`: Ἴστε, ἀδελφοί μου ἀγαπητοί· ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν.
  - `THGNT`: Ἴστε, ἀδελφοί μου ἀγαπητοί· ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν.
  - `WH1881`: Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν,
  - `Tisch8`: Ἴστε, ἀδελφοί μου ἀγαπητοί. ἔστω δὲ πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TCGNT (Byz)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `PT1904 (Byz)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TR-Scrivener (1894)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TR-Boyd (Elz/Scr/Steph)`: Ὥστε, ἀδελφοί μου ἀγαπητοί, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TR-Stephanus (1550)`: Ὥστε, ἀδελφοί μου ἀγαπητοὶ, ἔστω πᾶς ἄνθρωπος ταχὺς εἰς τὸ ἀκοῦσαι, βραδὺς εἰς τὸ λαλῆσαι, βραδὺς εἰς ὀργήν·
  - `TR-Elzevir (1624)`: ωστε αδελφοι μου αγαπητοι εστω πας ανθρωπος ταχυς εις το ακουσαι βραδυς εις το λαλησαι βραδυς εις οργην
  - `A (02)`: ιστε δε αδελφοι μου αγαπητοι και εστωσ πασ ανοσ̅ ταχυσ εισ το ακουσαι βραδυσ εισ το λαλησαι βραδυσ εισ οργην
  - `C (04)`: ιστε αδελφοι μου αγαπητοι εστω δε πασ ανοσ̅ ταχυσ εισ το ακουσαι βραδυσ εισ το λαλησαι βραδυσ εισ οργην
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Ἴστε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over Ὥστε (RP2018 (Byz), TR (KJTR)); ιστω (א (01)). [Omission in some witnesses] Adopted 'δὲ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 20 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
  - `SRGNT`: ὀργὴ γὰρ ἀνδρὸς, δικαιοσύνην Θεοῦ οὐκ ἐργάζεται.
  - `SBLGNT`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
  - `BHP`: ὀργὴ γὰρ ἀνδρὸς, δικαιοσύνην Θεοῦ οὐκ ἐργάζεται.
  - `Nestle1904`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐκ ἐργάζεται.
  - `RP2018 (Byz)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐ κατεργάζεται.
  - `TR (KJTR)`: Ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `B (03)`: οργη γαρ ανδροσ δικαιοσυνην θυ̅ ουκ εργαζεται
  - `א (01)`: οργη γαρ ανδροσ δικαιοσυνην θυ̅ ουκ εργαζεται
  - `NA28 (TAGNT)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐ κατεργάζεται
  - `THGNT`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
  - `WH1881`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
  - `Tisch8`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην θεοῦ οὐκ ἐργάζεται.
  - `TCGNT (Byz)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `PT1904 (Byz)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `TR-Scrivener (1894)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `TR-Boyd (Elz/Scr/Steph)`: ὀργὴ γὰρ ἀνδρὸς δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `TR-Stephanus (1550)`: ὀργὴ γὰρ ἀνδρὸς, δικαιοσύνην Θεοῦ οὐ κατεργάζεται.
  - `TR-Elzevir (1624)`: οργη γαρ ανδρος δικαιοσυνην θεου ου κατεργαζεται
  - `A (02)`: οργη γαρ ανδροσ δικαιοσυνην θυ̅ ουκ εργαζετε
  - `C (04)`: οργη γαρ ανδροσ δικαιοσυνην θυ̅ ου κατεργαζεται
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'οὐκ ἐργάζεται' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over οὐ κατεργάζεται (RP2018 (Byz), TR (KJTR)). Also normalised 5 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 21 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `SRGNT`: Διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `SBLGNT`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `BHP`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `Nestle1904`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `RP2018 (Byz)`: Διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πρᾳΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TR (KJTR)`: Διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `B (03)`: διο αποθεμενοι πασαν ρυπαριαν και περισσειαν κακιασ εν πραυτητι δεξασθε τον εμφυτον λογον τον δυναμενον σωσαι τασ ψυχασ υμων
  - `א (01)`: διο αποθεμενοι πασαν ρυπαριαν και περισσιαν κακιασ εμ πραυτητι δεξασθαι τον εμφυτον λογον τον δυναμενον σωσαι τασ ψυχασ υμων
  - `NA28 (TAGNT)`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `THGNT`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `WH1881`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `Tisch8`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TCGNT (Byz)`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `PT1904 (Byz)`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TR-Scrivener (1894)`: διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πρᾳΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TR-Boyd (Elz/Scr/Steph)`: Διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πρᾳΰτητι δέξασθε τὸν ἔμφυτον λόγον, τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TR-Stephanus (1550)`: Διὸ ἀποθέμενοι πᾶσαν ῥυπαρίαν καὶ περισσείαν κακίας, ἐν πραΰτητι δέξασθε τὸν ἔμφυτον λόγον τὸν δυνάμενον σῶσαι τὰς ψυχὰς ὑμῶν.
  - `TR-Elzevir (1624)`: διο αποθεμενοι πασαν ρυπαριαν και περισσειαν κακιας εν πραυτητι δεξασθε τον εμφυτον λογον τον δυναμενον σωσαι τας ψυχας υμων
  - `A (02)`: διο αποθεμενοι πασαν ρυπαριαν και περισσευμα κακιασ εν πραυτι δεξασθαι τον ενφυτον λογον τον δυναμενον σωσαι τασ ψυχασ υμων
  - `C (04)`: διο αποθεμενοι πασαν ρυπαριαν και περισειαν κακιασ εν πραυτητι δεξασθε τον εμφυτον λογον τον δυναμενον σωσαι τασ ψυχασ υμων
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εμ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'δέξασθε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over δεξασθαι (א (01)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 22 (Confidence: `70.3%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `SRGNT`: Γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `SBLGNT`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ ἀκροαταὶ μόνον παραλογιζόμενοι ἑαυτούς.
  - `BHP`: γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `Nestle1904`: γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ ἀκροαταὶ μόνον παραλογιζόμενοι ἑαυτούς.
  - `RP2018 (Byz)`: Γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταί, παραλογιζόμενοι ἑαυτούς.
  - `TR (KJTR)`: Γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταὶ, παραλογιζόμενοι ἑαυτούς.
  - `B (03)`: γεινεσθε δε ποιηται λογου και μη ακροαται μονον παραλογιζομενοι εαυτουσ
  - `א (01)`: γεινεσθαι δε ποιηται λογου και μη μονον ακροαται παραλογιζομενοι εαυτουσ
  - `NA28 (TAGNT)`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `THGNT`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `WH1881`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ ἀκροαταὶ μόνον παραλογιζόμενοι ἑαυτούς.
  - `Tisch8`: γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `TCGNT (Byz)`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταὶ παραλογιζόμενοι ἑαυτούς.
  - `PT1904 (Byz)`: Γίνεσθε δὲ ποιηταὶ λόγου καὶ μὴ μόνον ἀκροαταί, παραλογιζόμενοι ἑαυτούς.
  - `TR-Scrivener (1894)`: γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταί, παραλογιζόμενοι ἑαυτούς.
  - `TR-Boyd (Elz/Scr/Steph)`: Γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταί, παραλογιζόμενοι ἑαυτούς.
  - `TR-Stephanus (1550)`: γίνεσθε δὲ ποιηταὶ λόγου, καὶ μὴ μόνον ἀκροαταὶ, παραλογιζόμενοι ἑαυτούς·
  - `TR-Elzevir (1624)`: γινεσθε δε ποιηται λογου και μη μονον ακροαται παραλογιζομενοι εαυτους
  - `A (02)`: γινεσθαι δε ποιηται λογου και μη μονον ακροται παραλογιζομενοι εαυτουσ
  - `C (04)`: γεινεσθε δε ποιηται λογου και μη μονον ακροαται παραλογιζομενοι εαυτουσ
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Γίνεσθε' [SRGNT, SBLGNT, RP2018 (Byz), TR (KJTR), Nestle1904, BHP, B (03)] (weight 5.97, confidence 99%) over γεινεσθαι (א (01)). [Variation unit spanning several words] Adopted 'μόνον ἀκροαταὶ' [א (01), SRGNT, BHP, TR (KJTR), RP2018 (Byz)] (weight 4.11, confidence 71%) over ἀκροαταὶ μόνον (B (03), SBLGNT, Nestle1904). Also normalised 8 orthographic/surface variation(s).
- *confidence:* Verse confidence 70% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 23 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ,
  - `SRGNT`: Ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν, καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ.
  - `SBLGNT`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ,
  - `BHP`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν, καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ.
  - `Nestle1904`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `RP2018 (Byz)`: Ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `TR (KJTR)`: Ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν, καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ:
  - `B (03)`: οτι ει τισ ακροατησ λογου εστιν και ου ποιητησ ουτοσ εοικεν ανδρι κατανοουντι το προσωπον τησ γενεσεωσ αυτου εν εσοπτρω
  - `א (01)`: οτι ει τισ ακροατησ λογου εστιν και ου ποιητησ ουτοσ εοικεν ανδρι κατανοουντεσ το προσωπον τησ γενεσεωσ αυτου εν εσοπτρω
  - `NA28 (TAGNT)`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `THGNT`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `WH1881`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ,
  - `Tisch8`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶν καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `TCGNT (Byz)`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶ καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `PT1904 (Byz)`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶ καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `TR-Scrivener (1894)`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶ καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `TR-Boyd (Elz/Scr/Steph)`: Ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶ καὶ οὐ ποιητής, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὐτοῦ ἐν ἐσόπτρῳ·
  - `TR-Stephanus (1550)`: ὅτι εἴ τις ἀκροατὴς λόγου ἐστὶ καὶ οὐ ποιητὴς, οὗτος ἔοικεν ἀνδρὶ κατανοοῦντι τὸ πρόσωπον τῆς γενέσεως αὑτοῦ ἐν ἐσόπτρῳ·
  - `TR-Elzevir (1624)`: οτι ει τις ακροατης λογου εστιν και ου ποιητης ουτος εοικεν ανδρι κατανοουντι το προσωπον της γενεσεως αυτου εν εσοπτρω
  - `A (02)`: η τισ ακροατησ λογου εστιν και ου ποιητησ ουτοσ εοικεν ανδρι κατανοουντι το προσωπον τησ γενεσεωσ αυτου εν εσοπτρω
  - `C (04)`: οτι ει τισ ακροατησ λογου εστιν και ου ποιητησ ουτοσ εοικεν ανδρι κατανοουντι το προσωπον τησ γενεσεωσ αυτου εν εσοπτρω
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'κατανοοῦντι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over κατανοουντεσ (א (01)). Also normalised 19 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 24 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `SRGNT`: Κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `SBLGNT`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `BHP`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `Nestle1904`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `RP2018 (Byz)`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `TR (KJTR)`: Κατενόησεν γὰρ ἑαυτὸν, καὶ ἀπελήλυθεν, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `B (03)`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεωσ επελαθετο οποιοσ ην
  - `א (01)`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεωσ επελαθετο οποιοσ ην
  - `NA28 (TAGNT)`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `THGNT`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `WH1881`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `Tisch8`: κατενόησεν γὰρ ἑαυτὸν καὶ ἀπελήλυθεν καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `TCGNT (Byz)`: κατενόησε γὰρ ἑαυτὸν καὶ ἀπελήλυθε καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `PT1904 (Byz)`: κατενόησε γὰρ ἑαυτὸν καὶ ἀπελήλυθε, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `TR-Scrivener (1894)`: κατενόησε γὰρ ἑαυτὸν καὶ ἀπελήλυθε, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `TR-Boyd (Elz/Scr/Steph)`: κατενόησε γὰρ ἑαυτὸν καὶ ἀπελήλυθε, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν.
  - `TR-Stephanus (1550)`: κατενόησε γὰρ ἑαυτὸν, καὶ ἀπελήλυθε, καὶ εὐθέως ἐπελάθετο ὁποῖος ἦν·
  - `TR-Elzevir (1624)`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεως επελαθετο οποιος ην
  - `A (02)`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεωσ επελαθετο οποιοσ ην
  - `C (04)`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεωσ επελαθετο οποιοσ ην
  - `33`: κατενοησεν γαρ εαυτον και απεληλυθεν και ευθεως επελαθετο οποιος ην
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 10 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 25 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `SRGNT`: Ὁ δὲ παρακύψας εἰς νόμον τέλειον, τὸν τῆς ἐλευθερίας, καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος, ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `SBLGNT`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `BHP`: ὁ δὲ παρακύψας εἰς νόμον τέλειον, τὸν τῆς ἐλευθερίας, καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος, ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `Nestle1904`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `RP2018 (Byz)`: Ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `TR (KJTR)`: Ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας, καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος, ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `B (03)`: ο δε παρακυψασ εισ νομον τελειον τον τησ ελευθεριασ και παραμεινασ ουκ ακροατησ επιλησμονησ γενομενοσ αλλα ποιητησ εργου ουτοσ μακαριοσ εν τη ποιησει αυτου εσται
  - `א (01)`: ο δε παρακυψασ εισ νομον τελειον τον τησ ελευθεριασ και παραμινασ ουκ ακροατησ επιλησμονησ γενομενοσ αλλα ποιητησ εργου ουτοσ μακαριοσ εν τη ποιησει αυτου εσται
  - `NA28 (TAGNT)`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `THGNT`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `WH1881`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `Tisch8`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `TCGNT (Byz)`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου· οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `PT1904 (Byz)`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος, ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `TR-Scrivener (1894)`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `TR-Boyd (Elz/Scr/Steph)`: Ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὐτοῦ ἔσται.
  - `TR-Stephanus (1550)`: ὁ δὲ παρακύψας εἰς νόμον τέλειον τὸν τῆς ἐλευθερίας καὶ παραμείνας, οὗτος οὐκ ἀκροατὴς ἐπιλησμονῆς γενόμενος, ἀλλὰ ποιητὴς ἔργου, οὗτος μακάριος ἐν τῇ ποιήσει αὑτοῦ ἔσται.
  - `TR-Elzevir (1624)`: ο δε παρακυψας εις νομον τελειον τον της ελευθεριας και παραμεινας ουτος ουκ ακροατης επιλησμονης γενομενος αλλα ποιητης εργου ουτος μακαριος εν τη ποιησει αυτου εσται
  - `A (02)`: ο δε παρακυψασ εισ νομον τελειον τον τησ ελευθεριασ και παραμεινασ ουκ ακροατησ επιλησμονησ γενομενοσ αλλα ποιητησ εργου ουτοσ μακαριοσ εν τη ποιησει αυτου εσται
  - `C (04)`: ο δε παρακυψασ εισ νομον τελειον τον τησ ελευθεριασ και παραμεινασ ουκ ακροατησ επιλησμονησ γενομενοσ αλλα ποιητησ εργου ουτοσ μακαριοσ εν τη ποιησει αυτου εσται
  - `33`: ο δε παρακυψας εις νομον τελειον τον της ελευθεριας […] παραμεινας ουκ ακροατης επιλισμονης γενομενος αλλ ακροατης νομου και ποιητης […] ουτος μακαριος εν τη ποιησει αυτου εσται
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over οὗτος (RP2018 (Byz), TR (KJTR)). Also normalised 25 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 26 (Confidence: `66.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Εἴ τις δοκεῖ θρησκὸς εἶναι μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `SRGNT`: Εἴ τις δοκεῖ θρησκὸς εἶναι, μὴ χαλιναγωγῶν γλῶσσαν ἑαυτοῦ, ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `SBLGNT`: Εἴ τις δοκεῖ θρησκὸς εἶναι μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `BHP`: εἴ τις δοκεῖ θρησκὸς εἶναι, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `Nestle1904`: Εἴ τις δοκεῖ θρησκὸς εἶναι, μὴ χαλιναγωγῶν γλῶσσαν ἑαυτοῦ ἀλλὰ ἀπατῶν καρδίαν ἑαυτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `RP2018 (Byz)`: Εἴ τις δοκεῖ θρῆσκος εἶναι ἐν ὑμῖν, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `TR (KJTR)`: Εἴ τις δοκεῖ θρησκὸς εἶναι ἐν ὑμῖν, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `B (03)`: ει τισ δοκει θρησκοσ ειναι μη χαλινων γλωσσαν εαυτου αλλα απατων καρδιαν εαυτου τουτου ματαιοσ η θρησκεια
  - `א (01)`: ει τισ δοκει θρησκοσ ειναι μη χαλιναγωγων γλωσσαν αυτου αλλα απατων καρδιαν αυτου του ματαιοσ η θρησκια
  - `NA28 (TAGNT)`: Εἴ τις δοκεῖ θρησκὸς εἶναι μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλ᾽ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `THGNT`: Εἴ τις δοκεῖ θρῆσκος εἶναι μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `WH1881`: Εἴ τις δοκεῖ θρησκὸς εἶναι μὴ χαλιναγωγῶν γλῶσσαν ἑαυτοῦ ἀλλὰ ἀπατῶν καρδίαν ἑαυτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `Tisch8`: εἴ τις δοκεῖ θρησκὸς εἶναι, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκία.
  - `TCGNT (Byz)`: Εἴ τις δοκεῖ θρῆσκος εἶναι ἐν ὑμῖν μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ ἀλλὰ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `PT1904 (Byz)`: Εἴ τις δοκεῖ θρῆσκος εἶναι ἐν ὑμῖν μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλ᾽ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `TR-Scrivener (1894)`: εἴ τις δοκεῖ θρῆσκος εἶναι ἐν ὑμῖν, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλ᾽ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `TR-Boyd (Elz/Scr/Steph)`: Εἴ τις δοκεῖ θρῆσκος εἶναι ἐν ὑμῖν, μὴ χαλιναγωγῶν γλῶσσαν αὐτοῦ, ἀλλ᾿ ἀπατῶν καρδίαν αὐτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `TR-Stephanus (1550)`: Εἴ τις δοκεῖ θρησκὸς εἶναι ἐν ὑμῖν, μὴ χαλιναγωγῶν γλῶσσαν αὑτοῦ, ἀλλʼ ἀπατῶν καρδίαν αὑτοῦ, τούτου μάταιος ἡ θρησκεία.
  - `TR-Elzevir (1624)`: ει τις δοκει θρησκος ειναι εν υμιν μη χαλιναγωγων γλωσσαν αυτου αλλ απατων καρδιαν αυτου τουτου ματαιος η θρησκεια
  - `A (02)`: ει τισ δοκει θρησκοσ ειναι μη χαλιναγωγων γλωσσαν αυτου αλλα απατων καρδιαν αυτου τουτου ματαιοσ η θρησκεια
  - `C (04)`: ει δε τισ δοκει θρησκοσ ειναι μη χαλιναγων γλωσσαν αυτου αλλα απατων καρδιαν εαυτου τουτου ματαιοσ η θρησκεια
  - `33`: ει δε τις δοκει θρισκος ειναι μη χαλιναγωγων γλωσσαν αυτου αλλα απατων καρδιαν αυτου τουτου ματαιος η θρισκια
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἐν ὑμῖν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'χαλιναγωγῶν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over χαλινων (B (03)). [Lexical, morphological, or word-order variant] Adopted 'αὐτοῦ' [א (01), SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.10, confidence 70%) over ἑαυτοῦ (B (03), SRGNT, Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'αὐτοῦ' [א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.05, confidence 97%) over ἑαυτοῦ (B (03), Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'τούτου' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over του (א (01)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 66% = product of 5 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 27 (Confidence: `96.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `SRGNT`: Θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ Πατρὶ αὕτη ἐστίν: ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `SBLGNT`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `BHP`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ Πατρὶ αὕτη ἐστίν: ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `Nestle1904`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ Πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `RP2018 (Byz)`: Θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TR (KJTR)`: Θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ Θεῷ καὶ Πατρὶ αὕτη ἐστίν, Ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `B (03)`: θρησκεια καθαρα κι αμιαντοσ παρα τω θω̅ και πατρι αυτη εστιν επισκεπτεσθαι ορφανουσ και χηρασ εν τη θλειψει αυτων ασπιλον εαυτον τηρειν απο του κοσμου
  - `א (01)`: θρησκια καθαρα και αμιαντοσ παρα θω̅ και πατρι αυτη εστιν επισκεπτεσθε ορφανουσ και χηρασ εν τη θλιψει αυτων ασπιλον εαυτον τηριν απο του κοσμου
  - `NA28 (TAGNT)`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `THGNT`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `WH1881`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `Tisch8`: θρησκία καθαρὰ καὶ ἀμίαντος παρὰ θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TCGNT (Byz)`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ Θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `PT1904 (Byz)`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TR-Scrivener (1894)`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TR-Boyd (Elz/Scr/Steph)`: Θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ πατρὶ αὕτη ἐστίν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TR-Stephanus (1550)`: θρησκεία καθαρὰ καὶ ἀμίαντος παρὰ τῷ Θεῷ καὶ πατρὶ αὕτη ἐστὶν, ἐπισκέπτεσθαι ὀρφανοὺς καὶ χήρας ἐν τῇ θλίψει αὐτῶν, ἄσπιλον ἑαυτὸν τηρεῖν ἀπὸ τοῦ κόσμου.
  - `TR-Elzevir (1624)`: θρησκεια καθαρα και αμιαντος παρα τω θεω και πατρι αυτη εστιν επισκεπτεσθαι ορφανους και χηρας εν τη θλιψει αυτων ασπιλον εαυτον τηρειν απο του κοσμου
  - `A (02)`: θρησκεια γαρ καθαρα και αμιαντοσ παρα τω θω̅ και τω πρι̅ αυτη εστιν επισκεπτεσθαι ορφανουσ και χηρασ εν τη θλιψει αυτων ασπειλον σεαυτον τηρειν απο του κοσμου
  - `C (04)`: θρησκεια καθαρα και αμιαντοσ παρα τω θω̅ και πρι̅ αυτη εστιν επισκεπτεσθαι ορφανουσ και χηρασ εν τη θλιψει αυτων ασπιλον εαυτον τηρειν εκ του κοσμου
  - `33`: καθαρα και […] παρα τω θω̅ και πρι̅ αυτη εστιν επισκεπτεσθε ορφανους και χειρας εν τη θλιψει […] ασπηλον εαυτον τηρειν απο του κοσμου
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'καὶ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over κι (B (03)). [Omission in some witnesses] Adopted 'τῷ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over om. (א (01), RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐπισκέπτεσθαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επισκεπτεσθε (א (01)). Also normalised 22 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
