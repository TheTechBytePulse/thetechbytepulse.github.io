#!/usr/bin/env python3
"""
Auto-rename randomly named product images using local Ollama (gemma4).
Usage: python3 rename_product_images.py
Requires: Ollama running locally with gemma4 model pulled.
"""

import os
import shutil
import base64
import sys
import json
import urllib.request
import warnings
warnings.filterwarnings("ignore")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma4:latest"

PRODUCTS = {
    "desidiya-sunset-lamp.jpg":            "Desidiya 16-Color LED RGB Sunset Lamp",
    "elfora-overhead-phone-holder.jpg":    "Elfora Overhead Mobile Phone Holder long arm",
    "kenbrook-solar-dc-wire.jpg":          "Kenbrook Solar 6mm DC Wire red black 20 meters",
    "kenbrook-solar-branch-connector.jpg": "Kenbrook Solar 2-in-1 MC4 Branch Connector",
    "kenbrook-mc4-connectors.jpg":         "Kenbrook Solar MC4 Connectors pair",
    "proelite-ipad-screen-protector.jpg":  "ProElite Tempered Glass Screen Protector iPad 10.2",
    "amazon-basics-ipad-case.jpg":         "Amazon Basics Trifold iPad Case black",
    "dyazo-laptop-sleeve.jpg":             "Dyazo 13.3 inch Laptop Sleeve black with handle",
    "portronics-gan-charger.jpg":          "Portronics Adapto 45 GaN dual port fast charger",
    "portronics-lightning-cable.jpg":      "Portronics Konnect L Lightning USB cable white",
    "logitech-b170-mouse.jpg":             "Logitech B170 wireless USB mouse black",
    "green-soul-standing-desk.jpg":        "Green Soul Alex height adjustable standing desk",
    "cable-management-tray.jpg":           "Metal Under Desk Cable Management Tray black 42cm",
    "urbanmade-desk-mat.jpg":              "Urbanmade extended desk mat mouse pad large",
    "ruhe-kitchen-sink.jpg":               "Ruhe matte black quartz single bowl kitchen sink",
    "mrmop-spin-mop.jpg":                  "Mr.Mop 360 degree spin mop microfiber floor cleaning",
    "amigos-curtains.jpg":                 "Amigos cotton semi sheer grommet curtains floral",
    "blackdecker-screwdriver.jpg":         "BLACK+DECKER cordless screwdriver set orange",
    "aasons-hole-saw-set.jpg":             "AASONS hole saw drill bit set 6 pieces",
    "bathla-aluminium-ladder.jpg":         "Bathla aluminium step ladder foldable",
    "aarpee-bar-stool.jpg":                "Aarpee revolving height adjustable bar stool pair",
    "gm-extension-board.jpg":             "GM 3060 extension board 4 sockets 2 meter cord",
    "gm-flex-box.jpg":                     "GM 3041 Trio flex box 5 meter copper cord",
    "hit-mosquito-racquet.jpg":            "HIT rechargeable mosquito racquet bat LED",
    "pigeon-electric-kettle.jpg":          "Pigeon Amaze Plus electric kettle stainless steel",
    "philips-hair-dryer.jpg":              "Philips hair dryer 1000W purple",
    "omron-nebulizer.jpg":                 "Omron NE C101 compressor nebulizer",
    "dr-vaku-thermometer.jpg":             "DR VAKU infrared non-contact thermometer",
    "omron-bp-monitor.jpg":                "Omron HEM 7124 blood pressure monitor",
    "accu-chek-glucometer.jpg":            "Accu-Chek Instant S glucometer blood glucose",
    "boniry-folding-saw.jpg":              "Boniry folding saw plant cutter steel blade",
    "garbnoire-water-pipe.jpg":            "Garbnoire PVC garden water pipe hose yellow",
    "foldable-bbq-grill.jpg":              "foldable charcoal barbecue BBQ grill with skewers",
    "robustt-car-bed.jpg":                 "Robustt inflatable car bed back seat air pump",
}

PRODUCTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static/images/products")

def get_unidentified_images():
    # Only process files with random/unknown names (not already correctly named)
    all_correct_names = set(PRODUCTS.keys()) | {"README.md"}
    return sorted([
        f for f in os.listdir(PRODUCTS_DIR)
        if f not in all_correct_names
        and f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ])

def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def ask_ollama(image_path, candidates):
    img_b64 = image_to_base64(image_path)
    product_list_text = "\n".join(f"- {k}: {v}" for k, v in candidates.items())

    prompt = f"""You are a product image identifier. Look at this product image carefully.

Match it to exactly one item from the list below.
Reply with ONLY the exact filename key (e.g. omron-nebulizer.jpg) — no explanation, no punctuation, nothing else.
If you cannot match confidently, reply with exactly: UNKNOWN

Products:
{product_list_text}
"""

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "images": [img_b64],
        "stream": False
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["response"].strip()

def main():
    # Quick connectivity check
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=3)
    except Exception:
        print("ERROR: Ollama is not running. Start it with: ollama serve")
        sys.exit(1)

    unidentified = get_unidentified_images()
    if not unidentified:
        print("✅ No unidentified images found.")
        return

    already_named = set(os.listdir(PRODUCTS_DIR))
    remaining_products = {k: v for k, v in PRODUCTS.items() if k not in already_named}

    if not remaining_products:
        print("✅ All products already have images.")
        return

    print(f"Found {len(unidentified)} unidentified images.")
    print(f"Matching against {len(remaining_products)} remaining products.\n")

    rename_map = {}
    used_targets = set()

    for i, filename in enumerate(unidentified, 1):
        src = os.path.join(PRODUCTS_DIR, filename)
        candidates = {k: v for k, v in remaining_products.items() if k not in used_targets}
        if not candidates:
            print("⚠️  All products matched — stopping.")
            break

        print(f"[{i}/{len(unidentified)}] 🔍 {filename} ...", end=" ", flush=True)
        try:
            result = ask_ollama(src, candidates)
        except Exception as e:
            print(f"❌ Error: {e}")
            rename_map[filename] = None
            continue

        # Clean up result — model sometimes adds quotes or extra text
        result = result.strip().strip('"').strip("'").split("\n")[0].strip()

        if result == "UNKNOWN" or result not in candidates:
            print(f"❓ Unmatched (got: '{result}')")
            rename_map[filename] = None
        else:
            print(f"✅ → {result}")
            rename_map[filename] = result
            used_targets.add(result)

    print("\n" + "─" * 60)
    matched = {k: v for k, v in rename_map.items() if v}
    unmatched = [k for k, v in rename_map.items() if not v]

    print(f"\nRENAME PLAN ({len(matched)} files):")
    for old, new in matched.items():
        print(f"  {old}  →  {new}")

    if unmatched:
        print(f"\nUnmatched ({len(unmatched)} files):")
        for f in unmatched:
            print(f"  {f}")

    if not matched:
        print("Nothing to rename.")
        return

    confirm = input("\nApply renames? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return

    for old, new in matched.items():
        src = os.path.join(PRODUCTS_DIR, old)
        dst = os.path.join(PRODUCTS_DIR, new)
        if os.path.exists(dst):
            print(f"⚠️  {new} already exists — skipping {old}")
            continue
        shutil.move(src, dst)
        print(f"✅ {old} → {new}")

    print("\n🎉 Done! Run this script again if any images are still unmatched.")

if __name__ == "__main__":
    main()
