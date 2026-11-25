# Luke 02 — Saints Greek Critical Text

**Division:** `05_Salvation` · **Language:** `Greek` · **Engine:** `Textual Analysis Brain (Claude-designed · internal evidence · offline)` · **Updated:** `2026-11-25T00:07:45Z`

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
| **𝔓4** | Papyrus 4 — Paris Luke Papyrus (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Early Alexandrian Papyrus (Luke 1–6) |
| **A (02)** | Codex Alexandrinus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Byzantine (Gospels) / Premier Alexandrian (Acts, Epistles, Revelation) |
| **Ξ (040)** | Codex Zacynthius — 6th-c. Palimpsest of Luke 1–11 (ITSEE CC BY 4.0) | Tier 4 | CC BY 4.0 (UBIRA eData / ITSEE Birmingham) | Early Alexandrian Uncial (Luke 1–11) |
| **C (04)** | Codex Ephraemi Rescriptus Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Mixed Alexandrian / Early Eclectic Palimpsest |
| **W (032)** | Codex Washingtonianus / Freer Gospels (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Block-Mixed Gospels Uncial (Alexandrian, Western, Caesarean, Byzantine) |
| **33** | Minuscule 33 — Queen of the Cursives (INTF NTVMR & IGNTP Paul XML) | Tier 4 | CC BY 4.0 | Premier Alexandrian Minuscule (Gospels, Acts, Epistles) |
| **L (019)** | Codex Regius Direct Transcription (INTF NTVMR XML) | Tier 4 | CC BY 4.0 | Late Alexandrian Gospels Uncial (with Shorter & Longer Endings of Mark) |
| **D (05)** | Codex Bezae Cantabrigiensis Direct Transcription (CNTR Early MSS) | Tier 4 | CC BY-SA 4.0 | Premier Western Text-Type (Gospels & Acts) |
| **Θ (038)** | Codex Koridethi Direct Transcription (INTF NTVMR XML) | Tier 4 | CC BY 4.0 | Caesarean Gospels Uncial (Anchor Witness in Mark) |
| **1 (f¹)** | Minuscule 1 — Head of Family 1 / Lake Group (INTF NTVMR XML) | Tier 4 | CC BY 4.0 | Family 1 (Lake Group / Caesarean-Allied Gospels & Acts) |
| **13 (f¹³)** | Minuscule 13 — Head of Family 13 / Ferrar Group (INTF NTVMR XML) | Tier 4 | CC BY 4.0 | Family 13 (Ferrar Group / Caesarean-Allied Gospels) |

### Disregarded / Quarantined Sources (Excluded by AI Gatekeeper)
| Source | Status | Reason Excluded from Open Critical Text |
| :--- | :---: | :--- |
| Pickering-f35 | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-ND (Tier 5 — Owner-Authorized Apparatus)) — held in local Studio only; excluded from public open-licence exports. |
| Tregelles (1879) | `EXCLUDED_TIER5_OPEN_EXPORT` | Tier 5 (CC BY-NC-SA 3.0 (Owner-Authorized Apparatus Witness)) — held in local Studio only; excluded from public open-licence exports. |

### Versification & Alignment Notes
- 𝔓4: 2:2 not collated (wording does not match the reference verse)
- 𝔓4: 2:4 not collated (wording does not match the reference verse)

---

## Section II — Continuous Greek Critical Text

**1** Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην·
**2** (αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου·)
**3** καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
**4** Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυὶδ ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
**5** ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
**6** ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
**7** καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
**8** Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
**9** καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν·
**10** καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· Μὴ φοβεῖσθε, ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ,
**11** ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει Δαυίδ·
**12** καὶ τοῦτο ὑμῖν τὸ σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
**13** καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
**14** Δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
**15** Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· Διέλθωμεν δὴ ἕως Βηθλέεμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
**16** καὶ ἦλθον σπεύσαντες καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
**17** ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
**18** καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς,
**19** ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
**20** καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
**21** Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
**22** Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ,
**23** καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται,
**24** καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
**25** Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπʼ αὐτόν·
**26** καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἂν ἴδῃ τὸν χριστὸν κυρίου.
**27** καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ
**28** καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
**29** Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
**30** ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
**31** ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
**32** φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
**33** καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
**34** καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον,
**35** καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
**36** Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ (αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
**37** καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων,) ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
**38** καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
**39** Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέτ.
**40** Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπʼ αὐτό.
**41** Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
**42** καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
**43** καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
**44** νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
**45** καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἰερουσαλὴμ ἀναζητοῦντες αὐτόν.
**46** καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
**47** ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
**48** καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ζητοῦμέν σε.
**49** καὶ εἶπεν πρὸς αὐτούς· Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
**50** καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
**51** καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
**52** Καὶ Ἰησοῦς προέκοπτεν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.

---

## Section III — Critical Apparatus & Disregarded Surface Noise

### Luke 2:1
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) 𝔓4 **]** **om.** A (02) Ξ (040)
- **Apparatus:** `Αὐγούστου ἀπογράφεσθαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **αγουστου απογραφεσθε** א (01) ; **αυγουστου απογραψασθαι** 1 (f¹) 13 (f¹³) ; **αυγουστου του απογραφεσθαι** 33 L (019) W (032) Ξ (040) ; **αγουστου απογραφεσθαι** C (04) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Ἐγένετο` over `εγενετο`, `ἐγένετο` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραις` over `ημεραισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκείναις` over `εκειναισ`, `εκιναισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐξῆλθεν` over `εξηλθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόγμα` over `δογμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρὰ` over `παρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Καίσαρος` over `καισαροσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶσαν` over `πασαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἰκουμένην·` over `οικουμενην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:2
- **Apparatus:** `αὕτη` B (03) SRGNT RP2018 (Byz) TR (KJTR) SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 Θ (038) **]** **αυτην** א (01) ; **αυτη η** 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Ξ (040) ; **αυτη εγενετο** D (05) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 WH1881 Θ (038) **]** **ἡ** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Ξ (040) ; **εγενετο** D (05) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἀπογραφὴ πρώτη ἐγένετο` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) WH1881 Θ (038) Ξ (040) **]** **απογραφην εγενετο πρωτη** א (01) ; **απογραφη πρωτη** D (05) ; **ἀπογραφὴ ἐγένετο πρώτη** Tisch8 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `Κυρηνίου` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 33 C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **κυρεινου** B (03) W (032) ; **κυρινιου** 13 (f¹³) Ξ (040) ; **κηρυνιου** A (02) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἡγεμονεύοντος` over `ηγεμονευοντοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Συρίας` over `συριασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:3
- **Apparatus:** `πάντες ἀπογράφεσθαι ἕκαστος` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **εκαστοσ απογραφεσθε** א (01) ; **παντεσ** 𝔓4 *(partial substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἑαυτοῦ` B (03) SRGNT SBLGNT Nestle1904 BHP D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ἰδίαν** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **εαυτων** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `πόλιν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **πατριδα** D (05) ; **πολην** L (019) ; **χωραν** C (04)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπορεύοντο` over `επορευοντο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλιν.` over `πολιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:4
- **Apparatus:** `Ἰωσὴφ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ηωσηφ** L (019)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ο** Θ (038)
- **Apparatus:** `Ναζαρὲθ` א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 13 (f¹³) D (05) NA28 (TAGNT) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 Θ (038) **]** **Ναζαρέτ** B (03) RP2018 (Byz) TR (KJTR) 33 L (019) PT1904 (Byz) TCGNT (Byz) THGNT TR-Stephanus (1550) W (032) WH1881 Ξ (040) ; **ναζαραθ** A (02) C (04) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `τὴν Ἰουδαίαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **γην ιουδα** D (05)
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **την** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἥτις` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ητης** L (019)
- **Apparatus:** `καλεῖται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **καλειτε** A (02) D (05)
- **Apparatus:** `διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** D (05)
- *Disregarded Surface Variant:* kept `Ἀνέβη` over `ανεβη`, `ἀνέβη` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰωσὴφ` over `ιωσηφ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Γαλιλαίας` over `γαλειλαιασ`, `γαλιλαιασ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλεως` over `πολεωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰουδαίαν` over `ιουδαιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλιν` over `πολιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Δαυὶδ` over `δαυειδ`, `δαδ̅`, `Δαυεὶδ`, `Δαυεὶδ,`, `Δαυίδ,` (B (03), BHP, Nestle1904, RP2018 (Byz), TR (KJTR), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἥτις` over `ητισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καλεῖται` over `καλειται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Βηθλέεμ,` over `βηθλεεμ`, `Βηθλεέμ,` (B (03), Nestle1904, א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `διὰ` over `δια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶναι` over `ειναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξ` over `εξ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἴκου` over `οικου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατριᾶς` over `πατριασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Δαυίδ,` over `δαυειδ`, `δαδ̅`, `Δαυείδ,` (B (03), BHP, Nestle1904, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `πόλεως / π ολεως` (Θ (038)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:5
- **Apparatus:** `ἀπογράψασθαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **απογραφεσθαι** א (01) D (05) W (032) ; **συμ** A (02) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `σὺν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **συ** Θ (038) ; **om.** A (02)
- **Apparatus:** `Μαριὰμ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **μαρια** D (05) ; **μαρηαμ** L (019)
- **Apparatus:** `ἐμνηστευμένῃ αὐτῷ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP C (04) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **μεμνηστευμένῃ αὐτῷ γυναικί** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **μεμνηστευμενη αυτωι** 1 (f¹) ; **εμνηστευμενη αυτω γυναικι** A (02) *(partial substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐγκύῳ` SRGNT SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) א (01) BHP 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **εγγυω** B (03) ; **ενκυω δια το ειναι αυτον εξ οικου και πατριασ δαυειδ** D (05) ; **νεκυω** W (032) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `σὺν` over `συν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μαριὰμ` over `μαριαμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὔσῃ` over `ουση` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐγκύῳ` over `ενκυω`, `ἐνκύῳ` (BHP, א (01)) — *Spelling variant pooled before the vote with the reading 'ἐγκύῳ' (same word, different spelling); whether that reading was adopted is shown in the apparatus*

### Luke 2:6
- **Apparatus:** `ἐγένετο` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ωσ** D (05)
- **Apparatus:** `ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **παρεγεινοντο ετελεσθησαν** D (05) ; **εν το ειναι αυτους εκει επλησθησαν** L (019)
- **Apparatus:** `τῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **το** L (019) ; **ετελεσθησαν** D (05)
- *Disregarded Surface Variant:* kept `ἐγένετο` over `εγενετο`, `Ἐγένετο` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶναι` over `ειναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὺς` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκεῖ` over `εκει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπλήσθησαν` over `επλησθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἱ` over `αι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραι` over `ημεραι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τεκεῖν` over `τεκειν`, `τεκιν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτήν,` over `αυτην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῷ / τωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:7
- **Apparatus:** `τὸν πρωτότοκον,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) 𝔓4 **]** **om.** W (032)
- **Apparatus:** `ἐν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **επι** א (01) ; **εν τη** 33 PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **τῇ** RP2018 (Byz) TR (KJTR) 33 PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔτεκεν` over `ετεκεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `υἱὸν` over `υιον`, `υν̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `αὐτῆς` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρωτότοκον,` over `πρωτοτοκον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐσπαργάνωσεν` over `εσπαργανωσεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον`, `αὐτόν,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνέκλινεν` over `ανεκλεινεν`, `ανεκλινεν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φάτνῃ,` over `φατνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διότι` over `διοτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τόπος` over `τοποσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καταλύματι.` over `καταλυματι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῷ / τωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:8
- **Apparatus:** `Καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** D (05)
- **Apparatus:** `ποιμένες` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ποιμαινεσ** א (01) L (019) ; **ποιμενεσ δε** D (05) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αυτη** 33
- **Apparatus:** `χώρᾳ τῇ αὐτῇ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **χαρα ταυτη** D (05) ; **χωρα** 33 ; **χορα τη αυτη** Θ (038)
- **Apparatus:** `χώρᾳ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **χορα** Θ (038) ; **χαρα** D (05)
- **Apparatus:** `τῇ αὐτῇ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** 33 ; **ταυτη** D (05)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **τασ** D (05)
- **Apparatus:** `τῆς νυκτὸς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** Ξ (040)
- **Apparatus:** `τὴν ποίμνην` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **της ποιμνης** 1 (f¹) ; **την πιμνην** 13 (f¹³)
- **Apparatus:** `ποίμνην` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **πιμνην** 13 (f¹³) ; **ποιμνης** 1 (f¹)
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦσαν` over `ησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χώρᾳ` over `χωρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῇ` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγραυλοῦντες` over `αγραυλουντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυλάσσοντες` over `φυλασσοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυλακὰς` over `φυλακασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νυκτὸς` over `νυκτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποίμνην` over `ποιμνην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν.` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῇ χώρᾳ τῇ αὐτῇ / τηι χωραι τηι αυτηι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `φυλάσσοντες / φυλασσον τες` (L (019)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:9
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ἰδού** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `δόξα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **δοξαν** A (02)
- **Apparatus:** `κυρίου` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05) ; **θυ̅ (= θεοῦ)** Ξ (040)
- **Apparatus:** `περιέλαμψεν αὐτούς` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **επελαμψεν αυτοισ** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `φόβον μέγαν` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **σφοδρα** B (03) ; **φοβον μεγαν σφοδρα** W (032) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ`, `Καὶ,` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄγγελος` over `αγγελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐπέστη` over `επεστη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξα` over `δοξα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐφοβήθησαν` over `εφοβηθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:10
- **Apparatus:** `ὁ ἄγγελος·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** A (02)
- **Apparatus:** `φοβεῖσθε,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ξ (040) **]** **φοβεισθαι** A (02) W (032) ; **φοβησθαι** Θ (038)
- **Apparatus:** `μεγάλην` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **μεγαιην** D (05)
- **Apparatus:** `ἔσται` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **εστιν** א (01) ; **εσται και** D (05) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶπεν` over `ειπεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄγγελος·` over `αγγελοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μὴ` over `μη`, `“μὴ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φοβεῖσθε,` over `φοβεισθε`, `φοβισθε` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἰδοὺ` over `ιδου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γὰρ` over `γαρ`, `γάρ,` (B (03), RP2018 (Byz), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐαγγελίζομαι` over `ευαγγελιζομαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χαρὰν` over `χαραν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μεγάλην` over `μεγαλην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἥτις` over `ητισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παντὶ` over `παντι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαῷ,` over `λαω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `λαῷ, / λαωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:11
- **Apparatus:** `ἐτέχθη` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **εχθη** L (019)
- **Apparatus:** `ὅς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ο** 1 (f¹)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **κσ̅ (= κύριοσ)** W (032)
- **Apparatus:** `κύριος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **om.** W (032)
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι`, `Ὅτι` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐτέχθη` over `ετεχθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑμῖν` over `υμιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σήμερον` over `σημερον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σωτὴρ` over `σωτηρ`, `Σωτὴρ,`, `Σωτήρ,`, `σωτήρ,` (B (03), BHP, Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅς` over `οσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐστιν` over `εστιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χριστὸς` over `χσ̅`, `Χριστὸς,`, `Χριστὸς` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `κύριος` over `κσ̅`, `Κύριος,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλει` over `πολει`, `πολι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `Δαυίδ·` over `δαυειδ`, `δαδ̅`, `Δαυείδ.` (B (03), BHP, Nestle1904, א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*

### Luke 2:12
- **Apparatus:** `ὑμῖν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ημιν** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τὸ` א (01) SRGNT SBLGNT BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) Θ (038) **]** **om.** B (03) Nestle1904 WH1881 Ξ (040) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `εὑρήσετε` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Ξ (040) **]** **ευρησεται** א (01) 13 (f¹³) 33 A (02) L (019) W (032) Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `καὶ` B (03) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 L (019) NA28 (TAGNT) THGNT W (032) WH1881 Θ (038) Ξ (040) **]** **om.** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 ; **επι** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `κείμενον ἐν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT W (032) WH1881 Θ (038) Ξ (040) **]** **om.** א (01) ; **εν** D (05) Tisch8 ; **κείμενον ἐν τῇ** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **τῇ** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦτο` over `τουτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σημεῖον,` over `σημειον`, `σημιον` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `βρέφος` over `βρεφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐσπαργανωμένον` over `εσπαργανωμενον`, `εσσπαργανωμενον` (B (03), א (01)) — *Single / double consonant spelling (Ἰωάνης / Ἰωάννης type)*
- *Disregarded Surface Variant:* kept `φάτνῃ.` over `φατνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:13
- **Apparatus:** `ἐξαίφνης` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 33 D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 **]** **εξεφνησ** א (01) 13 (f¹³) A (02) L (019) W (032) WH1881 Θ (038) Ξ (040) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `οὐρανίου` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ουρανου** B (03) D (05) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `λεγόντων·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **λεγοντον** Θ (038)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐγένετο` over `εγενετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σὺν` over `συν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγγέλῳ` over `αγγελω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πλῆθος` over `πληθοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `στρατιᾶς` over `στρατειασ`, `στρατιασ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αἰνούντων` over `αινουντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸν` over `θν̅`, `Θεὸν`, `θεόν,`, `Θεὸν,` (B (03), BHP, Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λεγόντων·` over `λεγοντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἀγγέλῳ / αγγελωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:14
- **Apparatus:** `θεῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **θωι̅ (= θωι)** 1 (f¹)
- **Apparatus:** `ἐπὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **επη** L (019)
- **Apparatus:** `εὐδοκίας` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP A (02) D (05) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **εὐδοκία** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) Ξ (040) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Δόξα` over `δοξα`, `“δόξα` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑψίστοις` over `υψιστοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεῷ` over `θω̅`, `Θεῷ,`, `Θεῷ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γῆς` over `γησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνη` over `ειρηνη`, `ιρηνη` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθρώποις` over `ανθρωποισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:15
- **Apparatus:** `ἐγένετο` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **εγενετω** Θ (038)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **οι αγγελοι** D (05)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **οι αγγελοι** 13 (f¹³) 33 Θ (038)
- **Apparatus:** `τὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **των** Θ (038)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **και** 13 (f¹³) 33 D (05)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **καὶ οἱ ἄνθρωποι** RP2018 (Byz) TR (KJTR) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **και** A (02) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `οἱ ποιμένες` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ποιμαινεσ** א (01) ; **οι ανοι̅ (= οι ἄνθρωποι)** A (02) ; **οι ποιμαινες** L (019) ; **ποιμενες** Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐλάλουν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **εἶπον** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **οι ποιμαινεσ ειπον** A (02) ; **ειπαν** L (019) Ξ (040) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **λεγοντεσ** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δὴ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **δι** L (019) ; **om.** Ξ (040)
- **Apparatus:** `ἴδωμεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ειδομεν** 13 (f¹³)
- **Apparatus:** `γεγονὸς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **γεγονωσ** D (05)
- **Apparatus:** `ἐγνώρισεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **εγνωρησεν** L (019) Θ (038)
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐγένετο` over `εγενετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπῆλθον` over `απηλθον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀπʼ` over `απ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐρανὸν` over `ουρανον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄγγελοι,` over `αγγελοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀλλήλους·` over `αλληλουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Διέλθωμεν` over `διελθωμεν`, `“διέλθωμεν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὴ` over `δη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἕως` over `εωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Βηθλέεμ` over `βηθλεεμ`, `Βηθλεὲμ`, `Βηθλεέμ,` (B (03), Nestle1904, TR (KJTR), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἴδωμεν` over `ιδωμεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥῆμα` over `ρημα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦτο` over `τουτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γεγονὸς` over `γεγονοσ`, `γεγονός,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κύριος` over `κσ̅`, `Κύριος` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐγνώρισεν` over `εγνωρισεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν.` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τοῦτο / τ ουτο` (Θ (038)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:16
- **Apparatus:** `ἦλθον` א (01) SRGNT BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Θ (038) **]** **ἦλθαν** B (03) SBLGNT Nestle1904 L (019) NA28 (TAGNT) THGNT Tisch8 WH1881 Ξ (040) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `σπεύσαντες` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **σπευδοντεσ** D (05) ; **πισπευσαντες** Ξ (040)
- **Apparatus:** `ἀνεῦραν` B (03) SRGNT SBLGNT Nestle1904 L (019) NA28 (TAGNT) Tisch8 WH1881 **]** **ἀνεῦρον** א (01) BHP RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **ευρον** 1 (f¹) 13 (f¹³) D (05) W (032) ; **ευραν** Ξ (040) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `τε Μαριὰμ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **μαριαν** D (05)
- **Apparatus:** `φάτνῃ·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **φατνι** L (019)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σπεύσαντες` over `σπευσαντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τήν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μαριὰμ` over `μαριαμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰωσὴφ` over `ιωσηφ`, `Ἰωσήφ,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `βρέφος` over `βρεφοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κείμενον` over `κειμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φάτνῃ·` over `φατνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `Ἰωσὴφ / ιω σηφ` (L (019)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:17
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** Ξ (040)
- **Apparatus:** `ἐγνώρισαν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP D (05) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **διεγνώρισαν** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **εγνωρησαν** L (019) ; **διεγνωρησαν** Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `παιδίου τούτου.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **πεδιου** Θ (038) ; **παιδιου** 1 (f¹) D (05)
- **Apparatus:** `τούτου.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **om.** 1 (f¹) D (05) Θ (038)
- *Disregarded Surface Variant:* kept `ἰδόντες` over `ιδοντεσ`, `Ἰδόντες` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥήματος` over `ρηματοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαληθέντος` over `λαληθεντοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παιδίου` over `παιδιου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τούτου.` over `τουτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:18
- **Apparatus:** `οἱ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** 1 (f¹)
- **Apparatus:** `ἀκούσαντες ἐθαύμασαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ακουοντεσ εθαυμαζον** D (05)
- **Apparatus:** `τῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **τον** Θ (038)
- **Apparatus:** `λαληθέντων` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **λαληθετων** L (019)
- **Apparatus:** `ποιμένων` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ποιμαινων** L (019)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντες` over `παντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκούσαντες` over `ακουσαντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐθαύμασαν` over `εθαυμασαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαληθέντων` over `λαληθεντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιμένων` over `ποιμενων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτούς,` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:19
- **Apparatus:** `Μαρία` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP THGNT Tisch8 WH1881 Θ (038) **]** **Μαριὰμ** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Ξ (040) ; **μαρια συνετηρει** D (05) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `συνετήρει` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** D (05)
- **Apparatus:** `ταῦτα` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτῆς.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **εαυτης** 33
- *Disregarded Surface Variant:* kept `ἡ` over `η`, `Ἡ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντα` over `παντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συνετήρει` over `συνετηρει`, `συνετηρι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥήματα` over `ρηματα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συμβάλλουσα` over `συμβαλλουσα`, `συνβαλλουσα`, `συνβάλλουσα` (B (03), Nestle1904, א (01)) — *Prefix assimilation spelling (συνπ-/συμπ-, ἐνκ-/ἐγκ-, συνζ-/συζ-, Κενχρ-/Κεγχρ- type)*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρδίᾳ` over `καρδια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῆς.` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `συμβάλλουσα / συνβαλλουσα`, `συμβάλλουσα / συνβάλλουσα`, `συμβάλλουσα / συνβαλλουσα`, `συμβάλλουσα / συνβάλλουσα` (D (05), Tisch8, W (032), WH1881) — *Apparatus witness, not a variant: Prefix assimilation spelling (συνπ-/συμπ-, ἐνκ-/ἐγκ-, συνζ-/συζ-, Κενχρ-/Κεγχρ- type)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `συμβάλλουσα / συνβαλλου σα` (Θ (038)) — *Apparatus witness, not a variant: Word division differs, with a spelling difference*

### Luke 2:20
- **Apparatus:** `ὑπέστρεψαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **ἐπέστρεψαν** TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550)
- **Apparatus:** `ποιμένες` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 33 D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ποιμαινεσ** א (01) A (02) L (019) ; **ποιμεναις** 13 (f¹³) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τὸν θεὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τονθν̅ (= τονθν)** 13 (f¹³)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπέστρεψαν` over `υπεστρεψαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοξάζοντες` over `δοξαζοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἰνοῦντες` over `αινουντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸν` over `θν̅`, `Θεὸν` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶσιν` over `πασιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἷς` over `οισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἤκουσαν` over `ηκουσαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶδον` over `ειδον`, `ιδον` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καθὼς` over `καθωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλαλήθη` over `ελαληθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτούς.` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:21
- **Apparatus:** `ἐπλήσθησαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) A (02) L (019) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **επληρωθησαν αι** 33 ; **συνετελεσθησαν αι** D (05) ; **επληρωθησαν** Θ (038) ; **ἐπλήσθησαν αἱ** 13 (f¹³) PT1904 (Byz)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αἱ** 13 (f¹³) PT1904 (Byz)
- **Apparatus:** `ὀκτὼ τοῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **οκτωOMτου** 13 (f¹³)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αι** D (05)
- **Apparatus:** `περιτεμεῖν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **περητεμειν** Θ (038)
- **Apparatus:** `αὐτόν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 1 (f¹) A (02) L (019) NA28 (TAGNT) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **τὸ παιδίον** TR (KJTR) 33 PT1904 (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **το** 13 (f¹³) D (05) *(lexical substitution)*
  - *transcriptional: harmonisation:* The reading 'τὸ παιδίον' agrees with the wording of Luke 1:59. Assimilation to a parallel is possible, but for a substitution the direction of change is not certain.
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **om.** Θ (038) ; **παιδιον** 13 (f¹³) D (05)
- **Apparatus:** `αὐτοῦ Ἰησοῦς,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αυτουις̅ (= αυτουισ)** 13 (f¹³)
- **Apparatus:** `κληθὲν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **λεχθεν** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `συλλημφθῆναι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **συλημφθηναι** L (019)
- **Apparatus:** `αὐτὸν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αυτην** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τῇ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** D (05)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **μητροσ** D (05)
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτε` over `οτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπλήσθησαν` over `επλησθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραι` over `ημεραι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀκτὼ` over `οκτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περιτεμεῖν` over `περιτεμειν`, `περιτεμιν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκλήθη` over `εκληθη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄνομα` over `ονομα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦς,` over `ισ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγγέλου` over `αγγελου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸ` over `προ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συλλημφθῆναι` over `συλλημφθηναι`, `συλληφθῆναι`, `συνλημφθῆναι` (B (03), BHP, RP2018 (Byz), TR (KJTR), א (01)) — *Spelling variant pooled before the vote with the reading 'συλλημφθῆναι' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κοιλίᾳ.` over `κοιλια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `συλλημφθῆναι / συλληφθηναι`, `συλλημφθῆναι / συλληφθηναι`, `συλλημφθῆναι / συλληφθηναι`, `συλλημφθῆναι / συλληφθῆναι`, `συλλημφθῆναι / συλληφθῆναι`, `συλλημφθῆναι / συλληφθῆναι`, `συλλημφθῆναι / συλληφθῆναι`, `συλλημφθῆναι / συλληφθηναι`, `συλλημφθῆναι / συλληφθῆναι`, `συλλημφθῆναι / συλληφθῆναι` (1 (f¹), 13 (f¹³), 33, PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550)) — *Apparatus witness, not a variant: Nasal spelling (λημψ- / ληψ-)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῇ κοιλίᾳ. / τηι κοιλιαι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `συλλημφθῆναι / συνλημφθηναι`, `συλλημφθῆναι / συνλημφθηναι` (D (05), W (032)) — *Apparatus witness, not a variant: Prefix assimilation spelling (συνπ-/συμπ-, ἐνκ-/ἐγκ-, συνζ-/συζ-, Κενχρ-/Κεγχρ- type)*

