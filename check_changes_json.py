import subprocess
import json
import datetime
import os

def get_changed_files():
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Git командасын орындау кезінде қате пайда болды.")
        return
    
    lines = result.stdout.strip().split("\n")
    changed = []

    for line in lines:
        if line.strip():
            status = line[0:2].strip()
            filename = line[3:].strip()
            changed.append({"status": status, "file": filename})

    return changed


def save_to_json(data, output_file="changes.json"):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "date": str(datetime.datetime.now()),
            "changed_files": data
        }, f, indent=4, ensure_ascii=False)

    print(f"✅ Өзгерістер JSON файлына сақталды: {output_file}")


if __name__ == "__main__":
    files = get_changed_files()
    if not files:
        print("✅ Өзгерістер табылмады.")
    else:
        save_to_json(files)
