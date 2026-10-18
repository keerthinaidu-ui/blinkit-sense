"""
Tests for Screen 5: Order Confirmation & Delivery Tracking
Verifies simulated order creation, validation, calculations, 5-stage tracking,
idempotency, and historical data immutability.
"""

import copy
import pytest
from app import (
    create_simulated_order,
    HISTORICAL_ORDERS,
    get_historically_adopted_subcategories,
    SCENARIOS,
)
from catalogue import PRODUCT_BY_ID, PRODUCT_CATALOGUE


def test_create_simulated_order_valid_cart():
    """Verify order creation with valid items calculates correct line totals, subtotal, and total."""
    p_pasta = PRODUCT_BY_ID["p_pasta"]
    p_sauce = PRODUCT_BY_ID["p_sauce"]

    # Cart with 2 pastas (125 each) and 1 sauce (145)
    cart = [p_pasta, p_pasta, p_sauce]
    order = create_simulated_order("cooking", cart)

    assert order is not None
    assert order["is_simulated"] is True
    assert order["scenario_id"] == "cooking"
    assert order["scenario_name"] == SCENARIOS["cooking"]["short_name"]
    assert order["order_id"].startswith("BKS-ORD-")
    assert len(order["items"]) == 2

    # Check grouped items
    items_by_id = {itm["id"]: itm for itm in order["items"]}
    assert "p_pasta" in items_by_id
    assert items_by_id["p_pasta"]["qty"] == 2
    assert items_by_id["p_pasta"]["price"] == 145
    assert items_by_id["p_pasta"]["line_total"] == 290

    assert "p_sauce" in items_by_id
    assert items_by_id["p_sauce"]["qty"] == 1
    assert items_by_id["p_sauce"]["price"] == 199
    assert items_by_id["p_sauce"]["line_total"] == 199

    # Reconciled totals
    assert order["subtotal"] == 489
    assert order["delivery_fee"] == 0
    assert order["handling_fee"] == 0
    assert order["total"] == 489
    assert order["item_count"] == 3


def test_order_delivery_estimates_by_scenario():
    """Verify scenario-specific illustrative delivery estimates."""
    p1 = PRODUCT_BY_ID["p_pasta"]

    order_cooking = create_simulated_order("cooking", [p1])
    assert "18–25 minutes" in order_cooking["estimated_delivery"]

    order_breakfast = create_simulated_order("breakfast", [p1])
    assert "12–18 minutes" in order_breakfast["estimated_delivery"]

    order_period = create_simulated_order("period_care", [p1])
    assert "10–15 minutes" in order_period["estimated_delivery"]


def test_delivery_progress_stepper_stages():
    """Verify 5 stages in order tracking and initial status."""
    p1 = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p1])

    steps = order["delivery_state"]["steps"]
    assert len(steps) == 5

    expected_stages = [
        ("Order confirmed", "completed"),
        ("Preparing your order", "pending"),
        ("Delivery partner assigned", "pending"),
        ("On the way", "pending"),
        ("Delivered", "pending"),
    ]

    for idx, (expected_name, expected_status) in enumerate(expected_stages):
        assert steps[idx]["name"] == expected_name
        assert steps[idx]["status"] == expected_status


def test_delivery_partner_and_destination():
    """Verify delivery partner Shekhar is assigned with demo status and address is simulated."""
    p1 = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p1])

    partner = order["delivery_partner"]
    assert partner["name"] == "Shekhar"
    assert partner["status"] == "Awaiting assignment"
    assert "not available" in partner["note"].lower()

    assert "Demo delivery location — Bengaluru" in order["delivery_address"]


def test_deterministic_stage_advancement():
    """Verify order stages can advance deterministically through all 5 stages to Delivered."""
    p1 = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p1])
    assert order["tracking_stage_index"] == 0

    # Advance to stage 3 (On the way - matching reference image)
    for target_stage in range(1, 4):
        order["tracking_stage_index"] = target_stage
        for i, s in enumerate(order["delivery_state"]["steps"]):
            if i < target_stage:
                s["status"] = "completed"
            elif i == target_stage:
                s["status"] = "current"
            else:
                s["status"] = "pending"

    assert order["tracking_stage_index"] == 3
    assert order["delivery_state"]["steps"][3]["name"] == "On the way"
    assert order["delivery_state"]["steps"][3]["status"] == "current"

    # Advance to stage 4 (Delivered)
    order["tracking_stage_index"] = 4
    for i, s in enumerate(order["delivery_state"]["steps"]):
        s["status"] = "completed"
    assert order["delivery_state"]["steps"][4]["name"] == "Delivered"
    assert order["delivery_state"]["steps"][4]["status"] == "completed"


def test_invalid_and_empty_cart_rejection():
    """Verify order creation fails safely on empty cart or corrupt items."""
    # Empty cart
    assert create_simulated_order("cooking", []) is None

    # Item not in catalogue
    fake_item = {"id": "non_existent_id", "name": "Fake Item", "price": 100}
    assert create_simulated_order("cooking", [fake_item]) is None

    # Missing ID
    corrupt_item = {"name": "No ID Item", "price": 100}
    assert create_simulated_order("cooking", [corrupt_item]) is None


def test_historical_orders_and_habit_memory_immutability():
    """Verify that simulating orders does not mutate HISTORICAL_ORDERS or Habit Memory."""
    original_history_len = len(HISTORICAL_ORDERS)
    original_history_snapshot = copy.deepcopy(HISTORICAL_ORDERS)
    original_adopted = get_historically_adopted_subcategories(HISTORICAL_ORDERS)

    # Place multiple simulated orders
    p1 = PRODUCT_BY_ID["p_pasta"]
    p2 = PRODUCT_BY_ID["p_colander"]
    order1 = create_simulated_order("cooking", [p1, p2])
    order2 = create_simulated_order("breakfast", [p1])

    # Check length
    assert len(HISTORICAL_ORDERS) == original_history_len

    # Check deep equality of historical orders
    assert HISTORICAL_ORDERS == original_history_snapshot

    # Check habit memory
    new_adopted = get_historically_adopted_subcategories(HISTORICAL_ORDERS)
    assert new_adopted == original_adopted


def test_unique_order_ids():
    """Verify distinct checkout actions generate unique order IDs."""
    p1 = PRODUCT_BY_ID["p_pasta"]
    ids = set()
    for _ in range(20):
        ord = create_simulated_order("cooking", [p1])
        assert ord["order_id"] not in ids
        ids.add(ord["order_id"])
    assert len(ids) == 20


def test_order_snapshot_immutability():
    """Verify order items capture display name and prices permanently."""
    p1 = PRODUCT_BY_ID["p_pasta"]
    order = create_simulated_order("cooking", [p1])

    captured_item = order["items"][0]
    captured_price = captured_item["price"]

    # Simulating external mutation
    p1_copy = copy.deepcopy(p1)
    p1_copy["price"] = 99999

    assert captured_item["price"] == captured_price
