"""Independent checks of generated review identities, hashes and unchanged originals."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASELINE = "39a2bb990f252f9c867879f14942b200c4a86aa5"
data = json.loads((HERE / "focused-reviews.json").read_text(encoding="utf-8"))
baseline = json.loads(subprocess.check_output(["git", "show", BASELINE + ":exodus/verses.json"], cwd=ROOT))
units = [(str(c["chapter"]), v) for c in baseline["chapters"] if 16 <= c["chapter"] <= 27 for v in c["verses"]]
assert len(data["records"]) == len(units) == 345
for record, (chapter, verse) in zip(data["records"], units):
    assert (record["reference"], record["verse_anchor"], record["reading_section_id"], record["baseline_text"]) == (verse["reference"], verse["id"], chapter, verse["text"])
    assert record["candidate_sha256"] == hashlib.sha256(record["candidate_text"].encode("utf-8")).hexdigest()
    assert record["decision"] == ("propose_revision" if record["candidate_text"] != verse["text"] else "retain_provisionally")
    assert record["drafts"]["spoken"] == record["drafts"]["literary"] == record["candidate_text"]
    assert record["review"]["all_tokens_accounted_for"] is False
    assert all(record["review"][key] is None for key in ("independent_greek", "human_read_aloud", "editorial_acceptance"))
    assert record["source"]["running_text_read"] is True
    assert record["source"]["apparatus_consulted"] is False
    assert all(value is None for value in record["publication"].values())
    assert record["candidate_text"].count("“") == verse["text"].count("“")
    assert record["candidate_text"].count("”") == verse["text"].count("”")
assert not subprocess.check_output(["git", "diff", BASELINE, "--", "exodus/verses.json"], cwd=ROOT)
assert all(b"\r" not in path.read_bytes() for path in HERE.iterdir() if path.is_file())
assert [r["reference"] for r in data["records"] if r["decision"] == "propose_revision"] == ["Exodus 16:14", "Exodus 24:12"]
print("PASS: 345 identities, candidate hashes, quote preservation, provisional status, LF, and unchanged Exodus original.")