### Luke 2:22
- **Apparatus:** `ἐπλήσθησαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **επληροθησαν** Θ (038)
- **Apparatus:** `ἡμέραι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ημερα** Θ (038)
- **Apparatus:** `τοῦ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** B (03) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **αὐτῆς** TR (KJTR) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) ; **αυτου** D (05) ; **αυτον** Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `νόμον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **νομων** Θ (038)
- **Apparatus:** `Μωϋσέως` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 13 (f¹³) 33 D (05) NA28 (TAGNT) PT1904 (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **Μωσέως** RP2018 (Byz) TR (KJTR) 1 (f¹) A (02) L (019) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `παραστῆσαι` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **παραστησεται** א (01) ; **παραστησα** L (019) ; **παραστησε** Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τῷ κυρίῳ,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τωκω̅ (= τωκω)** 13 (f¹³) ; **τω κωι̅ (= τω κωι)** 1 (f¹) ; **κω̅ (= κυρίῳ)** D (05)
- **Apparatus:** `τῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05) ; **τωκω̅ (= τωκω)** 13 (f¹³)
- **Apparatus:** `κυρίῳ,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **κωι̅ (= κωι)** 1 (f¹) ; **om.** 13 (f¹³)
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτε` over `οτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπλήσθησαν` over `επλησθησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αἱ` over `αι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραι` over `ημεραι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθαρισμοῦ` over `καθαρισμου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνήγαγον` over `ανηγαγον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἱεροσόλυμα` over `ιεροσολυμα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίῳ,` over `κω̅`, `Κυρίῳ,`, `Κυρίῳ·` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### Luke 2:23
- **Apparatus:** `νόμῳ κυρίου` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **νομωκυ̅ (= νομωκυ)** 13 (f¹³)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τω** D (05)
- **Apparatus:** `διανοῖγον` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **διανοιγων** א (01) ; **διανυγον** Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἅγιον τῷ κυρίῳ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **αγιονκω̅ (= αγιονκω)** 13 (f¹³) ; **αγιον κω̅ (= αγιον κυρίῳ)** D (05)
- **Apparatus:** `τῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05) 13 (f¹³)
- *Disregarded Surface Variant:* kept `καθὼς` over `καθωσ`, `(Καθὼς` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γέγραπται` over `γεγραπται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμῳ` over `νομω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου` over `κυ̅`, `Κυρίου,`, `Κυρίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Πᾶν` over `παν`, `“πᾶν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄρσεν` over `αρσεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μήτραν` over `μητραν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἅγιον` over `αγιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίῳ` over `κω̅`, `Κυρίῳ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `κληθήσεται,` over `κληθησεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `νόμῳ / νομωι`, `τῷ / τωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:24
- **Apparatus:** `τῷ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **om.** RP2018 (Byz) TR (KJTR) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **νομωι** 1 (f¹) ; **νομωκυ̅ (= νομωκυ)** 13 (f¹³) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `νοσσοὺς` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **νεοσσοὺς** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) D (05) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοῦναι` over `δουναι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θυσίαν` over `θυσιαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρημένον` over `ειρημενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμῳ` over `νομω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου,` over `κυ̅`, `Κυρίου,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ζεῦγος` over `ζευγοσ`, `“Ζεῦγος`, `Ζεῦγος` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τρυγόνων` over `τρυγονων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἢ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δύο` over `δυο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περιστερῶν.` over `περιστερων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:25
- **Apparatus:** `ἰδοὺ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **ην** D (05) ; **ἰδοὺ ἦν** 1 (f¹) 13 (f¹³) 33 A (02) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038)
- **Apparatus:** `ἄνθρωπος ἦν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **ἦν ἄνθρωπος** RP2018 (Byz) TR (KJTR) 1 (f¹) 33 A (02) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **ανος̅ ενιλημ̅ (= ἄνθρωποσ ενιλημ)** 13 (f¹³) ; **ανθρωποσ** D (05) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `Ἰερουσαλὴμ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **Ἱεροσολύμοις** PT1904 (Byz) ; **om.** 13 (f¹³)
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **αυτου** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ὁ ἄνθρωπος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **οανος̅ (= οανοσ)** 13 (f¹³)
- **Apparatus:** `εὐλαβής` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ευσεβησ** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `προσδεχόμενος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **προσδεχομεμενοσ** D (05)
- **Apparatus:** `τοῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **τωι** 1 (f¹) ; **τω** L (019) Θ (038) ; **τουιηλ̅ (= τουιηλ)** 13 (f¹³)
- **Apparatus:** `τοῦ Ἰσραήλ, καὶ πνεῦμα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 **]** **τουιηλ̅ καιπνα̅ (= τουιηλ καιπνα)** 13 (f¹³) ; **τωι ιηλ̅ και πνα̅ (= τωι ἰσραὴλ και πνεῦμα)** 1 (f¹) ; **τοῦ Ἰσραήλ, καὶ πνεῦμα ἅγιον** D (05) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **τω ισλ̅ και πνα̅ (= τω ἰσραὴλ και πνεῦμα)** L (019) Θ (038)
- **Apparatus:** `ἦν ἅγιον` B (03) א (01) SRGNT Nestle1904 BHP SBLGNT RP2018 (Byz) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **Ἅγιον ἦν** TR (KJTR) D (05) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **αγιον** 1 (f¹) *(word-order transposition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰδοὺ` over `ιδου`, `ἰδού,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰερουσαλὴμ` over `ιερουσαλημ`, `Ἱερουσαλήμ,`, `Ἰερουσαλήμ,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `ᾧ` over `ω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὄνομα` over `ονομα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Συμεών,` over `συμεων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἄνθρωπος` over `ανθρωποσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτος` over `ουτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δίκαιος` over `δικαιοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προσδεχόμενος` over `προσδεχομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παράκλησιν` over `παρακλησιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰσραήλ,` over `ισραηλ`, `ιηλ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεῦμα` over `πνευμα`, `πνα̅`, `Πνεῦμα` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἐπʼ` over `επ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτόν·` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ᾧ / ωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:26
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **κεχρηματισμενοσ δε** D (05)
- **Apparatus:** `αὐτῷ κεχρηματισμένον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **om.** D (05) ; **αυτω κεχρηματισμενων** 13 (f¹³) ; **αυτω κεχρηματησμενον** Θ (038)
- **Apparatus:** `κεχρηματισμένον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **κεχρηματισμενων** 13 (f¹³) ; **κεχρηματησμενον** Θ (038) ; **om.** D (05)
- **Apparatus:** `ὑπὸ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **απο** L (019)
- **Apparatus:** `τοῦ πνεύματος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τουπνς̅ (= τουπνσ)** 13 (f¹³)
- **Apparatus:** `πρὶν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Θ (038) **]** **εωσ** א (01) ; **πριν η** 33 NA28 (TAGNT) Tisch8 WH1881 *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT BHP 1 (f¹) 13 (f¹³) A (02) D (05) L (019) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Θ (038) **]** **ἢ** SBLGNT Nestle1904 RP2018 (Byz) TR (KJTR) 33 NA28 (TAGNT) Tisch8 WH1881 *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, modern critical editions.
- **Apparatus:** `ἂν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 NA28 (TAGNT) THGNT Tisch8 WH1881 Θ (038) **]** **om.** RP2018 (Byz) TR (KJTR) W (032) ; **η** 1 (f¹) A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ιδειν** 13 (f¹³) ; **η να** L (019) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἴδῃ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **ηδη** 33 Θ (038)
- **Apparatus:** `τὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **om.** W (032) 13 (f¹³)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῷ` over `αυτω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κεχρηματισμένον` over `κεχρηματισμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπὸ` over `υπο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεύματος` over `πνευματοσ`, `πνσ̅`, `Πνεύματος` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἁγίου` over `αγιου`, `Ἁγίου,`, `Ἁγίου` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰδεῖν` over `ιδειν`, `ιδιν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `θάνατον` over `θανατον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἴδῃ` over `ιδη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χριστὸν` over `χν̅`, `Χριστὸν` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `κυρίου.` over `κυ̅`, `Κυρίου.` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `(adopted text)` over `αὐτῷ / αυτωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:27
- **Apparatus:** `τῷ πνεύματι` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **τωπνι̅ (= τωπνι)** 13 (f¹³) ; **το πνι̅ (= το πνεύματι)** Θ (038)
- **Apparatus:** `τῷ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **το** Θ (038) ; **τωπνι̅ (= τωπνι)** 13 (f¹³)
- **Apparatus:** `εἰσαγαγεῖν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **εισαγειν** A (02) W (032)
- **Apparatus:** `Ἰησοῦν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** א (01) *(omission / addition)*
  - *variant type: sacred name or title:* 'Ἰησοῦν' adds a sacred name or title; B (03) supports it, so the usual scribal tendency to expand such names gives no direction here.
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `εἰθισμένον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ηθισμενον** 33 A (02) ; **εθοσ** D (05)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦλθεν` over `ηλθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πνεύματι` over `πνευματι`, `πνι̅`, `Πνεύματι` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἱερόν·` over `ιερον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰσαγαγεῖν` over `εισαγαγειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοὺς` over `τουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γονεῖς` over `γονεισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παιδίον` over `παιδιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ποιῆσαι` over `ποιησαι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὺς` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰθισμένον` over `ειθισμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμου` over `νομου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῷ / τωι`, `τῷ / τωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:28
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **δε** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτὸ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **αὐτὸν** 13 (f¹³) PT1904 (Byz)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **αὐτοῦ** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `εὐλόγησεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **ηυλογησεν** D (05) W (032)
- **Apparatus:** `τὸν θεὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τονθν̅ (= τονθν)** 13 (f¹³)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸς` over `αυτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐδέξατο` over `εδεξατο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸ` over `αυτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀγκάλας` over `αγκαλασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὐλόγησεν` over `ευλογησεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεὸν` over `θν̅`, `Θεὸν`, `θεόν,`, `Θεόν,` (B (03), BHP, Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶπεν·` over `ειπεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:29
- **Apparatus:** `ἀπολύεις` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **απολλυεισ** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Νῦν` over `νυν`, `“νῦν` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δοῦλόν` over `δουλον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σου,` over `σου` (B (03), TR (KJTR), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `δέσποτα,` over `δεσποτα`, `Δέσποτα,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥῆμά` over `ρημα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σου` over `σου,` (RP2018 (Byz), TR (KJTR)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰρήνῃ·` over `ειρηνη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `εἰρήνῃ· / ειρηνηι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:30
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι`, `Ὅτι` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶδον` over `ειδον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὀφθαλμοί` over `οφθαλμοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σωτήριόν` over `σωτηριον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σου` over `σου,` (BHP, Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR)) — *Punctuation / spacing difference only*

### Luke 2:31
- **Apparatus:** `πρόσωπον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **πρωσωπον** Θ (038)
- **Apparatus:** `τῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** 1 (f¹)
- *Disregarded Surface Variant:* kept `ὃ` over `ο`, `Ὃ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡτοίμασας` over `ητοιμασασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρόσωπον` over `προσωπον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντων` over `παντων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαῶν,` over `λαων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:32
- **Apparatus:** `ἐθνῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `Ἰσραήλ.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ιστραηλ** D (05)
- *Disregarded Surface Variant:* kept `φῶς` over `φωσ`, `Φῶς` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποκάλυψιν` over `αποκαλυψιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐθνῶν` over `εθνων`, `Ἐθνῶν,` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δόξαν` over `δοξαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαοῦ` over `λαου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σου` over `σου,` (BHP, SRGNT) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `Ἰσραήλ.` over `ισραηλ`, `ιηλ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*

### Luke 2:33
- **Apparatus:** `ὁ πατὴρ αὐτοῦ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **Ἰωσὴφ** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **ο ιωσηφ** A (02) *(lexical substitution)*
  - *transcriptional: harmonisation:* The reading 'ὁ πατὴρ αὐτοῦ' agrees with the wording of Genesis 4:20. Assimilation to a parallel is possible, but for a substitution the direction of change is not certain.
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἡ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** 33
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 D (05) L (019) NA28 (TAGNT) THGNT W (032) WH1881 **]** **αὐτοῦ** א (01) RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **πασι** 1 (f¹)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μήτηρ` over `μητηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θαυμάζοντες` over `θαυμαζοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λαλουμένοις` over `λαλουμενοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ.` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:34
- **Apparatus:** `εὐλόγησεν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **ηυλογησεν** א (01) W (032) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `Συμεὼν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **Σιμεών,** TR-Scrivener (1894)
- **Apparatus:** `Μαριὰμ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **μαριαν** 13 (f¹³) D (05)
- **Apparatus:** `οὗτος` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ουτως** 13 (f¹³)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **εισ** D (05)
- **Apparatus:** `εἰς σημεῖον` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **σημιον** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὺς` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Συμεὼν` over `συμεων`, `Συμεών,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶπεν` over `ειπεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Μαριὰμ` over `μαριαμ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μητέρα` over `μητερα`, `μρα̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `αὐτοῦ·` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰδοὺ` over `ιδου`, `“ἰδοὺ,`, `Ἰδού,` (B (03), BHP, RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὗτος` over `ουτοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κεῖται` over `κειται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πτῶσιν` over `πτωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνάστασιν` over `αναστασιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πολλῶν` over `πολλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰσραὴλ` over `ισραηλ`, `ισλ̅`, `Ἰσραήλ,`, `Ἰσραήλ·` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀντιλεγόμενον,` over `αντιλεγομενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:35
- **Apparatus:** `δὲ` א (01) SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Θ (038) **]** **om.** B (03) SRGNT L (019) W (032) WH1881 Ξ (040) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `διελεύσεται` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **διελευσετε** L (019)
- **Apparatus:** `ἂν ἀποκαλυφθῶσιν ἐκ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **ανακαλυφθωσιν** D (05) ; **ανακαλυφθωσιν εκ** Θ (038) ; **αποκαλυφθωσιν εκ** Ξ (040)
- **Apparatus:** `ἂν ἀποκαλυφθῶσιν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **ανακαλυφθωσιν** Θ (038) D (05) ; **αποκαλυφθωσιν** Ξ (040)
- **Apparatus:** `ἂν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **om.** Ξ (040) ; **ανακαλυφθωσιν** D (05) Θ (038)
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **πονηροι** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `(Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοῦ` over `σου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῆς` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὴν` over `την` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ψυχὴν` over `ψυχην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διελεύσεται` over `διελευσεται` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥομφαία,` over `ρομφαια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅπως` over `οπωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἂν` over `αν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποκαλυφθῶσιν` over `αποκαλυφθωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πολλῶν` over `πολλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρδιῶν` over `καρδιων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διαλογισμοί.` over `διαλογισμοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ῥομφαία, ὅπως / ῥομφαία—ὅπως` (TCGNT (Byz)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:36
- **Apparatus:** `ἦν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** D (05)
- **Apparatus:** `Ἅννα προφῆτις,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ανα προφητης** L (019) ; **αννα προφητης** 1 (f¹) 13 (f¹³) 33 Θ (038)
- **Apparatus:** `προφῆτις,` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **προφητης** 1 (f¹) 13 (f¹³) 33 Θ (038) L (019)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **και** D (05)
- **Apparatus:** `προβεβηκυῖα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **προβεβηκοιια** Θ (038)
- **Apparatus:** `ζήσασα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **χηρευσασα** א (01) ; **ζησασα ετη** 1 (f¹) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ζησασα ετη επτα** A (02) D (05) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 13 (f¹³) 33 L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ἔτη** RP2018 (Byz) TR (KJTR) 1 (f¹) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **ετη επτα** A (02) D (05) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'ἔτη' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἔτη` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 13 (f¹³) 33 L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** RP2018 (Byz) TR (KJTR) 1 (f¹) A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'om.', 'ἔτη' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἅννα` over `αννα`, `Ἄννα` (B (03), Nestle1904, א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `προφῆτις,` over `προφητισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θυγάτηρ` over `θυγατηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Φανουήλ,` over `φανουηλ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκ` over `εκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `φυλῆς` over `φυλησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἀσήρ` over `ασηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(αὕτη` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προβεβηκυῖα` over `προβεβηκυια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραις` over `ημεραισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πολλαῖς,` over `πολλαισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετὰ` over `μετα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνδρὸς` over `ανδροσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑπτὰ` over `επτα`, `ζʹ` (B (03), א (01)) — *Letter-numeral abbreviation matched to an attested number of the same value*
- *Disregarded Surface Variant:* kept `ἀπὸ` over `απο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παρθενίας` over `παρθενειασ`, `παρθενιασ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτῆς,` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `(αὕτη / αυ τη`, `προβεβηκυῖα / προβεβη κυια`, `Ἀσήρ (αὕτη / Ἀσήρ—αὕτη` (13 (f¹³), L (019)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:37
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **ην** W (032)
- **Apparatus:** `ἕως` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 33 A (02) L (019) NA28 (TAGNT) THGNT Tisch8 WH1881 Ξ (040) **]** **ὡς** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) Θ (038) ; **om.** D (05) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ὀγδοήκοντα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) Tisch8 W (032) WH1881 Ξ (040) **]** **εβδομηκοντα** א (01) ; **ογδοηκοντατεσσαρων** TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀφίστατο` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **αφειστα** B (03) ; **αφιστατο απο** 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ἀπὸ** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **εκ** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἱεροῦ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ναου** D (05)
- **Apparatus:** `νηστείαις` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) Ξ (040) **]** **νηστιασ** א (01) ; **νηστιαισ τε** W (032) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `δεήσεσιν` SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) B (03) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **δεησιν** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `λατρεύουσα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **λατρεουσα** Θ (038)
- **Apparatus:** `νύκτα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **νυκταν** 13 (f¹³)
- **Apparatus:** `ἡμέραν.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ημερα** A (02)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὴ` over `αυτη`, `αὕτη` (B (03), RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `χήρα` over `χηρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐτῶν` over `ετων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τεσσάρων,)` over `τεσσαρων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἣ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἱεροῦ` over `ιερου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεήσεσιν` over `δεησεσι` (B (03)) — *Spelling variant pooled before the vote with the reading 'δεήσεσιν' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `λατρεύουσα` over `λατρευουσα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νύκτα` over `νυκτα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέραν.` over `ημεραν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:38
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **αὕτη** RP2018 (Byz) TR (KJTR) 13 (f¹³) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *transcriptional: haplography:* The omission in B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP is explicable by eye-skip between the two occurrences of 'αυτη' (between such common short words a possibility only; the vote is unchanged).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αυτηι** 1 (f¹)
- **Apparatus:** `ἀνθωμολογεῖτο` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ανθωμολογειτω** 13 (f¹³) ; **ανθωμωλογειτω** Θ (038)
- **Apparatus:** `θεῷ` B (03) א (01) SRGNT Nestle1904 BHP SBLGNT D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **κυρίῳ** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἐλάλει` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ελαλη** 13 (f¹³)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ἐν** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) D (05) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `Ἰερουσαλήμ` B (03) SRGNT SBLGNT Nestle1904 BHP TR (KJTR) RP2018 (Byz) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **ιηλμ̅ (= ιηλμ)** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῇ` over `αυτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὥρᾳ` over `ωρα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπιστᾶσα` over `επιστασα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθωμολογεῖτο` over `ανθωμολογειτο`, `ανθωμολογιτο` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλάλει` over `ελαλει` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `περὶ` over `περι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πᾶσιν` over `πασι`, `πασιν` (B (03), א (01)) — *Euphonic movable-nu (-ν) variation*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `προσδεχομένοις` over `προσδεχομενοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `λύτρωσιν` over `λυτρωσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ὥρᾳ / ωραι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:39
- **Apparatus:** `ἐτέλεσαν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **ετελεσεν** א (01) Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `πάντα` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ἅπαντα** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `τὰ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) W (032) WH1881 Ξ (040) **]** **om.** א (01) 1 (f¹) 13 (f¹³) D (05) L (019) Tisch8 Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἐπέστρεψαν` B (03) SRGNT SBLGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Ξ (040) **]** **ὑπέστρεψαν** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) D (05) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **επεστρεψεν** א (01) ; **om.** 1 (f¹) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `τὴν` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **om.** א (01) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `Γαλιλαίαν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Ξ (040) **]** **γαλιλεαν** Θ (038)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) D (05) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **τὴν** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) Ξ (040) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἑαυτῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) 1 (f¹) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT Tisch8 W (032) WH1881 Θ (038) Ξ (040) **]** **αὐτῶν** TR (KJTR) 13 (f¹³) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **εαυτον** L (019) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `Ναζαρέτ` א (01) SRGNT BHP RP2018 (Byz) TR (KJTR) 33 L (019) PT1904 (Byz) TCGNT (Byz) TR-Stephanus (1550) W (032) WH1881 Ξ (040) **]** **Ναζαρέθ** B (03) SBLGNT Nestle1904 13 (f¹³) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 Θ (038) ; **ναζαρα** 1 (f¹) ; **ναζαρατ** A (02) ; **ναζαρεθ καθωσ ερεθη δια του προφητου οτι ναζωραιοσ κληθησεται** D (05) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὡς` over `ωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸν` over `τον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `νόμον` over `νομον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κυρίου,` over `κυ̅`, `Κυρίου,` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Γαλιλαίαν` over `γαλειλαιαν`, `γαλιλαιαν` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πόλιν` over `πολιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:40
- **Apparatus:** `παιδίον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **πεδιον** L (019)
- **Apparatus:** `ηὔξανεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ιησ̅ εκραταιουτο (= ἰησοῦσ εκραταιουτο)** D (05)
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **πνεύματι** RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `σοφίᾳ` B (03) SRGNT SBLGNT Nestle1904 BHP 33 D (05) L (019) NA28 (TAGNT) THGNT W (032) WH1881 **]** **σοφίας** א (01) RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- **Apparatus:** `ἐπʼ αὐτό.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **εν αυτω** D (05) ; **ἐπ᾿ αὐτῷ.** 13 (f¹³) Θ (038)
- **Apparatus:** `αὐτό.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **αὐτῷ.** 13 (f¹³) Θ (038) D (05)
- *Disregarded Surface Variant:* kept `Τὸ` over `το`, `τὸ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παιδίον` over `παιδιον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ηὔξανεν` over `ηυξανεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐκραταιοῦτο` over `εκραταιουτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πληρούμενον` over `πληρουμενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χάρις` over `χαρισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `θεοῦ` over `θυ̅`, `Θεοῦ` (B (03), BHP, Nestle1904, SRGNT, TR (KJTR), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπʼ` over `επ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτό.` over `αυτο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:41
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **επορευοντο δε** D (05)
- **Apparatus:** `ἐπορεύοντο` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `κατʼ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **κατθ** Θ (038)
- **Apparatus:** `ἔτος εἰς Ἰερουσαλὴμ` B (03) SRGNT SBLGNT BHP TR (KJTR) Nestle1904 RP2018 (Byz) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **εθοσ ισ ιηλμ̅ (= εθοσ ισ ιηλμ)** א (01) ; **ετοσ εισ ιερουσαλημ εν** D (05) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπορεύοντο` over `επορευοντο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οἱ` over `οι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γονεῖς` over `γονεισ`, `γονισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατʼ` over `κατ`, `κατ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑορτῇ` over `εορτη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάσχα.` over `πασχα`, `Πάσχα.` (B (03), BHP, RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `κατʼ / κατα`, `κατʼ / καθ` (D (05), W (032)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### Luke 2:42
- **Apparatus:** `ἐτῶν δώδεκα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **οτων ιβʹ και** א (01) ; **ετων δεκα** 1 (f¹) ; **om.** C (04) ; **αυτω ετη** D (05) ; **αυτω ετη δωδεκα** L (019) ; **ετων δεκαδυο** W (032) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `ἀναβαινόντων αὐτῶν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα** RP2018 (Byz) TR (KJTR) 13 (f¹³) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **δυο αναβαντων αυτων εις ιεροσολυμα** 1 (f¹) ; **αναβαινοντων αυτων εις ιεροσολυμα** 33 A (02) ; **om.** C (04) ; **ιβʹ ανεβησαν οι γονεισ αυτου εχοντεσ αυτον** D (05) *(partial substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `τῆς` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τη** L (019)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **των αζυμων** D (05)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), Nestle1904, RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτε` over `οτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐγένετο` over `εγενετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατὰ` over `κατα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἔθος` over `εθοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῆς` over `τησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἑορτῆς` over `εορτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:43
- **Apparatus:** `τελειωσάντων` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **τελεσαντων** D (05)
- **Apparatus:** `ὑπέμεινεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **απεμεινεν** 1 (f¹) 33 D (05)
- **Apparatus:** `Ἰησοῦς` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** א (01) D (05) *(omission / addition)*
  - *variant type: sacred name or title:* 'Ἰησοῦς' adds a sacred name or title; B (03) supports it, so the usual scribal tendency to expand such names gives no direction here.
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ιησ̅ (= ἰησοῦσ)** D (05)
- **Apparatus:** `ἔγνωσαν οἱ` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **ἔγνω Ἰωσὴφ** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `γονεῖς` B (03) SRGNT SBLGNT Nestle1904 BHP א (01) 1 (f¹) 33 D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **καὶ ἡ μήτηρ** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) ; **γωνεις** Θ (038) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τελειωσάντων` over `τελειωσαντων`, `τελιωσαντων` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `τὰς` over `τασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέρας,` over `ημερασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑποστρέφειν` over `υποστρεφειν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὺς` over `αυτουσ`, `αὐτούς,` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπέμεινεν` over `υπεμεινεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `παῖς` over `παισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰερουσαλήμ,` over `ιερουσαλημ`, `Ἱερουσαλήμ,`, `Ἱερουσαλήμ·` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `γονεῖς` over `γονεισ`, `γονισ` (B (03), א (01)) — *Spelling variant pooled before the vote with the reading 'γονεῖς' (same word, different spelling); whether that reading was adopted is shown in the apparatus*
- *Disregarded Surface Variant:* kept `αὐτοῦ.` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῷ / τωι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:44
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **και** D (05)
- **Apparatus:** `δὲ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `εἶναι` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **om.** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'εἶναι', 'om.' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **εἶναι** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) C (04) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'εἶναι', 'om.' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **οδον** D (05)
- **Apparatus:** `ὁδὸν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** C (04) D (05)
- **Apparatus:** `συγγενεῦσιν` B (03) SBLGNT Nestle1904 BHP 1 (f¹) 13 (f¹³) 33 L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **συγγενέσιν** א (01) SRGNT RP2018 (Byz) TR (KJTR) A (02) C (04) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `καὶ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) C (04) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **om.** א (01) L (019) ; **και εν** 1 (f¹) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **ἐν** RP2018 (Byz) TR (KJTR) 1 (f¹) D (05) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `τοῖς γνωστοῖς` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** א (01) L (019) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `νομίσαντες` over `νομισαντεσ`, `Νομίσαντες` (B (03), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συνοδίᾳ` over `συνοδια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦλθον` over `ηλθον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμέρας` over `ημερασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁδὸν` over `οδον`, `ὁδόν,`, `ὁδόν·` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνεζήτουν` over `ανεζητουν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῇ / τηι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:45
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 33 C (04) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **αὐτόν** RP2018 (Byz) TR (KJTR) 13 (f¹³) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ἀναζητοῦντες` B (03) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) 13 (f¹³) 33 C (04) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **ζητοῦντες** א (01) RP2018 (Byz) TR (KJTR) A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μὴ` over `μη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εὑρόντες` over `ευροντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑπέστρεψαν` over `υπεστρεψαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ`, `ισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `Ἰερουσαλὴμ` over `ιερουσαλημ`, `Ἱερουσαλὴμ`, `Ἱερουσαλήμ,`, `Ἰερουσαλήμ,` (B (03), Nestle1904, RP2018 (Byz), TR (KJTR), א (01)) — *Accent or breathing differs between accented editions (editorial interpretation)*
- *Disregarded Surface Variant:* kept `αὐτόν.` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:46
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **καθημενον** D (05)
- **Apparatus:** `τῷ ἱερῷ καθεζόμενον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **τωι ιερωι καθημενον** 1 (f¹) ; **τω ιερω** D (05) ; **τω ιερω καθεζωμενον** Θ (038)
- **Apparatus:** `καθεζόμενον` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **om.** D (05) ; **καθεζωμενον** Θ (038) ; **καθημενον** 1 (f¹)
- **Apparatus:** `ἐν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **εμ** A (02) L (019)
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `ἐπερωτῶντα` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **επηρωτωντα** א (01) Θ (038) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `αὐτούς·` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **αυτον** C (04)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐγένετο` over `εγενετο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετὰ` over `μετα`, `μεθ’`, `μεθʼ` (B (03), RP2018 (Byz), TR (KJTR), א (01)) — *Elision (κατὰ / κατ’ type)*
- *Disregarded Surface Variant:* kept `ἡμέρας` over `ημερασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τρεῖς` over `τρισ`, `τρεισ` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `εὗρον` over `ευρον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῷ` over `τω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἱερῷ` over `ιερω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καθεζόμενον` over `καθεζομενον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μέσῳ` over `μεσω` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῶν` over `των` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διδασκάλων` over `διδασκαλων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀκούοντα` over `ακουοντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτούς·` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `μετὰ / μεθ`, `μετὰ / μεθ`, `μετὰ / μεθ`, `μετὰ / μεθ`, `μετὰ / μεθ᾽`, `μετὰ / μεθ᾿`, `μετὰ / μεθ᾽`, `μετὰ / μεθ᾿`, `μετὰ / μεθ`, `μετὰ / μεθ᾽`, `μετὰ / μεθʼ`, `μετὰ / μεθ` (13 (f¹³), A (02), C (04), D (05), PT1904 (Byz), TCGNT (Byz), TR-Boyd (Elz/Scr/Steph), TR-Elzevir (1624), TR-Scrivener (1894), TR-Stephanus (1550), Θ (038)) — *Apparatus witness, not a variant: Elision (κατὰ / κατ’ type)*

### Luke 2:47
- **Apparatus:** `οἱ ἀκούοντες αὐτοῦ` א (01) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **om.** B (03) W (032) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- *Disregarded Surface Variant:* kept `ἐξίσταντο` over `εξισταντο`, `Ἐξίσταντο` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δὲ` over `δε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πάντες` over `παντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐπὶ` over `επι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συνέσει` over `συνεσει`, `συνεσι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ταῖς` over `ταισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀποκρίσεσιν` over `αποκρισεσιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ.` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `(adopted text)` over `τῇ / τηι` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:48
- **Apparatus:** `εἶπεν` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) C (04) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **om.** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'εἶπεν', 'om.' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `om.` B (03) א (01) SRGNT SBLGNT Nestle1904 BHP 1 (f¹) D (05) L (019) NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 Θ (038) **]** **εἶπεν** RP2018 (Byz) TR (KJTR) 13 (f¹³) 33 A (02) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) *(word-order transposition)*
  - *variant type: transposition:* Units 'εἶπεν', 'om.' together form one word-order variant (RP2018 (Byz), TR (KJTR) transpose).
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical.
- **Apparatus:** `ὁ πατήρ σου κἀγὼ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) A (02) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) **]** **οι συγγενεισ και εγω** C (04) ; **ὁ πατήρ σου καὶ ἐγὼ** 1 (f¹) 33 L (019) WH1881 Θ (038) ; **ο πηρ̅ σου και (= ο πατὴρ σου και)** 13 (f¹³)
- **Apparatus:** `ζητοῦμέν` B (03) א (01) SRGNT Nestle1904 BHP WH1881 **]** **ἐζητοῦμέν** SBLGNT RP2018 (Byz) TR (KJTR) 1 (f¹) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) Θ (038) ; **οδυνομενοι εζητουμεν** 13 (f¹³) ; **και λυπουμενοι εζητουμεν** D (05) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, modern critical editions.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰδόντες` over `ιδοντεσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐξεπλάγησαν,` over `εξεπλαγησαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτὸν` over `αυτον` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μήτηρ` over `μητηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ·` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Τέκνον,` over `τεκνον`, `“τέκνον,` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τί` over `τι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐποίησας` over `εποιησασ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡμῖν` over `ημιν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὕτως;` over `ουτωσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἰδοὺ` over `ιδου`, `Ἰδοὺ,`, `Ἰδού,`, `ἰδού,` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὁ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατήρ` over `πατηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κἀγὼ` over `καγω`, `καὶ ἐγὼ` (B (03), SBLGNT, א (01)) — *Greek crasis (καὶ ἐγώ / κἀγώ type)*
- *Disregarded Surface Variant:* kept `ὀδυνώμενοι` over `οδυνωμενοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σε.` over `σε`, `σε.”` (B (03), BHP, SRGNT, א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `(adopted text)` over `κἀγὼ / και εγω`, `κἀγὼ / και εγω`, `κἀγὼ / και εγω`, `κἀγὼ / καὶ ἐγὼ`, `κἀγὼ / και εγω` (1 (f¹), 33, L (019), WH1881, Θ (038)) — *Apparatus witness, not a variant: Greek crasis (καὶ ἐγώ / κἀγώ type)*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ἐποίησας / εποι ησας` (L (019)) — *Apparatus witness, not a variant: Word division differs (same letters written as one word or two)*

