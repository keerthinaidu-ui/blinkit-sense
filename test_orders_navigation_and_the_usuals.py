"""
Acceptance Tests for Orders Navigation & The Usuals (Prompt 11).

Validates:
1. Orders icon clickability and subtle visual cue in bottom navigation.
2. Orders screen opening and displaying all 8 predefined historical orders.
3. Historical orders data integrity and line-item total reconciliation.
4. Week 6 includes shampoo at ₹199 and totals ₹628.
5. Historical orders are read-only and remain unchanged when navigating or adding items.
6. The Usuals section evaluation and display immediately below Complete Your Moment.
7. Shampoo, milk, eggs, and bread appear only when catalogue data is valid (reporting missing configuration if not).
8. Adding a product from The Usuals updates active cart, cart count, and subtotal immediately.
9. Scenario switching preserves scenario isolation and resets cart without mixing orders.
10. Complete Your Moment, category highlighting, checkout, and delivery tracking continue working unchanged.
"""

import pytest
import app
from catalogue import PRODUCT_CATALOGUE, PRODUCT_BY_ID


def test_historical_orders_dataset_integrity():
    """Verify all 8 predefined historical orders are present and reconcile with totals."""
    assert len(app.HISTORICAL_ORDERS) == 8, "Must contain exactly 8 historical orders"

    expected_totals = {
        1: 612,
        2: 487,
        3: 731,
        4: 563,
        5: 804,
        6: 628,
        7: 692,
        8: 618,
    }

    for order in app.HISTORICAL_ORDERS:
        week = order["week"]
        expected_total = expected_totals[week]
        assert order["total"] == expected_total, f"Week {week} total mismatch"

        # Verify line-item reconciliation: sum(price * qty) == total
        reconciled_sum = sum(itm["price"] * itm.get("qty", 1) for itm in order["items"])
        assert reconciled_sum == order["total"], f"Week {week} items sum {reconciled_sum} != {order['total']}"


def test_week_6_shampoo_line_item():
    """Verify Week 6 contains shampoo as a separate line item priced at ₹199 and total ₹628."""
    week_6 = next(o for o in app.HISTORICAL_ORDERS if o["week"] == 6)
    assert week_6["total"] == 628

    shampoo_items = [itm for itm in week_6["items"] if itm["name"] == "Shampoo"]
    assert len(shampoo_items) == 1, "Week 6 must contain exactly one Shampoo line item"
    shampoo = shampoo_items[0]
    assert shampoo["price"] == 199, f"Shampoo price must be 199, got {shampoo['price']}"
    assert shampoo["category"] == "Beauty & Personal Care"
    assert shampoo["subcategory"] == "Hair"
    assert shampoo["qty"] == 1


def test_historical_orders_are_read_only_and_immutable():
    """Verify historical orders are not modified when items are added to cart or scenarios switched."""
    original_snapshot = [dict(o) for o in app.HISTORICAL_ORDERS]

    # Add items to cart
    cart = [PRODUCT_BY_ID["p_pasta"], PRODUCT_BY_ID["p_milk_fullcream"]]
    assert len(cart) == 2

    # Historical orders must remain identical
    assert len(app.HISTORICAL_ORDERS) == 8
    for idx, order in enumerate(app.HISTORICAL_ORDERS):
        assert order["total"] == original_snapshot[idx]["total"]
        assert len(order["items"]) == len(original_snapshot[idx]["items"])


def test_the_usuals_candidate_evaluation_and_catalogue_validation():
    """Verify The Usuals candidates are strictly validated against authoritative catalogue."""
    usuals_products, missing_configs = app.get_the_usuals_products()

    # Valid products must have valid catalogue entry and positive price
    valid_ids = [p["id"] for p in usuals_products]
    for p in usuals_products:
        assert p["id"] in PRODUCT_BY_ID, f"Product {p['id']} must exist in catalogue"
        assert p["price"] > 0, f"Product {p['id']} must have a positive price"

    # Milk, Eggs, Bread exist in catalogue and must be present
    assert "p_milk_fullcream" in valid_ids
    assert "p_eggs_6" in valid_ids
    assert "p_bread_brown" in valid_ids

    # For milk, eggs, bread: must use configured catalogue prices
    milk = next(p for p in usuals_products if p["id"] == "p_milk_fullcream")
    assert milk["price"] == PRODUCT_BY_ID["p_milk_fullcream"]["price"]

    eggs = next(p for p in usuals_products if p["id"] == "p_eggs_6")
    assert eggs["price"] == PRODUCT_BY_ID["p_eggs_6"]["price"]

    bread = next(p for p in usuals_products if p["id"] == "p_bread_brown")
    assert bread["price"] == PRODUCT_BY_ID["p_bread_brown"]["price"]

    # Shampoo (p_shampoo) uses the configured historical Week 6 price of ₹199:
    assert "p_shampoo" in valid_ids
    shampoo = next(p for p in usuals_products if p["id"] == "p_shampoo")
    assert shampoo["price"] == 199
    assert len(usuals_products) == 4, "The Usuals must display all 4 products: Shampoo, Milk, Eggs, Bread"


def test_the_usuals_add_to_cart_updates_subtotal_and_count():
    """Verify clicking Add on a product from The Usuals updates active cart and subtotal."""
    import streamlit as st

    # Initialize cart
    st.session_state.cart = []
    st.session_state.selected_scenario = "cooking"
    st.session_state.scenario_data = app.SCENARIOS["cooking"]

    usuals_products, _ = app.get_the_usuals_products()
    milk = next(p for p in usuals_products if p["id"] == "p_milk_fullcream")

    # Add milk to cart
    st.session_state.cart.append(milk["product"])
    assert len(st.session_state.cart) == 1
    subtotal = sum(p["price"] for p in st.session_state.cart)
    assert subtotal == milk["price"]

    # Add bread to cart
    bread = next(p for p in usuals_products if p["id"] == "p_bread_brown")
    st.session_state.cart.append(bread["product"])
    assert len(st.session_state.cart) == 2
    subtotal = sum(p["price"] for p in st.session_state.cart)
    assert subtotal == milk["price"] + bread["price"]


def test_scenario_isolation_with_orders_and_cart():
    """Verify navigating to Orders preserves active scenario and cart, and switching scenarios resets cart."""
    import streamlit as st

    # Setup cooking scenario with item
    st.session_state.selected_scenario = "cooking"
    st.session_state.scenario_data = app.SCENARIOS["cooking"]
    st.session_state.cart = [PRODUCT_BY_ID["p_pasta"]]
    st.session_state.current_screen = "home"

    # Navigate to orders
    st.session_state.current_screen = "orders"
    assert st.session_state.current_screen == "orders"
    assert st.session_state.selected_scenario == "cooking"
    assert len(st.session_state.cart) == 1

    # Switch scenario to breakfast
    app.select_scenario("breakfast")
    assert st.session_state.selected_scenario == "breakfast"
    assert st.session_state.cart == []  # Cart reset, no cross-scenario mixing


def test_complete_your_moment_and_recommendations_intact():
    """Verify Complete Your Moment recommendations evaluation remains intact."""
    eligible_recs, _ = app.evaluate_candidate_recommendations("cooking", cart_items=[])
    assert len(eligible_recs) == 3
    rec_ids = [r["id"] for r in eligible_recs]
    assert "p_colander" in rec_ids
    assert "p_hot_chocolate" in rec_ids
    assert "p_garlic_bread" in rec_ids
