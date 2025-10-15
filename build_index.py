import json, os, pathlib, subprocess, sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent
LIB = ROOT / "library"
OUT = ROOT / "index.json"

def git_last_modified(path: pathlib.Path) -> str:
    try:
        # ISO 8601 commit date (author or committer date). Use %cI for strict ISO 8601.
        ts = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            cwd=str(ROOT)
        ).decode().strip()
        if ts:
            return ts
    except Exception:
        pass
    # Fallback to current UTC time
    return datetime.now(timezone.utc).isoformat()

def main():
    docs = []
    for p in sorted(LIB.glob("*.docx")):
        size = p.stat().st_size
        lm = git_last_modified(p)
        docs.append({
            "name": p.name,
            "stem": p.stem,
            "size_bytes": size,
            "last_modified": lm,
            "url": f"./library/{p.name}"
        })
    with OUT.open("w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)
    print(f"Wrote {OUT} with {len(docs)} items.")

if __name__ == "__main__":
    main()