### Luke 2:49
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** 13 (f¹³)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **δε** 13 (f¹³)
- **Apparatus:** `ἐζητεῖτέ` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **ζητειτε** א (01) W (032) ; **εζητειται** 33 C (04) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `οὐκ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ου** L (019)
- **Apparatus:** `ᾔδειτε` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **ηδητε** 13 (f¹³) ; **ηδειται** 33 ; **οιδατε** D (05) W (032)
- **Apparatus:** `μου` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **om.** W (032)
- **Apparatus:** `εἶναί` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **εινε** א (01) *(inflection or spelling (same stem))*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `με;` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **om.** 1 (f¹) 13 (f¹³) D (05) W (032) Θ (038)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἶπεν` over `ειπε`, `ειπεν` (B (03), א (01)) — *Euphonic movable-nu (-ν) variation*
- *Disregarded Surface Variant:* kept `πρὸς` over `προσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτούς·` over `αυτουσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Τί` over `τι`, `“τί` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `με;` over `με` (B (03), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `οὐκ` over `ουκ`, `Οὐκ` (B (03), RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ᾔδειτε` over `ηδειτε` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὅτι` over `οτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῖς` over `τοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τοῦ` over `του` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `πατρός` over `πατροσ`, `Πατρός` (B (03), Nestle1904, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `δεῖ` over `δει`, `δι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `με;` over `με`, `με;”` (B (03), BHP, SRGNT, א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `(adopted text)` over `ᾔδειτε / ηιδειτε` (1 (f¹)) — *Apparatus witness, not a variant: Iota adscript / subscript orthographic convention (αὐτῷ / αυτωι type)*

### Luke 2:50
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **δε** D (05)
- **Apparatus:** `ἐλάλησεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **ειπεν** 1 (f¹)
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοὶ` over `αυτοι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `οὐ` over `ου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `συνῆκαν` over `συνηκαν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὸ` over `το` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥῆμα` over `ρημα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὃ` over `ο` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐλάλησεν` over `ελαλησεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς.` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:51
- **Apparatus:** `αὐτῶν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 **]** **αυτον** Θ (038)
- **Apparatus:** `καὶ ἦλθεν` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05)
- **Apparatus:** `Ναζαρέτ` א (01) SRGNT RP2018 (Byz) TR (KJTR) BHP 33 L (019) PT1904 (Byz) TCGNT (Byz) TR-Stephanus (1550) W (032) WH1881 **]** **Ναζαρέθ** B (03) SBLGNT Nestle1904 1 (f¹) 13 (f¹³) NA28 (TAGNT) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) Tisch8 ; **ναζαρατ** A (02) Θ (038) ; **ναρεθ** D (05) *(proper-name spelling)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts, modern critical editions.
- **Apparatus:** `καὶ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** 13 (f¹³) D (05)
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **δε** 13 (f¹³) D (05)
- **Apparatus:** `διετήρει` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 **]** **ετηρει** W (032) ; **διετηρη** Θ (038)
- **Apparatus:** `πάντα` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** A (02) D (05)
- **Apparatus:** `om.` B (03) א (01) SRGNT Nestle1904 BHP NA28 (TAGNT) THGNT Tisch8 W (032) WH1881 **]** **ταῦτα** SBLGNT RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 C (04) L (019) PT1904 (Byz) TCGNT (Byz) TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **απαντα ταυτα** A (02) ; **παντα** D (05) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, modern critical editions.
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, TR (KJTR), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `κατέβη` over `κατεβη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μετʼ` over `μετ`, `μετ’` (B (03), Nestle1904, RP2018 (Byz), א (01)) — *Punctuation / spacing difference only*
- *Disregarded Surface Variant:* kept `αὐτῶν` over `αυτων` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦλθεν` over `ηλθεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `εἰς` over `εισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἦν` over `ην` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ὑποτασσόμενος` over `υποτασσομενοσ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῖς.` over `αυτοισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και`, `Καὶ` (B (03), RP2018 (Byz), SRGNT, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡ` over `η` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `μήτηρ` over `μητηρ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτοῦ` over `αυτου` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `διετήρει` over `διετηρει`, `διετηρι` (B (03), א (01)) — *Koine/Uncial itacistic spelling (ει / ι equivalence)*
- *Disregarded Surface Variant:* kept `πάντα` over `παντα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τὰ` over `τα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ῥήματα` over `ρηματα` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἐν` over `εν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `τῇ` over `τη` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καρδίᾳ` over `καρδια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `αὐτῆς.` over `αυτησ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

### Luke 2:52
- **Apparatus:** `om.` B (03) SRGNT SBLGNT Nestle1904 BHP RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 WH1881 Θ (038) **]** **ο** א (01) W (032) *(omission / addition)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `τῇ` B (03) SRGNT BHP W (032) WH1881 **]** **om.** SBLGNT RP2018 (Byz) TR (KJTR) 1 (f¹) 13 (f¹³) 33 A (02) C (04) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Θ (038) ; **ἐν τῇ** א (01) Nestle1904 NA28 (TAGNT) Tisch8 ; **ηλικια και** D (05) ; **τη ηλικια και** L (019) *(omission / addition)*
  - *external: independent streams:* Adopted reading: early manuscripts, modern critical editions; other reading(s): Byzantine / ecclesiastical, early manuscripts, modern critical editions.
- **Apparatus:** `καὶ ἡλικίᾳ` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **om.** D (05) L (019)
- **Apparatus:** `παρὰ θεῷ` B (03) SRGNT Nestle1904 BHP TR (KJTR) SBLGNT RP2018 (Byz) 1 (f¹) 13 (f¹³) 33 A (02) C (04) D (05) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **θυ̅ (= θυ)** א (01) *(lexical substitution)*
  - *external: independent streams:* Adopted reading: Byzantine / ecclesiastical, early manuscripts, modern critical editions; other reading(s): early manuscripts.
