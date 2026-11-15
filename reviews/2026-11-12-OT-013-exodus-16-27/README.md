# OT-013: Exodus 16–27

All **345 inherited units** have individualized provisional comparisons against the publisher's Rahlfs–Hanhart 2006 running Greek. **Two revisions are proposed, 343 units are retained provisionally, and none is accepted.** Original book files are untouched.

The proposed candidates are:

- **Exodus 16:14:** “there on the surface” becomes “behold, on the surface,” making the presentation marker explicit. The note acknowledges that inherited “there” already conveys part of its deictic function; this is a fidelity/register proposal, not proof of an error.
- **Exodus 24:12:** “which I have written to give them as law” becomes “which I have written to establish as law for them,” representing the dative recipients of the legislating verb. The appositional relation of tablets, law and commandments remains for fuller review.

Every unit has an authored, construction-focused close working draft, complete spoken/literary candidate, passage-specific Greek analysis, exact inherited text and stable anchor, candidate SHA-256, and honest review status. The close drafts highlight selected clause relationships; they are not complete token alignments. Retained candidates remain provisional, particularly where a record explicitly identifies difficult syntax or terminology. There is no claim of human read-aloud, independent human Greek expertise, apparatus consultation, editorial acceptance or publication.

The source numbering is preserved: **25:6 is absent**, the commandment order at **20:13–15** remains adultery/theft/murder, and **21:37** remains in chapter 21. Chapter counts are 36, 16, 27, 25, 26, 37, 30, 33, 18, 39, 37 and 21. There are no inherited poetic units in this scope.

Source-specific readings retained include the golden jar and Phoenicia in chapter 16, the hidden hand at 17:16, hating arrogance at 18:21, the Lord's departure at 19:22, thirty silver didrachmas at 21:32, the formed/unformed distinction at 21:22–23, the extended covenant wording at 23:22, seeing God's place at 24:10, appearing at 25:8, the pure-gold table at 25:23, nut-shaped bowls, and the veil screening the ark at 26:34. Ancient laws are translated as their source states them; these records do not supply contemporary legal rulings or medical conclusions.

Important unresolved issues include 18:11's pronouns, 21:17's sale/finding sequence, 22:2's liability/insolvency subject shift, 23:21's messenger language, and numerous technical construction terms. The court's wind directions and explicit **15-, 20- and 5-cubit heights** are preserved rather than silently harmonized. The repeated “hundred upon hundred / fifty upon fifty” construction at 27:18 may refer to corresponding sides; inherited “by” is flagged as potentially misleading. `number-audit.json` records focused numerical observations without claiming a complete engineering reconstruction.

`sources.json` records full source access for all twelve chapters. All chapter ends were visible in the publisher responses; the initially truncated bulk inherited-English read was completed in smaller chapter groups. No lexicon or apparatus was consulted for this batch, and no full Greek critical text is redistributed.

Rebuild from the repository root:

```powershell
python reviews/2026-11-12-OT-013-exodus-16-27/build_reviews.py
```

The builder pins baseline commit `39a2bb990f252f9c867879f14942b200c4a86aa5`, verifies scoped original data against it, and writes UTF-8 JSON with LF newlines. `validation.json` records coverage, identity, numbering, draft and status checks. Candidate hashes and LF endings were independently checked after generation.

Publisher sources, accessed 12 November 2026: [Exodus 16](https://www.die-bibel.de/en/bible/LXX/EXO.16), [17](https://www.die-bibel.de/en/bible/LXX/EXO.17), [18](https://www.die-bibel.de/en/bible/LXX/EXO.18), [19](https://www.die-bibel.de/en/bible/LXX/EXO.19), [20](https://www.die-bibel.de/en/bible/LXX/EXO.20), [21](https://www.die-bibel.de/en/bible/LXX/EXO.21), [22](https://www.die-bibel.de/en/bible/LXX/EXO.22), [23](https://www.die-bibel.de/en/bible/LXX/EXO.23), [24](https://www.die-bibel.de/en/bible/LXX/EXO.24), [25](https://www.die-bibel.de/en/bible/LXX/EXO.25), [26](https://www.die-bibel.de/en/bible/LXX/EXO.26), [27](https://www.die-bibel.de/en/bible/LXX/EXO.27).
