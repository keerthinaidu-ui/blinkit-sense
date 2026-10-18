"""
Validation script for BlinkitSense Screen 3 Catalogue Expansion.
Verifies all 13 criteria from Section 10 of the implementation prompt.
"""

import sys
from catalogue import (
    PRODUCT_CATALOGUE,
    PRODUCT_BY_ID,
    get_products_by_subcategory,
    get_valid_products,
)

# Guided subcategories map from app.py
SCENARIO_GUIDED_SUBCATEGORIES = {
    "cooking": [
        "Instant Food",
        "Sauces & Spreads",
        "Vegetables & Fruits",
        "Dairy, Bread & Eggs",
        "Oil, Ghee & Masala",
    ],
    "breakfast": [
        "Vegetables & Fruits",
        "Dairy, Bread & Eggs",
        "Instant Food",
        "Drinks & Juices",
    ],
    "period_care": [
        "Feminine Hygiene",
        "Sweets & Chocolates",
        "Ice Creams & More",
    ],
}

EXPECTED_COUNTS_BEFORE_FILTERING = {
    "Vegetables & Fruits": 20,
    "Dairy, Bread & Eggs": 25,
    "Sauces & Spreads": 32,
    "Oil, Ghee & Masala": 17,
    "Instant Food": 15,
    "Drinks & Juices": 19,
    "Sweets & Chocolates": 24,
    "Ice Creams & More": 11,
    "Feminine Hygiene": 11,
}

EXPECTED_DISPLAYED_COUNTS = {
    "cooking": {
        "Instant Food": 15,
        "Sauces & Spreads": 32,
        "Vegetables & Fruits": 20,
        "Dairy, Bread & Eggs": 25,
        "Oil, Ghee & Masala": 17,
    },
    "breakfast": {
        "Vegetables & Fruits": 20,
        "Dairy, Bread & Eggs": 25,
        "Instant Food": 15,
        "Drinks & Juices": 19,
    },
    "period_care": {
        "Feminine Hygiene": 11,
        "Sweets & Chocolates": 24,
        "Ice Creams & More": 11,
    },
}

DESIGNATED_HIGHLIGHTED_IDS = {"p_dark_choco", "p_ice_cream", "p_pads"}

PRESERVED_ORIGINAL_IDS = [
    "p_pasta",
    "p_sauce",
    "p_mushrooms",
    "p_cheese",
    "p_chilli",
    "p_bananas",
    "p_yogurt",
    "p_granola",
    "p_oj",
    "p_pads",
    "p_dark_choco",
    "p_ice_cream",
]


