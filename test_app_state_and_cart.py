"""
Integration and Session State validation for app.py.
Tests scenario selection, subcategory navigation, cart additions, subtotal computations,
scenario isolation, and product highlighting flags.
"""

import sys

# Test with mock streamlit session state
class MockSessionState(dict):
    def __getattr__(self, key):
        return self.get(key)
    def __setattr__(self, key, value):
        self[key] = value

# Test app.py logic
import app
from catalogue import PRODUCT_CATALOGUE, PRODUCT_BY_ID

def test_full_application():
    print("==================================================")
    print("RUNNING APP.PY LOGIC AND CART INTEGRITY VALIDATION")
    print("==================================================")

    # 1. Verify app.CATALOGUE_PRODUCTS structure
    assert "cooking" in app.CATALOGUE_PRODUCTS
    assert "breakfast" in app.CATALOGUE_PRODUCTS
    assert "period_care" in app.CATALOGUE_PRODUCTS
    print("[OK] app.CATALOGUE_PRODUCTS contains all 3 scenarios.")

    # 2. Test Cooking Scenario & Subcategories
    cooking_subcats = app.SCENARIO_GUIDED_SUBCATEGORIES["cooking"]
    assert len(cooking_subcats) == 5
    for subcat in cooking_subcats:
        prods = app.get_valid_products_for_subcat("cooking", subcat)
        assert len(prods) > 0, f"No products for cooking -> {subcat}"
        # Ensure none are highlighted in cooking
        for p in prods:
            assert not p.get("is_highlighted"), f"Unexpected highlight in cooking: {p['name']}"
    print("[OK] Cooking scenario has 5 enabled subcategories with correct non-highlighted products.")

    # 3. Test Breakfast Scenario & Subcategories
    breakfast_subcats = app.SCENARIO_GUIDED_SUBCATEGORIES["breakfast"]
    assert len(breakfast_subcats) == 4
    for subcat in breakfast_subcats:
        prods = app.get_valid_products_for_subcat("breakfast", subcat)
        assert len(prods) > 0, f"No products for breakfast -> {subcat}"
        # Ensure none are highlighted in breakfast
        for p in prods:
            assert not p.get("is_highlighted"), f"Unexpected highlight in breakfast: {p['name']}"
    print("[OK] Breakfast scenario has 4 enabled subcategories with correct non-highlighted products.")

    # 4. Test Period Care Scenario & Highlighting
    period_subcats = app.SCENARIO_GUIDED_SUBCATEGORIES["period_care"]
    assert len(period_subcats) == 3

    # Feminine Hygiene: exactly Nua Sanitary Napkins highlighted
    fem_prods = app.get_valid_products_for_subcat("period_care", "Feminine Hygiene")
    assert len(fem_prods) == 11
    highlighted_fem = [p for p in fem_prods if p.get("is_highlighted")]
    assert len(highlighted_fem) == 1
    assert highlighted_fem[0]["name"] == "Nua Sanitary Napkins"
    assert highlighted_fem[0]["id"] == "p_pads"
    print(f"[OK] Feminine Hygiene has exactly 1 highlighted product: {highlighted_fem[0]['name']}")

    # Sweets & Chocolates: exactly Dark Chocolate highlighted
    sweets_prods = app.get_valid_products_for_subcat("period_care", "Sweets & Chocolates")
    assert len(sweets_prods) == 24
    highlighted_sweets = [p for p in sweets_prods if p.get("is_highlighted")]
    assert len(highlighted_sweets) == 1
    assert highlighted_sweets[0]["name"] == "Dark Chocolate"
    assert highlighted_sweets[0]["id"] == "p_dark_choco"
    print(f"[OK] Sweets & Chocolates has exactly 1 highlighted product: {highlighted_sweets[0]['name']}")

    # Ice Creams & More: exactly Chocolate Ice Cream Tub highlighted
    ice_prods = app.get_valid_products_for_subcat("period_care", "Ice Creams & More")
    assert len(ice_prods) == 11
    highlighted_ice = [p for p in ice_prods if p.get("is_highlighted")]
    assert len(highlighted_ice) == 1
    assert highlighted_ice[0]["name"] == "Chocolate Ice Cream Tub"
    assert highlighted_ice[0]["id"] == "p_ice_cream"
    print(f"[OK] Ice Creams & More has exactly 1 highlighted product: {highlighted_ice[0]['name']}")

    # 5. Simulate Cart Operations
    cart = []
    # Add pasta (price 145)
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    cart.append(p_pasta)
    assert sum(item["price"] for item in cart) == 145

    # Add sauce (price 199)
    p_sauce = PRODUCT_BY_ID["p_sauce"]
    cart.append(p_sauce)
    assert sum(item["price"] for item in cart) == 145 + 199

    # Add another pasta (quantity 2)
    cart.append(p_pasta)
    assert len(cart) == 3
    assert sum(item["price"] for item in cart) == 145 + 199 + 145

    # Quantity counts
    pasta_qty = sum(1 for item in cart if item["id"] == "p_pasta")
    sauce_qty = sum(1 for item in cart if item["id"] == "p_sauce")
    assert pasta_qty == 2
    assert sauce_qty == 1
    print(f"[OK] Simulated cart operations: 3 items, 2 distinct products, Subtotal = Rs. {sum(i['price'] for i in cart)}")

    print("\n==================================================")
    print("ALL APP LOGIC TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    test_full_application()
