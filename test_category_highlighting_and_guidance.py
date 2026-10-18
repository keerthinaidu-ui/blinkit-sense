"""
BlinkitSense Acceptance Tests for Scenario-Based Category Highlighting & Animated User Guidance.
Validates all acceptance criteria:
1. Relevant categories and subcategories highlighted in yellow for cooking, breakfast, and period_care.
2. Unrelated categories remain visible, unhighlighted, and retain existing behavior.
3. Guidance accurately points to the correct category, subcategory, and product for the active scenario.
4. Step-by-step progress updating: guidance advances as products are added to cart.
5. Products already in cart are never prompted as needing to be added.
6. Guidance completion: transitions to 'all_added' when all required items are in cart.
7. Switching scenarios updates highlights and guidance without mixing scenario carts.
8. Preservation of recommendations, historical orders, checkout, and catalogue data integrity.
"""

import pytest
import app
from catalogue import PRODUCT_CATALOGUE, PRODUCT_BY_ID


def test_scenario_relevant_categories_and_subcategories():
    """Verify that relevant categories and subcategories are accurately identified for all 3 scenarios."""
    # 1. Cooking at Home
    guidance_cooking = app.get_scenario_guidance("cooking", cart_items=[])
    assert guidance_cooking["guided_categories"] == {"Grocery & Kitchen", "Snacks & Drinks"}
    assert guidance_cooking["guided_subcategories"] == {
        "Instant Food",
        "Sauces & Spreads",
        "Vegetables & Fruits",
        "Dairy, Bread & Eggs",
        "Oil, Ghee & Masala",
    }
    assert guidance_cooking["total_count"] == 5

    # 2. Quick Breakfast
    guidance_bfast = app.get_scenario_guidance("breakfast", cart_items=[])
    assert guidance_bfast["guided_categories"] == {"Grocery & Kitchen", "Snacks & Drinks"}
    assert guidance_bfast["guided_subcategories"] == {
        "Vegetables & Fruits",
        "Dairy, Bread & Eggs",
        "Instant Food",
        "Drinks & Juices",
    }
    assert guidance_bfast["total_count"] == 4

    # 3. Period Care
    guidance_pc = app.get_scenario_guidance("period_care", cart_items=[])
    assert guidance_pc["guided_categories"] == {"Beauty & Personal Care", "Snacks & Drinks"}
    assert guidance_pc["guided_subcategories"] == {
        "Feminine Hygiene",
        "Sweets & Chocolates",
        "Ice Creams & More",
    }
    assert guidance_pc["total_count"] == 3


def test_unrelated_categories_excluded_from_highlights():
    """Verify that categories unrelated to the scenario are not marked as relevant."""
    # Cooking: Beauty & Personal Care and Household Essentials are unrelated
    guidance_cooking = app.get_scenario_guidance("cooking", cart_items=[])
    assert "Beauty & Personal Care" not in guidance_cooking["guided_categories"]
    assert "Household Essentials" not in guidance_cooking["guided_categories"]

    # Breakfast: Beauty & Personal Care and Household Essentials are unrelated
    guidance_bfast = app.get_scenario_guidance("breakfast", cart_items=[])
    assert "Beauty & Personal Care" not in guidance_bfast["guided_categories"]
    assert "Household Essentials" not in guidance_bfast["guided_categories"]

    # Period Care: Grocery & Kitchen and Household Essentials are unrelated
    guidance_pc = app.get_scenario_guidance("period_care", cart_items=[])
    assert "Grocery & Kitchen" not in guidance_pc["guided_categories"]
    assert "Household Essentials" not in guidance_pc["guided_categories"]


def test_initial_guidance_next_step():
    """Verify that guidance initially targets the first required product in the scenario."""
    # Cooking initial target: Penne Pasta in Instant Food
    g_cooking = app.get_scenario_guidance("cooking", cart_items=[])
    assert g_cooking["added_count"] == 0
    assert g_cooking["all_added"] is False
    assert g_cooking["next_step"]["product_id"] == "p_pasta"
    assert g_cooking["next_step"]["subcategory"] == "Instant Food"
    assert g_cooking["next_step"]["category"] == "Snacks & Drinks"

    # Breakfast initial target: Robusta Bananas in Vegetables & Fruits
    g_bfast = app.get_scenario_guidance("breakfast", cart_items=[])
    assert g_bfast["added_count"] == 0
    assert g_bfast["all_added"] is False
    assert g_bfast["next_step"]["product_id"] == "p_bananas"
    assert g_bfast["next_step"]["subcategory"] == "Vegetables & Fruits"
    assert g_bfast["next_step"]["category"] == "Grocery & Kitchen"

    # Period Care initial target: Sanitary Pads in Feminine Hygiene
    g_pc = app.get_scenario_guidance("period_care", cart_items=[])
    assert g_pc["added_count"] == 0
    assert g_pc["all_added"] is False
    assert g_pc["next_step"]["product_id"] == "p_pads"
    assert g_pc["next_step"]["subcategory"] == "Feminine Hygiene"
    assert g_pc["next_step"]["category"] == "Beauty & Personal Care"


