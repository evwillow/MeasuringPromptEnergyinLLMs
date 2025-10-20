import os
import sys
import json
import argparse
from pathlib import Path
from datasets import load_dataset, disable_caching
from huggingface_hub import login

try:
    import orjson
    def dumps(x): return orjson.dumps(x).decode()
except Exception:
    def dumps(x): return json.dumps(x, separators=(',', ':'))

def load_token():
    t = os.getenv("HUGGINGFACE_HUB_TOKEN")
    if t: return t
    p = Path(".env")
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("HUGGINGFACE_HUB_TOKEN=") and not line.lstrip().startswith("#"):
                return line.split("=", 1)[1].strip()
    sys.stderr.write("Set HUGGINGFACE_HUB_TOKEN or add it to .env\n")
    sys.exit(1)

def progress(i, n):
    if not n: return
    k = 40
    bar = "=" * int(k * i / n) + "-" * (k - int(k * i / n))
    sys.stdout.write(f"\r[{bar}] {i:,}/{n:,} ({100*i/n:4.1f}%)")
    sys.stdout.flush()

def stream(sample_size, out_path, split, step):
    disable_caching()
    login(token=load_token())
    ds = load_dataset("lmsys/lmsys-chat-1m", split=split, streaming=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wrote = 0
    with open(out_path, "w", encoding="utf-8", buffering=1_048_576) as f:
        for wrote, ex in enumerate(ds, 1):
            f.write(dumps(ex) + "\n")
            if wrote % step == 0: progress(wrote, sample_size)
            if wrote >= sample_size: break
    progress(sample_size, sample_size); print()
    return wrote

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=1_000_000)
    ap.add_argument("--out", type=Path, default=Path("data/conversations.jsonl"))
    ap.add_argument("--split", type=str, default="train")
    ap.add_argument("--progress-every", type=int, default=50_000)
    a = ap.parse_args()
    n = stream(a.samples, a.out, a.split, a.progress_every)
    print(f"Wrote {n:,} lines → {a.out}")

if __name__ == "__main__":
    main()
