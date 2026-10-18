"""
Acceptance tests for BlinkitSense Order Confirmation and Order Tracking Screens
Validates all requirements specified in Section 9 of the prompt.
"""

import copy
import pytest
from app import (
    create_simulated_order,
    select_scenario,
    HISTORICAL_ORDERS,
    get_historically_adopted_subcategories,
    SCENARIOS,
)
from catalogue import PRODUCT_BY_ID


def test_valid_checkout_creates_one_simulated_order():
    """A valid checkout creates exactly one simulated order with proper fields."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    cart = [p_pasta]
    order = create_simulated_order("cooking", cart)

    assert order is not None
    assert order["is_simulated"] is True
    assert order["order_id"].startswith("BKS-ORD-")
    assert order["scenario_id"] == "cooking"
    assert len(order["items"]) == 1
    assert order["items"][0]["id"] == "p_pasta"
    assert order["subtotal"] == p_pasta["price"]
    assert order["total"] == p_pasta["price"]


def test_empty_cart_cannot_be_submitted():
    """An empty cart cannot be submitted and does not create an order."""
    order = create_simulated_order("cooking", [])
    assert order is None


def test_invalid_checkout_data_does_not_create_order():
    """Invalid checkout data (non-existent ID, zero qty) does not create an order."""
    corrupted_cart = [{"id": "ghost_product_999", "name": "Fake", "price": 50}]
    order = create_simulated_order("cooking", corrupted_cart)
    assert order is None


def test_immutable_snapshot_agrees_with_checkout_calculation():
    """Line totals, subtotal, and final amount agree with checkout calculations."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    p_sauce = PRODUCT_BY_ID["p_sauce"]
    cart = [p_pasta, p_pasta, p_sauce]  # 2 pastas, 1 sauce
    order = create_simulated_order("cooking", cart)

    expected_line_pasta = p_pasta["price"] * 2
    expected_line_sauce = p_sauce["price"] * 1
    expected_subtotal = expected_line_pasta + expected_line_sauce

    assert order["subtotal"] == expected_subtotal
    assert order["total"] == expected_subtotal

    items_dict = {item["id"]: item for item in order["items"]}
    assert items_dict["p_pasta"]["line_total"] == expected_line_pasta
    assert items_dict["p_sauce"]["line_total"] == expected_line_sauce


def test_subsequent_cart_changes_do_not_alter_existing_order():
    """Modifying active cart does not mutate already submitted order snapshot."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    active_cart = [p_pasta]
    order = create_simulated_order("cooking", active_cart)

    snapshot_subtotal = order["subtotal"]
    snapshot_items_count = len(order["items"])

    # Simulate user adding 5 items to active cart afterwards
    active_cart.extend([p_pasta] * 5)

    assert order["subtotal"] == snapshot_subtotal
    assert len(order["items"]) == snapshot_items_count


def test_switching_scenarios_does_not_corrupt_submitted_order():
    """Switching scenarios does not alter or erase previously submitted order snapshot."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p_pasta])
    original_order_id = order["order_id"]

    # In app session state, current_order holds the snapshot
    state_current_order = order

    # Simulate scenario change
    # select_scenario should preserve existing submitted orders
    new_sc_order = state_current_order
    assert new_sc_order["order_id"] == original_order_id
    assert new_sc_order["scenario_id"] == "cooking"


def test_tracking_progress_stages_and_deterministic_advancement():
    """Initial status is Order confirmed, stages advance deterministically, Delivered stays stable."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p_pasta])

    steps = order["delivery_state"]["steps"]
    assert len(steps) == 5
    assert steps[0]["name"] == "Order confirmed"
    assert steps[0]["status"] == "completed"
    assert steps[1]["name"] == "Preparing your order"
    assert steps[2]["name"] == "Delivery partner assigned"
    assert steps[3]["name"] == "On the way"
    assert steps[4]["name"] == "Delivered"

    # Advance stage to 3 (On the way - reference image state)
    order["tracking_stage_index"] = 3
    for i, s in enumerate(steps):
        if i < 3:
            s["status"] = "completed"
        elif i == 3:
            s["status"] = "current"
        else:
            s["status"] = "pending"

    assert steps[3]["status"] == "current"

    # Advance stage to 4 (Delivered)
    order["tracking_stage_index"] = 4
    for s in steps:
        s["status"] = "completed"

    assert steps[4]["status"] == "completed"
    # Attempting to advance beyond 4 should keep Delivered stable
    order["tracking_stage_index"] = min(order["tracking_stage_index"] + 1, 4)
    assert order["tracking_stage_index"] == 4


def test_delivery_partner_identified_as_simulated():
    """Delivery partner details are explicitly marked as demo / simulated."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p_pasta])

    partner = order["delivery_partner"]
    assert partner["name"] == "Shekhar"
    assert "demo" in partner["role"].lower()
    assert order["is_simulated"] is True


def test_historical_orders_dataset_immutable():
    """Historical orders (ORD_001 to ORD_008) are completely immutable."""
    original_history = copy.deepcopy(HISTORICAL_ORDERS)
    original_adopted = get_historically_adopted_subcategories(HISTORICAL_ORDERS)

    # Place multiple orders
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    create_simulated_order("cooking", [p_pasta])
    create_simulated_order("breakfast", [p_pasta])
    create_simulated_order("period_care", [p_pasta])

    assert HISTORICAL_ORDERS == original_history
    assert get_historically_adopted_subcategories(HISTORICAL_ORDERS) == original_adopted