def test_step_by_step_guidance_progression_cooking():
    """Verify that guidance advances step-by-step as products are added for cooking scenario."""
    cart = []

    # Step 1: empty cart -> target is p_pasta
    g1 = app.get_scenario_guidance("cooking", cart)
    assert g1["next_step"]["product_id"] == "p_pasta"
    assert g1["added_count"] == 0

    # User adds Penne Pasta
    cart.append(PRODUCT_BY_ID["p_pasta"])
    g2 = app.get_scenario_guidance("cooking", cart)
    assert g2["added_count"] == 1
    assert g2["next_step"]["product_id"] == "p_sauce"
    assert g2["next_step"]["subcategory"] == "Sauces & Spreads"

    # User adds Alfredo Pasta Sauce
    cart.append(PRODUCT_BY_ID["p_sauce"])
    g3 = app.get_scenario_guidance("cooking", cart)
    assert g3["added_count"] == 2
    assert g3["next_step"]["product_id"] == "p_mushrooms"
    assert g3["next_step"]["subcategory"] == "Vegetables & Fruits"

    # User adds Mushrooms
    cart.append(PRODUCT_BY_ID["p_mushrooms"])
    g4 = app.get_scenario_guidance("cooking", cart)
    assert g4["added_count"] == 3
    assert g4["next_step"]["product_id"] == "p_cheese"
    assert g4["next_step"]["subcategory"] == "Dairy, Bread & Eggs"

    # User adds Cheese
    cart.append(PRODUCT_BY_ID["p_cheese"])
    g5 = app.get_scenario_guidance("cooking", cart)
    assert g5["added_count"] == 4
    assert g5["next_step"]["product_id"] == "p_chilli"
    assert g5["next_step"]["subcategory"] == "Oil, Ghee & Masala"

    # User adds Chilli Flakes -> all 5 items added!
    cart.append(PRODUCT_BY_ID["p_chilli"])
    g6 = app.get_scenario_guidance("cooking", cart)
    assert g6["added_count"] == 5
    assert g6["all_added"] is True
    assert g6["next_step"] is None  # Guidance stops pointing to products!


def test_products_already_in_cart_not_prompted():
    """Verify that products already in the cart are skipped in guidance even if added out of order."""
    # User adds p_cheese and p_chilli first
    cart = [PRODUCT_BY_ID["p_cheese"], PRODUCT_BY_ID["p_chilli"]]
    g = app.get_scenario_guidance("cooking", cart)

    assert g["added_count"] == 2
    # The next step must be p_pasta (first missing item), not cheese or chilli
    assert g["next_step"]["product_id"] == "p_pasta"
    assert not any(item["product_id"] in ["p_cheese", "p_chilli"] and not item["is_added"] for item in g["scenario_items"])


def test_switching_scenarios_updates_highlights_and_resets_cart():
    """Verify switching scenario isolates carts and updates highlights."""
    import streamlit as st

    # Initialize session state for scenario selection test
    st.session_state.cart = [PRODUCT_BY_ID["p_pasta"]]
    st.session_state.selected_scenario = "cooking"
    st.session_state.scenario_data = app.SCENARIOS["cooking"]

    # Switch to breakfast
    app.select_scenario("breakfast")
    assert st.session_state.selected_scenario == "breakfast"
    assert st.session_state.cart == []  # Cart reset, no cross-scenario cart contamination

    guidance_bfast = app.get_scenario_guidance(st.session_state.selected_scenario, st.session_state.cart)
    assert guidance_bfast["next_step"]["product_id"] == "p_bananas"
    assert guidance_bfast["guided_subcategories"] == {
        "Vegetables & Fruits",
        "Dairy, Bread & Eggs",
        "Instant Food",
        "Drinks & Juices",
    }


def test_existing_functionality_preserved():
    """Verify that historical orders, recommendations, and catalogue remain intact and untouched."""
    # Historical orders intact
    assert len(app.HISTORICAL_ORDERS) == 8
    adopted = app.get_historically_adopted_subcategories()
    assert "Instant Food" in adopted

    # Authoritative catalogue mappings intact
    assert "p_pasta" in app.SCENARIO_SELECTED_PRODUCTS["cooking"]
    assert "p_bananas" in app.SCENARIO_SELECTED_PRODUCTS["breakfast"]
    assert "p_pads" in app.SCENARIO_SELECTED_PRODUCTS["period_care"]

    # Recommendations evaluation for Screen 4 intact
    eligible_recs, _ = app.evaluate_candidate_recommendations("cooking", cart_items=[])
    assert len(eligible_recs) == 3
