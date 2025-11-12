import os
from pathlib import Path

data_dir = Path("data")

for split in ["train", "val", "test"]:
    folder = data_dir / split
    if not folder.exists():
        print(f"❌ {split} folder missing!")
        continue

    classes = [d.name for d in folder.iterdir() if d.is_dir()]
    print(f"\n📂 {split.upper()} SET:")
    for c in classes:
        images = list((folder / c).glob("*"))
        print(f" - {c}: {len(images)} images")

print("\n✅ Dataset structure check complete.")