- **Apparatus:** `om.` B (03) BHP Nestle1904 RP2018 (Byz) SBLGNT SRGNT TR (KJTR) א (01) 1 (f¹) 13 (f¹³) 33 A (02) C (04) L (019) NA28 (TAGNT) PT1904 (Byz) TCGNT (Byz) THGNT TR-Boyd (Elz/Scr/Steph) TR-Elzevir (1624) TR-Scrivener (1894) TR-Stephanus (1550) Tisch8 W (032) WH1881 Θ (038) **]** **παρα** D (05)
- *Disregarded Surface Variant:* kept `Καὶ` over `και`, `καὶ` (B (03), BHP, א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `Ἰησοῦς` over `ισ̅` (B (03), א (01)) — *Nomen sacrum (contracted sacred name) for the full word*
- *Disregarded Surface Variant:* kept `προέκοπτεν` over `προεκοπτεν` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `σοφίᾳ` over `σοφια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἡλικίᾳ` over `ηλικια` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `χάριτι` over `χαριτι` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `καὶ` over `και` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*
- *Disregarded Surface Variant:* kept `ἀνθρώποις.` over `ανθρωποισ` (B (03), א (01)) — *Accentuation / capitalisation / breathing convention*

---

## Section IV — Verse-by-Verse Text-Critical Rationale & Witness Matrix

### Verse 1 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην·
  - `SRGNT`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `SBLGNT`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην·
  - `BHP`: ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `Nestle1904`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `RP2018 (Byz)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TR (KJTR)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `B (03)`: εγενετο δε εν ταισ ημεραισ εκειναισ εξηλθεν δογμα παρα καισαροσ αυγουστου απογραφεσθαι πασαν την οικουμενην
  - `א (01)`: εγενετο δε εν ταισ ημεραισ εκιναισ εξηλθεν δογμα παρα καισαροσ αγουστου απογραφεσθε πασαν την οικουμενην
  - `NA28 (TAGNT)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `THGNT`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `WH1881`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην·
  - `Tisch8`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθεν δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TCGNT (Byz)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθε δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `PT1904 (Byz)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις ἐξῆλθε δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TR-Scrivener (1894)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθε δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθε δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TR-Stephanus (1550)`: Ἐγένετο δὲ ἐν ταῖς ἡμέραις ἐκείναις, ἐξῆλθε δόγμα παρὰ Καίσαρος Αὐγούστου, ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην.
  - `TR-Elzevir (1624)`: εγενετο δε εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου απογραφεσθαι πασαν την οικουμενην
  - `𝔓4`: εγενετο δε εν … ημεραισ εκειναισ εξηλθεν δογμα …
  - `A (02)`: εγενετο εν ταισ ημεραισ εκειναισ εξηλθεν δογμα παρα καισαροσ αυγουστου απογραφεσθαι πασαν την οικουμενην
  - `Ξ (040)`: εγενετο εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου του απογραφεσθαι πασαν την οικουμενην
  - `C (04)`: εγενετο δε εν ταισ ημεραισ εκειναισ εξηλθεν δογμα παρα καισαροσ αγουστου απογραφεσθαι πασαν την οικουμενην
  - `W (032)`: εγενετο δε εν ταισ ημεραισ εκειναισ εξηλθεν δογμα παρα καισαροσ αυγουστου του απογραφεσθαι πασαν την οικουμενην
  - `33`: εγενετο δε εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου του απογραφεσθαι πασαν την οικουμενην
  - `L (019)`: εγενετο δε εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου του απογραφεσθαι πασαν την οικουμενην
  - `D (05)`: εγενετο δε εν ταισ ημεραισ εκειναισ εξηλθεν δογμα παρα καισαροσ αυγουστου απογραφεσθαι πασαν την οικουμενην
  - `Θ (038)`: εγενετο δε εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου απογραφεσθαι πασαν την οικουμενην
  - `1 (f¹)`: εγενετο δε εν ταις ημεραις εκειναις εξηλθε δογμα παρα καισαρος αυγουστου απογραψασθαι πασαν την οικουμενην
  - `13 (f¹³)`: εγενετο δε εν ταις ημεραις εκειναις εξηλθεν δογμα παρα καισαρος αυγουστου απογραψασθαι πασαν την οικουμενην
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'Αὐγούστου ἀπογράφεσθαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αγουστου απογραφεσθε (א (01)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 2 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** (αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου·)
  - `SRGNT`: (Αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.)
  - `SBLGNT`: (αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου·)
  - `BHP`: (αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.)
  - `Nestle1904`: αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `RP2018 (Byz)`: Αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TR (KJTR)`: (Αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.)
  - `B (03)`: αυτη απογραφη πρωτη εγενετο ηγεμονευοντοσ τησ συριασ κυρεινου
  - `א (01)`: αυτην απογραφην εγενετο πρωτη ηγεμονευοντοσ τησ συριασ κυρηνιου
  - `NA28 (TAGNT)`: αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `THGNT`: αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `WH1881`: (αὕτη ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου·)
  - `Tisch8`: αὕτη ἀπογραφὴ ἐγένετο πρώτη ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TCGNT (Byz)`: (αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.)
  - `PT1904 (Byz)`: αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TR-Scrivener (1894)`: αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TR-Boyd (Elz/Scr/Steph)`: Αὕτη ἡ ἀπογραφὴ πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TR-Stephanus (1550)`: αὕτη ἡ ἀπογραφὴ, πρώτη ἐγένετο ἡγεμονεύοντος τῆς Συρίας Κυρηνίου.
  - `TR-Elzevir (1624)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρηνιου
  - `A (02)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντοσ τησ συριασ κηρυνιου
  - `Ξ (040)`: αυτη η απογραφη πρωτη εγενετο ἡγεμονευοντος της συριας κυρινιου
  - `C (04)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντοσ τησ συριασ κυρηνιου
  - `W (032)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντοσ τησ συριασ κυρινου
  - `33`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρηνιου
  - `L (019)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρηνιου
  - `D (05)`: αυτη εγενετο απογραφη πρωτη ηγεμονευοντοσ τησ συριασ κυρηνιου
  - `Θ (038)`: αυτη απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρηνιου
  - `1 (f¹)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρηνιου
  - `13 (f¹³)`: αυτη η απογραφη πρωτη εγενετο ηγεμονευοντος της συριας κυρινιου
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'αὕτη' [B (03), SRGNT, RP2018 (Byz), TR (KJTR), SBLGNT, Nestle1904, BHP] (weight 5.97, confidence 99%) over αυτην (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἡ (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'ἀπογραφὴ πρώτη ἐγένετο' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απογραφην εγενετο πρωτη (א (01)). [Lexical, morphological, or word-order variant] Adopted 'Κυρηνίου' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over κυρεινου (B (03)). Reference apparatus (SBLGNT): αὕτη WH Treg NA28 ] + ἡ RP Reference apparatus (SBLGNT): καὶ WH Treg NA28 ] – RP Reference apparatus (SBLGNT): ἐλάλουν WH NA28 ] εἶπον Treg RP Reference apparatus (SBLGNT): μήτηρ WH Treg NA28 ] + αὐτοῦ RP Reference apparatus (SBLGNT): ἀφίστατο WH Treg NA28 ] + ἀπὸ RP Reference apparatus (SBLGNT): θεῷ WH Treg NA28 ] κυρίῳ RP Reference apparatus (SBLGNT): λύτρωσιν WH Treg NA28 ] + ἐν RP Reference apparatus (SBLGNT): ἐπέστρεψαν WH Treg NA28 ] ὑπέστρεψαν RP Reference apparatus (SBLGNT): εἰς WH Treg NA28 ] + τὴν RP Reference apparatus (SBLGNT): αὐτῶν WH NA28 ] + εἰς Ἱεροσόλυμα Treg RP Reference apparatus (SBLGNT): καὶ WH Treg NA28 ] + ἐν RP Reference apparatus (SBLGNT): ἀναζητοῦντες WH Treg NA28 ] ζητοῦντες RP Reference apparatus (SBLGNT): ἐζητοῦμέν Treg NA28 RP ] ζητοῦμέν WH Also normalised 3 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 3 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `SRGNT`: Καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `SBLGNT`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `BHP`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `Nestle1904`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `RP2018 (Byz)`: Καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `TR (KJTR)`: Καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `B (03)`: και επορευοντο παντεσ απογραφεσθαι εκαστοσ εισ την εαυτου πολιν
  - `א (01)`: και επορευοντο εκαστοσ απογραφεσθε εισ την εαυτων πολιν
  - `NA28 (TAGNT)`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `THGNT`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `WH1881`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `Tisch8`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἑαυτοῦ πόλιν.
  - `TCGNT (Byz)`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `PT1904 (Byz)`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `TR-Scrivener (1894)`: καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `TR-Stephanus (1550)`: Καὶ ἐπορεύοντο πάντες ἀπογράφεσθαι, ἕκαστος εἰς τὴν ἰδίαν πόλιν.
  - `TR-Elzevir (1624)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την ιδιαν πολιν
  - `𝔓4`: … παντεσ …
  - `A (02)`: και επορευοντο παντεσ απογραφεσθαι εκαστοσ εισ την ιδιαν πολιν
  - `Ξ (040)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την εαυτου πολιν
  - `C (04)`: και επορευοντο παντεσ απογραφεσθαι εκαστοσ εισ την ιδιαν χωραν
  - `W (032)`: και επορευοντο παντεσ απογραφεσθαι εκαστοσ εισ την εαυτου πολιν
  - `33`: και επορευοντο παντες απογραφεσθαι εκαστος εις την ιδιαν πολιν
  - `L (019)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την εαυτου πολην
  - `D (05)`: και επορευοντο παντεσ απογραφεσθαι εκαστοσ εισ την εαυτου πατριδα
  - `Θ (038)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την ιδιαν πολιν
  - `1 (f¹)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την ιδιαν πολιν
  - `13 (f¹³)`: και επορευοντο παντες απογραφεσθαι εκαστος εις την ιδιαν πολιν
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'πάντες ἀπογράφεσθαι ἕκαστος' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εκαστοσ απογραφεσθε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἑαυτοῦ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over ἰδίαν (RP2018 (Byz), TR (KJTR)); εαυτων (א (01)). Also normalised 5 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 4 (Confidence: `96.8%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυὶδ ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `SRGNT`: Ἀνέβη δὲ καὶ Ἰωσὴφ, ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ, εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυὶδ, ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `SBLGNT`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυὶδ ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `BHP`: ἀνέβη δὲ καὶ Ἰωσὴφ, ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ, εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυεὶδ, ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυείδ,
  - `Nestle1904`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυεὶδ ἥτις καλεῖται Βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυείδ,
  - `RP2018 (Byz)`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας, ἐκ πόλεως Ναζαρέτ, εἰς τὴν Ἰουδαίαν, εἰς πόλιν Δαυίδ, ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `TR (KJTR)`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας, ἐκ πόλεως Ναζαρέτ, εἰς τὴν Ἰουδαίαν, εἰς πόλιν Δαυίδ, ἥτις καλεῖται Βηθλέεμ· (διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ:)
  - `B (03)`: ανεβη δε και ιωσηφ απο τησ γαλειλαιασ εκ πολεωσ ναζαρετ εισ την ιουδαιαν εισ πολιν δαυειδ ητισ καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριασ δαυειδ
  - `א (01)`: ανεβη δε και ιωσηφ απο τησ γαλιλαιασ εκ πολεωσ ναζαρεθ εισ την ιουδαιαν εισ την πολιν δαδ̅ ητισ καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριασ δαδ̅
  - `NA28 (TAGNT)`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυὶδ ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `THGNT`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως ναζαρὲτ εἰς τὴν Ἰουδαίαν εἰς πόλιν δαυεὶδ ἥτις καλεῖται βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς δαυείδ,
  - `WH1881`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲτ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυεὶδ ἥτις καλεῖται Βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυείδ,
  - `Tisch8`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲθ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυεὶδ ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυείδ,
  - `TCGNT (Byz)`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲτ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυίδ, ἥτις καλεῖται Βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυίδ,
  - `PT1904 (Byz)`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας ἐκ πόλεως Ναζαρὲτ εἰς τὴν Ἰουδαίαν εἰς πόλιν Δαυΐδ, ἥτις καλεῖται Βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαυΐδ,
  - `TR-Scrivener (1894)`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας, ἐκ πόλεως Ναζαρέθ, εἰς τὴν Ἰουδαίαν, εἰς πόλιν Δαβίδ, ἥτις καλεῖται Βηθλεέμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαβίδ,
  - `TR-Boyd (Elz/Scr/Steph)`: Ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας, ἐκ πόλεως Ναζαρέθ, εἰς τὴν Ἰουδαίαν, εἰς πόλιν Δαβίδ, ἥτις καλεῖται Βηθλέεμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαβίδ,
  - `TR-Stephanus (1550)`: ἀνέβη δὲ καὶ Ἰωσὴφ ἀπὸ τῆς Γαλιλαίας, ἐκ πόλεως Ναζαρὲτ, εἰς τὴν Ἰουδαίαν, εἰς πόλιν Δαβὶδ ἥτις καλεῖται Βηθλεὲμ, διὰ τὸ εἶναι αὐτὸν ἐξ οἴκου καὶ πατριᾶς Δαβὶδ,
  - `TR-Elzevir (1624)`: ανεβη δε και ιωσηφ απο της γαλιλαιας εκ πολεως ναζαρεθ εις την ιουδαιαν εις πολιν δαβιδ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαβιδ
  - `A (02)`: ανεβη δε και ιωσηφ απο τησ γαλιλαιασ εκ πολεωσ ναζαραθ εισ την ιουδαιαν εισ πολιν δαδ̅ ητισ καλειτε βηθλεεμ δια το ειναι αυτον εξ οικου και πατριασ δαδ̅
  - `Ξ (040)`: ανεβη δε και ϊωσηφ απο της γαλιλαιας εκ πολεως ναζαρετ εις την ϊουδαιαν εις πολιν δαυειδ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαυειδ
  - `C (04)`: ανεβη δε και ιωσηφ απο τησ γαλιλαιασ εκ πολεωσ ναζαραθ εισ την ιουδαιαν εισ πολιν δαδ̅ ητισ καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριασ δαδ̅
  - `W (032)`: ανεβη δε και ιωσηφ απο τησ γαλιλαιασ εκ πολεωσ ναζαρετ εισ την ιουδαιαν εισ πολιν δαυειδ ητισ καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριασ δαυειδ
  - `33`: ανεβη δε και ιωσηφ απο της γαλιλαιας εκ πολεως ναζαρετ εις την ιουδαιαν εις πολιν δαδ̅ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαδ̅
  - `L (019)`: ανεβη δε και ηωσηφ απο της γαλιλαιας εκ πολεως ναζαρετ εις την ιουδαιαν εις πολιν δαδ̅ ητης καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαδ̅
  - `D (05)`: ανεβη δε και ιωσηφ απο τησ γαλιλαιασ εκ πολεωσ ναζαρεθ εισ γην ιουδα εισ πολιν δαυειδ ητισ καλειτε βηθλεεμ
  - `Θ (038)`: ανεβη δε και ο ιωσηφ απο της γαλιλαιας εκ π ολεως ναζαρεθ εις την ιουδαιαν εις πολιν δαδ̅ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαδ̅
  - `1 (f¹)`: ανεβη δε και ιωσηφ απο της γαλιλαιας εκ πολεως ναζαρεθ εις την ιουδαιαν εις πολιν δαδ̅ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαδ̅
  - `13 (f¹³)`: ανεβη δε και ιωσηφ απο της γαλιλαιας εκ πολεως ναζαρεθ εις την ιουδαιαν εις πολιν δαδ̅ ητις καλειται βηθλεεμ δια το ειναι αυτον εξ οικου και πατριας δαδ̅
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Ναζαρὲθ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.63, confidence 98%) over Ναζαρέτ (B (03), RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over την (א (01)). Also normalised 27 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 5 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
  - `SRGNT`: ἀπογράψασθαι σὺν Μαριὰμ, τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
  - `SBLGNT`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
  - `BHP`: ἀπογράψασθαι σὺν Μαριὰμ, τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐνκύῳ.
  - `Nestle1904`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
  - `RP2018 (Byz)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `TR (KJTR)`: Ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `B (03)`: απογραψασθαι συν μαριαμ τη εμνηστευμενη αυτω ουση εγγυω
  - `א (01)`: απογραφεσθαι συν μαριαμ τη εμνηστευμενη αυτω ουση ενκυω
  - `NA28 (TAGNT)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ οὔσῃ ἐγκύῳ.
  - `THGNT`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ οὔσῃ ἐνκύῳ.
  - `WH1881`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐνκύῳ.
  - `Tisch8`: ἀπογράψασθαι σὺν Μαριὰμ τῇ ἐμνηστευμένῃ αὐτῷ, οὔσῃ ἐγκύῳ.
  - `TCGNT (Byz)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `PT1904 (Byz)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `TR-Scrivener (1894)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `TR-Boyd (Elz/Scr/Steph)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικί, οὔσῃ ἐγκύῳ.
  - `TR-Stephanus (1550)`: ἀπογράψασθαι σὺν Μαριὰμ τῇ μεμνηστευμένῃ αὐτῷ γυναικὶ, οὔσῃ ἐγκύῳ.
  - `TR-Elzevir (1624)`: απογραψασθαι συν μαριαμ τη μεμνηστευμενη αυτω γυναικι ουση εγκυω
  - `A (02)`: συμ μαριαμ τη εμνηστευμενη αυτω γυναικι ουση ενκυω
  - `Ξ (040)`: απογραψασθαι συν μαριαμ τη εμνηστευμενη αυτω ουση εγκυω
  - `C (04)`: απογραψασθαι συν μαριαμ … εμνηστευμενη αυτω …
  - `W (032)`: απογραφεσθαι συν μαριαμ τη εμνηστευμενη αυτω ουση νεκυω
  - `33`: […] συν μαριαμ τη μεμνηστευμενη αυτω γυναικι ουση εγκυω
  - `L (019)`: απογραψασθαι συν μαρηαμ τη εμνηστευμενη αυτω ουση εγκυω
  - `D (05)`: απογραφεσθαι συν μαρια τη εμνηστευμενη αυτω ουση ενκυω δια το ειναι αυτον εξ οικου και πατριασ δαυειδ
  - `Θ (038)`: απογραψασθαι συ μαριαμ τη μεμνηστευμενη αυτω γυναικι ουση εγκυω
  - `1 (f¹)`: απογραψασθαι συν μαριαμ τηι μεμνηστευμενη αυτωι ουσηι εγκυωι
  - `13 (f¹³)`: απογραψασθαι συν μαριαμ τη μεμνηστευμενη αυτω γυναικι ουση εγκυω
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἀπογράψασθαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απογραφεσθαι (א (01)). [Variation unit spanning several words] Adopted 'ἐμνηστευμένῃ αὐτῷ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over μεμνηστευμένῃ αὐτῷ γυναικί (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἐγκύῳ' [SRGNT, SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR), א (01), BHP] (weight 5.95, confidence 99%) over εγγυω (B (03)). Also normalised 5 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 6 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `SRGNT`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `SBLGNT`: ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `BHP`: ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `Nestle1904`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `RP2018 (Byz)`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `TR (KJTR)`: Ἐγένετο δὲ, ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `B (03)`: εγενετο δε εν τω ειναι αυτουσ εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `א (01)`: εγενετο δε εν τω ειναι αυτουσ εκει επλησθησαν αι ημεραι του τεκιν αυτην
  - `NA28 (TAGNT)`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `THGNT`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `WH1881`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `Tisch8`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `TCGNT (Byz)`: ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `PT1904 (Byz)`: ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν,
  - `TR-Scrivener (1894)`: ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν.
  - `TR-Stephanus (1550)`: Ἐγένετο δὲ ἐν τῷ εἶναι αὐτοὺς ἐκεῖ, ἐπλήσθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν·
  - `TR-Elzevir (1624)`: εγενετο δε εν τω ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `𝔓4`: … ημεραι … αυτην
  - `A (02)`: εγενετο δε εν τω ειναι αυτουσ εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `Ξ (040)`: εγενετο δε εν τω ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `W (032)`: εγενετο δε εν τω ειναι αυτουσ εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `33`: εγενετο δε εν τω ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `L (019)`: εγενετο δε εν το ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `D (05)`: ωσ δε παρεγεινοντο ετελεσθησαν αι ημεραι του τεκειν αυτην
  - `Θ (038)`: εγενετο δε εν τω ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `1 (f¹)`: εγενετο δε εν τωι ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
  - `13 (f¹³)`: εγενετο δε εν τω ειναι αυτους εκει επλησθησαν αι ημεραι του τεκειν αυτην
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 13 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence)).

### Verse 7 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `SRGNT`: Καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν, καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `SBLGNT`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `BHP`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν, καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `Nestle1904`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `RP2018 (Byz)`: Καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτόν, καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TR (KJTR)`: Καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτόν, καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ· διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `B (03)`: και ετεκεν τον υιον αυτησ τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλεινεν αυτον εν φατνη διοτι ουκ ην αυτοισ τοποσ εν τω καταλυματι
  - `א (01)`: και ετεκεν τον υν̅ αυτησ τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον επι φατνη διοτι ουκ ην αυτοισ τοποσ εν τω καταλυματι
  - `NA28 (TAGNT)`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `THGNT`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `WH1881`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `Tisch8`: καὶ ἔτεκεν τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TCGNT (Byz)`: καὶ ἔτεκε τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `PT1904 (Byz)`: καὶ ἔτεκε τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TR-Scrivener (1894)`: καὶ ἔτεκε τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτόν, καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἔτεκε τὸν υἱὸν αὐτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτόν, καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TR-Stephanus (1550)`: καὶ ἔτεκε τὸν υἱὸν αὑτῆς τὸν πρωτότοκον, καὶ ἐσπαργάνωσεν αὐτὸν, καὶ ἀνέκλινεν αὐτὸν ἐν τῇ φάτνῃ, διότι ουκʼ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι.
  - `TR-Elzevir (1624)`: και ετεκεν τον υιον αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν τη φατνη διοτι ουκ ην αυτοις τοπος εν τω καταλυματι
  - `𝔓4`: … τον υιον … τον πρωτοτοκον … εσπαργανωσεν αυτον και … αυτον … διοτι ουκ …
  - `A (02)`: και ετεκεν τον υιον αυτησ τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλεινεν αυτον εν φατνη διοτι ουκ ην αυτοισ τοποσ εν τω καταλυματι
  - `Ξ (040)`: και ετεκεν τον ὑϊον αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοις τοπος εν τω […]
  - `W (032)`: και ετεκεν τον υιον αυτησ και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοισ τοποσ εν τω καταλυματι
  - `33`: και ετεκεν τον υν̅ αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν τη φατνη διοτι ουκ ην αυτοις τοπος εν τω καταλυματι
  - `L (019)`: και ετεκεν τον υν̅ αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοις τοπος εν τω καταλυματι
  - `D (05)`: και ετεκεν τον υιον αυτησ τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοισ τοποσ εν τω καταλυματι
  - `Θ (038)`: και ετεκεν τον υιον αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοις τοπος εν τω καταλυματι
  - `1 (f¹)`: και ετεκεν τον υιον αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν τη φατνηι διοτι ουκ ην αυτοις τοπος εν τωι καταλυματι
  - `13 (f¹³)`: και ετεκεν τον υιον αυτης τον πρωτοτοκον και εσπαργανωσεν αυτον και ανεκλινεν αυτον εν φατνη διοτι ουκ ην αυτοις τοπος εν τω καταλυματι
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επι (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τῇ (RP2018 (Byz), TR (KJTR)). Also normalised 22 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 8 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `SRGNT`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ, ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `SBLGNT`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `BHP`: καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ, ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `Nestle1904`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `RP2018 (Byz)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `TR (KJTR)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες, καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `B (03)`: και ποιμενεσ ησαν εν τη χωρα τη αυτη αγραυλουντεσ και φυλασσοντεσ φυλακασ τησ νυκτοσ επι την ποιμνην αυτων
  - `א (01)`: και ποιμαινεσ ησαν εν τη χωρα τη αυτη αγραυλουντεσ και φυλασσοντεσ φυλακασ τησ νυκτοσ επι την ποιμνην αυτων
  - `NA28 (TAGNT)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `THGNT`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `WH1881`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `Tisch8`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `TCGNT (Byz)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `PT1904 (Byz)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `TR-Scrivener (1894)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ποιμένες ἦσαν ἐν τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὐτῶν.
  - `TR-Stephanus (1550)`: Καὶ ποιμένες ἦσαν ενʼ τῇ χώρᾳ τῇ αὐτῇ ἀγραυλοῦντες, καὶ φυλάσσοντες φυλακὰς τῆς νυκτὸς ἐπὶ τὴν ποίμνην αὑτῶν·
  - `TR-Elzevir (1624)`: και ποιμενες ησαν εν τη χωρα τη αυτη αγραυλουντες και φυλασσοντες φυλακας της νυκτος επι την ποιμνην αυτων
  - `A (02)`: και ποιμενεσ ησαν εν τη χωρα τη αυτη αγραυλουντεσ και φυλασσοντεσ φυλακασ τησ νυκτοσ επι την ποιμνην αυτων
  - `Ξ (040)`: και ποιμενες ησαν εν τη χωρα τη αυτη αγραυλουντες και φυλασσοντες φυλακας επι την ποιμνην αυτων
  - `W (032)`: και ποιμενεσ ησαν εν τη χωρα τη αυτη αγραυλουντεσ και φυλασσοντεσ φυλακασ τησ νυκτοσ επι την ποιμνην αυτων
  - `33`: και ποιμενες ησαν εν τη αυτη χωρα αγραυλουντες και φυλασσοντες φυλακας της νυκτος επι την ποιμνην […]
  - `L (019)`: και ποιμαινες ησαν εν τη χωρα τη αυτη αγραυλουντες και φυλασσον τες φυλακας της νυκτος επι την ποιμνην αυτων
  - `D (05)`: ποιμενεσ δε ησαν εν τη χαρα ταυτη αγραυλουντεσ και φυλασσοντεσ τασ φυλακασ τησ νυκτοσ επι την ποιμνην αυτων
  - `Θ (038)`: και ποιμενες ησαν εν τη χορα τη αυτη αγραυλουντες και φυλασσοντες φυλακας της νυκτος επι την ποιμνην αυτων
  - `1 (f¹)`: και ποιμενες ησαν εν τηι χωραι τηι αυτηι αγραυλουντες και φυλασσοντες φυλακας της νυκτος επι της ποιμνης αυτων
  - `13 (f¹³)`: και ποιμενες ησαν εν τη χωρα τη αυτη αγραυλουντες και φυλασσοντες φυλακας της νυκτος επι την πιμνην αυτων
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ποιμένες' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ποιμαινεσ (א (01)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 9 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν·
  - `SRGNT`: Καὶ ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν
  - `SBLGNT`: καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν·
  - `BHP`: καὶ ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `Nestle1904`: καὶ ἄγγελος Κυρίου ἐπέστη αὐτοῖς καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `RP2018 (Byz)`: Καὶ ἰδού, ἄγγελος κυρίου ἐπέστη αὐτοῖς, καὶ δόξα κυρίου περιέλαμψεν αὐτούς· καὶ ἐφοβήθησαν φόβον μέγαν.
  - `TR (KJTR)`: Καὶ, ἰδού, ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς: καὶ ἐφοβήθησαν φόβον μέγαν.
  - `B (03)`: και αγγελοσ κυ̅ επεστη αυτοισ και δοξα κυ̅ περιελαμψεν αυτουσ και εφοβηθησαν σφοδρα
  - `א (01)`: και αγγελοσ κυ̅ επεστη αυτοισ και δοξα κυ̅ επελαμψεν αυτοισ και εφοβηθησαν φοβον μεγαν
  - `NA28 (TAGNT)`: καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς, καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `THGNT`: καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς, καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `WH1881`: καὶ ἄγγελος Κυρίου ἐπέστη αὐτοῖς καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν·
  - `Tisch8`: καὶ ἄγγελος κυρίου ἐπέστη αὐτοῖς καὶ δόξα κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `TCGNT (Byz)`: καὶ ἰδού, ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `PT1904 (Byz)`: καὶ ἰδοὺ ἄγγελος Κυρίου ἐπέστη αὐτοῖς καὶ δόξα Κυρίου περιέλαμψεν αὐτούς, καὶ ἐφοβήθησαν φόβον μέγαν.
  - `TR-Scrivener (1894)`: καὶ ἰδού, ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς· καὶ ἐφοβήθησαν φόβον μέγαν.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἰδού, ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς· καὶ ἐφοβήθησαν φόβον μέγαν.
  - `TR-Stephanus (1550)`: καὶ ἰδοὺ ἄγγελος Κυρίου ἐπέστη αὐτοῖς, καὶ δόξα Κυρίου περιέλαμψεν αὐτούς. καὶ ἐφοβήθησαν φόβον μέγαν·
  - `TR-Elzevir (1624)`: και ιδου αγγελος κυριου επεστη αυτοις και δοξα κυριου περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
  - `A (02)`: και ιδου αγγελοσ κυ̅ επεστη αυτοισ και δοξαν κυ̅ περιελαμψεν αυτουσ και εφοβηθησαν φοβον μεγαν
  - `Ξ (040)`: και αγγελος κυ̅ επεστη αυτοις και δοξα θυ̅ περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
  - `W (032)`: και αγγελοσ κυ̅ επεστη αυτοισ και δοξα κυ̅ περιελαμψεν αυτουσ και εφοβηθησαν φοβον μεγαν σφοδρα
  - `33`: και ιδου αγγελος κυ̅ επεστη αυτοις και δοξα κυ̅ περιελαμψεν αυτους και […] φοβον μεγαν
  - `L (019)`: και αγγελος κυ̅ επεστη αυτοις και δοξα κυ̅ περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
  - `D (05)`: και ιδου αγγελοσ κυ̅ επεστη αυτοισ και δοξα περιελαμψεν αυτουσ και εφοβηθησαν φοβον μεγαν
  - `Θ (038)`: και ιδου αγγελος κυ̅ επεστη αυτοις και δοξα κυ̅ περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
  - `1 (f¹)`: και ιδου αγγελος κυ̅ επεστη αυτοις και δοξα κυ̅ περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
  - `13 (f¹³)`: και ιδου αγγελος κυ̅ επεστη αυτοις και δοξα κυ̅ περιελαμψεν αυτους και εφοβηθησαν φοβον μεγαν
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἰδού (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'περιέλαμψεν αὐτούς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επελαμψεν αυτοισ (א (01)). [Variation unit spanning several words] Adopted 'φόβον μέγαν' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over σφοδρα (B (03)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 10 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· Μὴ φοβεῖσθε, ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ,
  - `SRGNT`: Καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, “Μὴ φοβεῖσθε, ἰδοὺ γὰρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ,
  - `SBLGNT`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· Μὴ φοβεῖσθε, ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ,
  - `BHP`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, “μὴ φοβεῖσθε· ἰδοὺ γὰρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ·
  - `Nestle1904`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος Μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ,
  - `RP2018 (Byz)`: Καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε· ἰδοὺ γάρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ·
  - `TR (KJTR)`: Καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε: ἰδοὺ, γὰρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ.
  - `B (03)`: και ειπεν αυτοισ ο αγγελοσ μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητισ εσται παντι τω λαω
  - `א (01)`: και ειπεν αυτοισ ο αγγελοσ μη φοβισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητισ εστιν παντι τω λαω
  - `NA28 (TAGNT)`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ
  - `THGNT`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ
  - `WH1881`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος Μὴ φοβεῖσθε, ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ,
  - `Tisch8`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ,
  - `TCGNT (Byz)`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε· ἰδοὺ γάρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ,
  - `PT1904 (Byz)`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος· μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ,
  - `TR-Scrivener (1894)`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε· ἰδοὺ γάρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ·
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε· ἰδοὺ γάρ, εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ·
  - `TR-Stephanus (1550)`: καὶ εἶπεν αὐτοῖς ὁ ἄγγελος, Μὴ φοβεῖσθε· ἰδοὺ γὰρ εὐαγγελίζομαι ὑμῖν χαρὰν μεγάλην, ἥτις ἔσται παντὶ τῷ λαῷ,
  - `TR-Elzevir (1624)`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητις εσται παντι τω λαω
  - `A (02)`: και ειπεν αυτοισ μη φοβεισθαι ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητισ εσται παντι τω λαω
  - `Ξ (040)`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ϊδου γαρ ευαγγελιζομαι ὑμιν χαραν μεγαλην ητις εσται παντι τω λαω
  - `W (032)`: και ειπεν αυτοισ ο αγγελοσ μη φοβεισθαι ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητισ εσται παντι τω λαω
  - `33`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ιδου γαρ ευαγγελιζομαι […] […] μεγαλην ητις εσται παντι τω λαω
  - `L (019)`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητις εσται παντι τω λαω
  - `D (05)`: και ειπεν αυτοισ ο αγγελοσ μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμειν χαραν μεγαιην ητισ εσται και παντι τω λαω
  - `Θ (038)`: και ειπεν αυτοις ο αγγελος μη φοβησθαι ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητις εσται παντι τω λαω
  - `1 (f¹)`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητις εσται παντι τω λαωι
  - `13 (f¹³)`: και ειπεν αυτοις ο αγγελος μη φοβεισθε ιδου γαρ ευαγγελιζομαι υμιν χαραν μεγαλην ητις εσται παντι τω λαω
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἔσται' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εστιν (א (01)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 11 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει Δαυίδ·
  - `SRGNT`: ὅτι ἐτέχθη ὑμῖν σήμερον Σωτὴρ, ὅς ἐστιν Χριστὸς, Κύριος, ἐν πόλει Δαυίδ.
  - `SBLGNT`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει Δαυίδ·
  - `BHP`: ὅτι ἐτέχθη ὑμῖν σήμερον Σωτὴρ, ὅς ἐστιν Χριστὸς, Κύριος, ἐν πόλει Δαυείδ.
  - `Nestle1904`: ὅτι ἐτέχθη ὑμῖν σήμερον Σωτήρ, ὅς ἐστιν Χριστὸς Κύριος, ἐν πόλει Δαυείδ.
  - `RP2018 (Byz)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτήρ, ὅς ἐστιν χριστὸς κύριος, ἐν πόλει Δαυίδ.
  - `TR (KJTR)`: Ὅτι ἐτέχθη ὑμῖν σήμερον Σωτὴρ, ὅς ἐστιν Χριστὸς Κύριος, ἐν πόλει Δαυίδ.
  - `B (03)`: οτι ετεχθη υμιν σημερον σωτηρ οσ εστιν χσ̅ κσ̅ εν πολει δαυειδ
  - `א (01)`: οτι ετεχθη υμιν σημερον σωτηρ οσ εστιν χσ̅ κσ̅ εν πολι δαδ̅
  - `NA28 (TAGNT)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει Δαυίδ.
  - `THGNT`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει δαυείδ.
  - `WH1881`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος ἐν πόλει Δαυείδ·
  - `Tisch8`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν Χριστὸς κύριος ἐν πόλει Δαυείδ·
  - `TCGNT (Byz)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτήρ, ὅς ἐστι Χριστὸς Κύριος, ἐν πόλει Δαυίδ.
  - `PT1904 (Byz)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτήρ, ὅς ἐστι Χριστὸς Κύριος, ἐν πόλει Δαυΐδ.
  - `TR-Scrivener (1894)`: ὅτι ἐτέχθη ὑμῖν σήμερον Σωτήρ, ὅς ἐστι Χριστὸς Κύριος, ἐν πόλει Δαβίδ.
  - `TR-Boyd (Elz/Scr/Steph)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτήρ, ὅς ἐστι Χριστὸς Κύριος, ἐν πόλει Δαβίδ.
  - `TR-Stephanus (1550)`: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ, ὅς ἐστι Χριστὸς Κύριος, ἐν πόλει Δαβίδ.
  - `TR-Elzevir (1624)`: οτι ετεχθη υμιν σημερον σωτηρ ος εστιν χριστος κυριος εν πολει δαβιδ
  - `A (02)`: οτι ετεχθη υμιν σημερον σωτηρ οσ εστιν χσ̅ κσ̅ εν πολει δαδ̅
  - `Ξ (040)`: οτι ετεχθη ὑμιν σημερον σωτηρ ος εστιν χς̅ κς̅ εν πολει δαδ̅
  - `W (032)`: οτι ετεχθη υμιν σημερον σωτηρ οσ εστιν κσ̅ χσ̅ εν πολει δαυειδ
  - `33`: οτι ετεχθη υμιν σημερον σηρ̅ ος εστιν χς̅ […] […] […] […]
  - `L (019)`: οτι εχθη υμιν σημερον σηρ̅ ος εστιν χς̅ κς̅ εν πολει δαδ̅
  - `D (05)`: οτι ετεχθη υμειν σημερον σωτηρ οσ εστιν χρσ̅ κσ̅ εν πολει δαυειδ
  - `Θ (038)`: οτι ετεχθη υμιν σημερον σωτηρ ος εστιν χς̅ κς̅ εν πολει δαδ̅
  - `1 (f¹)`: οτι ετεχθη υμιν σημερον σηρ̅ ο εστι χς̅ κς̅ εν πολει δαδ̅
  - `13 (f¹³)`: οτι ετεχθη υμιν σημερον σηρ̅ ος εστιν χς̅ κς̅ εν πολει δαδ̅
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 12 surface variation(s) (Accentuation / capitalisation / breathing convention; Koine/Uncial itacistic spelling (ει / ι equivalence); Nomen sacrum (contracted sacred name) for the full word).

### Verse 12 (Confidence: `91.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ τοῦτο ὑμῖν τὸ σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `SRGNT`: Καὶ τοῦτο ὑμῖν τὸ σημεῖον: εὑρήσετε βρέφος ἐσπαργανωμένον, καὶ κείμενον ἐν φάτνῃ.”
  - `SBLGNT`: καὶ τοῦτο ὑμῖν τὸ σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `BHP`: καὶ τοῦτο ὑμῖν τὸ σημεῖον: εὑρήσετε βρέφος ἐσπαργανωμένον, καὶ κείμενον ἐν φάτνῃ.”
  - `Nestle1904`: καὶ τοῦτο ὑμῖν σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `RP2018 (Byz)`: Καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν φάτνῃ.
  - `TR (KJTR)`: Καὶ τοῦτο ὑμῖν τὸ σημεῖον· Εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν τῇ φάτνῃ.
  - `B (03)`: και τουτο υμιν σημειον ευρησετε βρεφοσ εσπαργανωμενον και κειμενον εν φατνη
  - `א (01)`: και τουτο ημιν το σημιον ευρησεται βρεφοσ εσσπαργανωμενον επι φατνη
  - `NA28 (TAGNT)`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `THGNT`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `WH1881`: καὶ τοῦτο ὑμῖν σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ.
  - `Tisch8`: καὶ τοῦτο ὑμῖν τὸ σημεῖον, εὑρήσετε βρέφος ἐσπαργανωμένον ἐν φάτνῃ.
  - `TCGNT (Byz)`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν φάτνῃ.
  - `PT1904 (Byz)`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν φάτνῃ.
  - `TR-Scrivener (1894)`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν τῇ φάτνῃ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν τῇ φάτνῃ.
  - `TR-Stephanus (1550)`: καὶ τοῦτο ὑμῖν τὸ σημεῖον· εὑρήσετε βρέφος ἐσπαργανωμένον, κείμενον ἐν τῇ φάτνῃ.
  - `TR-Elzevir (1624)`: και τουτο υμιν το σημειον ευρησετε βρεφος εσπαργανωμενον κειμενον εν τη φατνη
  - `A (02)`: και τουτο υμειν το σημειον ευρησεται βρεφοσ εσπαργανωμενον κειμενον εν φατνη
  - `Ξ (040)`: και τουτο ὑμιν σημειον ευρησετε βρεφος εσπαργανωμενον και κειμενον εν φατνη
  - `W (032)`: και τουτο υμιν το σημιον ευρησεται βρεφοσ εσπαργανωμενον και κειμενον εν φατνη
  - `33`: και τουτο υμιν το σημειον ευρησεται βρεφος εσπαργανωμενον και […] […] […]
  - `L (019)`: και τουτο υμιν το σημειον ευρησεται βρεφος εσπαργανωμενον και κειμενον εν φατνη
  - `D (05)`: και τουτο υμειν το σημειον εστω ευρησετε βρεφοσ εσπαργανωμενον εν φατνη
  - `Θ (038)`: και τουτο υμιν το σημειον ευρησεται βρεφος εσπαργανωμενον και κειμενον εν φατνη
  - `1 (f¹)`: και τουτο υμιν το σημειον ευρησετε βρεφος εσπαργανωμενον και κειμενον εν φατνηι
  - `13 (f¹³)`: και τουτο υμιν το σημειον ευρησεται βρεφος εσπαργανωμενον κειμενον εν φατνη
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ὑμῖν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ημιν (א (01)). [Omission in some witnesses] Adopted 'τὸ' [א (01), SRGNT, SBLGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.05, confidence 97%) over om. (B (03), Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'εὑρήσετε' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ευρησεται (א (01)). [Omission in some witnesses] Adopted 'καὶ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)); επι (א (01)). [Variation unit spanning several words] Adopted 'κείμενον ἐν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.45, confidence 99%) over τῇ (TR (KJTR)). Also normalised 6 orthographic/surface variation(s).
- *confidence:* Verse confidence 92% = product of 6 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 13 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
  - `SRGNT`: Καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν Θεὸν καὶ λεγόντων,
  - `SBLGNT`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
  - `BHP`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν Θεὸν καὶ λεγόντων,
  - `Nestle1904`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν Θεὸν καὶ λεγόντων
  - `RP2018 (Byz)`: Καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν θεόν, καὶ λεγόντων,
  - `TR (KJTR)`: Καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν Θεὸν, καὶ λεγόντων,
  - `B (03)`: και εξαιφνησ εγενετο συν τω αγγελω πληθοσ στρατειασ ουρανου αινουντων τον θν̅ και λεγοντων
  - `א (01)`: και εξεφνησ εγενετο συν τω αγγελω πληθοσ στρατιασ ουρανιου αινουντων τον θν̅ και λεγοντων
  - `NA28 (TAGNT)`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
  - `THGNT`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
  - `WH1881`: καὶ ἐξέφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων
  - `Tisch8`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν θεὸν καὶ λεγόντων·
  - `TCGNT (Byz)`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν Θεὸν καὶ λεγόντων,
  - `PT1904 (Byz)`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου αἰνούντων τὸν Θεὸν καὶ λεγόντων·
  - `TR-Scrivener (1894)`: καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν Θεόν, καὶ λεγόντων,
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν Θεόν, καὶ λεγόντων,
  - `TR-Stephanus (1550)`: Καὶ ἐξαίφνης ἐγένετο σὺν τῷ ἀγγέλῳ πλῆθος στρατιᾶς οὐρανίου, αἰνούντων τὸν Θεὸν, καὶ λεγόντων,
  - `TR-Elzevir (1624)`: και εξαιφνης εγενετο συν τω αγγελω πληθος στρατιας ουρανιου αινουντων τον θεον και λεγοντων
  - `A (02)`: και εξεφνησ εγενετο συν τω αγγελω πληθοσ στρατιασ ουρανιου αινουντων τον θν̅ και λεγοντων
  - `Ξ (040)`: και εξεφνης εγενετο συν τω αγγελω πληθος στρατιας ουρανιου αινουντων τον θν̅ και λεγοντων
  - `W (032)`: και εξεφνησ εγενετο συν τω αγγελω πληθοσ στρατιασ ουρανιου αινουντων τον θν̅ και λεγοντων
  - `33`: και εξαιφνης εγενετο συν τω αγγελω πληθος στρατειας ουρανιου […] […] […] […] λεγοντων
  - `L (019)`: και εξεφνης εγενετο συν τω αγγελω πληθος στρατιας ουνιου̅ αινουντων τον θν̅ και λεγοντων
  - `D (05)`: και εξαιφνησ εγενετο συν τω αγγελω πληθοσ στρατειασ ουρανου αιτουντων τον θν̅ και λεγοντων
  - `Θ (038)`: και εξεφνης εγενετο συν τω αγγελω πληθος στρατιας ουρανιου αινουντων τον θν̅ και λεγοντον
  - `1 (f¹)`: και εξαιφνης εγενετο συν τω αγγελωι πληθος στρατιας ουνιου̅ αινουντων τον θν̅ και λεγοντων
  - `13 (f¹³)`: και εξεφνης εγενετο συν τω αγγελω πληθος στρατιας ουνιου̅ αινουντων τον θν̅ και λεγοντων
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐξαίφνης' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εξεφνησ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'οὐρανίου' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over ουρανου (B (03)). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 14 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `SRGNT`: “Δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας!”
  - `SBLGNT`: Δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `BHP`: “δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας!”
  - `Nestle1904`: Δόξα ἐν ὑψίστοις Θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `RP2018 (Byz)`: Δόξα ἐν ὑψίστοις θεῷ, καὶ ἐπὶ γῆς εἰρήνη· ἐν ἀνθρώποις εὐδοκία.
  - `TR (KJTR)`: Δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη, ἐν ἀνθρώποις εὐδοκία.
  - `B (03)`: δοξα εν υψιστοισ θω̅ και επι γησ ειρηνη εν ανθρωποισ ευδοκιασ
  - `א (01)`: δοξα εν υψιστοισ θω̅ και επι γησ ιρηνη εν ανθρωποισ ευδοκιασ
  - `NA28 (TAGNT)`: δόξα ἐν ὑψίστοις θεῷ, καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `THGNT`: δόξα ἐν ὑψίστοις θεῷ, καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `WH1881`: Δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `Tisch8`: δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας.
  - `TCGNT (Byz)`: Δόξα ἐν ὑψίστοις Θεῷ καὶ ἐπὶ γῆς εἰρήνη· ἐν ἀνθρώποις εὐδοκία.
  - `PT1904 (Byz)`: δόξα ἐν ὑψίστοις Θεῷ καὶ ἐπὶ γῆς εἰρήνη, ἐν ἀνθρώποις εὐδοκία .
  - `TR-Scrivener (1894)`: Δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη· ἐν ἀνθρώποις εὐδοκία.
  - `TR-Boyd (Elz/Scr/Steph)`: Δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη· ἐν ἀνθρώποις εὐδοκία.
  - `TR-Stephanus (1550)`: Δόξα ἐν ὑψίστοις Θεῷ, καὶ ἐπὶ γῆς εἰρήνη, ἐν ἀνθρώποις εὐδοκία.
  - `TR-Elzevir (1624)`: δοξα εν υψιστοις θεω και επι γης ειρηνη εν ανθρωποις ευδοκια
  - `A (02)`: δοξα εν υψιστοισ θω̅ και επι γησ ειρηνη εν ανοισ̅ ευδοκιασ
  - `Ξ (040)`: δοξα εν ὑψιστοις θω̅ και επι γης ειρηνη εν ανοις̅ ευδοκια
  - `W (032)`: δοξα εν υψιστοισ θω̅ και επι γησ ειρηνη εν ανοισ̅ ευδοκειασ
  - `33`: δοξα εν υψιστοις θω̅ και επι γης ειρηνη εν ανοις̅ […]
  - `L (019)`: δοξα εν υψιστοις θω̅ και επη γης ειρηνη εν ανοις̅ ευδοκια
  - `D (05)`: δοξα εν υψιστοισ θω̅ και επι γησ ειρηνη εν ανθρωποισ ευδοκιασ
  - `Θ (038)`: δοξα εν υψιστοις θω̅ και επι γης ειρηνη εν ανθρωποις ευδοκια
  - `1 (f¹)`: δοξα εν υψιστοις θωι̅ και επι γης ειρηνη εν ανοις̅ ευδοκια
  - `13 (f¹³)`: δοξα εν υψιστοις θω̅ και επι γης ειρηνη εν ανοις̅ ευδοκια
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'εὐδοκίας' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over εὐδοκία (RP2018 (Byz), TR (KJTR)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 15 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· Διέλθωμεν δὴ ἕως Βηθλέεμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `SRGNT`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους, “Διέλθωμεν δὴ ἕως Βηθλέεμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.”
  - `SBLGNT`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· Διέλθωμεν δὴ ἕως Βηθλέεμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `BHP`: καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους, “διέλθωμεν δὴ ἕως Βηθλέεμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.”
  - `Nestle1904`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπ’ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους Διέλθωμεν δὴ ἕως Βηθλεὲμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `RP2018 (Byz)`: Καὶ ἐγένετο, ὡς ἀπῆλθον ἀπ’ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλέεμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `TR (KJTR)`: Καὶ ἐγένετο, ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἀνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλεέμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `B (03)`: και εγενετο ωσ απηλθον απ αυτων εισ τον ουρανον οι αγγελοι οι ποιμενεσ ελαλουν προσ αλληλουσ διελθωμεν δη εωσ βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονοσ ο ο κσ̅ εγνωρισεν ημιν
  - `א (01)`: και εγενετο ωσ απηλθον απ αυτων εισ τον ουρανον οι αγγελοι ποιμαινεσ ελαλουν προσ αλληλουσ λεγοντεσ διελθωμεν δη εωσ βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονοσ ο ο κσ̅ εγνωρισεν ημιν
  - `NA28 (TAGNT)`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπ᾽ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· διέλθωμεν δὴ ἕως Βηθλέεμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `THGNT`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπ᾽ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· διέλθωμεν δὴ ἕως βηθλεὲμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `WH1881`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους Διέλθωμεν δὴ ἕως Βηθλεὲμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `Tisch8`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπ’ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, οἱ ποιμένες ἐλάλουν πρὸς ἀλλήλους· διέλθωμεν δὴ ἕως Βηθλεὲμ καὶ ἴδωμεν τὸ ῥήμα τοῦτο τὸ γεγονὸς ὃ ὁ κύριος ἐγνώρισεν ἡμῖν.
  - `TCGNT (Byz)`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπ᾽ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλεὲμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `PT1904 (Byz)`: καὶ ἐγένετο ὡς ἀπῆλθον ἀπ᾽ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους· διέλθωμεν δὴ ἕως Βηθλεὲμ καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `TR-Scrivener (1894)`: Καὶ ἐγένετο, ὡς ἀπῆλθον ἀπ᾽ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλεέμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐγένετο, ὡς ἀπῆλθον ἀπ᾿ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλέεμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονός, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `TR-Stephanus (1550)`: Καὶ ἐγένετο ὡς ἀπῆλθον ἀπʼ αὐτῶν εἰς τὸν οὐρανὸν οἱ ἄγγελοι, καὶ οἱ ἄνθρωποι οἱ ποιμένες εἶπον πρὸς ἀλλήλους, Διέλθωμεν δὴ ἕως Βηθλεὲμ, καὶ ἴδωμεν τὸ ῥῆμα τοῦτο τὸ γεγονὸς, ὃ ὁ Κύριος ἐγνώρισεν ἡμῖν.
  - `TR-Elzevir (1624)`: και εγενετο ως απηλθον απ αυτων εις τον ουρανον οι αγγελοι και οι ανθρωποι οι ποιμενες ειπον προς αλληλους διελθωμεν δη εως βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονος ο ο κυριος εγνωρισεν ημιν
  - `A (02)`: και εγενετο ωσ απηλθον απ αυτων εισ τον ουνον̅ οι αγγελοι και οι ανοι̅ οι ποιμαινεσ ειπον προσ αλληλουσ διελθωμεν δη εωσ βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονοσ ο ο κσ̅ εγνωρισεν ημειν
  - `Ξ (040)`: και εγενετο ως απηλθον απ αυτων εις τον ουρανον οι αγγελοι οι ποιμενες ειπαν προς αλληλους διελθωμεν εως βηθλεεμ και ϊδωμεν το ρημα τουτο το γεγονος ο ο κς̅ εγνωρισεν ημιν
  - `W (032)`: και εγενετο ωσ απηλθον απ αυτων εισ τον ουρανον οι αγγελοι οι ποιμενεσ ελαλουν προσ αλληλουσ διελθωμεν δη εωσ βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονοσ ο ο κσ̅ εγνωρισεν ημιν
  - `33`: […] […] ως απηλθον απ αυτων οι αγγελοι εις τον ουρανον και οι ανοι̅ οι […] […] […] […] διελθωμεν δη εως βηθλεεμ και ειδωμεν το ρημα τουτο το γεγονος ο ο κς̅ εγνωρισεν ημιν
  - `L (019)`: και εγενετο ως απηλθον απ αυτων εις τον ουνον̅ οι αγγελοι οι ποιμαινες ειπαν προς αλληλους διελθωμεν δι εως βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονος ο ο κς̅ εγνωρησεν ημιν
  - `D (05)`: και εγενετο ωσ απηλθον οι αγγελοι απ αυτων εισ τον ουρανον και οι ανθρωποι οι ποιμενεσ ειπον προσ αλληλουσ διελθωμεν δη εωσ βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονωσ ο ο κσ̅ εγνωρισεν ημειν
  - `Θ (038)`: και εγενετω ως απηλθον απ αυτων οι αγγελοι εις των ουρανον οι ποιμενες ειπον προς αλληλους διελθωμεν δη εως βηθλεεμ και ιδωμεν το ρημα τ ουτο το γεγονος ο ο κς̅ εγνωρησεν ημιν
  - `1 (f¹)`: και εγενετο ως απηλθον απ αυτων εις τον ουνον̅ οι αγγελοι οι ποιμενες ειπον προς αλληλους διελθωμεν δη εως βηθλεεμ και ιδωμεν το ρημα τουτο το γεγονος ο ο κς̅ εγνωρισεν ημιν
  - `13 (f¹³)`: και εγενετο ως απηλθον απ αυτων οι αγγελοι εις τον ουνον̅ και οι ανοι̅ οι ποιμενες ειπον προς αυτους διελθωμεν δη εως βηθλεεμ και ειδομεν το ρημα τουτο το γεγονος ο ο κς̅ εγνωρισεν ημιν
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over καὶ οἱ ἄνθρωποι (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'οἱ ποιμένες' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ποιμαινεσ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐλάλουν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over εἶπον (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over λεγοντεσ (א (01)). Also normalised 29 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 16 (Confidence: `58.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἦλθον σπεύσαντες καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
  - `SRGNT`: Καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ, καὶ τὸ βρέφος, κείμενον ἐν τῇ φάτνῃ.
  - `SBLGNT`: καὶ ἦλθαν σπεύσαντες καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
  - `BHP`: καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ, καὶ τὸ βρέφος, κείμενον ἐν τῇ φάτνῃ.
  - `Nestle1904`: καὶ ἦλθαν σπεύσαντες, καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
  - `RP2018 (Byz)`: Καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσήφ, καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `TR (KJTR)`: Καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ, καὶ τὸν Ἰωσήφ, καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `B (03)`: και ηλθαν σπευσαντεσ και ανευραν την τε μαριαμ και τον ιωσηφ και το βρεφοσ κειμενον εν τη φατνη
  - `א (01)`: και ηλθον σπευσαντεσ και ανευρον την τε μαριαμ και τον ιωσηφ και το βρεφοσ κειμενον εν τη φατνη
  - `NA28 (TAGNT)`: καὶ ἦλθαν σπεύσαντες καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `THGNT`: καὶ ἦλθαν σπεύσαντες καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `WH1881`: καὶ ἦλθαν σπεύσαντες καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
  - `Tisch8`: καὶ ἦλθαν σπεύσαντες, καὶ ἀνεῦραν τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ·
  - `TCGNT (Byz)`: καὶ ἦλθον σπεύσαντες καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `PT1904 (Byz)`: καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `TR-Scrivener (1894)`: καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσήφ, καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσήφ, καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `TR-Stephanus (1550)`: Καὶ ἦλθον σπεύσαντες, καὶ ἀνεῦρον τήν τε Μαριὰμ καὶ τὸν Ἰωσὴφ, καὶ τὸ βρέφος κείμενον ἐν τῇ φάτνῃ.
  - `TR-Elzevir (1624)`: και ηλθον σπευσαντες και ανευρον την τε μαριαμ και τον ιωσηφ και το βρεφος κειμενον εν τη φατνη
  - `A (02)`: και ηλθον σπευσαντεσ και ανευρον την τε μαριαμ και τον ιωσηφ και το βρεφοσ κειμενον εν τη φατνη
  - `Ξ (040)`: και ηλθαν πισπευσαντες και ευραν την τε μαριαμ και τον ϊωσηφ και το βρεφος κειμενον εν τη φατνη
  - `W (032)`: και ηλθον σπευσαντεσ και ευρον την τε μαριαμ και τον ιωσηφ και το βρεφοσ κειμενον εν τη φατνη
  - `33`: και ηλθον σπευσαντες και ανευρον την τε μαριαμ και τον ιωσηφ και το βρεφος κειμενον εν τη φατνη
  - `L (019)`: και ηλθαν σπευσαντες και ανευραν την τε μαριαμ και τον ιω σηφ και το βρεφος κειμενον εν τη φατνι
  - `D (05)`: και ηλθον σπευδοντεσ και ευρον την μαριαν και τον ιωσηφ και το βρεφοσ κειμενον εν τη φατνη
  - `Θ (038)`: και ηλθον σπευσαντες και ανευρον την τε μαριαμ και τον ιωσηφ και το βρεφος κειμενον εν τη φατνη
  - `1 (f¹)`: και ηλθον σπευσαντες και ευρον την τε μαριαμ και τον ιωσηφ και το βρεφος κειμενον εν τη φατνη
  - `13 (f¹³)`: και ηλθον σπευσαντες και ευρον την τε μαριαμ και τον ιωσηφ και το βρεφος κειμενον εν τη φατνη
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἦλθον' [א (01), SRGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.11, confidence 71%) over ἦλθαν (B (03), SBLGNT, Nestle1904). [Lexical, morphological, or word-order variant] Adopted 'ἀνεῦραν' [B (03), SRGNT, SBLGNT, Nestle1904] (weight 3.77, confidence 83%) over ἀνεῦρον (א (01), BHP, RP2018 (Byz), TR (KJTR)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 59% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 17 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `SRGNT`: Ἰδόντες δὲ, ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς, περὶ τοῦ παιδίου τούτου.
  - `SBLGNT`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `BHP`: ἰδόντες δὲ, ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς, περὶ τοῦ παιδίου τούτου.
  - `Nestle1904`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `RP2018 (Byz)`: Ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `TR (KJTR)`: Ἰδόντες δὲ, διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `B (03)`: ιδοντεσ δε εγνωρισαν περι του ρηματοσ του λαληθεντοσ αυτοισ περι του παιδιου τουτου
  - `א (01)`: ιδοντεσ δε εγνωρισαν περι του ρηματοσ του λαληθεντοσ αυτοισ περι του παιδιου τουτου
  - `NA28 (TAGNT)`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `THGNT`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `WH1881`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `Tisch8`: ἰδόντες δὲ ἐγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `TCGNT (Byz)`: ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `PT1904 (Byz)`: ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου·
  - `TR-Scrivener (1894)`: ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `TR-Stephanus (1550)`: ἰδόντες δὲ διεγνώρισαν περὶ τοῦ ῥήματος τοῦ λαληθέντος αὐτοῖς περὶ τοῦ παιδίου τούτου.
  - `TR-Elzevir (1624)`: ιδοντες δε διεγνωρισαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου τουτου
  - `A (02)`: ιδοντεσ δε διεγνωρισαν περι του ρηματοσ του λαληθεντοσ αυτοισ περι του παιδιου τουτου
  - `Ξ (040)`: ιδοντες εγνωρισαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου τουτου
  - `W (032)`: ιδοντεσ δε εγνωρισαν περι του ρηματοσ του λαληθεντοσ αυτοισ περι του παιδιου τουτου
  - `33`: ιδοντες δε διεγνωρισαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου τουτου
  - `L (019)`: ιδοντες δε εγνωρησαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου τουτου
  - `D (05)`: ιδοντεσ δε εγνωρισαν περι του ρηματοσ του λαληθεντοσ αυτοισ περι του παιδιου
  - `Θ (038)`: ιδοντες δε διεγνωρησαν περη του ρηματος του λαληθεντος αυτοις περι του πεδιου
  - `1 (f¹)`: ιδοντες δε διεγνωρισαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου
  - `13 (f¹³)`: ιδοντες δε διεγνωρισαν περι του ρηματος του λαληθεντος αυτοις περι του παιδιου τουτου
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐγνώρισαν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over διεγνώρισαν (RP2018 (Byz), TR (KJTR)). Also normalised 12 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 18 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς,
  - `SRGNT`: Καὶ πάντες οἱ ἀκούσαντες, ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `SBLGNT`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς,
  - `BHP`: καὶ πάντες οἱ ἀκούσαντες, ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `Nestle1904`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς·
  - `RP2018 (Byz)`: Καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `TR (KJTR)`: Καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `B (03)`: και παντεσ οι ακουσαντεσ εθαυμασαν περι των λαληθεντων υπο των ποιμενων προσ αυτουσ
  - `א (01)`: και παντεσ οι ακουσαντεσ εθαυμασαν περι των λαληθεντων υπο των ποιμενων προσ αυτουσ
  - `NA28 (TAGNT)`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `THGNT`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `WH1881`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς,
  - `Tisch8`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς·
  - `TCGNT (Byz)`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `PT1904 (Byz)`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `TR-Scrivener (1894)`: καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `TR-Stephanus (1550)`: Καὶ πάντες οἱ ἀκούσαντες ἐθαύμασαν περὶ τῶν λαληθέντων ὑπὸ τῶν ποιμένων πρὸς αὐτούς.
  - `TR-Elzevir (1624)`: και παντες οι ακουσαντες εθαυμασαν περι των λαληθεντων υπο των ποιμενων προς αυτους
  - `A (02)`: και παντεσ οι ακουσαντεσ εθαυμασαν περι των λαληθεντων υπο των ποιμενων προσ αυτουσ
  - `Ξ (040)`: και παντες οι ακουσαντες εθαυμασαν περι των λαληθεντων ὑπο των ποιμενων προς αυτους
  - `W (032)`: και παντεσ οι ακουσαντεσ εθαυμασαν περι των λαληθεντων υπο των ποιμενων προσ αυτουσ
  - `33`: και παντες οι ακουσαντες εθαυμασαν περι των λαληθεντων υπο των ποιμενων προς αυτους
  - `L (019)`: και παντες οι ακουσαντες εθαυμασαν περι των λαληθετων υπο των ποιμαινων προς αυτους
  - `D (05)`: και παντεσ οι ακουοντεσ εθαυμαζον περι των λαληθεντων υπο των ποιμενων προσ αυτουσ
  - `Θ (038)`: και παντες οι ακουσαντες εθαυμασαν περι τον λαληθεντων υπο των ποιμενων προς αυτους
  - `1 (f¹)`: και παντες ακουσαντες εθαυμασαν περι των λαληθεντων υπο των ποιμενων προς αυτους
  - `13 (f¹³)`: και παντες οι ακουσαντες εθαυμασαν περι των λαληθεντων υπο των ποιμενων προς αυτους
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 13 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 19 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `SRGNT`: Ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `SBLGNT`: ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `BHP`: ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `Nestle1904`: ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συνβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `RP2018 (Byz)`: Ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR (KJTR)`: Ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `B (03)`: η δε μαρια παντα συνετηρει τα ρηματα συμβαλλουσα εν τη καρδια αυτησ
  - `א (01)`: η δε μαρια παντα συνετηρι τα ρηματα ταυτα συνβαλλουσα εν τη καρδια αυτησ
  - `NA28 (TAGNT)`: Ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `THGNT`: Ἡ δὲ μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `WH1881`: ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συνβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `Tisch8`: ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συνβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TCGNT (Byz)`: ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `PT1904 (Byz)`: ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Scrivener (1894)`: ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Stephanus (1550)`: Ἡ δὲ Μαριὰμ πάντα συνετήρει τὰ ῥήματα ταῦτα, συμβάλλουσα ἐν τῇ καρδίᾳ αὑτῆς.
  - `TR-Elzevir (1624)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτης
  - `A (02)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτησ
  - `Ξ (040)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτης
  - `W (032)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συνβαλλουσα εν τη καρδια αυτησ
  - `33`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια εαυτης
  - `L (019)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτης
  - `D (05)`: η δε μαρια συνετηρει παντα τα ρηματα ταυτα συνβαλλουσα εν τη καρδια αυτησ
  - `Θ (038)`: η δε μαρια παντα συνετηρει τα ρηματα ταυτα συνβαλλου σα εν τη καρδια αυτης
  - `1 (f¹)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτης
  - `13 (f¹³)`: η δε μαριαμ παντα συνετηρει τα ρηματα ταυτα συμβαλλουσα εν τη καρδια αυτης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Μαρία' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over Μαριὰμ (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'ταῦτα' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 20 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `SRGNT`: Καὶ ὑπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `SBLGNT`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `BHP`: καὶ ὑπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `Nestle1904`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `RP2018 (Byz)`: Καὶ ὑπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TR (KJTR)`: Καὶ ὑπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `B (03)`: και υπεστρεψαν οι ποιμενεσ δοξαζοντεσ και αινουντεσ τον θν̅ επι πασιν οισ ηκουσαν και ειδον καθωσ ελαληθη προσ αυτουσ
  - `א (01)`: και υπεστρεψαν οι ποιμαινεσ δοξαζοντεσ και αινουντεσ τον θν̅ επι πασιν οισ ηκουσαν και ιδον καθωσ ελαληθη προσ αυτουσ
  - `NA28 (TAGNT)`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `THGNT`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `WH1881`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `Tisch8`: καὶ ὑπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ ἴδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TCGNT (Byz)`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `PT1904 (Byz)`: καὶ ὑπέστρεψαν οἱ ποιμένες δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TR-Scrivener (1894)`: καὶ ἐπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TR-Stephanus (1550)`: καὶ ἐπέστρεψαν οἱ ποιμένες, δοξάζοντες καὶ αἰνοῦντες τὸν Θεὸν ἐπὶ πᾶσιν οἷς ἤκουσαν καὶ εἶδον, καθὼς ἐλαλήθη πρὸς αὐτούς.
  - `TR-Elzevir (1624)`: και επεστρεψαν οι ποιμενες δοξαζοντες και αινουντες τον θεον επι πασιν οις ηκουσαν και ειδον καθως ελαληθη προς αυτους
  - `A (02)`: και υπεστρεψαν οι ποιμαινεσ δοξαζοντεσ και αινουντεσ τον θν̅ επι πασιν οισ ηκουσαν και ιδον καθωσ ελαληθη προσ αυτουσ
  - `W (032)`: και υπεστρεψαν οι ποιμενεσ δοξαζοντεσ και αινουντεσ τον θν̅ επι πασιν οισ ηκουσαν και ιδον καθωσ ελαληθη προσ αυτουσ
  - `33`: και υπεστρεψαν οι ποιμενες δοξαζοντες και αινουντες τον θν̅ επι πασιν οις ηκουσαν και ιδον καθως ελαληθη προς αυτους
  - `L (019)`: και υπεστρεψαν οι ποιμαινες δοξαζοντες και αινουντες τον θν̅ επι πασιν οις ηκουσαν και ιδον καθως ελαληθη προς αυτους
  - `D (05)`: και υπεστρεψαν οι ποιμενεσ δοξαζοντεσ και αινουντεσ τον θν̅ επι πασιν οισ ηκουσαν και ιδον καθωσ ελαληθη προσ αυτουσ
  - `Θ (038)`: και υπεστρεψαν οι ποιμενες δοξαζοντες και αινουντες τον θν̅ επι πασιν οις ηκουσαν και ειδον καθως ελαληθη προς αυτους
  - `1 (f¹)`: και υπεστρεψαν οι ποιμενες δοξαζοντες και αινουντες τον θν̅ επι πασιν οις ηκουσαν και ειδον καθως ελαληθη προς αυτους
  - `13 (f¹³)`: και υπεΣτρεψαν οι ποιμεναις δοξαζοντες και αινουντες τονθν̅ επι πασιν οις ηκουσαν και ιδον καθως ελαληθη προς αυτους
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ποιμένες' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ποιμαινεσ (א (01)). Also normalised 18 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 21 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `SRGNT`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `SBLGNT`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `BHP`: καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συνλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `Nestle1904`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `RP2018 (Byz)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TR (KJTR)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν τὸ παιδίον, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `B (03)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν αυτον και εκληθη το ονομα αυτου ισ̅ το κληθεν υπο του αγγελου προ του συλλημφθηναι αυτον εν τη κοιλια
  - `א (01)`: και οτε επλησθησαν ημεραι οκτω του περιτεμιν αυτον και εκληθη το ονομα αυτου ισ̅ το λεχθεν υπο του αγγελου προ του συλλημφθηναι αυτην εν τη κοιλια
  - `NA28 (TAGNT)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτὸν καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `THGNT`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `WH1881`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `Tisch8`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλλημφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TCGNT (Byz)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν αὐτόν, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `PT1904 (Byz)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι ὀκτὼ τοῦ περιτεμεῖν τὸ παιδίον, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TR-Scrivener (1894)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν τὸ παιδίον, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν τὸ παιδίον, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TR-Stephanus (1550)`: Καὶ ὅτε ἐπλήσθησαν ἡμέραι ὀκτὼ τοῦ περιτεμεῖν τὸ παιδίον, καὶ ἐκλήθη τὸ ὄνομα αὐτοῦ Ἰησοῦς, τὸ κληθὲν ὑπὸ τοῦ ἀγγέλου πρὸ τοῦ συλληφθῆναι αὐτὸν ἐν τῇ κοιλίᾳ.
  - `TR-Elzevir (1624)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν το παιδιον και εκληθη το ονομα αυτου ιησους το κληθεν υπο του αγγελου προ του συλληφθηναι αυτον εν τη κοιλια
  - `A (02)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν αυτον και εκληθη το ονομα αυτου ισ̅ το κληθεν υπο του αγγελου προ του συλλημφθηναι αυτον εν τη κοιλια
  - `Ξ (040)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν αυτον και εκληθη το ονομα αυτου ις̅ το κληθεν ὑπο του αγγελου προ του συλλημφθηναι αυτον εν τη κοιλια
  - `W (032)`: και οτε επλησθησαν ημεραι οκτω του περιτεμιν αυτον και εκληθη το ονομα αυτου ισ̅ το κληθεν υπο του αγγελου προ του συνλημφθηναι αυτον εν τη κοιλια
  - `33`: και οτε επληρωθησαν αι ημεραι οκτω του περιτεμειν το παιδιον και εκληθη το ονομα αυτου ις̅ το κληθεν υπο του αγγελου προ του συλληφθηναι αυτον εν τη κοιλια
  - `L (019)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν αυτον και εκληθη το ονομα αυτου ις̅ το κληθεν υπο του αγγελου προ του συλημφθηναι αυτον εν τη κοιλια
  - `D (05)`: και οτε συνετελεσθησαν αι ημεραι αι οκτω του περιτεμειν το παιδιον ωνομασθη το ονομα αυτου ιησ̅ το κληθεν υπο του αγγελου προ του συνλημφθηναι αυτον εν κοιλια μητροσ
  - `Θ (038)`: και οτε επληρωθησαν ημεραι οκτω του περητεμειν αυτον εκληθη το ονομα αυτου ις̅ το κληθεν υπο του αγγελου προ του συλλημφθηναι αυτον εν τη κοιλια
  - `1 (f¹)`: και οτε επλησθησαν ημεραι οκτω του περιτεμειν αυτον και εκληθη το ονομα αυτου ις̅ το κληθεν υπο του αγγελου προ του συλληφθηναι αυτον εν τηι κοιλιαι
  - `13 (f¹³)`: Και οτε επλησθησαν αι ημεραι οκτωOMτου περιτεμειν το παιδιον εκληθη το ονομα αυτουις̅ το κληθεν υπο του αγγελου προ του συλληφθηναι αυτον εν τη κοιλια
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'αὐτόν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over τὸ παιδίον (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'κληθὲν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over λεχθεν (א (01)). [Lexical, morphological, or word-order variant] Adopted 'αὐτὸν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over αυτην (א (01)). Also normalised 23 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 22 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ,
  - `SRGNT`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ Κυρίῳ,
  - `SBLGNT`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ,
  - `BHP`: καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ Κυρίῳ,
  - `Nestle1904`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ Κυρίῳ,
  - `RP2018 (Byz)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα, παραστῆσαι τῷ κυρίῳ-
  - `TR (KJTR)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῆς κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα, παραστῆσαι τῷ Κυρίῳ·
  - `B (03)`: και οτε επλησθησαν αι ημεραι καθαρισμου αυτων κατα τον νομον μωυσεωσ ανηγαγον αυτον εισ ιεροσολυμα παραστησαι τω κω̅
  - `א (01)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωυσεωσ ανηγαγον αυτον εισ ιεροσολυμα παραστησεται τω κω̅
  - `NA28 (TAGNT)`: καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ
  - `THGNT`: καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ
  - `WH1881`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωυσέως, ἀνήγαγον αὐτὸν εἰς Ἰεροσόλυμα παραστῆσαι τῷ κυρίῳ,
  - `Tisch8`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν, κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ κυρίῳ,
  - `TCGNT (Byz)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ Κυρίῳ
  - `PT1904 (Byz)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν κατὰ τὸν νόμον Μωϋσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα παραστῆσαι τῷ Κυρίῳ,
  - `TR-Scrivener (1894)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῆς κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα, παραστῆσαι τῷ Κυρίῳ
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῆς κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα, παραστῆσαι τῷ Κυρίῳ —
  - `TR-Stephanus (1550)`: καὶ ὅτε ἐπλήσθησαν αἱ ἡμέραι τοῦ καθαρισμοῦ αὐτῶν, κατὰ τὸν νόμον Μωσέως, ἀνήγαγον αὐτὸν εἰς Ἱεροσόλυμα, παραστῆσαι τῷ Κυρίῳ,
  - `TR-Elzevir (1624)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτης κατα τον νομον μωσεως ανηγαγον αυτον εις ιεροσολυμα παραστησαι τω κυριω
  - `A (02)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωσεωσ ανηγαγον αυτον εισ ιεροσολυμα παραστησαι τω κω̅
  - `Ξ (040)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον […] …
  - `W (032)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωυσεωσ ανηγαγον αυτον εισ ιεροσολυμα παραστησαι τω κω̅
  - `33`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωυσεως ανηγαγον αυτον εις ιεροσολυμα παραστησαι τω κω̅
  - `L (019)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωσεως ανηγαγον αυτον εις ιεροσολυμα παραστησα τω κω̅
  - `D (05)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτου κατα τον νομον μωυσεωσ ανηγαγον αυτον εισ ιεροσολυμα παραστησαι κω̅
  - `Θ (038)`: και οτε επληροθησαν αι ημερα του καθαρησμου αυτον κατα τον νομων μωυσεως ανηγαγον αυτον εις ιεροσολυμα παραστησε τω κω̅
  - `1 (f¹)`: και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωσεως ανηγαγον αυτον εις ιεροσολυμα παραστησαι τω κωι̅
  - `13 (f¹³)`: Και οτε επλησθησαν αι ημεραι του καθαρισμου αυτων κατα τον νομον μωυσεως ανηγαγον Αυτον εις ιεροσολυμα παραστησαι τωκω̅
- **Philological Rationale:** [Omission in some witnesses] Adopted 'τοῦ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). [Lexical, morphological, or word-order variant] Adopted 'αὐτῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over αὐτῆς (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'Μωϋσέως' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over Μωσέως (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'παραστῆσαι' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over παραστησεται (א (01)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 23 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται,
  - `SRGNT`: καθὼς γέγραπται ἐν νόμῳ Κυρίου, ὅτι “Πᾶν ἄρσεν διανοῖγον μήτραν, ἅγιον τῷ Κυρίῳ κληθήσεται”,
  - `SBLGNT`: καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται,
  - `BHP`: καθὼς γέγραπται ἐν νόμῳ Κυρίου, ὅτι “πᾶν ἄρσεν διανοῖγον μήτραν, ἅγιον τῷ Κυρίῳ κληθήσεται”·
  - `Nestle1904`: καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται,
  - `RP2018 (Byz)`: καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται-
  - `TR (KJTR)`: (Καθὼς γέγραπται ἐν νόμῳ Κυρίου, ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται·)
  - `B (03)`: καθωσ γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τω κω̅ κληθησεται
  - `א (01)`: καθωσ γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγων μητραν αγιον τω κω̅ κληθησεται
  - `NA28 (TAGNT)`: καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται·
  - `THGNT`: καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται·
  - `WH1881`: καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται,
  - `Tisch8`: καθὼς γέγραπται ἐν νόμῳ κυρίου ὅτι πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ κυρίῳ κληθήσεται,
  - `TCGNT (Byz)`: (καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται),
  - `PT1904 (Byz)`: καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται,
  - `TR-Scrivener (1894)`: (καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται),
  - `TR-Boyd (Elz/Scr/Steph)`: καθὼς γέγραπται ἐν νόμῳ Κυρίου ὅτι Πᾶν ἄρσεν διανοῖγον μήτραν ἅγιον τῷ Κυρίῳ κληθήσεται —
  - `TR-Stephanus (1550)`: (καθὼς γέγραπται ἐν νόμῳ Κυρίου, Ὅτι πᾶν ἄρσεν διανοῖγον μήτραν, ἅγιον τῷ Κυρίῳ κληθήσεται·)
  - `TR-Elzevir (1624)`: καθως γεγραπται εν νομω κυριου οτι παν αρσεν διανοιγον μητραν αγιον τω κυριω κληθησεται
  - `A (02)`: καθωσ γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τω κω̅ κληθησεται
  - `W (032)`: καθωσ γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τω κω̅ κληθησεται
  - `33`: καθως γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τω κω̅ κληθησεται
  - `L (019)`: καθως γεγραπται εν νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τω κω̅ κληθησεται
  - `D (05)`: καθωσ γεγραπται εν τω νομω κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον κω̅ κληθησεται
  - `Θ (038)`: καθως γεγραπται εν νομω κυ̅ οτι παν αρσεν διανυγον μητραν αγιον τω κω̅ κληθησεται
  - `1 (f¹)`: καθως γεγραπται εν νομωι κυ̅ οτι παν αρσεν διανοιγον μητραν αγιον τωι κω̅ κληθησεται
  - `13 (f¹³)`: καθως γεγραπται εν νομωκυ̅ οτι παν αρσεν διανοιγον μητραν αγιονκω̅ κληθησεται
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'διανοῖγον' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over διανοιγων (א (01)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 24 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `SRGNT`: καὶ τοῦ δοῦναι θυσίαν, κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ Κυρίου, “Ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.”
  - `SBLGNT`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `BHP`: καὶ τοῦ δοῦναι θυσίαν, κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ Κυρίου, “ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.”
  - `Nestle1904`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ Κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `RP2018 (Byz)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ κυρίου, Ζεῦγος τρυγόνων ἢ δύο νεοσσοὺς περιστερῶν.
  - `TR (KJTR)`: Καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, Ζεῦγος τρυγόνων, ἢ δύο νεοσσοὺς περιστερῶν.
  - `B (03)`: και του δουναι θυσιαν κατα το ειρημενον εν τω νομω κυ̅ ζευγοσ τρυγονων η δυο νοσσουσ περιστερων
  - `א (01)`: και του δουναι θυσιαν κατα το ειρημενον εν τω νομω κυ̅ ζευγοσ τρυγονων η δυο νοσσουσ περιστερων
  - `NA28 (TAGNT)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ κυρίου· ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `THGNT`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ κυρίου· ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `WH1881`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ Κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `Tisch8`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν τῷ νόμῳ, κυρίου, ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν.
  - `TCGNT (Byz)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, ζεῦγος τρυγόνων ἢ δύο νεοσσοὺς περιστερῶν.
  - `PT1904 (Byz)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, ζεῦγος τρυγόνων ἢ δύο νεοσσοὺς περιστερῶν.
  - `TR-Scrivener (1894)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, Ζεῦγος τρυγόνων ἢ δύο νεοσσοὺς περιστερῶν.
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ τοῦ δοῦναι θυσίαν κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, Ζεῦγος τρυγόνων ἢ δύο νεοσσοὺς περιστερῶν.
  - `TR-Stephanus (1550)`: καὶ τοῦ δοῦναι θυσίαν, κατὰ τὸ εἰρημένον ἐν νόμῳ Κυρίου, ζεῦγος τρυγόνων, ἢ δύο νεοσσοὺς περιστερῶν.
  - `TR-Elzevir (1624)`: και του δουναι θυσιαν κατα το ειρημενον εν νομω κυριου ζευγος τρυγονων η δυο νεοσσους περιστερων
  - `A (02)`: και του δουναι θυσιαν κατα το ειρημενον εν νομω κυ̅ ζευγοσ τρυγονων η δυο νεοσσουσ περιστερων
  - `W (032)`: και του δουναι θυσιαν κατα το ειρημενον εν τω νομω κυ̅ ζευγοσ τρυγονων η δυο νοσσουσ περιστερων
  - `33`: και του δουναι θυσιαν κατα το ειρημενον εν νομω κυ̅ ζευγος τρυγονων η δυο νεοσσους περιστερων
  - `L (019)`: και του δουναι θυσιαν κατα το ειρημενον εν τω νομω κυ̅ ζευγος τρυγονων η δυο νεοσσους περιστερων
  - `D (05)`: και του δουναι θυσιαν κατα το ειρημενον εν τω νομω κυ̅ ζευγοσ τρυγονων η δυο νεοσσουσ περιστερων
  - `Θ (038)`: και του δουναι θυσιαν κατα το ειρημενον εν νομω κυ̅ ζευγος τρυγονων η δυο νοσσους περιστερων
  - `1 (f¹)`: και του δουναι θυσιαν κατα το ειρημενον εν νομωι κυ̅ ζευγος τρυγονων η δυο νοσσους περιστερων
  - `13 (f¹³)`: και του δουναι θυσιαν κατα το ειρημενον εν νομωκυ̅ ζευγος τρυγονων η δυο νεοσσους περιστερων
- **Philological Rationale:** [Omission in some witnesses] Adopted 'τῷ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'νοσσοὺς' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over νεοσσοὺς (RP2018 (Byz), TR (KJTR)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 25 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπʼ αὐτόν·
  - `SRGNT`: Καὶ ἰδοὺ, ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ, ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα ἦν Ἅγιον ἐπʼ αὐτόν.
  - `SBLGNT`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπʼ αὐτόν·
  - `BHP`: καὶ ἰδοὺ, ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ, ᾧ ὄνομα Συμεών· καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα ἦν Ἅγιον ἐπʼ αὐτόν.
  - `Nestle1904`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα ἦν Ἅγιον ἐπ’ αὐτόν·
  - `RP2018 (Byz)`: Καὶ ἰδού, ἦν ἄνθρωπος ἐν Ἱερουσαλήμ, ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπ’ αὐτόν.
  - `TR (KJTR)`: Καὶ, ἰδού, ἦν ἄνθρωπος ἐν Ἰερουσαλήμ, ᾧ ὄνομα Συμεών· καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ: καὶ Πνεῦμα Ἅγιον ἦν ἐπʼ αὐτόν.
  - `B (03)`: και ιδου ανθρωποσ ην εν ιερουσαλημ ω ονομα συμεων και ο ανθρωποσ ουτοσ δικαιοσ και ευλαβησ προσδεχομενοσ παρακλησιν του ισραηλ και πνευμα ην αγιον επ αυτον
  - `א (01)`: και ιδου ανθρωποσ ην εν ιερουσαλημ ω ονομα αυτου συμεων και ο ανθρωποσ ουτοσ δικαιοσ και ευσεβησ προσδεχομενοσ παρακλησιν του ιηλ̅ και πνα̅ ην αγιον επ αυτον
  - `NA28 (TAGNT)`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεὼν καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβὴς προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ· καὶ πνεῦμα ἦν ἅγιον ἐπ᾽ αὐτόν.
  - `THGNT`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν ἱερουσαλὴμ ᾧ ὄνομα Συμεὼν καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβὴς προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ· καὶ πνεῦμα ἦν ἅγιον ἐπ᾽ αὐτόν.
  - `WH1881`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἰερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπʼ αὐτόν·
  - `Tisch8`: Καὶ ἰδοὺ ἄνθρωπος ἦν ἐν Ἱερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἦν ἅγιον ἐπ’ αὐτόν·
  - `TCGNT (Byz)`: Καὶ ἰδού, ἦν ἄνθρωπος ἐν Ἱερουσαλὴμ ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβὴς προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα ἦν Ἅγιον ἐπ᾽ αὐτόν.
  - `PT1904 (Byz)`: Καὶ ἰδοὺ ἦν ἄνθρωπος ἐν Ἱεροσολύμοις ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα ἦν Ἅγιον ἐπ᾽ αὐτόν·
  - `TR-Scrivener (1894)`: καὶ ἰδού, ἦν ἄνθρωπος ἐν Ἱερουσαλήμ, ᾧ ὄνομα Σιμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ Πνεῦμα Ἅγιον ἦν ἐπ᾽ αὐτόν.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἰδού, ἦν ἄνθρωπος ἐν Ἱερουσαλήμ, ᾧ ὄνομα Συμεών, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβής, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ, καὶ πνεῦμα ἅγιον ἦν ἐπ᾿ αὐτόν.
  - `TR-Stephanus (1550)`: Καὶ ἰδοὺ ἦν ἄνθρωπος ἐν Ἱερουσαλὴμ, ᾧ ὄνομα Συμεὼν, καὶ ὁ ἄνθρωπος οὗτος δίκαιος καὶ εὐλαβὴς, προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ· καὶ πνεῦμα ἅγιον ἦν ἐπʼ αὐτὸν,
  - `TR-Elzevir (1624)`: και ιδου ην ανθρωπος εν ιερουσαλημ ω ονομα συμεων και ο ανθρωπος ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν του ισραηλ και πνευμα αγιον ην επ αυτον
  - `A (02)`: και ιδου ην ανοσ̅ εν ιλημ̅ ω ονομα συμεων και ο ανοσ̅ ουτοσ δικαιοσ και ευλαβησ προσδεχομενοσ παρακλησιν του ιηλ̅ και πνα̅ ην αγιον επ αυτον
  - `W (032)`: και ιδου ανθρωποσ ην εν ιερουσαλημ ω ονομα συμεων και ο ανθρωποσ ουτοσ δικαιοσ και ευλαβησ προσδεχομενοσ παρακλησιν του ισραηλ και πνα̅ ην αγιον επ αυτον
  - `33`: και ιδου ην ανος̅ εν ιερουσαλημ ω ονομα συμεων και ο ανος̅ ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν του ιηλ̅ και πνα̅ ην αγιον επ αυτον
  - `L (019)`: και ιδου ην ανος̅ εν ιλημ̅ ω ονομα συμεων και ο ανος̅ ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν τω ισλ̅ και πνα̅ ην αγιον επ αυτον
  - `D (05)`: και ην ανθρωποσ εν ιερουσαλημ ω ονομα συμεων και ο ανθρωποσ ουτοσ δικαιοσ και ευλαβησ προσδεχομεμενοσ παρακλησιν του ισραηλ και πνα̅ αγιον ην επ αυτον
  - `Θ (038)`: και ιδου ην ανος̅ εν ιερουσαλημ ω ονομα συμεων και ο ανθρωπος ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν τω ισραηλ και πνα̅ ην αγιον επ αυτον
  - `1 (f¹)`: και ιδου ην ανος̅ εν ιλημ̅ ωι ονομα συμεων και ο ανος̅ ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν τωι ιηλ̅ και πνα̅ αγιον επ αυτον
  - `13 (f¹³)`: και ιδου ην ανος̅ ενιλημ̅ ω ονομα συμεων και οανος̅ ουτος δικαιος και ευλαβης προσδεχομενος παρακλησιν τουιηλ̅ καιπνα̅ ην αγιον επ αυτον
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἄνθρωπος ἦν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἦν ἄνθρωπος (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over αυτου (א (01)). [Lexical, morphological, or word-order variant] Adopted 'εὐλαβής' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ευσεβησ (א (01)). [Variation unit spanning several words] Adopted 'ἦν ἅγιον' [B (03), א (01), SRGNT, Nestle1904, BHP, SBLGNT, RP2018 (Byz)] (weight 6.33, confidence 99%) over Ἅγιον ἦν (TR (KJTR)). Also normalised 21 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 26 (Confidence: `81.3%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἂν ἴδῃ τὸν χριστὸν κυρίου.
  - `SRGNT`: Καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἂν ἴδῃ τὸν Χριστὸν Κυρίου.
  - `SBLGNT`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἢ ἂν ἴδῃ τὸν χριστὸν κυρίου.
  - `BHP`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἂν ἴδῃ τὸν Χριστὸν Κυρίου.
  - `Nestle1904`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἢ ἂν ἴδῃ τὸν Χριστὸν Κυρίου.
  - `RP2018 (Byz)`: Καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν χριστὸν κυρίου.
  - `TR (KJTR)`: Καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου, μὴ ἰδεῖν θάνατον, πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `B (03)`: και ην αυτω κεχρηματισμενον υπο του πνευματοσ του αγιου μη ιδειν θανατον πριν αν ιδη τον χν̅ κυ̅
  - `א (01)`: και ην αυτω κεχρηματισμενον υπο του πνσ̅ του αγιου μη ιδιν θανατον εωσ αν ιδη τον χν̅ κυ̅
  - `NA28 (TAGNT)`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἢ ἂν ἴδῃ τὸν χριστὸν κυρίου
  - `THGNT`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἂν ἴδῃ τὸν χριστὸν κυρίου
  - `WH1881`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου μὴ ἰδεῖν θάνατον πρὶν [ἢ] ἂν ἴδῃ τὸν χριστὸν Κυρίου.
  - `Tisch8`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἢ ἂν ἴδῃ τὸν Χριστὸν κυρίου.
  - `TCGNT (Byz)`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `PT1904 (Byz)`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `TR-Scrivener (1894)`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ Πνεύματος τοῦ Ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `TR-Stephanus (1550)`: καὶ ἦν αὐτῷ κεχρηματισμένον ὑπὸ τοῦ πνεύματος τοῦ ἁγίου, μὴ ἰδεῖν θάνατον πρὶν ἢ ἴδῃ τὸν Χριστὸν Κυρίου.
  - `TR-Elzevir (1624)`: και ην αυτω κεχρηματισμενον υπο του πνευματος του αγιου μη ιδειν θανατον πριν η ιδη τον χριστον κυριου
  - `A (02)`: και ην αυτω κεχρηματισμενον υπο του πνσ̅ του αγιου μη ιδειν θανατον πριν η ιδη τον χν̅ κυ̅
  - `W (032)`: και ην αυτω κεχρηματισμενον υπο του πνσ̅ του αγιου μη ιδιν θανατον πριν ειδη χν̅ κυ̅
  - `33`: και ην αυτω κεχρηματισμενον υπο του πνς̅ του αγιου μη ιδειν θανατον πριν η αν ηδη τον χν̅ κυ̅
  - `L (019)`: και ην αυτω κεχρηματισμενον απο του πνς̅ του αγιου μη ιδειν θανατον πριν η να ιδη τον χν̅ κυ̅
  - `D (05)`: κεχρηματισμενοσ δε ην υπο του πνσ̅ του αγιου μη ιδειν θανατον πριν η ιδη τον χρν̅ κυ̅
  - `Θ (038)`: και ην αυτω κεχρηματησμενον υπο του πνς̅ του αγιου μη ιδειν θανατον πριν αν ηδη τον χν̅ κυ̅
  - `1 (f¹)`: και ην αυτωι κεχρηματισμενον υπο του πνς̅ του αγιου μη ιδειν θανατον πριν η ιδηι τον χριστον κυ̅
  - `13 (f¹³)`: και ην αυτω κεχρηματισμενων υπο τουπνς̅ του αγιου μη ιδειν θανατον πριν ιδειν […] χν̅ κυ̅
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'πρὶν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εωσ (א (01)). [Omission in some witnesses] Adopted 'om.' [B (03), א (01), SRGNT, BHP] (weight 3.89, confidence 83%) over ἢ (SBLGNT, Nestle1904, RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'ἂν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 81% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 27 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ
  - `SRGNT`: Καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς, τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `SBLGNT`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ
  - `BHP`: καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς, τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `Nestle1904`: καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `RP2018 (Byz)`: Καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TR (KJTR)`: Καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν: καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `B (03)`: και ηλθεν εν τω πνευματι εισ το ιερον και εν τω εισαγαγειν τουσ γονεισ το παιδιον ιν̅ του ποιησαι αυτουσ κατα το ειθισμενον του νομου περι αυτου
  - `א (01)`: και ηλθεν εν τω πνι̅ εισ το ιερον και εν τω εισαγαγειν τουσ γονεισ το παιδιον του ποιησαι αυτουσ κατα το ειθισμενον του νομου περι αυτου
  - `NA28 (TAGNT)`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `THGNT`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `WH1881`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ
  - `Tisch8`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TCGNT (Byz)`: καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `PT1904 (Byz)`: καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TR-Scrivener (1894)`: καὶ ἦλθεν ἐν τῷ Πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TR-Stephanus (1550)`: καὶ ἦλθεν ἐν τῷ πνεύματι εἰς τὸ ἱερόν· καὶ ἐν τῷ εἰσαγαγεῖν τοὺς γονεῖς τὸ παιδίον Ἰησοῦν, τοῦ ποιῆσαι αὐτοὺς κατὰ τὸ εἰθισμένον τοῦ νόμου περὶ αὐτοῦ,
  - `TR-Elzevir (1624)`: και ηλθεν εν τω πνευματι εις το ιερον και εν τω εισαγαγειν τους γονεις το παιδιον ιησουν του ποιησαι αυτους κατα το ειθισμενον του νομου περι αυτου
  - `A (02)`: και ηλθεν εν τω πνι̅ εισ το ιερον και εν τω εισαγειν τουσ γονεισ το παιδιον ιν̅ του ποιησαι αυτουσ κατα το ηθισμενον του νομου περι αυτου
  - `W (032)`: και ηλθεν εν τω πνι̅ εισ το ιερον και εν τω εισαγειν τουσ γονεισ το παιδιον ιν̅ του ποιησαι αυτουσ κατα το ειθεισμενον του νομου περι αυτου
  - `33`: και ηλθεν εν τω πνι̅ εις το ιερον και εν τω εισαγαγειν τους γονεις το παιδιον ιν̅ του ποιησαι αυτους κατα το ηθισμενον του νομου περι αυτου
  - `L (019)`: και ηλθεν εν τω πνι̅ εις το ιερον και εν τω εισαγαγειν τους γονεις το παιδιον ιν̅ του ποιησαι αυτους κατα το ειθισμενον του νομου περι αυτου
  - `D (05)`: και ηλθεν εν τω πνι̅ εισ το ιερον και εν τω εισαγαγειν τουσ γονεισ το παιδιον ιην̅ του ποιησαι αυτουσ κατα το εθοσ του νομου περι αυτου
  - `Θ (038)`: και ηλθεν εν το πνι̅ εις το ιερον και εν τω εισαγαγειν τους γονεις το παιδιον ιν̅ του ποιησαι αυτους κατα το ειθεισμενον του νομου περι αυτου
  - `1 (f¹)`: και ηλθεν εν τωι πνι̅ εις το ιερον και εν τωι εισαγαγειν τους γονεις το παιδιον ιν̅ του ποιησαι αυτους κατα το ειθισμενον του νομου περι αυτου
  - `13 (f¹³)`: και ηλθεν εν τωπνι̅ εις το ιερον και εν τω εισαγαγειν τους γονεις το παιδιονιν̅ […] ποιησαι αυτους κατα το ιθισμενον του νομου περι αυτου
- **Philological Rationale:** [Omission in some witnesses] Adopted 'Ἰησοῦν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). Also normalised 26 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 28 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
  - `SRGNT`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας, καὶ εὐλόγησεν τὸν Θεὸν καὶ εἶπεν,
  - `SBLGNT`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
  - `BHP`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας, καὶ εὐλόγησεν τὸν Θεὸν καὶ εἶπεν,
  - `Nestle1904`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν Θεὸν καὶ εἶπεν
  - `RP2018 (Byz)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὐτοῦ, καὶ εὐλόγησεν τὸν θεόν, καὶ εἶπεν,
  - `TR (KJTR)`: Καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὐτοῦ, καὶ εὐλόγησεν τὸν Θεόν, καὶ εἶπεν,
  - `B (03)`: και αυτοσ εδεξατο αυτο εισ τασ αγκαλασ και ευλογησεν τον θν̅ και ειπεν
  - `א (01)`: και αυτοσ δε εδεξατο αυτο εισ τασ αγκαλασ και ευλογησεν τον θν̅ και ειπεν
  - `NA28 (TAGNT)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
  - `THGNT`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
  - `WH1881`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν
  - `Tisch8`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας καὶ εὐλόγησεν τὸν θεὸν καὶ εἶπεν·
  - `TCGNT (Byz)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὐτοῦ καὶ εὐλόγησε τὸν Θεὸν καὶ εἶπε,
  - `PT1904 (Byz)`: καὶ αὐτὸς ἐδέξατο αὐτὸν εἰς τὰς ἀγκάλας αὐτοῦ καὶ εὐλόγησε τὸν Θεὸν καὶ εἶπε·
  - `TR-Scrivener (1894)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὐτοῦ, καὶ εὐλόγησε τὸν Θεόν, καὶ εἶπε,
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὐτοῦ, καὶ εὐλόγησε τὸν Θεόν, καὶ εἶπε,
  - `TR-Stephanus (1550)`: καὶ αὐτὸς ἐδέξατο αὐτὸ εἰς τὰς ἀγκάλας αὑτοῦ, καὶ εὐλόγησε τὸν Θεὸν, καὶ εἶπε,
  - `TR-Elzevir (1624)`: και αυτος εδεξατο αυτο εις τας αγκαλας αυτου και ευλογησεν τον θεον και ειπεν
  - `A (02)`: και αυτοσ εδεξατο αυτο εισ τασ αγκαλασ αυτου και ευλογησεν τον θν̅ και ειπεν
  - `W (032)`: και αυτοσ εδεξατο αυτο εισ τασ ανκαλασ και ηυλογησεν τον θν̅ και ειπεν
  - `33`: και αυτος εδεξατο αυτο εις τας αγκαλας αυτου και ευλογησεν τον θν̅ και ειπεν
  - `L (019)`: και αυτος εδεξατο αυτο εις τας αγκαλας και ευλογησεν τον θν̅ και ειπεν
  - `D (05)`: και αυτοσ εδεξατο αυτο εισ τασ ανκαλασ αυτου και ηυλογησεν τον θν̅ και ειπεν
  - `Θ (038)`: και αυτος εδεξατο αυτο εις τας αγκαλας αυτου και ευλογησεν τον θν̅ και ειπεν
  - `1 (f¹)`: και αυτος εδεξατο αυτο εις τας αγκαλας αυτου και ευλογησεν τον θν̅ και ειπεν
  - `13 (f¹³)`: και […] εδεξατο αυτον εις τας αγκαλας αυτου και ευλογησε τονθν̅ και ειπεν
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over δε (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over αὐτοῦ (RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 29 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `SRGNT`: “Νῦν ἀπολύεις τὸν δοῦλόν σου, Δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `SBLGNT`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `BHP`: “νῦν ἀπολύεις τὸν δοῦλόν σου, Δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `Nestle1904`: Νῦν ἀπολύεις τὸν δοῦλόν σου, Δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `RP2018 (Byz)`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου, ἐν εἰρήνῃ·
  - `TR (KJTR)`: Νῦν ἀπολύεις τὸν δοῦλόν σου Δέσποτα, κατὰ τὸ ῥῆμά σου, ἐν εἰρήνῃ:
  - `B (03)`: νυν απολυεισ τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `א (01)`: νυν απολλυεισ τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `NA28 (TAGNT)`: νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ
  - `THGNT`: νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ
  - `WH1881`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `Tisch8`: νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `TCGNT (Byz)`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ·
  - `PT1904 (Byz)`: νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου ἐν εἰρήνῃ,
  - `TR-Scrivener (1894)`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου, ἐν εἰρήνῃ·
  - `TR-Boyd (Elz/Scr/Steph)`: Νῦν ἀπολύεις τὸν δοῦλόν σου, δέσποτα, κατὰ τὸ ῥῆμά σου, ἐν εἰρήνῃ·
  - `TR-Stephanus (1550)`: Νῦν ἀπολύεις τὸν δοῦλόν σου δέσποτα, κατὰ τὸ ῥῆμά σου, ἐν εἰρήνῃ·
  - `TR-Elzevir (1624)`: νυν απολυεις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `A (02)`: νυν απολυεισ τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `W (032)`: νυν απολυεισ τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `33`: νυν απολυεις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `L (019)`: νυν απολυεις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `D (05)`: νυν απολυεισ τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `Θ (038)`: νυν απολυεις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
  - `1 (f¹)`: νυν απολυεις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνηι
  - `13 (f¹³)`: νυν απολυ εις τον δουλον σου δεσποτα κατα το ρημα σου εν ειρηνη
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἀπολύεις' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over απολλυεισ (א (01)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 30 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
  - `SRGNT`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `SBLGNT`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
  - `BHP`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `Nestle1904`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `RP2018 (Byz)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TR (KJTR)`: Ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `B (03)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `א (01)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `NA28 (TAGNT)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
  - `THGNT`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
  - `WH1881`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου
  - `Tisch8`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TCGNT (Byz)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `PT1904 (Byz)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TR-Scrivener (1894)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TR-Boyd (Elz/Scr/Steph)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TR-Stephanus (1550)`: ὅτι εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου,
  - `TR-Elzevir (1624)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `A (02)`: οτι ιδον οι οφθαλμοι μου το σωτηριον σου
  - `W (032)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `33`: οτι ιδον οι οφθαλμοι μου το σωτηριον σου
  - `L (019)`: οτι ιδον οι οφθαλμοι μου το σριον̅ σου
  - `D (05)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `Θ (038)`: οτι ειδον οι οφθαλμοι μου το σωτηριον σου
  - `1 (f¹)`: οτι ειδον οι οφθαλμοι μου το σριον̅ σου
  - `13 (f¹³)`: οτι ειδον οι οφθαλμοι μου το σριον̅ σου
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 7 surface variation(s) (Accentuation / capitalisation / breathing convention; Punctuation / spacing difference only).

### Verse 31 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `SRGNT`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `SBLGNT`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `BHP`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `Nestle1904`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `RP2018 (Byz)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν·
  - `TR (KJTR)`: Ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν·
  - `B (03)`: ο ητοιμασασ κατα προσωπον παντων των λαων
  - `א (01)`: ο ητοιμασασ κατα προσωπον παντων των λαων
  - `NA28 (TAGNT)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `THGNT`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `WH1881`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `Tisch8`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `TCGNT (Byz)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `PT1904 (Byz)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν,
  - `TR-Scrivener (1894)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν·
  - `TR-Boyd (Elz/Scr/Steph)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν·
  - `TR-Stephanus (1550)`: ὃ ἡτοίμασας κατὰ πρόσωπον πάντων τῶν λαῶν·
  - `TR-Elzevir (1624)`: ο ητοιμασας κατα προσωπον παντων των λαων
  - `A (02)`: ο ητοιμασασ κατα προσωπον παντων των λαων
  - `W (032)`: ο ητοιμασασ κατα προσωπον παντων των λαων
  - `33`: ο ητοιμασας κατα προσωπον παντων των λαων
  - `L (019)`: ο ητοιμασας κατα προσωπον παντων των λαων
  - `D (05)`: ο ητοιμασασ κατα προσωπον παντων των λαων
  - `Θ (038)`: ο ητοιμασας κατα πρωσωπον παντων των λαων
  - `1 (f¹)`: ο ητοιμασας κατα προσωπον παντων λαων
  - `13 (f¹³)`: ο ητοιμασας κατα προσωπον παντων των λαων
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 7 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 32 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `SRGNT`: ‘φῶς εἰς ἀποκάλυψιν ἐθνῶν’ καὶ δόξαν λαοῦ σου, Ἰσραήλ.”
  - `SBLGNT`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `BHP`: ‘φῶς εἰς ἀποκάλυψιν ἐθνῶν’ καὶ δόξαν λαοῦ σου, Ἰσραήλ.”
  - `Nestle1904`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `RP2018 (Byz)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν, καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TR (KJTR)`: Φῶς εἰς ἀποκάλυψιν Ἐθνῶν, καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `B (03)`: φωσ εισ αποκαλυψιν εθνων και δοξαν λαου σου ισραηλ
  - `א (01)`: φωσ εισ αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `NA28 (TAGNT)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `THGNT`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `WH1881`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `Tisch8`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TCGNT (Byz)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `PT1904 (Byz)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TR-Scrivener (1894)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν, καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TR-Boyd (Elz/Scr/Steph)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν, καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TR-Stephanus (1550)`: φῶς εἰς ἀποκάλυψιν ἐθνῶν, καὶ δόξαν λαοῦ σου Ἰσραήλ.
  - `TR-Elzevir (1624)`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ισραηλ
  - `A (02)`: φωσ εισ αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `W (032)`: φωσ εισ αποκαλυψιν εθνων και δοξαν λαου σου ισραηλ
  - `33`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `L (019)`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `D (05)`: φωσ εισ αποκαλυψιν και δοξαν λαου σου ιστραηλ
  - `Θ (038)`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `1 (f¹)`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
  - `13 (f¹³)`: φως εις αποκαλυψιν εθνων και δοξαν λαου σου ιηλ̅
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 9 surface variation(s) (Accentuation / capitalisation / breathing convention; Nomen sacrum (contracted sacred name) for the full word; Punctuation / spacing difference only).

### Verse 33 (Confidence: `96.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `SRGNT`: Καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `SBLGNT`: καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `BHP`: καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `Nestle1904`: καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `RP2018 (Byz)`: Καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TR (KJTR)`: Καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `B (03)`: και ην ο πατηρ αυτου και η μητηρ θαυμαζοντεσ επι τοισ λαλουμενοισ περι αυτου
  - `א (01)`: και ην ο πατηρ αυτου και η μητηρ αυτου θαυμαζοντεσ επι τοισ λαλουμενοισ περι αυτου
  - `NA28 (TAGNT)`: Καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `THGNT`: Καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `WH1881`: καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `Tisch8`: καὶ ἦν ὁ πατὴρ αὐτοῦ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TCGNT (Byz)`: Καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `PT1904 (Byz)`: καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TR-Scrivener (1894)`: καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TR-Stephanus (1550)`: Καὶ ἦν Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ θαυμάζοντες ἐπὶ τοῖς λαλουμένοις περὶ αὐτοῦ.
  - `TR-Elzevir (1624)`: και ην ιωσηφ και η μητηρ αυτου θαυμαζοντες επι τοις λαλουμενοις περι αυτου
  - `A (02)`: και ην ο ιωσηφ και η μηρ̅ αυτου θαυμαζοντεσ επι τοισ λαλουμενοισ περι αυτου
  - `Ξ (040)`: … θαυμαζοντες επι τοις λαλουμενοις περι αυτου
  - `W (032)`: και ην ο πατηρ αυτου και η μητηρ θαυμαζοντεσ επι τοισ λαλουμενοισ περι αυτου
  - `33`: και ην ιωσηφ και μηρ̅ θαυμαζοντες επι τοις λαλουμενοις περι αυτου
  - `L (019)`: και ην ο πηρ̅ αυτου και η μηρ̅ θαυμαζοντες επι τοις λαλουμενοις περι αυτου
  - `D (05)`: και ην ο πατηρ αυτου και η μητηρ θαυμαζοντεσ επι τοισ λαλουμενοισ περι αυτου
  - `Θ (038)`: και ην ιωσηφ και η μηρ̅ αυτου θαυμαζοντες επι τοις λαλουμενοις περι αυτου
  - `1 (f¹)`: και ην ο πηρ̅ αυτου και η μηρ̅ θαυμαζοντες επι πασι τοις λαλουμενοις περι αυτου
  - `13 (f¹³)`: και ην ιωσηφ και η μηρ̅ αυτου θαυμαζοντες επι τοις λαλουμενοις περι αυτου
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ὁ πατὴρ αὐτοῦ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over Ἰωσὴφ (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.77, confidence 98%) over αὐτοῦ (א (01), RP2018 (Byz), TR (KJTR)). Also normalised 11 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 34 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον,
  - `SRGNT`: Καὶ εὐλόγησεν αὐτοὺς Συμεὼν, καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, “Ἰδοὺ, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ, καὶ εἰς σημεῖον ἀντιλεγόμενον,
  - `SBLGNT`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον,
  - `BHP`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν, καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, “ἰδοὺ, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ, καὶ εἰς σημεῖον ἀντιλεγόμενον·
  - `Nestle1904`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον
  - `RP2018 (Byz)`: Καὶ εὐλόγησεν αὐτοὺς Συμεών, καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδού, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραήλ, καὶ εἰς σημεῖον ἀντιλεγόμενον·
  - `TR (KJTR)`: Καὶ εὐλόγησεν αὐτοὺς Συμεών, καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδού, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραήλ· καὶ εἰς σημεῖον ἀντιλεγόμενον·
  - `B (03)`: και ευλογησεν αυτουσ συμεων και ειπεν προσ μαριαμ την μητερα αυτου ιδου ουτοσ κειται εισ πτωσιν και αναστασιν πολλων εν τω ισραηλ και εισ σημειον αντιλεγομενον
  - `א (01)`: και ηυλογησεν αυτουσ συμεων και ειπεν προσ μαριαμ την μρα̅ αυτου ιδου ουτοσ κειται εισ πτωσιν και αναστασιν πολλων εν τω ισλ̅ και σημιον αντιλεγομενον
  - `NA28 (TAGNT)`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον.
  - `THGNT`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον.
  - `WH1881`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον,
  - `Tisch8`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπεν πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον.
  - `TCGNT (Byz)`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπε πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδού, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον—
  - `PT1904 (Byz)`: καὶ εὐλόγησεν αὐτοὺς Συμεὼν καὶ εἶπε πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ· ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ καὶ εἰς σημεῖον ἀντιλεγόμενον.
  - `TR-Scrivener (1894)`: καὶ εὐλόγησεν αὐτοὺς Σιμεών, καὶ εἶπε πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδού, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραήλ, καὶ εἰς σημεῖον ἀντιλεγόμενον·
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ εὐλόγησεν αὐτοὺς Συμεών, καὶ εἶπε πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδού, οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραήλ, καὶ εἰς σημεῖον ἀντιλεγόμενον·
  - `TR-Stephanus (1550)`: Καὶ εὐλόγησεν αὐτοὺς Συμεὼν, καὶ εἶπε πρὸς Μαριὰμ τὴν μητέρα αὐτοῦ, Ἰδοὺ οὗτος κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραὴλ, καὶ εἰς σημεῖον ἀντιλεγόμενον
  - `TR-Elzevir (1624)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μητερα αυτου ιδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ισραηλ και εις σημειον αντιλεγομενον
  - `A (02)`: και ευλογησεν αυτουσ συμεων και ειπεν προσ μαριαμ την μρα̅ αυτου ιδου ουτοσ κειται εισ πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εισ σημειον αντιλεγομενον
  - `Ξ (040)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μητερα αυτου ϊδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημειον αντιλεγομενον
  - `W (032)`: και ηυλογησεν αυτουσ συμεων και ειπεν προσ μαριαμ την μρα̅ αυτου ιδου ουτοσ κειται εισ πτωσιν και αναστασιν πολλων εν τω ισραηλ και εισ σημιον αντιλεγομενον
  - `33`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μρα̅ αυτου ιδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημειον αντιλεγομενον
  - `L (019)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μρα̅ αυτου ιδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημιον αντιλεγομενον
  - `D (05)`: και ευλογησεν αυτουσ συμεων και ειπεν προσ μαριαν την μητερα αυτου ιδου ουτοσ κειται εισ πτωσιν και εισ αναστασιν πολλων εν τω ισραηλ και εισ σημειον αντιλεγομενον
  - `Θ (038)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μρα̅ αυτου ιδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημειον αντιλεγομενον
  - `1 (f¹)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαμ την μρα̅ αυτου ιδου ουτος κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημειον αντιλεγομενον
  - `13 (f¹³)`: και ευλογησεν αυτους συμεων και ειπεν προς μαριαν την μρα̅ αυτου ιδου ουτως κειται εις πτωσιν και αναστασιν πολλων εν τω ιηλ̅ και εις σημειον αντιλεγομενον
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'εὐλόγησεν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ηυλογησεν (א (01)). [Variation unit spanning several words] Adopted 'εἰς σημεῖον' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over σημιον (א (01)). Also normalised 23 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 35 (Confidence: `95.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `SRGNT`: καὶ σοῦ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.”
  - `SBLGNT`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `BHP`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία· ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.”
  - `Nestle1904`: —καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία—, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `RP2018 (Byz)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία· ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TR (KJTR)`: (Καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία,) ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `B (03)`: και σου αυτησ την ψυχην διελευσεται ρομφαια οπωσ αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `א (01)`: και σου δε αυτησ την ψυχην διελευσεται ρομφαια οπωσ αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι πονηροι
  - `NA28 (TAGNT)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `THGNT`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `WH1881`: καὶ σοῦ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `Tisch8`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TCGNT (Byz)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία—ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `PT1904 (Byz)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία, ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TR-Scrivener (1894)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία· ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία· ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TR-Stephanus (1550)`: (καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία,) ὅπως ἂν ἀποκαλυφθῶσιν ἐκ πολλῶν καρδιῶν διαλογισμοί.
  - `TR-Elzevir (1624)`: και σου δε αυτης την ψυχην διελευσεται ρομφαια οπως αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `A (02)`: και σου δε αυτησ την ψυχην διελευσεται ρομφαια οπωσ αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `Ξ (040)`: και σου αυτης την ψυχην διελευσεται ρομφαια οπως αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `W (032)`: και σου αυτησ την ψυχην διελευσεται ρομφαια οπωσ αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `33`: και σου δε αυτης την ψυχην διελευσεται ρομφαια οπως αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `L (019)`: και σου αυτης την ψυχην διελευσετε ρομφαια οπως αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `D (05)`: και σου δε αυτησ την ψυχην διελευσεται ρομφαια οπωσ ανακαλυφθωσιν πολλων καρδιων διαλογισμοι
  - `Θ (038)`: και σου δε αυτης την ψυχην διελευσεται ρομφαια οπως ανακαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `1 (f¹)`: και σου δε αυτης την ψυχην διελευσεται ρομφαια οπως αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
  - `13 (f¹³)`: και σου δε αυτης την ψυχην διελευσεται ρομφαια οπως αν αποκαλυφθωσιν εκ πολλων καρδιων διαλογισμοι
- **Philological Rationale:** [Omission in some witnesses] Adopted 'δὲ' [א (01), SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.00, confidence 96%) over om. (B (03), SRGNT). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over πονηροι (א (01)). Also normalised 14 orthographic/surface variation(s).
- *confidence:* Verse confidence 95% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 36 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ (αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `SRGNT`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `SBLGNT`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ (αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `BHP`: καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `Nestle1904`: Καὶ ἦν Ἄννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `RP2018 (Byz)`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ- αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `TR (KJTR)`: Καὶ ἦν Ἅννα, προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ: αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς·
  - `B (03)`: και ην αννα προφητισ θυγατηρ φανουηλ εκ φυλησ ασηρ αυτη προβεβηκυια εν ημεραισ πολλαισ ζησασα μετα ανδροσ ετη επτα απο τησ παρθενειασ αυτησ
  - `א (01)`: και ην αννα προφητισ θυγατηρ φανουηλ εκ φυλησ ασηρ αυτη προβεβηκυια εν ημεραισ πολλαισ χηρευσασα μετα ανδροσ ετη ζʹ απο τησ παρθενιασ αυτησ
  - `NA28 (TAGNT)`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς·
  - `THGNT`: Καὶ ἦν ἄννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενείας αὐτῆς·
  - `WH1881`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ, (αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `Tisch8`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, Ζήσασα μετὰ ἀνδρὸς ἔτη ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `TCGNT (Byz)`: Καὶ ἦν Ἄννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `PT1904 (Byz)`: Καὶ ἦν Ἄννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ· αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `TR-Scrivener (1894)`: καὶ ἦν Ἄννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ (αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἦν Ἅννα προφῆτις, θυγάτηρ Φανουήλ, ἐκ φυλῆς Ἀσήρ — αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὐτῆς,
  - `TR-Stephanus (1550)`: Καὶ ἦν Ἄννα προφῆτις θυγάτηρ Φανουὴλ ἐκ φυλῆς Ἀσὴρ, αὕτη προβεβηκυῖα ἐν ἡμέραις πολλαῖς, ζήσασα ἔτη μετὰ ἀνδρὸς ἑπτὰ ἀπὸ τῆς παρθενίας αὑτῆς,
  - `TR-Elzevir (1624)`: και ην αννα προφητις θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβηκυια εν ημεραις πολλαις ζησασα ετη μετα ανδρος επτα απο της παρθενιας αυτης
  - `A (02)`: και ην αννα προφητισ θυγατηρ φανουηλ εκ φυλησ ασηρ αυτη προβεβηκυια εν ημεραισ πολλαισ ζησασα ετη επτα μετα ανδροσ απο τησ παρθενειασ αυτησ
  - `Ξ (040)`: και ην αννα προφητις θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβηκυϊα εν ημεραις πολλαις ζησασα μετα ανδρος ετη επτα απο της παρθενειας αυτης
  - `W (032)`: και ην αννα προφητισ θυγατηρ φανουηλ εκ φυλησ ασηρ αυτη προβεβηκυια εν ημεραισ πολλαισ ζησασα μετα ανδροσ ετη ζʹ απο τησ παρθενιασ αυτησ
  - `33`: και ην αννα προφητης θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβηκυια εν ημεραις πολλαις ζησασα μετα ανδρος ετη επτα απο της παρθενιας αυτης
  - `L (019)`: και ην ανα προφητης θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβη κυια εν ημεραις πολλαις ζησασα μετα ανδρος ετη επτα απο της παρθενιας αυτης
  - `D (05)`: και αννα προφητισ θυγατηρ φανουηλ εκ φυλησ ασηρ και αυτη προβεβηκυια εν ημεραισ πολλαισ ζησασα ετη επτα μετα ανδροσ απο τησ παρθενειασ αυτησ
  - `Θ (038)`: και ην αννα προφητης θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβηκοιια εν ημεραις πολλαις ζησασα μετ ανδρος ετη επτα απο της παρθενιας αυτης
  - `1 (f¹)`: και ην αννα προφητης θυγατηρ φανουηλ εκ φυλης ασηρ αυτη προβεβηκυια εν ημεραις πολλαις ζησασα ετη μετα ανδρος επτα απο της παρθενιας αυτης
  - `13 (f¹³)`: και ην αννα προφητης θυγατηρ φανουηλ εκ φυλης ασηρ αυ τη προβεβηκυια εν ημεραις πολλαις ζησασα μετα ανδρος ετη επτα απο της παρθενιας αυτης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ζήσασα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over χηρευσασα (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἔτη (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'ἔτη' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). Also normalised 21 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 37 (Confidence: `94.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων,) ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `SRGNT`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `SBLGNT`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων,) ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `BHP`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `Nestle1904`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `RP2018 (Byz)`: καὶ αὕτη χήρα ὡς ἐτῶν ὀγδοήκοντα τεσσάρων- ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `TR (KJTR)`: Καὶ αὐτὴ χήρα ὡς ἐτῶν ὀγδοηκοντα τεσσάρων, ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `B (03)`: και αυτη χηρα εωσ ετων ογδοηκοντα τεσσαρων η ουκ αφειστα του ιερου νηστειαισ και δεησεσι λατρευουσα νυκτα και ημεραν
  - `א (01)`: και αυτη χηρα εωσ ετων εβδομηκοντα τεσσαρων η ουκ αφιστατο εκ του ιερου νηστιασ και δεησιν λατρευουσα νυκτα και ημεραν
  - `NA28 (TAGNT)`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν·
  - `THGNT`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν·
  - `WH1881`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων,) ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσιν λατρεύουσα νύκτα καὶ ἡμέραν.
  - `Tisch8`: καὶ αὐτὴ χήρα ἕως ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο τοῦ ἱεροῦ νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν.
  - `TCGNT (Byz)`: καὶ αὐτὴ χήρα ὡς ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν.
  - `PT1904 (Byz)`: καὶ αὐτὴ χήρα ὡς ἐτῶν ὀγδοήκοντα τεσσάρων, ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν·
  - `TR-Scrivener (1894)`: καὶ αὕτη χήρα ὡς ἐτῶν ὀγδοηκοντατεσσάρων), ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν.
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ αὕτη χήρα ὡς ἐτῶν ὀγδοήκοντα τεσσάρων — ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν.
  - `TR-Stephanus (1550)`: καὶ αὕτη χήρα ὡς ἐτῶν ὀγδοηκοντατεσσάρων, ἣ οὐκ ἀφίστατο ἀπὸ τοῦ ἱεροῦ, νηστείαις καὶ δεήσεσι λατρεύουσα νύκτα καὶ ἡμέραν.
  - `TR-Elzevir (1624)`: και αυτη χηρα ως ετων ογδοηκοντατεσσαρων η ουκ αφιστατο απο του ιερου νηστειαις και δεησεσιν λατρευουσα νυκτα και ημεραν
  - `A (02)`: και αυτη χηρα εωσ ετων ογδοηκοντα τεσσαρων η ουκ αφιστατο απο του ιερου νηστιαισ και δεησεσιν λατρευουσα νυκτα και ημερα
  - `Ξ (040)`: και αυτη χηρα εως ετων ογδοηκοντα τεσσαρων η ουχ […] […] ϊερου νηστειαις και δεησεσιν λατρευουσα νυκτα και ημεραν
  - `W (032)`: και ην αυτη χηρα ωσ ετων πʹ δʹ η ουκ αφιστατο του ιερου νηστιαισ τε και δεησεσιν λατρευουσα νυκτα και ημεραν
  - `33`: και αυτη χηρα εως ετων ογδοηκοντα τεσσαρων η ουκ αφιστατο απο του ιερου νηστειαις και δεησεσι λατρευουσα νυκτα και ημεραν
  - `L (019)`: και αυτη χηρα εως ετων ογδοηκοντα τεσσαρων η ουκ αφειστατο του ιερου νηστειαις και δεησεσι λατρευουσα νυκτα και ημεραν
  - `D (05)`: και αυτη χηρα ετων πʹ δʹ η ουκ αφιστατο του ναου νηστειαισ και δεησεσι λατρευουσα νυκτα και ημεραν
  - `Θ (038)`: και αυτη χηρα ως ετων πδʹ η ουκ αφιστατο απο του ιερου νηστειαις και δεησεσιν λατρεουσα νυκτα και ημεραν
  - `1 (f¹)`: και αυτη χηρα ως ετων ογδοηκοντα τεσσαρων η ουκ αφιστατο απο του ιερου νηστειαις και δεησεσι λατρευουσα νυκτα και ημεραν
  - `13 (f¹³)`: και αυτη χηρα ως ετων ογδοηκοντα τεσσαρων η ουκ αφιστατο απο του ιερου νηστειαις και δεησεσι λατρευουσα νυκταν και ημεραν
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἕως' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ὡς (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ὀγδοήκοντα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εβδομηκοντα (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἀφίστατο' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over αφειστα (B (03)). [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.77, confidence 99%) over ἀπὸ (RP2018 (Byz), TR (KJTR)); εκ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'νηστείαις' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over νηστιασ (א (01)). [Lexical, morphological, or word-order variant] Adopted 'δεήσεσιν' [SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR), B (03)] (weight 5.97, confidence 99%) over δεησιν (א (01)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 94% = product of 6 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 38 (Confidence: `96.1%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `SRGNT`: Καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα, ἀνθωμολογεῖτο τῷ Θεῷ, καὶ ἐλάλει περὶ αὐτοῦ, πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `SBLGNT`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `BHP`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα, ἀνθωμολογεῖτο τῷ Θεῷ, καὶ ἐλάλει περὶ αὐτοῦ, πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `Nestle1904`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `RP2018 (Byz)`: Καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ κυρίῳ, καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `TR (KJTR)`: Καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Κυρίῳ, καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν ἐν Ἰερουσαλήμ.
  - `B (03)`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω θω̅ και ελαλει περι αυτου πασι τοισ προσδεχομενοισ λυτρωσιν ιερουσαλημ
  - `א (01)`: και αυτη τη ωρα επιστασα ανθωμολογιτο τω θω̅ και ελαλει περι αυτου πασιν τοισ προσδεχομενοισ λυτρωσιν ιηλμ̅
  - `NA28 (TAGNT)`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `THGNT`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν ἱερουσαλήμ.
  - `WH1881`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ.
  - `Tisch8`: καὶ αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ θεῷ καὶ ἐλάλει περὶ αὐτοῦ πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἱερουσαλήμ.
  - `TCGNT (Byz)`: καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Κυρίῳ καὶ ἐλάλει περὶ αὐτοῦ πᾶσι τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `PT1904 (Byz)`: καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Κυρίῳ καὶ ἐλάλει περὶ αὐτοῦ πᾶσι τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `TR-Scrivener (1894)`: καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Κυρίῳ, καὶ ἐλάλει περὶ αὐτοῦ πᾶσι τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα ἀνθωμολογεῖτο τῷ Κυρίῳ, καὶ ἐλάλει περὶ αὐτοῦ πᾶσι τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `TR-Stephanus (1550)`: καὶ αὕτη αὐτῇ τῇ ὥρᾳ ἐπιστᾶσα, ἀνθωμολογεῖτο τῷ Κυρίῳ, καὶ ἐλάλει περὶ αὐτοῦ πᾶσι τοῖς προσδεχομένοις λύτρωσιν ἐν Ἱερουσαλήμ.
  - `TR-Elzevir (1624)`: και αυτη αυτη τη ωρα επιστασα ανθωμολογειτο τω κυριω και ελαλει περι αυτου πασιν τοις προσδεχομενοις λυτρωσιν εν ιερουσαλημ
  - `A (02)`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω κω̅ και ελαλει περι αυτου πασιν τοισ προσδεχομενοισ λυτρωσιν εν ιηλμ̅
  - `Ξ (040)`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω θω̅ και ελαλει περι αυτου πασιν τοις προσδεχομενοις λυτρωσιν ιλημ̅
  - `W (032)`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω θω̅ και ελαλει περι αυτου πασι τοισ προσδεχομενοισ λυτρωσιν ιερουσαλημ
  - `33`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω κω̅ και ελαλει περι αυτου πασιν τοις προσδεχομενοις λυτρωσιν εν ιερουσαλημ
  - `L (019)`: και αυτη τη ωρα επιστασα ανθωμολογειτο τω θω̅ και ελαλει περι αυτου πασιν τοις προσδεχομενοις λυτρωσιν εν ιλημ̅
  - `D (05)`: και αυτη τη ωρα επιστασα ανθωμολογιτο τω θω̅ και ελαλει περι αυτου πασιν τοισ προσδεχομενοισ λυτρωσιν εν ιερουσαλημ
  - `Θ (038)`: και αυτη αυτη τη ωρα επιστασα ανθωμωλογειτω τω κω̅ και ελαλει περι αυτου πασιν τοις προσδεχομενοις λυτρωσιν εν ιερουσαλημ
  - `1 (f¹)`: και αυτη αυτηι τη ωραι επιστασα ανθωμολογειτο τω κω̅ και ελαλει περι αυτου πασι τοις προσδεχομενοις λυτρωσιν ιλημ̅
  - `13 (f¹³)`: και αυτη αυτη τη ωρα επιστασα ανθωμολογειτω τω κω̅ και ελαλη περι αυτου πασι τοις προσδεχομενοις λυτρωσιν εν ιλημ̅
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over αὕτη (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'θεῷ' [B (03), א (01), SRGNT, Nestle1904, BHP, SBLGNT] (weight 5.61, confidence 99%) over κυρίῳ (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἐν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'Ἰερουσαλήμ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, TR (KJTR), RP2018 (Byz)] (weight 5.97, confidence 99%) over ιηλμ̅ (= ιηλμ) (א (01)). Also normalised 15 orthographic/surface variation(s).
- *confidence:* Verse confidence 96% = product of 4 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 39 (Confidence: `66.2%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέτ.
  - `SRGNT`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον Κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς πόλιν ἑαυτῶν Ναζαρέτ.
  - `SBLGNT`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέθ.
  - `BHP`: καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον Κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς πόλιν ἑαυτῶν Ναζαρέτ.
  - `Nestle1904`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον Κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέθ.
  - `RP2018 (Byz)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς τὴν πόλιν ἑαυτῶν Ναζαρέτ.
  - `TR (KJTR)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς τὴν πόλιν αὐτῶν Ναζαρέτ.
  - `B (03)`: και ωσ ετελεσαν παντα τα κατα τον νομον κυ̅ επεστρεψαν εισ την γαλειλαιαν εισ πολιν εαυτων ναζαρεθ
  - `א (01)`: και ωσ ετελεσεν παντα κατα τον νομον κυ̅ επεστρεψεν εισ γαλιλαιαν εισ πολιν εαυτων ναζαρετ
  - `NA28 (TAGNT)`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέθ.
  - `THGNT`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέθ.
  - `WH1881`: Καὶ ὡς ἐτέλεσαν πάντα τὰ κατὰ τὸν νόμον Κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέτ.
  - `Tisch8`: Καὶ ὡς ἐτέλεσαν πάντα κατὰ τὸν νόμον κυρίου, ἐπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς πόλιν ἑαυτῶν Ναζαρέθ.
  - `TCGNT (Byz)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς τὴν πόλιν ἑαυτῶν Ναζαρέτ.
  - `PT1904 (Byz)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς τὴν πόλιν ἑαυτῶν Ναζαρέτ.
  - `TR-Scrivener (1894)`: καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς τὴν πόλιν αὐτῶν Ναζαρέθ.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν, εἰς τὴν πόλιν αὐτῶν Ναζαρέθ.
  - `TR-Stephanus (1550)`: Καὶ ὡς ἐτέλεσαν ἅπαντα τὰ κατὰ τὸν νόμον Κυρίου, ὑπέστρεψαν εἰς τὴν Γαλιλαίαν εἰς τὴν πόλιν αὑτῶν Ναζαρέτ.
  - `TR-Elzevir (1624)`: και ως ετελεσαν απαντα τα κατα τον νομον κυριου υπεστρεψαν εις την γαλιλαιαν εις την πολιν αυτων ναζαρεθ
  - `A (02)`: και ωσ ετελεσαν απαντα τα κατα τον νομον κυ̅ υπεστρεψαν εισ την γαλιλαιαν εισ την πολιν εαυτων ναζαρατ
  - `Ξ (040)`: και ως ετελεσαν παντα τα κατα τον νομον κυ̅ επεστρεψαν εις την γαλιλαιαν εις την πολιν εαυτων ναζαρετ
  - `W (032)`: και ωσ ετελεσαν παντα τα κατα τον νομον κυ̅ επεστρεψαν εισ την γαλιλαιαν εισ πολιν εαυτων ναζαρετ
  - `33`: και ως ετελεσαν απαντα τα κατα τον νομον κυ̅ υπεστρεψαν εις την γαλιλαιαν εις την πολιν εαυτων ναζαρετ
  - `L (019)`: και ως ετελεσαν παντα κατα τον νομον κυ̅ υπεστρεψαν εις την γαλιλαιαν εις την πολιν εαυτον ναζαρετ
  - `D (05)`: και ωσ ετελεσαν απαντα κατα τον νομον κυ̅ υπεστρεψαν εισ την γαλιλαιαν εισ πολιν εαυτων ναζαρεθ καθωσ ερεθη δια του προφητου οτι ναζωραιοσ κληθησεται
  - `Θ (038)`: και ως ετελεσεν απαντα κατα τον νομον κυ̅ υπεστρεψαν εις την γαλιλεαν εις την πολιν εαυτων ναζαρεθ
  - `1 (f¹)`: και ως ετελεσαν απαντα κατα τον νομον υπεστρεψαν εις την γαλιλαιαν εις πολιν εαυτων ναζαρα
  - `13 (f¹³)`: και ως ετελεσαν απαντα κατα τον νομον κυ̅ υπεστρεψαν εις την γαλιλαιαν εις την πολιν αυτων ναζαρεθ
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐτέλεσαν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ετελεσεν (א (01)). [Lexical, morphological, or word-order variant] Adopted 'πάντα' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἅπαντα (RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'τὰ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Lexical, morphological, or word-order variant] Adopted 'ἐπέστρεψαν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 99%) over ὑπέστρεψαν (RP2018 (Byz), TR (KJTR)); επεστρεψεν (א (01)). [Omission in some witnesses] Adopted 'τὴν' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over τὴν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἑαυτῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz)] (weight 6.33, confidence 99%) over αὐτῶν (TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'Ναζαρέτ' [א (01), SRGNT, BHP, RP2018 (Byz), TR (KJTR)] (weight 4.11, confidence 71%) over Ναζαρέθ (B (03), SBLGNT, Nestle1904). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 66% = product of 8 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 40 (Confidence: `96.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπʼ αὐτό.
  - `SRGNT`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο, πληρούμενον σοφίᾳ, καὶ χάρις Θεοῦ ἦν ἐπʼ αὐτό.
  - `SBLGNT`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπʼ αὐτό.
  - `BHP`: τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο, πληρούμενον σοφίᾳ, καὶ χάρις Θεοῦ ἦν ἐπʼ αὐτό.
  - `Nestle1904`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις Θεοῦ ἦν ἐπ’ αὐτό.
  - `RP2018 (Byz)`: Τὸ δὲ παιδίον ηὔξανεν, καὶ ἐκραταιοῦτο πνεύματι, πληρούμενον σοφίας· καὶ χάρις θεοῦ ἦν ἐπ’ αὐτό.
  - `TR (KJTR)`: Τὸ δὲ παιδίον ηὔξανεν, καὶ ἐκραταιοῦτο πνεύματι, πληρούμενον σοφίας: καὶ χάρις Θεοῦ ἦν ἐπʼ αὐτό.
  - `B (03)`: το δε παιδιον ηυξανεν και εκραταιουτο πληρουμενον σοφια και χαρισ θυ̅ ην επ αυτο
  - `א (01)`: το δε παιδιον ηυξανεν και εκραταιουτο πληρουμενον σοφιασ και χαρισ θυ̅ ην επ αυτο
  - `NA28 (TAGNT)`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπ᾽ αὐτό.
  - `THGNT`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπ᾽ αὐτό.
  - `WH1881`: Τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίᾳ, καὶ χάρις θεοῦ ἦν ἐπʼ αὐτό.
  - `Tisch8`: τὸ δὲ παιδίον ηὔξανεν καὶ ἐκραταιοῦτο πληρούμενον σοφίας, καὶ χάρις θεοῦ ἦν ἐπ’ αὐτό.
  - `TCGNT (Byz)`: τὸ δὲ παιδίον ηὔξανε καὶ ἐκραταιοῦτο πνεύματι πληρούμενον σοφίας, καὶ χάρις Θεοῦ ἦν ἐπ᾽ αὐτό.
  - `PT1904 (Byz)`: Τὸ δὲ παιδίον ηὔξανε καὶ ἐκραταιοῦτο πνεύματι πληρούμενον σοφίας, καὶ χάρις Θεοῦ ἦν ἐπ᾽ αὐτό.
  - `TR-Scrivener (1894)`: Τὸ δὲ παιδίον ηὔξανε, καὶ ἐκραταιοῦτο πνεύματι, πληρούμενον σοφίας· καὶ χάρις Θεοῦ ἦν ἐπ᾽ αὐτό.
  - `TR-Boyd (Elz/Scr/Steph)`: Τὸ δὲ παιδίον ηὔξανε, καὶ ἐκραταιοῦτο πνεύματι, πληρούμενον σοφίας· καὶ χάρις Θεοῦ ἦν ἐπ᾿ αὐτό.
  - `TR-Stephanus (1550)`: τὸ δὲ παιδίον ηὔξανε καὶ ἐκραταιοῦτο πνεύματι, πληρούμενον σοφίας· καὶ χάρις Θεοῦ ἦν ἐπʼ αὐτό.
  - `TR-Elzevir (1624)`: το δε παιδιον ηυξανεν και εκραταιουτο πνευματι πληρουμενον σοφιας και χαρις θεου ην επ αυτο
  - `A (02)`: το δε παιδιον ηυξανεν και εκραταιουτο πνι̅ πληρουμενον σοφιασ και χαρισ θυ̅ ην επ αυτο
  - `W (032)`: το δε παιδιον ηυξανεν και εκραταιουτο πληρουμενον σοφια και χαρισ θυ̅ ην επ αυτο
  - `33`: το δε παιδιον ηυξανεν και εκραταιουτο πνι̅ πληρουμενον σοφια και χαρις θυ̅ ην επ αυτο
  - `L (019)`: το δε πεδιον ηυξανε και εκραταιουτο πληρουμενον σοφια και χαρις θυ̅ ην επ αυτο
  - `D (05)`: το δε παιδιον ιησ̅ εκραταιουτο και ηυξανετο πληρουμενον σοφια και χαρισ θυ̅ ην εν αυτω
  - `Θ (038)`: το δε παιδιον ηυξανεν και εκραταιουτο πνι̅ πληρουμενον σοφιας και χαρις θυ̅ ην επ αυτω
  - `1 (f¹)`: το δε παιδιον ηυξανεν και εκραταιουτο πνι̅ πληρουμενον σοφιας και χαρις θυ̅ ην επ αυτο
  - `13 (f¹³)`: το δε παιδιον ηυξανε και εκραταιουτο πνι̅ πληρουμενον σοφιας και χαρις θυ̅ ην επ αυτω
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over πνεύματι (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'σοφίᾳ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over σοφίας (א (01), RP2018 (Byz), TR (KJTR)). Also normalised 13 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 41 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `SRGNT`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ Πάσχα.
  - `SBLGNT`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `BHP`: καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ Πάσχα.
  - `Nestle1904`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ’ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `RP2018 (Byz)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ’ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ Πάσχα.
  - `TR (KJTR)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `B (03)`: και επορευοντο οι γονεισ αυτου κατ ετοσ εισ ιερουσαλημ τη εορτη του πασχα
  - `א (01)`: και επορευοντο οι γονισ αυτου κατ εθοσ ισ ιηλμ̅ τη εορτη του πασχα
  - `NA28 (TAGNT)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾽ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `THGNT`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾽ ἔτος εἰς ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `WH1881`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἰερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `Tisch8`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ’ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `TCGNT (Byz)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾽ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `PT1904 (Byz)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾽ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `TR-Scrivener (1894)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾽ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατ᾿ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ Πάσχα.
  - `TR-Stephanus (1550)`: Καὶ ἐπορεύοντο οἱ γονεῖς αὐτοῦ κατʼ ἔτος εἰς Ἱερουσαλὴμ τῇ ἑορτῇ τοῦ πάσχα.
  - `TR-Elzevir (1624)`: και επορευοντο οι γονεις αυτου κατ ετος εις ιερουσαλημ τη εορτη του πασχα
  - `A (02)`: και επορευοντο οι γονεισ αυτου κατ ετοσ εισ ιλημ̅ τη εορτη του πασχα
  - `W (032)`: και επορευοντο οι γονεισ αυτου καθ ετοσ εισ ιερουσαλημ τη εορτη του πασχα
  - `33`: και επορευοντο οι γονεις αυτου κατ ετος εις ιερουσαλημ τη εορτη του πασχα
  - `L (019)`: και επορευοντο οι γονεις αυτου κατ ετος εις ιλημ̅ τη εορτη του πασχα
  - `D (05)`: επορευοντο δε και οι γονεισ αυτου κατα ετοσ εισ ιερουσαλημ εν τη εορτη του πασχα
  - `Θ (038)`: και επορευοντο οι γονεις αυτου κατθ ετος εις ιερουσαλημ τη εορτη του πασχα
  - `1 (f¹)`: και επορευοντο οι γονεις αυτου κατ ετος εις ιλημ̅ τη εορτη του πασχα
  - `13 (f¹³)`: και επορευοντο οι γονεις αυτου κατ ετος εις ιλημ̅ τη εορτη του πασχα
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἔτος εἰς Ἰερουσαλὴμ' [B (03), SRGNT, SBLGNT, BHP, TR (KJTR), Nestle1904, RP2018 (Byz)] (weight 5.97, confidence 99%) over εθοσ ισ ιηλμ̅ (= εθοσ ισ ιηλμ) (א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 42 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `SRGNT`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `SBLGNT`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `BHP`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `Nestle1904`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `RP2018 (Byz)`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `TR (KJTR)`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἰεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς.
  - `B (03)`: και οτε εγενετο ετων δωδεκα αναβαινοντων αυτων κατα το εθοσ τησ εορτησ
  - `א (01)`: και οτε εγενετο οτων ιβʹ και αναβαινοντων αυτων κατα το εθοσ τησ εορτησ
  - `NA28 (TAGNT)`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `THGNT`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `WH1881`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `Tisch8`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβαινόντων αὐτῶν κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `TCGNT (Byz)`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `PT1904 (Byz)`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς
  - `TR-Scrivener (1894)`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `TR-Stephanus (1550)`: καὶ ὅτε ἐγένετο ἐτῶν δώδεκα, ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα, κατὰ τὸ ἔθος τῆς ἑορτῆς,
  - `TR-Elzevir (1624)`: και οτε εγενετο ετων δωδεκα αναβαντων αυτων εις ιεροσολυμα κατα το εθος της εορτης
  - `A (02)`: και οτε εγενετο ετων δωδεκα αναβαινοντων αυτων εισ ιεροσολυμα κατα το εθοσ τησ εορτησ
  - `C (04)`: … ιεροσολυμα κατα το εθοσ τησ εορτησ
  - `W (032)`: και οτε εγενετο ετων δεκαδυο αναβαινοντων αυτων κατα το εθοσ τησ εορτησ
  - `33`: και οτε εγενετο ετων δωδεκα αναβαινοντων αυτων εις ιεροσολυμα κατα το εθος της εορτης
  - `L (019)`: και οτε εγενετο αυτω ετη δωδεκα αναβαινοντων αυτων κατα το εθος τη εορτης
  - `D (05)`: και οτε εγενετο αυτω ετη ιβʹ ανεβησαν οι γονεισ αυτου εχοντεσ αυτον κατα το εθοσ τησ εορτησ των αζυμων
  - `Θ (038)`: και οτε εγενετο ετων δωδεκα αναβαντων αυτων εις ιεροσολυμα κατα το εθος της εορτης
  - `1 (f¹)`: και οτε εγενετο ετων δεκα δυο αναβαντων αυτων εις ιεροσολυμα κατα το εθος της εορτης
  - `13 (f¹³)`: και οτε εγενετο ετων δωδεκα αναβαντων αυτων εις ιεροσολυμα κατα το εθος της εορτης
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'ἐτῶν δώδεκα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over οτων ιβʹ και (א (01)). [Variation unit spanning several words] Adopted 'ἀναβαινόντων αὐτῶν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἀναβάντων αὐτῶν εἰς Ἱεροσόλυμα (RP2018 (Byz), TR (KJTR)). Also normalised 8 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 43 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `SRGNT`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς, ὑπέμεινεν Ἰησοῦς, ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `SBLGNT`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `BHP`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς, ὑπέμεινεν Ἰησοῦς, ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `Nestle1904`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `RP2018 (Byz)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτούς, ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ· καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ·
  - `TR (KJTR)`: Καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτούς, ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ· καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ.
  - `B (03)`: και τελειωσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ υπεμεινεν ισ̅ ο παισ εν ιερουσαλημ και ουκ εγνωσαν οι γονεισ αυτου
  - `א (01)`: και τελιωσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ υπεμεινεν ο παισ εν ιερουσαλημ και ουκ εγνωσαν οι γονισ αυτου
  - `NA28 (TAGNT)`: καὶ τελειωσάντων τὰς ἡμέρας ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `THGNT`: καὶ τελειωσάντων τὰς ἡμέρας ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν ἱερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `WH1881`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἰερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `Tisch8`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ, καὶ οὐκ ἔγνωσαν οἱ γονεῖς αὐτοῦ.
  - `TCGNT (Byz)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ, καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ.
  - `PT1904 (Byz)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ, καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ.
  - `TR-Scrivener (1894)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτούς, ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ· καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ·
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτούς, ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ· καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ·
  - `TR-Stephanus (1550)`: καὶ τελειωσάντων τὰς ἡμέρας, ἐν τῷ ὑποστρέφειν αὐτοὺς, ὑπέμεινεν Ἰησοῦς ὁ παῖς ἐν Ἱερουσαλήμ· καὶ οὐκ ἔγνω Ἰωσὴφ καὶ ἡ μήτηρ αὐτοῦ.
  - `TR-Elzevir (1624)`: και τελειωσαντων τας ημερας εν τω υποστρεφειν αυτους υπεμεινεν ιησους ο παις εν ιερουσαλημ και ουκ εγνω ιωσηφ και η μητηρ αυτου
  - `A (02)`: και τελειωσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ υπεμεινεν ισ̅ ο παισ εν ιλημ̅ και ουκ εγνω ιωσηφ και η μηρ̅ αυτου
  - `C (04)`: και τελιωσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ υπεμεινεν ισ̅ ο παισ εν ιλημ̅ και ουκ εγνω ιωσηφ και η μηρ̅ αυτου
  - `W (032)`: και τελιωσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ υπεμεινεν ισ̅ ο παισ εν ιερουσαλημ και ουκ εγνωσαν οι γονεισ αυτου
  - `33`: και τελειωσαντων τας ημερας εν τω υποστρεφειν αυτους απεμεινεν ις̅ ο παις εν ιερουσαλημ και ουκ εγνωσαν οι γονεις αυτου
  - `L (019)`: και τελειωσαντων τας ημερας εν τω υποστρεφειν αυτους υπεμεινεν ις̅ ο παις εν ιλημ̅ και ουκ εγνωσαν οι γονεις αυτου
  - `D (05)`: και τελεσαντων τασ ημερασ εν τω υποστρεφειν αυτουσ απεμεινεν ο παισ ιησ̅ εν ιερουσαλημ και ουκ εγνωσαν οι γονισ αυτου
  - `Θ (038)`: και τελιωσαντων τας ημερας εν τω υποστρεφειν αυτους υπεμεινεν ις̅ ο παις εν ιλημ̅ και ουκ εγνωσαν οι γωνεις αυτου
  - `1 (f¹)`: και τελειωσαντων τας ημερας εν τωι υποστρεφειν αυτους απεμεινεν ις̅ ο παις εν ιλημ̅ και ουκ εγνωσαν οι γονεις αυτου
  - `13 (f¹³)`: και τελειωσαντων τας ημερας εν τω υποστρεφειν αυτους υπεμεινεν ις̅ ο παις εν ιλημ̅ και ουκ εγνω ιωσηφ και η μηρ̅ αυτου
- **Philological Rationale:** [Omission in some witnesses] Adopted 'Ἰησοῦς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Variation unit spanning several words] Adopted 'ἔγνωσαν οἱ' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over ἔγνω Ἰωσὴφ (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'γονεῖς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, א (01)] (weight 5.61, confidence 99%) over καὶ ἡ μήτηρ (RP2018 (Byz), TR (KJTR)). Also normalised 17 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 44 (Confidence: `76.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `SRGNT`: Νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ, ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσιν καὶ τοῖς γνωστοῖς,
  - `SBLGNT`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `BHP`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ, ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `Nestle1904`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `RP2018 (Byz)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι, ἦλθον ἡμέρας ὁδόν, καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσιν καὶ ἐν τοῖς γνωστοῖς·
  - `TR (KJTR)`: Νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι, ἦλθον ἡμέρας ὁδόν· καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσιν καὶ ἐν τοῖς γνωστοῖς.
  - `B (03)`: νομισαντεσ δε αυτον ειναι εν τη συνοδια ηλθον ημερασ οδον και ανεζητουν αυτον εν τοισ συγγενευσιν και τοισ γνωστοισ
  - `א (01)`: νομισαντεσ δε αυτον ειναι εν τη συνοδια ηλθον ημερασ οδον και ανεζητουν αυτον εν τοισ συγγενεσιν
  - `NA28 (TAGNT)`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς.
  - `THGNT`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς.
  - `WH1881`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `Tisch8`: νομίσαντες δὲ αὐτὸν εἶναι ἐν τῇ συνοδίᾳ ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενεῦσιν καὶ τοῖς γνωστοῖς,
  - `TCGNT (Byz)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσι καὶ ἐν τοῖς γνωστοῖς,
  - `PT1904 (Byz)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι ἦλθον ἡμέρας ὁδὸν καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσι καὶ ἐν τοῖς γνωστοῖς·
  - `TR-Scrivener (1894)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι, ἦλθον ἡμέρας ὁδόν, καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσι καὶ ἐν τοῖς γνωστοῖς·
  - `TR-Boyd (Elz/Scr/Steph)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι, ἦλθον ἡμέρας ὁδόν, καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσι καὶ ἐν τοῖς γνωστοῖς·
  - `TR-Stephanus (1550)`: νομίσαντες δὲ αὐτὸν ἐν τῇ συνοδίᾳ εἶναι, ἦλθον ἡμέρας ὁδὸν, καὶ ἀνεζήτουν αὐτὸν ἐν τοῖς συγγενέσι καὶ ἐν τοῖς γνωστοῖς·
  - `TR-Elzevir (1624)`: νομισαντες δε αυτον εν τη συνοδια ειναι ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συγγενεσιν και εν τοις γνωστοις
  - `A (02)`: νομισαντεσ δε αυτον εν τη συνοδια ειναι ηλθον ημερασ οδον και ανεζητουν αυτον εν τοισ συγγενεσιν και τοισ γνωστοισ
  - `C (04)`: νομισαντεσ δε αυτον εν τη συνοδια ειναι ηλθον ημερασ και ανεζητουν αυτον εν τοισ συγγενεσιν και τοισ γνωστοισ
  - `W (032)`: νομισαντεσ δε αυτον ειναι εν τη συνοδια ηλθον ημερασ οδον και ανεζητουν αυτον εν τοισ συγγενευσιν και τοισ γνωστοισ
  - `33`: νομισαντες δε αυτον ειναι εν τη συνοδια ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συγγενευσι και τοις γνωστοις
  - `L (019)`: νομισαντες δε αυτον ειναι εν τη συνοδια ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συγγενευσει
  - `D (05)`: και νομισαντεσ αυτον ειναι εν τη συνοδια ηλθον οδον ημερασ και ανεζητουν αυτον εν τοισ συνγενεσιν και εν τοισ γνωστοισ
  - `Θ (038)`: νομισαντες δε αυτον ειναι εν τη συνοδια ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συνγενευσιν και εν τοις γνωστοις
  - `1 (f¹)`: νομισαντες δε αυτον ειναι εν τηι συνοδια ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συγγενευσι και εν τοις γνωστοις
  - `13 (f¹³)`: νομισαντες δε αυτον εν τη συνοδια ειναι ηλθον ημερας οδον και ανεζητουν αυτον εν τοις συγγενευσιν και τοις γνωστοις
- **Philological Rationale:** [Omission in some witnesses] Adopted 'εἶναι' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over εἶναι (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'συγγενεῦσιν' [B (03), SBLGNT, Nestle1904, BHP] (weight 3.70, confidence 80%) over συγγενέσιν (א (01), SRGNT, RP2018 (Byz), TR (KJTR)). [Omission in some witnesses] Adopted 'καὶ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over ἐν (RP2018 (Byz), TR (KJTR)). [Variation unit spanning several words] Adopted 'τοῖς γνωστοῖς' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over om. (א (01)). Also normalised 14 orthographic/surface variation(s).
- *confidence:* Verse confidence 77% = product of 5 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 45 (Confidence: `96.9%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἰερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `SRGNT`: καὶ μὴ εὑρόντες, ὑπέστρεψαν εἰς Ἰερουσαλὴμ, ἀναζητοῦντες αὐτόν.
  - `SBLGNT`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἰερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `BHP`: καὶ μὴ εὑρόντες, ὑπέστρεψαν εἰς Ἰερουσαλὴμ, ἀναζητοῦντες αὐτόν.
  - `Nestle1904`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἱερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `RP2018 (Byz)`: καὶ μὴ εὑρόντες αὐτόν, ὑπέστρεψαν εἰς Ἱερουσαλήμ, ζητοῦντες αὐτόν.
  - `TR (KJTR)`: Καὶ μὴ εὑρόντες αὐτόν, ὑπέστρεψαν εἰς Ἰερουσαλήμ, ζητοῦντες αὐτόν.
  - `B (03)`: και μη ευροντεσ υπεστρεψαν εισ ιερουσαλημ αναζητουντεσ αυτον
  - `א (01)`: και μη ευροντεσ υπεστρεψαν ισ ιερουσαλημ ζητουντεσ αυτον
  - `NA28 (TAGNT)`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἰερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `THGNT`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς ἱερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `WH1881`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἰερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `Tisch8`: καὶ μὴ εὑρόντες ὑπέστρεψαν εἰς Ἱερουσαλὴμ ἀναζητοῦντες αὐτόν.
  - `TCGNT (Byz)`: καὶ μὴ εὑρόντες αὐτὸν ὑπέστρεψαν εἰς Ἱερουσαλὴμ ζητοῦντες αὐτόν.
  - `PT1904 (Byz)`: καὶ μὴ εὑρόντες αὐτὸν ὑπέστρεψαν εἰς Ἱερουσαλὴμ ζητοῦντες αὐτόν.
  - `TR-Scrivener (1894)`: καὶ μὴ εὑρόντες αὐτόν, ὑπέστρεψαν εἰς Ἱερουσαλήμ, ζητοῦντες αὐτόν.
  - `TR-Boyd (Elz/Scr/Steph)`: καὶ μὴ εὑρόντες αὐτόν, ὑπέστρεψαν εἰς Ἱερουσαλήμ, ζητοῦντες αὐτόν.
  - `TR-Stephanus (1550)`: καὶ μὴ εὑρόντες αὐτὸν, ὑπέστρεψαν εἰς Ἱερουσαλὴμ, ζητοῦντες αὐτόν.
  - `TR-Elzevir (1624)`: και μη ευροντες αυτον υπεστρεψαν εις ιερουσαλημ ζητουντες αυτον
  - `A (02)`: και μη ευροντεσ αυτον υπεστρεψαν εισ ιλημ̅ ζητουντεσ αυτον
  - `C (04)`: και μη ευροντεσ υπεστρεψαν εισ ιλημ̅ αναζητουντεσ αυτον
  - `W (032)`: και μη ευροντεσ υπεστρεψαν εισ ιερουσαλημ αναζητουντεσ αυτον
  - `33`: και μη ευροντες υπεστρεψαν εις ιερουσαλημ αναζητουντες αυτον
  - `L (019)`: και μη ευροντες υπεστρεψαν εις ιλημ̅ αναζητουντες αυτον
  - `D (05)`: και μη ευρισκοντεσ υπεστρεψαν εισ ιερουσαλημ αναζητουντεσ αυτον
  - `Θ (038)`: και μη ευροντες αυτον υπεστρεψαν εις ιερουσαλημ αναζητουντες αυτον
  - `1 (f¹)`: και μη ευροντες υπεστρεψαν εις ιλημ̅ αναζητουντες αυτον
  - `13 (f¹³)`: και μη ευροντες αυτον υπεστρεψαν εις ιλημ̅ αναζητουντες αυτον
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over αὐτόν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ἀναζητοῦντες' [B (03), SRGNT, SBLGNT, Nestle1904, BHP] (weight 4.65, confidence 98%) over ζητοῦντες (א (01), RP2018 (Byz), TR (KJTR)). Also normalised 7 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 46 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `SRGNT`: Καὶ ἐγένετο μετὰ ἡμέρας τρεῖς, εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς.
  - `SBLGNT`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `BHP`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς, εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς.
  - `Nestle1904`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `RP2018 (Byz)`: Καὶ ἐγένετο, μεθ’ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν, καὶ ἐπερωτῶντα αὐτούς.
  - `TR (KJTR)`: Καὶ ἐγένετο, μεθʼ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν, καὶ ἐπερωτῶντα αὐτούς.
  - `B (03)`: και εγενετο μετα ημερασ τρισ ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτουσ
  - `א (01)`: και εγενετο μετα ημερασ τρεισ ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επηρωτωντα αυτουσ
  - `NA28 (TAGNT)`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς.
  - `THGNT`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς.
  - `WH1881`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `Tisch8`: καὶ ἐγένετο μετὰ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `TCGNT (Byz)`: καὶ ἐγένετο μεθ᾽ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς.
  - `PT1904 (Byz)`: καὶ ἐγένετο μεθ᾽ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων καὶ ἀκούοντα αὐτῶν καὶ ἐπερωτῶντα αὐτούς·
  - `TR-Scrivener (1894)`: καὶ ἐγένετο, μεθ᾽ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν, καὶ ἐπερωτῶντα αὐτούς.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἐγένετο, μεθ᾿ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ, καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν, καὶ ἐπερωτῶντα αὐτούς.
  - `TR-Stephanus (1550)`: Καὶ ἐγένετο, μεθʼ ἡμέρας τρεῖς εὗρον αὐτὸν ἐν τῷ ἱερῷ καθεζόμενον ἐν μέσῳ τῶν διδασκάλων, καὶ ἀκούοντα αὐτῶν, καὶ ἐπερωτῶντα αὐτούς.
  - `TR-Elzevir (1624)`: και εγενετο μεθ ημερας τρεις ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτους
  - `A (02)`: και εγενετο μεθ ημερασ τρεισ ευρον αυτον εν τω ιερω καθεζομενον εμ μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτουσ
  - `C (04)`: και εγενετο μεθ ημερασ τρεισ ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτον
  - `W (032)`: και εγενετο μετα ημερασ τρισ ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτουσ
  - `33`: και εγενετο μετα ημερας τρεις ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτους
  - `L (019)`: και εγενετο μετα ημερας τρεις ευρον αυτον εν τω ιερω καθεζομενον εμ μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτους
  - `D (05)`: και εγενετο μεθ ημερασ τρεισ ευρον αυτον καθημενον εν τω ιερω εν μεσω των διδασκαλων ακουοντα αυτων και επερωτωντα αυτουσ
  - `Θ (038)`: και εγενετο μεθ ημερας τρεις ευρον αυτον εν τω ιερω καθεζωμενον εν μεσω των διδασκαλων και ακουοντα αυτων και επηρωτωντα αυτους
  - `1 (f¹)`: και εγενετο μετα ημερας τρεις ευρον αυτον εν τωι ιερωι καθημενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτους
  - `13 (f¹³)`: και εγενετο μεθ ημερας τρεις ευρον αυτον εν τω ιερω καθεζομενον εν μεσω των διδασκαλων και ακουοντα αυτων και επερωτωντα αυτους
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐπερωτῶντα' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over επηρωτωντα (א (01)). Also normalised 20 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 47 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `SRGNT`: Ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `SBLGNT`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `BHP`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `Nestle1904`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `RP2018 (Byz)`: Ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TR (KJTR)`: Ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `B (03)`: εξισταντο δε παντεσ επι τη συνεσει και ταισ αποκρισεσιν αυτου
  - `א (01)`: εξισταντο δε παντεσ οι ακουοντεσ αυτου επι τη συνεσι και ταισ αποκρισεσιν αυτου
  - `NA28 (TAGNT)`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `THGNT`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `WH1881`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `Tisch8`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TCGNT (Byz)`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `PT1904 (Byz)`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TR-Scrivener (1894)`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TR-Boyd (Elz/Scr/Steph)`: Ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TR-Stephanus (1550)`: ἐξίσταντο δὲ πάντες οἱ ἀκούοντες αὐτοῦ, ἐπὶ τῇ συνέσει καὶ ταῖς ἀποκρίσεσιν αὐτοῦ.
  - `TR-Elzevir (1624)`: εξισταντο δε παντες οι ακουοντες αυτου επι τη συνεσει και ταις αποκρισεσιν αυτου
  - `A (02)`: εξισταντο δε παντεσ οι ακουοντεσ αυτου επι τη συνεσει και ταισ αποκρισεσιν αυτου
  - `C (04)`: εξισταντο δε παντεσ οι ακουοντεσ αυτου επι τη συνεσι και ταισ αποκρισεσιν αυτου
  - `W (032)`: εξισταντο δε παντεσ επι τη συνεσει και ταισ αποκρισεσιν αυτου
  - `33`: εξισταντο δε παντες οι ακουοντες αυτου επι τη συνεσει και ταις αποκρισεσιν αυτου
  - `L (019)`: εξισταντο δε παντες οι ακουοντες αυτου επι τη συνεσει και ταις αποκρισεσιν αυτου
  - `D (05)`: εξεισταντο δε παντεσ οι ακουοντεσ αυτου επι τη συνεσει και ταισ αποκρισεσιν αυτου
  - `Θ (038)`: εξεισταντο δε παντες οι ακουοντες αυτου επι τη συνεσει και ταις αποκρισεσιν αυτου
  - `1 (f¹)`: εξισταντο δε παντες οι ακουοντες αυτου επι τηι συνεσει και ταις αποκρισεσιν αυτου
  - `13 (f¹³)`: εξισταντο δε παντες οι ακουοντες αυτου επι τη συνεσει και ταις αποκρισεσιν αυτου
- **Philological Rationale:** [Variation unit spanning several words] Adopted 'οἱ ἀκούοντες αὐτοῦ' [א (01), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.95, confidence 99%) over om. (B (03)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 99% = product of 1 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 48 (Confidence: `97.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ζητοῦμέν σε.
  - `SRGNT`: Καὶ ἰδόντες αὐτὸν, ἐξεπλάγησαν καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ, “Τέκνον, τί ἐποίησας ἡμῖν οὕτως; Ἰδοὺ, ὁ πατήρ σου κἀγὼ, ὀδυνώμενοι ζητοῦμέν σε.”
  - `SBLGNT`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου καὶ ἐγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `BHP`: καὶ ἰδόντες αὐτὸν, ἐξεπλάγησαν καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ, “τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ, ὁ πατήρ σου κἀγὼ, ὀδυνώμενοι ζητοῦμεν σε.”
  - `Nestle1904`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ζητοῦμέν σε.
  - `RP2018 (Byz)`: Καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν· καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπεν, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; Ἰδού, ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TR (KJTR)`: Καὶ ἰδόντες αὐτὸν, ἐξεπλάγησαν: καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπεν, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδού, ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `B (03)`: και ιδοντεσ αυτον εξεπλαγησαν και ειπεν προσ αυτον η μητηρ αυτου τεκνον τι εποιησασ ημιν ουτωσ ιδου ο πατηρ σου καγω οδυνωμενοι ζητουμεν σε
  - `א (01)`: και ιδοντεσ αυτον εξεπλαγησαν και ειπεν προσ αυτον η μητηρ αυτου τεκνον τι εποιησασ ημιν ουτωσ ιδου ο πατηρ σου καγω οδυνωμενοι ζητουμεν σε
  - `NA28 (TAGNT)`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `THGNT`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `WH1881`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου καὶ ἐγὼ ὀδυνώμενοι ζητοῦμέν σε.
  - `Tisch8`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ εἶπεν πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ· τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TCGNT (Byz)`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπε, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδού, ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `PT1904 (Byz)`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν, καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπε· τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TR-Scrivener (1894)`: καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν· καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπε, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδού, ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ ἰδόντες αὐτὸν ἐξεπλάγησαν· καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπε, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; Ἰδού, ὁ πατήρ σου κἀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TR-Stephanus (1550)`: καὶ ἰδόντες αὐτὸν, ἐξεπλάγησαν· καὶ πρὸς αὐτὸν ἡ μήτηρ αὐτοῦ εἶπε, Τέκνον, τί ἐποίησας ἡμῖν οὕτως; ἰδοὺ ὁ πατήρ σου κᾀγὼ ὀδυνώμενοι ἐζητοῦμέν σε.
  - `TR-Elzevir (1624)`: και ιδοντες αυτον εξεπλαγησαν και προς αυτον η μητηρ αυτου ειπεν τεκνον τι εποιησας ημιν ουτως ιδου ο πατηρ σου καγω οδυνωμενοι εζητουμεν σε
  - `A (02)`: και ιδοντεσ αυτον εξεπλαγησαν και προσ αυτον η μηρ̅ αυτου ειπεν τεκνον τι εποιησασ ημειν ουτωσ ιδου ο πηρ̅ σου καγω οδυνωμενοι εζητουμεν σε
  - `C (04)`: και ιδοντεσ αυτον εξεπλαγησαν και ειπεν προσ αυτον η μηρ̅ αυτου τεκνον τι εποιησασ ημιν ουτωσ ιδου οι συγγενεισ … και εγω οδυνωμενοι εζητουμεν σε
  - `W (032)`: και ειδοντεσ αυτον εξεπλαγησαν και ειπεν προσ αυτον η μητηρ αυτου τεκνον τι εποιησασ ημιν ουτωσ ιδου ο πατηρ σου καγω οδυνουμενοι εζητουμεν σε
  - `33`: και ιδοντες αυτον εξεπλαγησαν και προς αυτον η μηρ̅ αυτου ειπεν τεκνον τι εποιησας ημιν ουτως ιδου ο πηρ̅ σου και εγω οδυνωμενοι εζητουμεν σε
  - `L (019)`: και ιδοντες αυτον εξεπλαγησαν και ειπεν προς αυτον η μηρ̅ αυτου τεκνον τι εποι ησας ημιν ουτως ιδου ο πηρ̅ σου και εγω οδυνωμενοι εζητουμεν σε
  - `D (05)`: και ιδοντεσ αυτον εξεπλαγησαν και ειπεν προσ αυτον η μητηρ αυτου τεκνον τι εποιησασ ημειν ουτωσ ιδου ο πατηρ σου καγω οδυνωμενοι και λυπουμενοι εζητουμεν σε
  - `Θ (038)`: και ιδοντες αυτον εξεπλαγησαν και ειπεν προς αυτον η μηρ̅ αυτου τεκνον τι εποιησας ημιν ουτως ιδου ο πηρ̅ σου και εγω οδυνωμενοι εζητουμεν σε
  - `1 (f¹)`: και ιδοντες αυτον εξεπλαγησαν και ειπεν προς αυτον η μηρ̅ αυτου τεκνον τι εποιησας ημιν ουτως ιδου ο πηρ̅ σου και εγω οδυνωμενοι εζητουμεν σε
  - `13 (f¹³)`: και ιδοντες αυτον εξεπλαγησαν και προς αυτον η μηρ̅ αυτου ειπεν τεκνον τι εποιησας ημιν ουτως ιδου ο πηρ̅ σου και εγω οδυνομενοι εζητουμεν σε
- **Philological Rationale:** [Omission in some witnesses] Adopted 'εἶπεν' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.61, confidence 99%) over om. (RP2018 (Byz), TR (KJTR)). [Addition / omission between witnesses] Adopted 'om.' [B (03), א (01), SRGNT, SBLGNT, Nestle1904, BHP] (weight 5.73, confidence 99%) over εἶπεν (RP2018 (Byz), TR (KJTR)). [Lexical, morphological, or word-order variant] Adopted 'ζητοῦμέν' [B (03), א (01), SRGNT, Nestle1904, BHP] (weight 4.67, confidence 98%) over ἐζητοῦμέν (SBLGNT, RP2018 (Byz), TR (KJTR)). Also normalised 21 orthographic/surface variation(s).
- *confidence:* Verse confidence 97% = product of 2 unit confidence(s); 1 split-transposition duplicate(s) counted once; calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 49 (Confidence: `98.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ εἶπεν πρὸς αὐτούς· Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `SRGNT`: Καὶ εἶπεν πρὸς αὐτούς, “Τί ὅτι ἐζητεῖτέ με; Οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;”
  - `SBLGNT`: καὶ εἶπεν πρὸς αὐτούς· Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `BHP`: καὶ εἶπεν πρὸς αὐτούς, “τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;”
  - `Nestle1904`: καὶ εἶπεν πρὸς αὐτούς Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ Πατρός μου δεῖ εἶναί με;
  - `RP2018 (Byz)`: Καὶ εἶπεν πρὸς αὐτούς, Τί ὅτι ἐζητεῖτέ με; Οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TR (KJTR)`: Καὶ εἶπεν πρὸς αὐτούς, Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ Πατρός μου δεῖ εἶναί με;
  - `B (03)`: και ειπε προσ αυτουσ τι οτι εζητειτε με ουκ ηδειτε οτι εν τοισ του πατροσ μου δει ειναι με
  - `א (01)`: και ειπεν προσ αυτουσ τι οτι ζητειτε με ουκ ηδειτε οτι εν τοισ του πατροσ μου δι εινε με
  - `NA28 (TAGNT)`: Καὶ εἶπεν πρὸς αὐτούς· τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `THGNT`: Καὶ εἶπεν πρὸς αὐτούς· τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `WH1881`: καὶ εἶπεν πρὸς αὐτούς Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `Tisch8`: καὶ εἶπεν πρὸς αὐτούς· τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TCGNT (Byz)`: καὶ εἶπε πρὸς αὐτούς, Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `PT1904 (Byz)`: καὶ εἶπε πρὸς αὐτούς· τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TR-Scrivener (1894)`: καὶ εἶπε πρὸς αὐτούς, Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ εἶπε πρὸς αὐτούς, Τί ὅτι ἐζητεῖτέ με; Οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TR-Stephanus (1550)`: καὶ εἶπε πρὸς αὐτοὺς, Τί ὅτι ἐζητεῖτέ με; οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με;
  - `TR-Elzevir (1624)`: και ειπεν προς αυτους τι οτι εζητειτε με ουκ ηδειτε οτι εν τοις του πατρος μου δει ειναι με
  - `A (02)`: και ειπεν προσ αυτουσ τι οτι εζητειτε με ουκ ηδειτε οτι εν τοισ του πρσ̅ μου δει ειναι με
  - `C (04)`: και ειπεν προσ αυτουσ τι οτι εζητειται με ουκ ηδειτε οτι εν τοισ του πρσ̅ μου δει ειναι με
  - `W (032)`: και ειπεν προσ αυτουσ τι οτι ζητειτε με ουκ οιδατε οτι εν τοισ του πατροσ δει με ειναι
  - `33`: και ειπεν προς αυτους τι οτι εζητειται με ουκ ηδειται οτι εν τοις του πρς̅ μου δει ειναι με
  - `L (019)`: και ειπεν προς αυτους τι οτι εζητειτε με ου ηδειτε οτι εν τοις του πρς̅ μου δει ειναι με
  - `D (05)`: και ειπεν προσ αυτουσ τι οτι εζητειτε με ουκ οιδατε οτι εν τοισ του πρσ̅ μου δει με ειναι
  - `Θ (038)`: και ειπεν προς αυτους τι οτι εζητειτε με ουκ ηδειτε οτι εν τοις του πρς̅ μου δει με ειναι
  - `1 (f¹)`: και ειπεν προς αυτους τι οτι εζητειτε με ουκ ηιδειτε οτι εν τοις του πρς̅ μου δει με ειναι
  - `13 (f¹³)`: ειπεν δε προς αυτους τι οτι εζητειτε με ουκ ηδητε οτι εν τοις του πρς̅ μου δει με ειναι
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'ἐζητεῖτέ' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over ζητειτε (א (01)). [Lexical, morphological, or word-order variant] Adopted 'εἶναί' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 5.97, confidence 99%) over εινε (א (01)). Also normalised 16 orthographic/surface variation(s).
- *confidence:* Verse confidence 98% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 50 (Confidence: `99.0%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `SRGNT`: Καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `SBLGNT`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `BHP`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `Nestle1904`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `RP2018 (Byz)`: Καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TR (KJTR)`: Καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `B (03)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `א (01)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `NA28 (TAGNT)`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `THGNT`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `WH1881`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `Tisch8`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TCGNT (Byz)`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `PT1904 (Byz)`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TR-Scrivener (1894)`: καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TR-Stephanus (1550)`: Καὶ αὐτοὶ οὐ συνῆκαν τὸ ῥῆμα ὃ ἐλάλησεν αὐτοῖς.
  - `TR-Elzevir (1624)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοις
  - `A (02)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `C (04)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `W (032)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `33`: και αυτοι ου […] το ρημα ο ελαλησεν αυτοις
  - `L (019)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοις
  - `D (05)`: αυτοι δε ου συνηκαν το ρημα ο ελαλησεν αυτοισ
  - `Θ (038)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοις
  - `1 (f¹)`: και αυτοι ου συνηκαν το ρημα ο ειπεν αυτοις
  - `13 (f¹³)`: και αυτοι ου συνηκαν το ρημα ο ελαλησεν αυτοις
- **Philological Rationale:** Substantively unanimous across SRGNT, SBLGNT, BHP, Nestle1904, RP2018 (Byz), TR (KJTR), B (03), א (01). Normalised 9 surface variation(s) (Accentuation / capitalisation / breathing convention).

### Verse 51 (Confidence: `69.6%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `SRGNT`: Καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. Καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `SBLGNT`: καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέθ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `BHP`: καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρὲτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `Nestle1904`: καὶ κατέβη μετ’ αὐτῶν καὶ ἦλθεν εἰς Ναζαρὲθ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `RP2018 (Byz)`: Καὶ κατέβη μετ’ αὐτῶν, καὶ ἦλθεν εἰς Ναζαρέτ· καὶ ἦν ὑποτασσόμενος αὐτοῖς. Καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR (KJTR)`: Καὶ κατέβη μετʼ αὐτῶν, καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς: καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `B (03)`: και κατεβη μετ αυτων και ηλθεν εισ ναζαρεθ και ην υποτασσομενοσ αυτοισ και η μητηρ αυτου διετηρει παντα τα ρηματα εν τη καρδια αυτησ
  - `א (01)`: και κατεβη μετ αυτων και ηλθεν εισ ναζαρετ και ην υποτασσομενοσ αυτοισ και η μητηρ αυτου διετηρι παντα τα ρηματα εν τη καρδια αυτησ
  - `NA28 (TAGNT)`: καὶ κατέβη μετ᾽ αὐτῶν καὶ ἦλθεν εἰς Ναζαρὲθ καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `THGNT`: καὶ κατέβη μετ᾽ αὐτῶν καὶ ἦλθεν εἰς Ναζαρὲθ καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `WH1881`: καὶ κατέβη μετʼ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `Tisch8`: καὶ κατέβη μετ’ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέθ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TCGNT (Byz)`: καὶ κατέβη μετ᾽ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `PT1904 (Byz)`: καὶ κατέβη μετ᾽ αὐτῶν καὶ ἦλθεν εἰς Ναζαρέτ, καὶ ἦν ὑποτασσόμενος αὐτοῖς. καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Scrivener (1894)`: καὶ κατέβη μετ᾽ αὐτῶν, καὶ ἦλθεν εἰς Ναζαρέθ· καὶ ἦν ὑποτασσόμενος αὐτοῖς· καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ κατέβη μετ᾿ αὐτῶν, καὶ ἦλθεν εἰς Ναζαρέθ· καὶ ἦν ὑποτασσόμενος αὐτοῖς. Καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς.
  - `TR-Stephanus (1550)`: καὶ κατέβη μετʼ αὐτῶν, καὶ ἦλθεν εἰς Ναζαρέτ. καὶ ἦν ὑποτασσόμενος αὐτοῖς. Καὶ ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὑτῆς.
  - `TR-Elzevir (1624)`: και κατεβη μετ αυτων και ηλθεν εις ναζαρεθ και ην υποτασσομενος αυτοις και η μητηρ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτης
  - `A (02)`: και κατεβη μετ αυτων και ηλθεν εισ ναζαρατ και ην υποτασσομενοσ αυτοισ και η μηρ̅ αυτου διετηρει τα ρηματα απαντα ταυτα εν τη καρδια αυτησ
  - `C (04)`: … ην υποτασσομενοσ αυτοισ και η μητηρ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτησ
  - `W (032)`: και κατεβη μετ αυτων και ηλθεν εισ ναζαρετ και ην υποτασσομενοσ αυτοισ και η μητηρ αυτου ετηρει παντα τα ρηματα εν τη καρδια αυτησ
  - `33`: και κατεβη μετ αυτων και ηλθεν εις ναζαρετ και ην υποτασσομενος αυτοις και η μηρ̅ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτης
  - `L (019)`: και κατεβη μετ αυτων και ηλθεν εις ναζαρετ και ην υποτασσομενος αυτοις και η μηρ̅ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτης
  - `D (05)`: και κατεβη μετ αυτων εισ ναρεθ και ην υποτασσομενοσ αυτοισ η δε μητηρ αυτου διετηρει τα ρηματα παντα εν τη καρδια αυτησ
  - `Θ (038)`: και κατεβη μετ αυτον και ηλθεν εις ναζαρατ και ην υποτασσομενος αυτοις και η μηρ̅ αυτου διετηρη παντα τα ρηματα ταυτα εν τη καρδια αυτης
  - `1 (f¹)`: και κατεβη μετ αυτων και ηλθεν εις ναζαρεθ και ην υποτασσομενος αυτοις και η μηρ̅ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτης
  - `13 (f¹³)`: και κατεβη μετ αυτων και ηλθεν εις ναζαρεθ και ην υποτασσομενος αυτοις η δε μηρ̅ αυτου διετηρει παντα τα ρηματα ταυτα εν τη καρδια αυτης
- **Philological Rationale:** [Lexical, morphological, or word-order variant] Adopted 'Ναζαρέτ' [א (01), SRGNT, RP2018 (Byz), TR (KJTR), BHP] (weight 4.11, confidence 71%) over Ναζαρέθ (B (03), SBLGNT, Nestle1904). [Omission in some witnesses] Adopted 'om.' [B (03), א (01), SRGNT, Nestle1904, BHP] (weight 4.79, confidence 98%) over ταῦτα (SBLGNT, RP2018 (Byz), TR (KJTR)). Also normalised 23 orthographic/surface variation(s).
- *confidence:* Verse confidence 70% = product of 2 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).

### Verse 52 (Confidence: `64.7%` · Source: `Textual Analysis Brain (Claude-designed · internal evidence · offline)`)
- **Critical Text:** Καὶ Ἰησοῦς προέκοπτεν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `SRGNT`: Καὶ Ἰησοῦς προέκοπτεν τῇ σοφίᾳ, καὶ ἡλικίᾳ, καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `SBLGNT`: Καὶ Ἰησοῦς προέκοπτεν σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `BHP`: καὶ Ἰησοῦς προέκοπτεν τῇ σοφίᾳ, καὶ ἡλικίᾳ, καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `Nestle1904`: Καὶ Ἰησοῦς προέκοπτεν ἐν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `RP2018 (Byz)`: Καὶ Ἰησοῦς προέκοπτεν σοφίᾳ καὶ ἡλικίᾳ, καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `TR (KJTR)`: Καὶ Ἰησοῦς προέκοπτεν σοφίᾳ καὶ ἡλικίᾳ, καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `B (03)`: και ισ̅ προεκοπτεν τη σοφια και ηλικια και χαριτι παρα θω̅ και ανθρωποισ
  - `א (01)`: και ο ισ̅ προεκοπτεν εν τη σοφια και ηλικια και χαριτι θυ̅ και ανθρωποισ
  - `NA28 (TAGNT)`: Καὶ Ἰησοῦς προέκοπτεν ἐν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `THGNT`: Καὶ Ἰησοῦς προέκοπτεν σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `WH1881`: Καὶ Ἰησοῦς προέκοπτεν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `Tisch8`: καὶ Ἰησοῦς προέκοπτεν ἐν τῇ σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις.
  - `TCGNT (Byz)`: Καὶ Ἰησοῦς προέκοπτε σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `PT1904 (Byz)`: Καὶ Ἰησοῦς προέκοπτε σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `TR-Scrivener (1894)`: Καὶ Ἰησοῦς προέκοπτε σοφίᾳ καὶ ἡλικίᾳ, καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `TR-Boyd (Elz/Scr/Steph)`: Καὶ Ἰησοῦς προέκοπτε σοφίᾳ καὶ ἡλικίᾳ, καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `TR-Stephanus (1550)`: καὶ Ἰησοῦς προέκοπτε σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ Θεῷ καὶ ἀνθρώποις.
  - `TR-Elzevir (1624)`: και ιησους προεκοπτεν σοφια και ηλικια και χαριτι παρα θεω και ανθρωποις
  - `A (02)`: και ισ̅ προεκοπτεν σοφια και ηλικια και χαριτι παρα θω̅ και ανοισ̅
  - `C (04)`: και ισ̅ προεκοπτεν σοφια και ηλικια και χαριτι παρα θω̅ και ανοισ̅
  - `W (032)`: και ο ισ̅ προεκοπτεν τη σοφια και ηλικια και χαριτι παρα θω̅ και ανθρωποισ
  - `33`: και ις̅ προεκοπτεν σοφια και ηλικια και χαριτι παρα θω̅ και ανοις̅
  - `L (019)`: και ις̅ προεκοπτεν εν τη ηλικια και σοφια και χαριτι παρα θω̅ και ανοις̅
  - `D (05)`: και ιησ̅ προεκοπται ηλικια και σοφια και χαριτι παρα θω̅ και παρα ανθρωποισ
  - `Θ (038)`: και ις̅ προεκοπτεν σοφια και ηλικια και χαριτι παρα θω̅ και ανοις̅
  - `1 (f¹)`: και ις̅ προεκοπτεν σοφια και ηλικια και χαριτι παρα θω̅ και ανοις̅
  - `13 (f¹³)`: και ις̅ προεκοπτε σοφια και ηλικια και χαριτι παρα θω̅ και ανοις̅
- **Philological Rationale:** [Addition / omission between witnesses] Adopted 'om.' [B (03), SRGNT, SBLGNT, Nestle1904, BHP, RP2018 (Byz), TR (KJTR)] (weight 6.09, confidence 99%) over ο (א (01)). [Addition / omission between witnesses] Adopted 'τῇ' [B (03), SRGNT, BHP] (weight 2.81, confidence 66%) over om. (SBLGNT, RP2018 (Byz), TR (KJTR)); ἐν τῇ (א (01), Nestle1904). [Variation unit spanning several words] Adopted 'παρὰ θεῷ' [B (03), SRGNT, Nestle1904, BHP, TR (KJTR), SBLGNT, RP2018 (Byz)] (weight 5.97, confidence 99%) over θυ̅ (= θυ) (א (01)). Also normalised 10 orthographic/surface variation(s).
- *confidence:* Verse confidence 65% = product of 3 unit confidence(s); calibrated on the Greek NT (probability that a modern critical edition agrees, fitted with a whole stream of witnesses held out).