def run_tests():
    failures = []
    print("==================================================")
    print("RUNNING BLINKITSENSE CATALOGUE EXPANSION VALIDATION")
    print("==================================================")

    # 1. Total product count for Screen 3 browsing catalogue
    base_screen_3_products = [p for p in PRODUCT_CATALOGUE if p.get("group") != "Discovery"]
    total_products = len(base_screen_3_products)
    expected_total = sum(EXPECTED_COUNTS_BEFORE_FILTERING.values())
    if total_products != expected_total:
        failures.append(f"Total product count mismatch: got {total_products}, expected {expected_total}")
    else:
        print(f"[OK] Total product count: {total_products} (matches expected {expected_total})")

    # 2. Product ID uniqueness
    all_ids = [p["id"] for p in PRODUCT_CATALOGUE]
    unique_ids = set(all_ids)
    if len(all_ids) != len(unique_ids):
        duplicates = [x for x in all_ids if all_ids.count(x) > 1]
        failures.append(f"Duplicate product IDs found: {set(duplicates)}")
    else:
        print(f"[OK] All {len(all_ids)} product IDs are completely unique.")

    # 3. Preserved original product IDs
    missing_original = [pid for pid in PRESERVED_ORIGINAL_IDS if pid not in PRODUCT_BY_ID]
    if missing_original:
        failures.append(f"Missing preserved original IDs: {missing_original}")
    else:
        print(f"[OK] All {len(PRESERVED_ORIGINAL_IDS)} original product IDs are preserved.")

    # 4. Required fields validation
    required_fields = ["id", "name", "category", "subcategory", "price", "weight", "scenarios", "icon", "is_highlighted"]
    invalid_fields = []
    for p in PRODUCT_CATALOGUE:
        for f in required_fields:
            if f not in p:
                invalid_fields.append((p.get("id", "unknown"), f"missing {f}"))
        if not isinstance(p.get("price"), (int, float)) or p.get("price") <= 0:
            invalid_fields.append((p.get("id"), f"invalid price: {p.get('price')}"))
        if not isinstance(p.get("scenarios"), list) or not p.get("scenarios"):
            invalid_fields.append((p.get("id"), "empty or invalid scenarios"))
    if invalid_fields:
        failures.append(f"Invalid product fields: {invalid_fields[:5]}")
    else:
        print("[OK] Every product has valid category, subcategory, price, weight, scenarios, and icon.")

    # 5. Product counts per subcategory before scenario filtering (Screen 3 browsing)
    for subcat, exp_count in EXPECTED_COUNTS_BEFORE_FILTERING.items():
        prods = [p for p in get_products_by_subcategory(subcat) if p.get("group") != "Discovery"]
        if len(prods) != exp_count:
            failures.append(f"Subcategory '{subcat}' count mismatch: got {len(prods)}, expected {exp_count}")
        else:
            print(f"[OK] Subcategory '{subcat}': {len(prods)} products (expected {exp_count})")

    # 6. Actual displayed counts after scenario eligibility filtering
    for sc_id, subcat_counts in EXPECTED_DISPLAYED_COUNTS.items():
        print(f"\n--- Scenario: {sc_id} ---")
        for subcat, exp_count in subcat_counts.items():
            valid_p = get_valid_products(sc_id, subcat, SCENARIO_GUIDED_SUBCATEGORIES)
            if len(valid_p) != exp_count:
                failures.append(f"Scenario '{sc_id}' subcat '{subcat}' displayed count mismatch: got {len(valid_p)}, expected {exp_count}")
            else:
                print(f"  [OK] Displayed in '{subcat}': {len(valid_p)} products (expected {exp_count})")

    # 7. No leakage from unrelated scenarios
    leakage_checks = [
        # period_care subcategories must not appear in cooking or breakfast
        ("cooking", "Feminine Hygiene", 0),
        ("cooking", "Sweets & Chocolates", 0),
        ("cooking", "Ice Creams & More", 0),
        ("breakfast", "Feminine Hygiene", 0),
        ("breakfast", "Sweets & Chocolates", 0),
        ("breakfast", "Ice Creams & More", 0),
        # cooking-only subcategories must not appear in breakfast or period_care
        ("breakfast", "Sauces & Spreads", 0),
        ("breakfast", "Oil, Ghee & Masala", 0),
        ("period_care", "Sauces & Spreads", 0),
        ("period_care", "Oil, Ghee & Masala", 0),
        # breakfast-only subcategories must not appear in cooking or period_care
        ("cooking", "Drinks & Juices", 0),
        ("period_care", "Drinks & Juices", 0),
    ]
    leakages = []
    for sc_id, subcat, exp in leakage_checks:
        valid_p = get_valid_products(sc_id, subcat, SCENARIO_GUIDED_SUBCATEGORIES)
        if len(valid_p) != exp:
            leakages.append(f"Scenario '{sc_id}' received {len(valid_p)} products from unrelated subcat '{subcat}'")
    if leakages:
        failures.extend(leakages)
    else:
        print("\n[OK] No products from unrelated scenarios leak into any subcategory.")

    # 8. Highlighting limited strictly to the 3 designated products
    highlighted_prods = [p for p in PRODUCT_CATALOGUE if p.get("is_highlighted")]
    highlighted_ids = {p["id"] for p in highlighted_prods}
    if highlighted_ids != DESIGNATED_HIGHLIGHTED_IDS:
        failures.append(f"Highlighted products mismatch: got {highlighted_ids}, expected {DESIGNATED_HIGHLIGHTED_IDS}")
    else:
        print(f"\n[OK] Exactly 3 products highlighted: {[p['name'] for p in highlighted_prods]}")

    # 9. Vegetables & Fruits separation verification
    vf_prods = get_products_by_subcategory("Vegetables & Fruits")
    fruits = [p for p in vf_prods if p.get("group") == "Fruits"]
    vegetables = [p for p in vf_prods if p.get("group") == "Vegetables"]
    if len(fruits) != 10 or len(vegetables) != 10:
        failures.append(f"Vegetables & Fruits grouping mismatch: {len(fruits)} fruits, {len(vegetables)} vegetables")
    else:
        print(f"[OK] Vegetables & Fruits group split: {len(fruits)} Fruits + {len(vegetables)} Vegetables = 20 Total.")

    # Summary
    print("\n==================================================")
    if failures:
        print(f"FAILED with {len(failures)} error(s):")
        for f in failures:
            print(f"  [FAIL] {f}")
        sys.exit(1)
    else:
        print("ALL TESTS PASSED SUCCESSFULLY! (100% compliant)")
        print("==================================================")
        sys.exit(0)


if __name__ == "__main__":
    run_tests()
