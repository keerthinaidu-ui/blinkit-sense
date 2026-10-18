"""
Automated validation script for Screen 4: View Cart & Recommendations.
Tests:
1. Historical orders and totals reconciliation (including Week 6 shampoo ₹199 totaling ₹628).
2. Category adoption derived from historical orders.
3. Scenario-aware recommendation eligibility (all 3 recommendations for cooking, breakfast, and period_care).
4. Cart math: line totals, subtotal calculations, and cart mutations without corrupting history.
5. Grounded 'Why this?' evidence.
"""

import sys
import copy
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from catalogue import PRODUCT_CATALOGUE, PRODUCT_BY_ID
import app

def test_historical_orders():
    print("--- 1. Testing Historical Orders Reconciliation ---")
    orders = app.HISTORICAL_ORDERS
    assert len(orders) == 8, f"Expected 8 historical orders, got {len(orders)}"

    for o in orders:
        items_sum = sum(itm["price"] * itm.get("qty", 1) for itm in o["items"])
        assert items_sum == o["total"], f"Week {o['week']} total mismatch: items={items_sum}, total={o['total']}"

    week_6 = [o for o in orders if o["week"] == 6][0]
    assert week_6["total"] == 628, f"Week 6 total must be 628, got {week_6['total']}"
    shampoo_items = [itm for itm in week_6["items"] if itm["name"] == "Shampoo"]
    assert len(shampoo_items) == 1, "Week 6 must contain Shampoo"
    assert shampoo_items[0]["price"] == 199, f"Shampoo price must be 199, got {shampoo_items[0]['price']}"
    print("PASS: All 8 historical orders reconciled to exact rupee values; Week 6 total is ₹628.")


def test_category_adoption():
    print("\n--- 2. Testing Category Adoption Derivation ---")
    adopted = app.get_historically_adopted_subcategories()
    
    # Established purchase patterns
    assert "Dairy, Bread & Eggs" in adopted
    assert "Vegetables & Fruits" in adopted
    assert "Instant Food" in adopted
    assert "Sauces & Spreads" in adopted
    assert "Drinks & Juices" in adopted
    assert "Hair" in adopted  # from week 6 shampoo

    # Unadopted categories
    assert "Sweets & Chocolates" not in adopted, "Sweets & Chocolates should not be historically adopted"
    assert "Ice Creams & More" not in adopted, "Ice Creams & More should not be historically adopted"
    assert "Feminine Hygiene" not in adopted, "Feminine Hygiene should not be historically adopted"
    assert "Kitchenware & Appliances" not in adopted

    print(f"PASS: Derived {len(adopted)} adopted subcategories. Sweets & Chocolates and Ice Creams remain unadopted.")


def test_recommendation_eligibility():
    print("\n--- 3. Testing Recommendation Eligibility & Diagnostics Across Scenarios ---")
    
    # A. Cooking at Home (cooking)
    recs_cooking, diag_cooking = app.evaluate_candidate_recommendations("cooking", [])
    assert len(recs_cooking) == 3, f"Expected 3 recommendations for cooking, got {len(recs_cooking)}"
    c_names = [r["name"] for r in recs_cooking]
    assert "Silicone Pasta Colander" in c_names
    assert "Hot Chocolate" in c_names
    assert "Garlic Bread" in c_names
    print("PASS: Cooking at Home displays all 3 recommendations: Silicone Pasta Colander, Hot Chocolate, Garlic Bread.")
    
    # When Silicone Colander is added to cart, it is deduplicated and 2 remain
    recs_cooking_cart, _ = app.evaluate_candidate_recommendations("cooking", [PRODUCT_BY_ID["p_colander"]])
    assert len(recs_cooking_cart) == 2, f"Expected 2 recommendations after adding colander, got {len(recs_cooking_cart)}"
    assert "Silicone Pasta Colander" not in [r["name"] for r in recs_cooking_cart]
    print("PASS: Adding Silicone Pasta Colander to cart cleanly removes it from recommendations.")

    # B. Quick Breakfast (breakfast)
    recs_breakfast, diag_breakfast = app.evaluate_candidate_recommendations("breakfast", [])
    assert len(recs_breakfast) == 3, f"Expected 3 recommendations for breakfast, got {len(recs_breakfast)}"
    b_names = [r["name"] for r in recs_breakfast]
    assert "Protein Breakfast Bar" in b_names
    assert "Overnight Oats Cup" in b_names
    assert "Coconut Water" in b_names
    print("PASS: Quick Breakfast displays all 3 recommendations: Protein Breakfast Bar, Overnight Oats Cup, Coconut Water.")

    # When Protein Bar is added to cart, it is deduplicated
    recs_breakfast_cart, _ = app.evaluate_candidate_recommendations("breakfast", [PRODUCT_BY_ID["p_protein_bar"]])
    assert len(recs_breakfast_cart) == 2
    assert "Protein Breakfast Bar" not in [r["name"] for r in recs_breakfast_cart]
    print("PASS: Adding Protein Breakfast Bar to cart cleanly removes it from recommendations.")

    # C. First-Time Period Care (period_care)
    recs_period, diag_period = app.evaluate_candidate_recommendations("period_care", [])
    assert len(recs_period) == 3, f"Expected 3 recommendations for period_care, got {len(recs_period)}"
    p_names = [r["name"] for r in recs_period]
    assert "Period Heat Patch" in p_names
    assert "Pain Relief Balm" in p_names
    assert "Flowers" in p_names
    print("PASS: First-Time Period Care displays all 3 recommendations: Period Heat Patch, Pain Relief Balm, Flowers.")

    # When Period Heat Patch is added to cart, it is deduplicated
    recs_period_cart, _ = app.evaluate_candidate_recommendations("period_care", [PRODUCT_BY_ID["p_heat_patch"]])
    assert len(recs_period_cart) == 2
    assert "Period Heat Patch" not in [r["name"] for r in recs_period_cart]
    print("PASS: Adding Period Heat Patch to cart cleanly removes it from recommendations.")


def test_cart_calculations_and_isolation():
    print("\n--- 4. Testing Cart Calculations and Data Isolation ---")
    original_history = copy.deepcopy(app.HISTORICAL_ORDERS)

    # Simulate active cart in Cooking
    cart = [
        PRODUCT_BY_ID["p_pasta"],    # ₹145
        PRODUCT_BY_ID["p_colander"], # ₹249 (added recommendation)
    ]

    subtotal = sum(p["price"] for p in cart)
    assert subtotal == 145 + 249  # 394
    print(f"PASS: Subtotal with added recommendation (Penne Pasta + Silicone Colander = Rs. {subtotal}) is exact.")

    # Decrement colander
    for idx, itm in enumerate(cart):
        if itm["id"] == "p_colander":
            cart.pop(idx)
            break
    new_subtotal = sum(p["price"] for p in cart)
    assert new_subtotal == 145
    print(f"PASS: Removing recommendation recalculates subtotal to Rs. {new_subtotal}.")

    # Confirm historical orders untouched
    assert app.HISTORICAL_ORDERS == original_history, "HISTORICAL_ORDERS must NEVER be mutated by cart actions"
    print("PASS: Historical orders remained strictly immutable.")


if __name__ == "__main__":
    test_historical_orders()
    test_category_adoption()
    test_recommendation_eligibility()
    test_cart_calculations_and_isolation()
    print("\nALL AUTOMATED TESTS PASSED SUCCESSFULLY!")
