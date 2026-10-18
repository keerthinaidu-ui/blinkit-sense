"""
BlinkitSense - Screen 1: Mobile Scenario Selection & Screen 2: Home
A fictional, AI-powered product discovery concept inspired by Blinkit's quick-commerce shopping experience.
"""

from pathlib import Path
import importlib
import random
import streamlit as st
import streamlit.components.v1 as components
from assets.subcategory_assets import get_subcategory_data_uri, get_subcategory_meta
import catalogue
importlib.reload(catalogue)
from catalogue import PRODUCT_CATALOGUE, PRODUCT_BY_ID, get_valid_products

# 1. Page Configuration
st.set_page_config(
    page_title="BlinkitSense",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Load Custom CSS
def load_css():
    css_file = Path(__file__).parent / "styles" / "custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# 3. Single Structured Configuration for Scenarios
SCENARIOS = {
    "cooking": {
        "id": "cooking",
        "title": "Saturday Evening — Cooking at Home",
        "short_name": "Cooking at Home",
        "context_label": "SATURDAY · 7:05 PM",
        "time": "7:05",
        "location_weather": "Bengaluru · Heavy rain",
        "weather_icon": "🌧️",
        "mission": "Prepare dinner at home.",
        "description": "Get ingredients for a comforting homemade meal, with relevant discoveries that make cooking easier.",
        "illustration": "🍲",
    },
    "breakfast": {
        "id": "breakfast",
        "title": "Monday Morning — Quick Breakfast",
        "short_name": "Quick Breakfast",
        "context_label": "MONDAY · 8:15 AM",
        "time": "8:15",
        "location_weather": "Bengaluru · Hot and sunny",
        "weather_icon": "☀️",
        "mission": "Find a quick, low-effort breakfast before a 9:30 AM meeting.",
        "description": "Build a simple breakfast with convenient ingredients for a busy morning.",
        "illustration": "🥣",
    },
    "period_care": {
        "id": "period_care",
        "title": "Wednesday Evening — First-Time Period Care",
        "short_name": "First-Time Period Care",
        "context_label": "WEDNESDAY · 8:20 PM",
        "time": "8:20",
        "location_weather": "Bengaluru · Warm evening",
        "weather_icon": "🌙",
        "mission": "Shop for period-care products.",
        "description": "Find essential period-care products in a discreet, straightforward shopping experience.",
        "illustration": "🌸",
    },
}

# 4. Taxonomy & Scenario-Specific Guided Subcategories
CATEGORY_TAXONOMY = {
    "Grocery & Kitchen": [
        "Vegetables & Fruits",
        "Atta, Rice & Dal",
        "Oil, Ghee & Masala",
        "Dairy, Bread & Eggs",
        "Bakery & Biscuits",
        "Dry Fruits & Cereals",
        "Chicken, Meat & Fish",
        "Kitchenware & Appliances",
    ],
    "Snacks & Drinks": [
        "Chips & Namkeen",
        "Sweets & Chocolates",
        "Drinks & Juices",
        "Tea, Coffee & Milk Drinks",
        "Instant Food",
        "Sauces & Spreads",
        "Paan Corner",
        "Ice Creams & More",
    ],
    "Beauty & Personal Care": [
        "Bath & Body",
        "Hair",
        "Skin & Face",
        "Beauty & Cosmetics",
        "Feminine Hygiene",
        "Baby Care",
        "Health & Pharma",
        "Sexual Wellness",
    ],
    "Household Essentials": [
        "Home & Lifestyle",
        "Cleaners & Repellents",
        "Electronics",
        "Stationery & Games",
        "Stores",
        "E-Cards",
    ],
}

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

# Authoritative Scenario Product Selections (Eligible products for each scenario)
SCENARIO_SELECTED_PRODUCTS = {
    "cooking": {
        "p_pasta",       # Penne Pasta (Instant Food)
        "p_sauce",       # Pasta sauce (Sauces & Spreads)
        "p_mushrooms",   # Mushrooms (Vegetables & Fruits)
        "p_cheese",      # Cheese (Dairy, Bread & Eggs)
        "p_chilli",      # Chilli flakes (Oil, Ghee & Masala)
    },
    "breakfast": {
        "p_bananas",     # Bananas (Vegetables & Fruits)
        "p_yogurt",      # Greek yogurt (Dairy, Bread & Eggs)
        "p_granola",     # Granola (Instant Food)
        "p_oj",          # Orange juice (Drinks & Juices)
    },
    "period_care": {
        "p_pads",        # Sanitary Pads (Feminine Hygiene)
        "p_dark_choco",  # Dark Chocolate (Sweets & Chocolates)
        "p_ice_cream",   # Chocolate Ice Cream (Ice Creams & More)
    },
}

# Authoritative Historical Orders (Rohan Mehta - 8 weeks of historical purchase data)
HISTORICAL_ORDERS = [
    {
        "order_id": "ORD_001",
        "week": 1,
        "total": 612,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Bread", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 45, "qty": 1},
            {"name": "Bananas", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 38, "qty": 1},
            {"name": "Pasta", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 145, "qty": 1},
            {"name": "Pasta Sauce", "category": "Snacks & Drinks", "subcategory": "Sauces & Spreads", "price": 149, "qty": 1},
            {"name": "Chips", "category": "Snacks & Drinks", "subcategory": "Chips & Namkeen", "price": 45, "qty": 1},
            {"name": "Coke", "category": "Snacks & Drinks", "subcategory": "Drinks & Juices", "price": 45, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_002",
        "week": 2,
        "total": 487,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Bread", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 45, "qty": 1},
            {"name": "Chicken", "category": "Grocery & Kitchen", "subcategory": "Chicken, Meat & Fish", "price": 150, "qty": 1},
            {"name": "Onions", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 35, "qty": 1},
            {"name": "Tomatoes", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 32, "qty": 1},
            {"name": "Coffee", "category": "Snacks & Drinks", "subcategory": "Tea, Coffee & Milk Drinks", "price": 40, "qty": 1},
            {"name": "Biscuits", "category": "Snacks & Drinks", "subcategory": "Bakery & Biscuits", "price": 40, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_003",
        "week": 3,
        "total": 731,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Vegetables", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 80, "qty": 1},
            {"name": "Pasta", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 145, "qty": 1},
            {"name": "Pasta Sauce", "category": "Snacks & Drinks", "subcategory": "Sauces & Spreads", "price": 149, "qty": 1},
            {"name": "Cheese", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 110, "qty": 1},
            {"name": "Chilli Flakes", "category": "Grocery & Kitchen", "subcategory": "Oil, Ghee & Masala", "price": 45, "qty": 1},
            {"name": "Coke", "category": "Snacks & Drinks", "subcategory": "Drinks & Juices", "price": 45, "qty": 1},
            {"name": "Maggi", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 12, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_004",
        "week": 4,
        "total": 563,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Bread", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 45, "qty": 1},
            {"name": "Chicken", "category": "Grocery & Kitchen", "subcategory": "Chicken, Meat & Fish", "price": 150, "qty": 1},
            {"name": "Rice", "category": "Grocery & Kitchen", "subcategory": "Atta, Rice & Dal", "price": 98, "qty": 1},
            {"name": "Dal", "category": "Grocery & Kitchen", "subcategory": "Atta, Rice & Dal", "price": 45, "qty": 1},
            {"name": "Coffee", "category": "Snacks & Drinks", "subcategory": "Tea, Coffee & Milk Drinks", "price": 40, "qty": 1},
            {"name": "Chips", "category": "Snacks & Drinks", "subcategory": "Chips & Namkeen", "price": 40, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_005",
        "week": 5,
        "total": 804,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Vegetables", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 80, "qty": 1},
            {"name": "Pasta", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 145, "qty": 1},
            {"name": "Pasta Sauce", "category": "Snacks & Drinks", "subcategory": "Sauces & Spreads", "price": 149, "qty": 1},
            {"name": "Mushrooms", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 55, "qty": 1},
            {"name": "Cheese", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 110, "qty": 1},
            {"name": "Coffee", "category": "Snacks & Drinks", "subcategory": "Tea, Coffee & Milk Drinks", "price": 80, "qty": 1},
            {"name": "Coke", "category": "Snacks & Drinks", "subcategory": "Drinks & Juices", "price": 40, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_006",
        "week": 6,
        "total": 628,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Bread", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 45, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Bananas", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 38, "qty": 1},
            {"name": "Maggi", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 72, "qty": 1},
            {"name": "Biscuits", "category": "Snacks & Drinks", "subcategory": "Bakery & Biscuits", "price": 50, "qty": 1},
            {"name": "Chips", "category": "Snacks & Drinks", "subcategory": "Chips & Namkeen", "price": 79, "qty": 1},
            {"name": "Shampoo", "category": "Beauty & Personal Care", "subcategory": "Hair", "price": 199, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_007",
        "week": 7,
        "total": 692,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Chicken", "category": "Grocery & Kitchen", "subcategory": "Chicken, Meat & Fish", "price": 110, "qty": 1},
            {"name": "Onions", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 35, "qty": 1},
            {"name": "Tomatoes", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 32, "qty": 1},
            {"name": "Pasta", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 145, "qty": 1},
            {"name": "Cheese", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 110, "qty": 1},
            {"name": "Pasta Sauce", "category": "Snacks & Drinks", "subcategory": "Sauces & Spreads", "price": 75, "qty": 1},
            {"name": "Coke", "category": "Snacks & Drinks", "subcategory": "Drinks & Juices", "price": 40, "qty": 1},
        ],
    },
    {
        "order_id": "ORD_008",
        "week": 8,
        "total": 618,
        "items": [
            {"name": "Milk", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 60, "qty": 1},
            {"name": "Eggs", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 85, "qty": 1},
            {"name": "Bread", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 45, "qty": 1},
            {"name": "Mushrooms", "category": "Grocery & Kitchen", "subcategory": "Vegetables & Fruits", "price": 55, "qty": 1},
            {"name": "Pasta", "category": "Snacks & Drinks", "subcategory": "Instant Food", "price": 145, "qty": 1},
            {"name": "Pasta Sauce", "category": "Snacks & Drinks", "subcategory": "Sauces & Spreads", "price": 70, "qty": 1},
            {"name": "Cheese", "category": "Grocery & Kitchen", "subcategory": "Dairy, Bread & Eggs", "price": 110, "qty": 1},
            {"name": "Coffee", "category": "Snacks & Drinks", "subcategory": "Tea, Coffee & Milk Drinks", "price": 30, "qty": 1},
            {"name": "Biscuits", "category": "Snacks & Drinks", "subcategory": "Bakery & Biscuits", "price": 18, "qty": 1},
        ],
    },
]

def get_historically_adopted_subcategories(orders=HISTORICAL_ORDERS) -> set:
    """Derives category adoption from the product-level historical records."""
    adopted = set()
    for o in orders:
        for itm in o.get("items", []):
            subcat = itm.get("subcategory")
            if subcat:
                adopted.add(subcat)
    return adopted


# Authoritative candidate configuration for Screen 4: Complete Your Moment
RECOMMENDATION_CANDIDATES = {
    "cooking": [
        {
            "id": "p_colander",
            "name": "Silicone Pasta Colander",
            "category": "Grocery & Kitchen",
            "subcategory": "Kitchenware & Appliances",
            "price": 249,
            "weight": "1 pc",
            "icon": "🥣",
            "why_this": "Why this? A convenient kitchen tool to easily drain boiled pasta.",
            "requires_classification": False,
        },
        {
            "id": "p_hot_chocolate",
            "name": "Hot Chocolate",
            "category": "Snacks & Drinks",
            "subcategory": "Tea, Coffee & Milk Drinks",
            "price": 199,
            "weight": "200g",
            "icon": "☕",
            "why_this": "Why this? A comforting warm beverage for a rainy evening.",
            "requires_classification": False,
        },
        {
            "id": "p_garlic_bread",
            "name": "Garlic Bread",
            "category": "Grocery & Kitchen",
            "subcategory": "Bakery & Biscuits",
            "price": 129,
            "weight": "250g",
            "icon": "🥖",
            "why_this": "Why this? A warm, savoury accompaniment for your pasta dinner.",
            "requires_classification": False,
        },
    ],
    "breakfast": [
        {
            "id": "p_protein_bar",
            "name": "Protein Breakfast Bar",
            "category": "Snacks & Drinks",
            "subcategory": "Chips & Namkeen",
            "price": 149,
            "weight": "50g",
            "icon": "🍫",
            "why_this": "Why this? A quick protein option for busy mornings.",
            "requires_classification": False,
        },
        {
            "id": "p_overnight_oats",
            "name": "Overnight Oats Cup",
            "category": "Snacks & Drinks",
            "subcategory": "Instant Food",
            "price": 179,
            "weight": "100g",
            "icon": "🥣",
            "why_this": "Why this? A ready-to-eat morning meal before early meetings.",
            "requires_classification": False,
        },
        {
            "id": "p_coconut_water",
            "name": "Coconut Water",
            "category": "Snacks & Drinks",
            "subcategory": "Drinks & Juices",
            "price": 60,
            "weight": "200ml",
            "icon": "🥥",
            "why_this": "Why this? Light, refreshing hydration for a sunny start.",
            "requires_classification": False,
        },
    ],
    "period_care": [
        {
            "id": "p_heat_patch",
            "name": "Period Heat Patch",
            "category": "Beauty & Personal Care",
            "subcategory": "Feminine Hygiene",
            "price": 199,
            "weight": "3 pcs",
            "icon": "♨️",
            "why_this": "Why this? A gentle warming patch designed for your self-care routine.",
        },
        {
            "id": "p_pain_balm",
            "name": "Pain Relief Balm",
            "category": "Beauty & Personal Care",
            "subcategory": "Feminine Hygiene",
            "price": 149,
            "weight": "25g",
            "icon": "🧴",
            "why_this": "Why this? A soothing topical balm for gentle comfort.",
        },
        {
            "id": "p_flowers",
            "name": "Flowers",
            "category": "Beauty & Personal Care",
            "subcategory": "Self-Care & Gifting",
            "price": 249,
            "weight": "1 bunch",
            "icon": "💐",
            "why_this": "Why this? Fresh flowers to brighten your day and lift your mood.",
        },
    ],
}


def evaluate_candidate_recommendations(scenario_id: str, cart_items: list = None):
    """
    Evaluates scenario recommendation candidates:
    1. Candidate must be configured for the active scenario.
    2. Must exist in authoritative catalogue (PRODUCT_BY_ID) with valid required fields.
    3. Cannot already be in active cart (duplicate-cart exclusion).
    4. Mission relevance supported by configured demo signals and rationale.
    Returns: (eligible_recommendations, diagnostics_list)
    """
    if cart_items is None:
        cart_items = []
    cart_pids = {p.get("id") for p in cart_items}
    candidates = RECOMMENDATION_CANDIDATES.get(scenario_id, [])

    eligible = []
    diagnostics = []

    for cand in candidates:
        pid = cand["id"]
        name = cand["name"]

        # 1. Catalogue existence
        prod = PRODUCT_BY_ID.get(pid)
        if not prod:
            diagnostics.append({
                "id": pid,
                "name": name,
                "status": "EXCLUDED",
                "reason": "Missing from authoritative catalogue.",
            })
            continue

        # 2. Required fields
        if not (prod.get("name") and prod.get("price") and prod.get("subcategory") and prod.get("category")):
            diagnostics.append({
                "id": pid,
                "name": name,
                "status": "EXCLUDED",
                "reason": "Invalid or missing required catalogue fields.",
            })
            continue

        # 3. Scenario association
        if scenario_id not in prod.get("scenarios", []):
            diagnostics.append({
                "id": pid,
                "name": name,
                "status": "EXCLUDED",
                "reason": f"Product not configured for scenario '{scenario_id}'.",
            })
            continue

        # 4. Cart exclusion (already in cart)
        if pid in cart_pids:
            diagnostics.append({
                "id": pid,
                "name": name,
                "status": "EXCLUDED",
                "reason": "Product is already in active cart.",
            })
            continue

        # All validation passed: candidate is eligible
        subcat = prod.get("subcategory")
        diagnostics.append({
            "id": pid,
            "name": name,
            "status": "ELIGIBLE",
            "reason": f"Valid discovery candidate for scenario '{scenario_id}' in '{subcat}'.",
        })
        eligible.append({
            "id": pid,
            "name": prod["name"],
            "price": prod["price"],
            "weight": prod.get("weight", ""),
            "icon": prod.get("icon", "📦"),
            "why_this": cand["why_this"],
            "product": prod,
        })

    return eligible, diagnostics


def get_cart_recommendations(scenario_id: str, cart_items: list) -> list:
    """Returns eligible discovery recommendations for Screen 4."""
    eligible, _ = evaluate_candidate_recommendations(scenario_id, cart_items)
    return eligible


# Backwards-compatible map derived from the authoritative single source of truth (catalogue.py)
CATALOGUE_PRODUCTS = {
    sc_id: {
        subcat: [
            p for p in PRODUCT_CATALOGUE
            if p["subcategory"] == subcat and sc_id in p["scenarios"]
        ]
        for subcat in SCENARIO_GUIDED_SUBCATEGORIES.get(sc_id, [])
    }
    for sc_id in SCENARIOS
}

# 4b. Authoritative Candidate Configuration for The Usuals (Screen 4: View Cart)
USUALS_CANDIDATE_CONFIGS = [
    {
        "id": "p_shampoo",
        "name": "Shampoo",
        "expected_price": 199,
        "is_shampoo": True,
    },
    {
        "id": "p_milk_fullcream",
        "name": "Milk",
        "expected_price": None,
        "is_shampoo": False,
    },
    {
        "id": "p_eggs_6",
        "name": "Eggs",
        "expected_price": None,
        "is_shampoo": False,
    },
    {
        "id": "p_bread_brown",
        "name": "Bread",
        "expected_price": None,
        "is_shampoo": False,
    },
]


def get_the_usuals_products():
    """
    Evaluates candidates for 'The Usuals':
    1. Verifies that each candidate has a valid product ID and corresponding catalogue entry in PRODUCT_BY_ID.
    2. Verifies that the catalogue entry has a usable positive price.
    3. For shampoo, must use the configured historical Week 6 price of ₹199.
    4. For milk, eggs, and bread, uses their configured catalogue prices (not assumed from historical order totals).
    5. If a required product is missing from the catalogue or lacks a valid price, does not invent missing data.
    Returns: (valid_products, missing_configs)
    """
    valid_products = []
    missing_configs = []

    for cand in USUALS_CANDIDATE_CONFIGS:
        pid = cand["id"]
        cname = cand["name"]
        prod = PRODUCT_BY_ID.get(pid)

        if not prod:
            missing_configs.append(f"{cname} (ID '{pid}') is missing from the authoritative catalogue.")
            continue

        price = cand["expected_price"] if cand["is_shampoo"] else prod.get("price")
        if not price or price <= 0:
            missing_configs.append(f"{cname} (ID '{pid}') lacks a valid positive price.")
            continue

        valid_products.append({
            "id": pid,
            "name": prod.get("name", cname),
            "price": int(price),
            "weight": prod.get("weight", ""),
            "icon": prod.get("icon", "📦"),
            "product": prod,
        })

    return valid_products, missing_configs


# 5. Session State Initialization
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "scenario_selection"

# Handle query parameters for direct navigation (e.g., clicking bottom-nav links ?nav=orders&scenario=...)
if hasattr(st, "query_params"):
    if "scenario" in st.query_params:
        nav_scenario = st.query_params.get("scenario")
        if nav_scenario in SCENARIOS:
            st.session_state.selected_scenario = nav_scenario
            st.session_state.scenario_data = SCENARIOS[nav_scenario]

    if "nav" in st.query_params:
        nav_screen = st.query_params.get("nav")
        if nav_screen == "orders":
            st.session_state.current_screen = "orders"
            st.session_state.force_scroll_top = True
        elif nav_screen in ("scenario_selection", "scenarios", "scenario"):
            st.session_state.current_screen = "scenario_selection"
            st.session_state.force_scroll_top = True
        elif nav_screen in ("categories", "category", "home"):
            st.session_state.current_screen = "home"
            st.session_state.force_scroll_top = True
            sc_id = st.session_state.get("selected_scenario") or "cooking"
            st.session_state.selected_scenario = sc_id
            st.session_state.scenario_data = SCENARIOS.get(sc_id, SCENARIOS["cooking"])
        elif nav_screen in ("cart", "view_cart"):
            st.session_state.current_screen = "view_cart"
            st.session_state.force_scroll_top = True
        try:
            st.query_params.clear()
        except Exception:
            pass

if "selected_scenario" not in st.session_state or st.session_state.selected_scenario is None:
    st.session_state.selected_scenario = "cooking"

if "scenario_data" not in st.session_state or st.session_state.scenario_data is None:
    st.session_state.scenario_data = SCENARIOS["cooking"]

if "cart" not in st.session_state:
    st.session_state.cart = []

if "active_subcat" not in st.session_state:
    st.session_state.active_subcat = None

if "selected_subcat" not in st.session_state:
    st.session_state.selected_subcat = None

if "current_order" not in st.session_state:
    st.session_state.current_order = None

if "simulated_orders" not in st.session_state:
    st.session_state.simulated_orders = []

if "order_flow_stage" not in st.session_state:
    st.session_state.order_flow_stage = "checkout"

if "auto_navigated_to_tracking" not in st.session_state:
    st.session_state.auto_navigated_to_tracking = False

if "demo_tip_selected" not in st.session_state:
    st.session_state.demo_tip_selected = None


# 5b. HTML Sanitizer to prevent Streamlit Markdown code-block interpretation
def clean_html(html_str: str) -> str:
    """Strips leading/trailing whitespace and empty lines so Markdown never interprets HTML as code blocks."""
    return "\n".join(line.strip() for line in html_str.splitlines() if line.strip())


# 5c. Discoverability Engine & Scenario Guidance Helper
def get_scenario_guidance(scenario_id: str, cart_items: list = None) -> dict:
    """
    Authoritative discoverability engine:
    1. Derives scenario-relevant categories and subcategories strictly from existing
       SCENARIO_GUIDED_SUBCATEGORIES, SCENARIO_SELECTED_PRODUCTS, and PRODUCT_CATALOGUE.
    2. Dynamically tracks progress against required scenario products in active cart.
    3. Provides exactly one contextual next-action guidance step at a time.
    4. Automatically signals completion when all required items are in cart.
    """
    if not scenario_id or scenario_id not in SCENARIOS:
        scenario_id = "cooking"
    if cart_items is None:
        cart_items = st.session_state.get("cart", [])

    cart_pids = {item.get("id") for item in cart_items if item.get("id")}
    guided_subcats = SCENARIO_GUIDED_SUBCATEGORIES.get(scenario_id, [])
    selected_pids = SCENARIO_SELECTED_PRODUCTS.get(scenario_id, set())

    scenario_items = []
    guided_cats = set()

    for subcat in guided_subcats:
        prods = [
            p for p in PRODUCT_CATALOGUE
            if p.get("subcategory") == subcat and p.get("id") in selected_pids and scenario_id in p.get("scenarios", [])
        ]
        if prods:
            prod = prods[0]
            cat = prod.get("category", "")
            guided_cats.add(cat)
            is_added = prod["id"] in cart_pids
            scenario_items.append({
                "product_id": prod["id"],
                "product_name": prod["name"],
                "subcategory": subcat,
                "category": cat,
                "is_added": is_added,
                "product": prod,
            })

    added_count = sum(1 for item in scenario_items if item["is_added"])
    total_count = len(scenario_items)
    all_added = (total_count > 0 and added_count == total_count)

    next_step = None
    if not all_added:
        for item in scenario_items:
            if not item["is_added"]:
                next_step = item
                break

    return {
        "scenario_id": scenario_id,
        "guided_categories": guided_cats,
        "guided_subcategories": set(guided_subcats),
        "scenario_items": scenario_items,
        "added_count": added_count,
        "total_count": total_count,
        "all_added": all_added,
        "next_step": next_step,
    }


# 6. Helper Function to Select Scenario
def select_scenario(scenario_id: str):
    scenario = SCENARIOS.get(scenario_id)
    if scenario:
        st.session_state.selected_scenario = scenario_id
        st.session_state.scenario_data = scenario
        st.session_state.cart = []
        # Note: Do not clear current_order; switching scenarios preserves submitted order snapshot
        st.session_state.current_screen = "home"
        st.session_state.force_scroll_top = True
        guided = SCENARIO_GUIDED_SUBCATEGORIES.get(scenario_id, [])
        st.session_state.active_subcat = guided[0] if guided else None
        st.session_state.selected_subcat = guided[0] if guided else None


# 6b. Catalogue Validation Helper for Screen 3
def get_valid_products_for_subcat(scenario_id: str, subcat: str) -> list:
    """
    Returns every valid catalogue product that satisfies ALL conditions:
    1. The scenario is valid and known.
    2. The selected subcategory is enabled for that scenario.
    3. The product belongs to the exact selected subcategory.
    4. The product is explicitly eligible for the scenario.
    5. Required fields are valid (id, name, weight, positive price).
    """
    return get_valid_products(scenario_id, subcat, SCENARIO_GUIDED_SUBCATEGORIES)


# 6c. Subcategory Navigation Handler
def handle_subcategory_click(subcat: str):
    """
    Navigation handler: Validates that the selected subcategory is enabled
    for the current scenario before changing screens. If invalid or disabled,
    leaves the user on Home without changing the cart or selected scenario.
    """
    scenario_id = st.session_state.get("selected_scenario") or "cooking"
    if not st.session_state.get("selected_scenario"):
        st.session_state.selected_scenario = "cooking"
        st.session_state.scenario_data = SCENARIOS["cooking"]

    if not scenario_id or scenario_id not in SCENARIOS:
        return

    guided_subcats = SCENARIO_GUIDED_SUBCATEGORIES.get(scenario_id, [])
    if subcat not in guided_subcats:
        return

    # Valid and enabled: store subcategory state and navigate to Screen 3
    st.session_state.active_subcat = subcat
    st.session_state.selected_subcat = subcat
    st.session_state.current_screen = "product_listing"
    st.session_state.force_scroll_top = True


# 6d. Fixed Floating View Cart Bar Helper
def render_floating_cart_bar():
    if not st.session_state.cart:
        return
    cart_count = len(st.session_state.cart)
    cart_total = sum(p.get("price", 0) for p in st.session_state.cart)
    item_label = "ITEM" if cart_count == 1 else "ITEMS"

    scenario_id = st.session_state.get("selected_scenario") or "cooking"
    guidance = get_scenario_guidance(scenario_id, st.session_state.cart)
    is_all_added = guidance["all_added"]

    wrapper_class = "floating-cart-wrapper floating-cart-wrapper-pulse" if is_all_added else "floating-cart-wrapper"
    st.markdown(f'<div class="{wrapper_class}"></div>', unsafe_allow_html=True)
    screen_key = st.session_state.get("current_screen", "screen")
    
    btn_text = (
        f"🛒   {cart_count} {item_label} · ₹{cart_total}   ·   👉 View Cart Now →"
        if is_all_added
        else f"🛒   {cart_count} {item_label} · ₹{cart_total}   ·   View Cart →"
    )

    if st.button(
        btn_text,
        key=f"btn_floating_view_cart_{screen_key}",
        type="primary",
        use_container_width=True,
    ):
        st.session_state.current_screen = "view_cart"
        st.session_state.force_scroll_top = True
        st.rerun()


# 6e. Order Creation & Validation Helper for Screen 5
def create_simulated_order(scenario_id: str, cart_items: list) -> dict:
    """
    Validates cart contents and creates an immutable snapshot of the placed order.
    Returns None if cart is empty or invalid.
    """
    if not cart_items:
        return None

    # Group items by ID and validate
    item_map = {}
    for item in cart_items:
        pid = item.get("id")
        if not pid or pid not in PRODUCT_BY_ID:
            return None
        prod = PRODUCT_BY_ID[pid]
        if pid not in item_map:
            item_map[pid] = {
                "id": pid,
                "name": prod["name"],
                "price": int(prod["price"]),
                "weight": prod.get("weight", ""),
                "icon": prod.get("icon", "📦"),
                "category": prod.get("category", ""),
                "subcategory": prod.get("subcategory", ""),
                "qty": 0,
            }
        item_map[pid]["qty"] += 1

    ordered_items = []
    subtotal = 0
    for pid, itm in item_map.items():
        qty = itm["qty"]
        if qty <= 0:
            return None
        line_total = itm["price"] * qty
        itm["line_total"] = line_total
        subtotal += line_total
        ordered_items.append(itm)

    if not ordered_items or subtotal <= 0:
        return None

    # Deterministic or timestamp-based unique order ID
    order_num = random.randint(10000, 99999)
    order_id = f"BKS-ORD-{order_num}"
    sc_data = SCENARIOS.get(scenario_id, {})

    est_time = "15–20 minutes · Bengaluru"
    if scenario_id == "cooking":
        est_time = "18–25 minutes · Bengaluru"
    elif scenario_id == "breakfast":
        est_time = "12–18 minutes · Bengaluru"
    elif scenario_id == "period_care":
        est_time = "10–15 minutes (Priority) · Bengaluru"

    return {
        "order_id": order_id,
        "is_simulated": True,
        "scenario_id": scenario_id,
        "scenario_name": sc_data.get("short_name", "Shopping Mission"),
        "scenario_time": sc_data.get("time", "9:41"),
        "items": ordered_items,
        "item_count": sum(itm["qty"] for itm in ordered_items),
        "subtotal": subtotal,
        "delivery_fee": 0,
        "handling_fee": 0,
        "total": subtotal,
        "estimated_delivery": est_time,
        "delivery_address": "Demo delivery location — Bengaluru",
        "tracking_stage_index": 0,
        "delivery_partner": {
            "name": "Shekhar",
            "role": "Demo Delivery Partner",
            "status": "Awaiting assignment",
            "avatar": "🛵",
            "note": "Partner details are not available in this demo state until dispatched.",
            "store_distance": "0.5 km away",
        },
        "delivery_state": {
            "current_step": 0,
            "steps": [
                {"name": "Order confirmed", "status": "completed", "desc": f"Confirmed at {sc_data.get('time', '9:41')}"},
                {"name": "Preparing your order", "status": "pending", "desc": "Items being packed at nearest dark store"},
                {"name": "Delivery partner assigned", "status": "pending", "desc": "Shekhar assigned as demo partner"},
                {"name": "On the way", "status": "pending", "desc": "Out for delivery to your location"},
                {"name": "Delivered", "status": "pending", "desc": "Delivered to your doorstep"},
            ],
        },
    }


# 7. Smartphone Hardware UI Helpers
def reset_screen_scroll(scroll_mode="top"):
    """
    Ensures that when a screen is displayed, the view is properly scrolled:
    - Default ("top"): resets scroll position of .block-container and ancestor containers to the top.
    - "scenario_3_home": positions the home screen so that Snacks & Drinks and
      Beauty & Personal Care (the scenario-relevant categories) are immediately visible.
    """
    js_code = f"""
    <div class="scroll-top-helper" style="display:none;width:0;height:0;margin:0;padding:0;"></div>
    <script>
    (function() {{
        try {{
            if (window.frameElement) {{
                window.frameElement.style.cssText = 'position:absolute!important;width:0!important;height:0!important;border:none!important;opacity:0!important;pointer-events:none!important;margin:0!important;padding:0!important;';
                var parentWrapper = window.frameElement.closest('[data-testid="stCustomComponentV1"]') || window.frameElement.parentElement;
                if (parentWrapper) {{
                    parentWrapper.style.cssText = 'position:absolute!important;width:0!important;height:0!important;border:none!important;opacity:0!important;pointer-events:none!important;margin:0!important;padding:0!important;';
                }}
            }}
        }} catch (e) {{}}

        var scrollMode = "{scroll_mode}";

        function doScroll() {{
            try {{
                var p = (window.parent && window.parent.document) ? window.parent.document : document;
                var win = window.parent || window;
                var container = p.querySelector('.block-container');

                if (scrollMode === 'scenario_3_home') {{
                    var anchor = p.getElementById('scenario3-scroll-anchor') ||
                                 p.getElementById('cat-header-beauty-and-personal-care') ||
                                 p.querySelector('.cat-beauty-and-personal-care-container');
                    if (anchor && typeof anchor.scrollIntoView === 'function') {{
                        anchor.scrollIntoView({{ block: 'end', inline: 'nearest', behavior: 'instant' }});
                    }} else if (container) {{
                        container.scrollTop = 500;
                    }}
                }} else {{
                    var targets = [
                        container,
                        p.querySelector('[data-testid="stMainBlockContainer"]'),
                        p.querySelector('.stMainBlockContainer'),
                        p.querySelector('[data-testid="stAppViewContainer"]'),
                        p.querySelector('section.main'),
                        p.documentElement,
                        p.body
                    ];
                    for (var i = 0; i < targets.length; i++) {{
                        var el = targets[i];
                        if (el) {{
                            el.scrollTop = 0;
                            if (typeof el.scrollTo === 'function') {{
                                el.scrollTo({{ top: 0, left: 0, behavior: 'instant' }});
                            }}
                        }}
                    }}
                    if (typeof win.scrollTo === 'function') {{
                        win.scrollTo({{ top: 0, left: 0, behavior: 'instant' }});
                    }}
                    var topTarget = p.querySelector('.phone-status-bar') || container;
                    if (topTarget && typeof topTarget.scrollIntoView === 'function') {{
                        topTarget.scrollIntoView({{ block: 'start', inline: 'nearest', behavior: 'instant' }});
                    }}
                }}
            }} catch (e) {{}}
        }}

        doScroll();
        if (typeof requestAnimationFrame === 'function') {{
            requestAnimationFrame(doScroll);
        }}
        setTimeout(doScroll, 10);
        setTimeout(doScroll, 40);
        setTimeout(doScroll, 100);
        setTimeout(doScroll, 200);
        setTimeout(doScroll, 400);
    }})();
    </script>
    """
    components.html(js_code, height=0)
    try:
        st.html(js_code, unsafe_allow_javascript=True)
    except Exception:
        pass


def render_phone_status_bar():
    # Ensure every screen displays appropriately from top, or aligned for scenario 3
    current_screen = st.session_state.get('current_screen', 'scenario_selection')
    selected_scenario = st.session_state.get('selected_scenario')
    current_token = f"{current_screen}:{st.session_state.get('selected_subcat', '')}:{selected_scenario}"
    if st.session_state.get("_last_screen_token") != current_token or st.session_state.get("force_scroll_top"):
        scroll_mode = "scenario_3_home" if (current_screen == "home" and selected_scenario == "period_care") else "top"
        reset_screen_scroll(scroll_mode=scroll_mode)
        st.session_state._last_screen_token = current_token
        st.session_state.force_scroll_top = False

    time_str = "9:41"
    selected_sc = st.session_state.get("selected_scenario")
    if selected_sc and selected_sc in SCENARIOS:
        time_str = SCENARIOS[selected_sc].get("time", "9:41")

    st.markdown(
        f"""
        <div class="phone-status-bar">
            <div class="status-left">
                <span class="status-time">{time_str}</span>
            </div>
            <div class="status-center">
                <div class="dynamic-island">
                    <span class="camera-lens"></span>
                </div>
            </div>
            <div class="status-right">
                <svg class="status-icon" width="16" height="12" viewBox="0 0 17 12" fill="none">
                    <rect x="1" y="8" width="2.5" height="4" rx="0.7" fill="#1F1F1F" />
                    <rect x="5" y="5.5" width="2.5" height="6.5" rx="0.7" fill="#1F1F1F" />
                    <rect x="9" y="3" width="2.5" height="9" rx="0.7" fill="#1F1F1F" />
                    <rect x="13" y="0.5" width="2.5" height="11.5" rx="0.7" fill="#1F1F1F" />
                </svg>
                <svg class="status-icon" width="15" height="12" viewBox="0 0 16 12" fill="none">
                    <path d="M8 9.5C8.82843 9.5 9.5 8.82843 9.5 8C9.5 7.17157 8.82843 6.5 8 6.5C7.17157 6.5 6.5 7.17157 6.5 8C6.5 8.82843 7.17157 9.5 8 9.5Z" fill="#1F1F1F" />
                    <path d="M4.6 4.9C6.5 3.3 9.5 3.3 11.4 4.9" stroke="#1F1F1F" stroke-width="1.6" stroke-linecap="round" />
                    <path d="M2 2.3C5.3 -0.5 10.7 -0.5 14 2.3" stroke="#1F1F1F" stroke-width="1.6" stroke-linecap="round" />
                </svg>
                <svg class="status-icon" width="23" height="12" viewBox="0 0 25 12" fill="none">
                    <rect x="0.75" y="0.75" width="20.5" height="10.5" rx="3" stroke="#1F1F1F" stroke-width="1.5" />
                    <rect x="2.5" y="2.5" width="15" height="7" rx="1.5" fill="#1F1F1F" />
                    <path d="M23 4.2V7.8C23.6 7.4 24 6.7 24 6C24 5.3 23.6 4.6 23 4.2Z" fill="#1F1F1F" />
                </svg>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_phone_home_indicator():
    st.markdown(
        """
        <div class="phone-home-indicator-container">
            <div class="phone-home-indicator"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_phone_bottom_nav(active_tab="home"):
    cart_count = len(st.session_state.cart) if "cart" in st.session_state else 0
    badge_html = f'<span class="bottom-nav-badge">{cart_count}</span>' if cart_count > 0 else ""

    home_active = " active" if active_tab == "home" else ""
    categories_active = " active" if active_tab == "categories" else ""
    orders_active = " active" if active_tab == "orders" else ""
    cart_active = " active" if active_tab == "cart" else ""

    home_stroke = "#0C831F" if active_tab == "home" else "#666666"
    categories_stroke = "#0C831F" if active_tab == "categories" else "#666666"
    orders_stroke = "#0C831F" if active_tab == "orders" else "#1F1F1F"
    cart_stroke = "#0C831F" if active_tab == "cart" else "#666666"
    home_fill = "#0C831F" if active_tab == "home" else "none"
    categories_fill = "rgba(12, 131, 31, 0.12)" if active_tab == "categories" else "none"
    orders_fill = "rgba(12, 131, 31, 0.12)" if active_tab == "orders" else "none"

    scr = st.session_state.get("current_screen", "home")
    curr_scenario = st.session_state.get("selected_scenario") or "cooking"
    key_suffix = f"{scr}_{active_tab}_{curr_scenario}"

    def _set_nav_screen(target_screen):
        st.session_state.current_screen = target_screen
        st.session_state.force_scroll_top = True
        if target_screen == "home":
            sc_id = st.session_state.get("selected_scenario") or "cooking"
            st.session_state.selected_scenario = sc_id
            st.session_state.scenario_data = SCENARIOS.get(sc_id, SCENARIOS["cooking"])

    cols = st.columns(4)

    # 1. Home (takes user to Screen 1: Scenario Selection)
    with cols[0]:
        st.markdown(
            f'<div class="bottom-nav-col"><a href="?nav=scenario_selection&scenario={curr_scenario}" target="_self" class="bottom-nav-item{home_active}">'
            f'<svg class="bottom-nav-icon" viewBox="0 0 24 24" fill="{home_fill}" stroke="{home_stroke}" stroke-width="1.5">'
            f'<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>'
            f'<polyline points="9 22 9 12 15 12 15 22" fill="#FFFFFF"></polyline>'
            f'</svg>'
            f'<span>Home</span>'
            f'</a></div>',
            unsafe_allow_html=True,
        )
        if st.button("Home", key=f"btn_nav_home_{key_suffix}", on_click=_set_nav_screen, args=("scenario_selection",), type="tertiary", use_container_width=True):
            st.session_state.current_screen = "scenario_selection"
            st.session_state.force_scroll_top = True
            st.rerun()

    # 2. Categories (takes user to Screen 2: Home of the active scenario)
    with cols[1]:
        st.markdown(
            f'<div class="bottom-nav-col"><a href="?nav=categories&scenario={curr_scenario}" target="_self" class="bottom-nav-item{categories_active}">'
            f'<svg class="bottom-nav-icon" viewBox="0 0 24 24" fill="{categories_fill}" stroke="{categories_stroke}" stroke-width="2">'
            f'<rect x="3" y="3" width="7" height="7" rx="1.5"></rect>'
            f'<rect x="14" y="3" width="7" height="7" rx="1.5"></rect>'
            f'<rect x="14" y="14" width="7" height="7" rx="1.5"></rect>'
            f'<rect x="3" y="14" width="7" height="7" rx="1.5"></rect>'
            f'</svg>'
            f'<span>Categories</span>'
            f'</a></div>',
            unsafe_allow_html=True,
        )
        if st.button("Categories", key=f"btn_nav_categories_{key_suffix}", on_click=_set_nav_screen, args=("home",), type="tertiary", use_container_width=True):
            st.session_state.current_screen = "home"
            sc_id = st.session_state.get("selected_scenario") or "cooking"
            st.session_state.selected_scenario = sc_id
            st.session_state.scenario_data = SCENARIOS.get(sc_id, SCENARIOS["cooking"])
            st.session_state.force_scroll_top = True
            st.rerun()

    # 3. Orders (Clickable with subtle visual cue)
    with cols[2]:
        st.markdown(
            f'<div class="bottom-nav-col"><a href="?nav=orders&scenario={curr_scenario}" target="_self" class="bottom-nav-item interactive-orders{orders_active}" title="Past Orders">'
            f'<svg class="bottom-nav-icon" viewBox="0 0 24 24" fill="{orders_fill}" stroke="{orders_stroke}" stroke-width="2">'
            f'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>'
            f'<polyline points="14 2 14 8 20 8"></polyline>'
            f'<line x1="16" y1="13" x2="8" y2="13"></line>'
            f'<line x1="16" y1="17" x2="8" y2="17"></line>'
            f'</svg>'
            f'<span>Orders</span>'
            f'</a></div>',
            unsafe_allow_html=True,
        )
        if st.button("Orders", key=f"btn_nav_orders_{key_suffix}", on_click=_set_nav_screen, args=("orders",), type="tertiary", use_container_width=True):
            st.session_state.current_screen = "orders"
            st.rerun()

    # 4. Cart
    with cols[3]:
        st.markdown(
            f'<div class="bottom-nav-col"><a href="?nav=cart&scenario={curr_scenario}" target="_self" class="bottom-nav-item{cart_active}">'
            f'<svg class="bottom-nav-icon" viewBox="0 0 24 24" fill="none" stroke="{cart_stroke}" stroke-width="2">'
            f'<circle cx="9" cy="21" r="1"></circle>'
            f'<circle cx="20" cy="21" r="1"></circle>'
            f'<path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>'
            f'</svg>'
            f'<span>Cart</span>{badge_html}'
            f'</a></div>',
            unsafe_allow_html=True,
        )
        if st.button("Cart", key=f"btn_nav_cart_{key_suffix}", on_click=_set_nav_screen, args=("view_cart",), type="tertiary", use_container_width=True):
            st.session_state.current_screen = "view_cart"
            st.rerun()


# 8. Render Screen 1: Scenario Selection
def render_scenario_selection():
    render_phone_status_bar()

    # A. Header
    st.markdown(
        """
        <div class="header-container">
            <span class="brand-badge">blinkit</span>
            <div class="header-text-group">
                <div class="brand-title">
                    BlinkitSense
                    <span class="brand-discovery-icon">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0C831F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                        </svg>
                    </span>
                </div>
                <div class="brand-tagline">Discover what fits your moment.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # B. Screen Heading
    st.markdown(
        """
        <div class="heading-section">
            <h1 class="main-heading">What's the occasion today?</h1>
            <div class="sub-heading">Choose a shopping situation to get started.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # C. Scenario Cards (Exact order: cooking, breakfast, period_care)
    scenario_order = ["cooking", "breakfast", "period_care"]

    for sc_id in scenario_order:
        sc = SCENARIOS[sc_id]

        with st.container(border=True):
            st.markdown(
                f"""
                <div class="scenario-meta-row">
                    <span class="scenario-context-label">{sc['context_label']}</span>
                    <span class="scenario-weather-pill">{sc['weather_icon']} {sc['location_weather']}</span>
                </div>
                <div class="scenario-title-row">
                    <div class="scenario-card-title">{sc['title']}</div>
                    <div class="scenario-illustration-box">{sc['illustration']}</div>
                </div>
                <div class="scenario-mission"><strong>Mission:</strong> {sc['mission']}</div>
                <div class="scenario-description">"{sc['description']}"</div>
                """,
                unsafe_allow_html=True,
            )

            # Primary Action Button
            if st.button("Start Shopping", key=f"btn_{sc['id']}", type="primary", use_container_width=True):
                select_scenario(sc["id"])
                st.rerun()

    # D. Subtle Demo Disclaimer
    st.markdown(
        """
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="home")

    render_phone_home_indicator()


# 9. Render Scenario Confirmation (With Continue Button directly above Switch Scenario)
def render_scenario_confirmation():
    render_phone_status_bar()

    sc = st.session_state.scenario_data
    short_name = sc["short_name"] if sc else "Unknown"
    scenario_id = st.session_state.selected_scenario

    # Header
    st.markdown(
        """
        <div class="header-container">
            <span class="brand-badge">blinkit</span>
            <div class="header-text-group">
                <div class="brand-title">
                    BlinkitSense
                    <span class="brand-discovery-icon">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0C831F" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                        </svg>
                    </span>
                </div>
                <div class="brand-tagline">Discover what fits your moment.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Confirmation Card
    st.markdown(
        f"""
        <div class="placeholder-card">
            <span class="placeholder-badge">Screen 1 Complete</span>
            <div class="placeholder-title">Scenario selected: {short_name}</div>
            <div class="placeholder-detail">
                The scenario has been successfully recorded in session state. Tap <strong>Continue</strong> to open Screen 2: Home.
            </div>
            <div class="status-row">
                <div class="status-item">
                    <span class="status-label">Scenario ID:</span>
                    <span class="status-value">{scenario_id}</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Context:</span>
                    <span class="status-value">{sc['context_label']}</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Environment:</span>
                    <span class="status-value">{sc['location_weather']}</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Active Cart:</span>
                    <span class="status-value">Initialized ({len(st.session_state.cart)} items)</span>
                </div>
                <div class="status-item">
                    <span class="status-label">Next Screen:</span>
                    <span class="status-value">Screen 2: Home</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # 1. Continue button placed immediately above Switch Scenario
    if st.button("Continue", key="btn_continue", type="primary", use_container_width=True):
        st.session_state.current_screen = "home"
        st.rerun()

    # 2. Switch Scenario button
    if st.button("← Switch Scenario (Test Mode)", key="btn_switch_scenario", type="secondary", use_container_width=True):
        st.session_state.current_screen = "scenario_selection"
        st.session_state.force_scroll_top = True
        st.rerun()

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="home")

    st.markdown(
        """
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()


# 10. Render Screen 2: Home (With Scenario-Specific Highlighted Categories & Animated Guidance)
def render_screen_2_home():
    render_phone_status_bar()

    scenario_id = st.session_state.selected_scenario or "cooking"
    sc = st.session_state.scenario_data or SCENARIOS.get(scenario_id, SCENARIOS["cooking"])
    if not st.session_state.get("scenario_data"):
        st.session_state.scenario_data = sc
    if not st.session_state.get("selected_scenario"):
        st.session_state.selected_scenario = scenario_id
    guidance = get_scenario_guidance(scenario_id, st.session_state.cart)
    guided_subcats = guidance["guided_subcategories"]
    guided_cats = guidance["guided_categories"]
    added_count = guidance["added_count"]
    total_count = guidance["total_count"]
    all_added = guidance["all_added"]
    next_step = guidance["next_step"]

    # Delivery & Context Header
    st.markdown(
        clean_html(f"""
        <div class="home-header-card">
            <div class="home-delivery-row">
                <span class="delivery-badge">⚡ 10 MINS</span>
                <span class="location-context">Bengaluru · {sc['location_weather']}</span>
            </div>
            <div class="home-search-bar">
                <span>🔍</span>
                <span>Search "{sc['mission'][:28]}..."</span>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Contextual Animated Mission Guidance Banner
    if all_added:
        banner_html = f"""
        <div class="guidance-banner guidance-banner-completed">
            <div class="guidance-header-row">
                <span class="guidance-badge-done">✨ MISSION COMPLETE</span>
                <span class="guidance-count">{total_count}/{total_count} items in cart</span>
            </div>
            <div class="guidance-banner-msg">
                🎉 All required items added! Tap <strong>View Cart</strong> below to complete checkout.
            </div>
        </div>
        """
    elif next_step:
        pct = int((added_count / max(total_count, 1)) * 100)
        banner_html = f"""
        <div class="guidance-banner">
            <div class="guidance-header-row">
                <span class="guidance-badge-step">👉 STEP {added_count + 1} OF {total_count}</span>
                <span class="guidance-count">{added_count}/{total_count} added</span>
            </div>
            <div class="guidance-banner-msg">
                Open <span class="guidance-highlight-target">{next_step['subcategory']}</span> in <em>{next_step['category']}</em> to add <strong>{next_step['product_name']}</strong>.
            </div>
            <div class="guidance-progress-track">
                <div class="guidance-progress-fill" style="width: {pct}%;"></div>
            </div>
        </div>
        """
    else:
        banner_html = ""

    if banner_html:
        st.markdown(clean_html(banner_html), unsafe_allow_html=True)

    # Full 4-Category Taxonomy with Yellow Highlight for Scenario-Relevant Categories
    st.markdown(
        """
        <div style="font-size: 13.5px; font-weight: 800; color: #1F1F1F; margin: 8px 0 6px 2px;">
            Shop by Category
        </div>
        """,
        unsafe_allow_html=True,
    )

    for cat_name, subcats in CATEGORY_TAXONOMY.items():
        is_cat_relevant = cat_name in guided_cats
        guided_in_cat = [s for s in subcats if s in guided_subcats]
        cat_slug = cat_name.lower().replace(" ", "-").replace("&", "and")

        with st.container(border=True):
            # Header of Category: Yellow background highlight on relevant category headers
            if is_cat_relevant:
                cat_header_html = f"""
                <div class="category-name-title category-title-highlighted cat-{cat_slug}-container" id="cat-header-{cat_slug}">
                    <span class="cat-title-text">⚡ {cat_name}</span>
                    <span class="category-badge-yellow">{len(guided_in_cat)} relevant</span>
                </div>
                """
            else:
                cat_header_html = f"""
                <div class="category-name-title cat-{cat_slug}-container" id="cat-header-{cat_slug}">
                    <span>{cat_name}</span>
                    <span class="category-badge-count">0 available</span>
                </div>
                """
            st.markdown(clean_html(cat_header_html), unsafe_allow_html=True)

            # 4-Column Compact Shopping Grid matching reference screenshot
            chunk_size = 4
            chunks = [subcats[i:i + chunk_size] for i in range(0, len(subcats), chunk_size)]
            for row_idx, chunk in enumerate(chunks):
                grid_cols = st.columns(chunk_size)
                for c_idx, subcat in enumerate(chunk):
                    with grid_cols[c_idx]:
                        is_enabled = subcat in guided_subcats
                        is_active = (st.session_state.active_subcat == subcat)
                        data_uri = get_subcategory_data_uri(subcat)
                        meta = get_subcategory_meta(subcat)
                        short_label = meta.get("short_label", subcat)
                        slug = meta.get("slug", subcat.lower().replace(" ", "_"))

                        subcat_item = next((it for it in guidance["scenario_items"] if it["subcategory"] == subcat), None)
                        is_item_in_cart = subcat_item["is_added"] if subcat_item else False
                        is_next_action = (next_step is not None and next_step["subcategory"] == subcat)

                        # Determine step-wise small number or LAST for guided subcategory
                        step_label = None
                        if is_enabled and scenario_id in SCENARIO_GUIDED_SUBCATEGORIES:
                            guided_list = SCENARIO_GUIDED_SUBCATEGORIES[scenario_id]
                            if subcat in guided_list:
                                step_idx = guided_list.index(subcat) + 1
                                if step_idx == len(guided_list):
                                    step_label = "LAST"
                                else:
                                    step_label = str(step_idx)

                        if not is_enabled:
                            card_class = "subcat-card subcat-card-disabled"
                            label_class = "subcat-tile-label"
                            active_badge = ""
                            guided_badge = ""
                        else:
                            # Yellow highlighted relevant subcategories
                            label_class = "subcat-tile-label subcat-tile-label-highlighted"
                            guided_badge = '<div class="subcat-guided-dot"></div>'
                            if is_item_in_cart:
                                card_class = "subcat-card subcat-card-enabled subcat-card-done"
                                active_badge = '<div class="subcat-done-check">✓</div>'
                            elif is_next_action:
                                # Next action cue: displays step number or LAST with animated cue
                                card_class = "subcat-card subcat-card-enabled subcat-card-next-action"
                                if step_label == "LAST":
                                    active_badge = '<div class="subcat-step-badge subcat-step-badge-next subcat-step-badge-last">LAST</div>'
                                else:
                                    active_badge = f'<div class="subcat-step-badge subcat-step-badge-next">{step_label}</div>'
                            elif step_label:
                                card_class = "subcat-card subcat-card-enabled"
                                if step_label == "LAST":
                                    active_badge = '<div class="subcat-step-badge subcat-step-badge-last">LAST</div>'
                                else:
                                    active_badge = f'<div class="subcat-step-badge">{step_label}</div>'
                            elif is_active:
                                card_class = "subcat-card subcat-card-active subcat-card-enabled"
                                active_badge = '<div class="subcat-active-check">✓</div>'
                            else:
                                card_class = "subcat-card subcat-card-enabled"
                                active_badge = ""

                        card_html = (
                            f'<div class="{card_class}">'
                            f'<div class="subcat-tile-squircle">'
                            f'<img src="{data_uri}" class="subcat-svg-img" alt="{subcat}" />'
                            f'{active_badge}{guided_badge}'
                            f'</div>'
                            f'<div class="{label_class}">{short_label}</div>'
                            f'</div>'
                        )
                        st.markdown(clean_html(card_html), unsafe_allow_html=True)

                        if is_enabled:
                            clicked = st.button(
                                f"Browse {subcat}",
                                key=f"grid_btn_{cat_name[:3]}_{slug}_{row_idx}_{c_idx}",
                                help=f"Browse {subcat}",
                                type="tertiary",
                                use_container_width=True,
                                on_click=handle_subcategory_click,
                                args=(subcat,),
                            )
                            if clicked:
                                handle_subcategory_click(subcat)
                                st.rerun()

            # Anchor for scenario 3 home alignment
            if cat_name == "Beauty & Personal Care":
                st.markdown('<div id="scenario3-scroll-anchor" style="position:relative;top:0;left:0;width:1px;height:1px;pointer-events:none;opacity:0;"></div>', unsafe_allow_html=True)

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="categories")

    # Switch Scenario / Back Button
    st.write("")
    if st.button("← Switch Scenario", key="btn_home_back_scenario", type="secondary", use_container_width=True):
        st.session_state.current_screen = "scenario_selection"
        st.session_state.force_scroll_top = True
        st.rerun()

    # Fixed Floating View Cart Bar if items exist
    render_floating_cart_bar()

    # Subtle Demo Disclaimer
    st.markdown(
        """
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()


# 11a. Product Card Component for Screen 3 Two-Column Shopping Grid
def render_product_card(prod: dict, is_eligible: bool, is_next_target: bool = False):
    qty = sum(1 for item in st.session_state.cart if item.get("id") == prod["id"])
    
    if is_next_target and qty == 0:
        highlight_class = "pdp-card-highlighted pdp-card-guided-pulse"
        highlight_dot = '<div class="pdp-guide-pill">REQUIRED</div>'
    elif is_eligible:
        highlight_class = "pdp-card-highlighted"
        highlight_dot = '<div class="pdp-highlight-dot"></div>'
    else:
        highlight_class = ""
        highlight_dot = ""

    card_html = (
        f'<div class="pdp-grid-card {highlight_class}">'
        f'{highlight_dot}'
        f'<div class="pdp-grid-img-box"><span class="pdp-grid-emoji">{prod.get("icon", "📦")}</span></div>'
        f'<div class="pdp-grid-info">'
        f'<div class="pdp-grid-name" title="{prod["name"]}">{prod["name"]}</div>'
        f'<div class="pdp-grid-weight">{prod.get("weight", "")}</div>'
        f'<div class="pdp-grid-price">₹{prod.get("price", 0)}</div>'
        f'</div>'
        f'</div>'
    )

    with st.container(border=True):
        st.markdown(clean_html(card_html), unsafe_allow_html=True)
        if is_eligible:
            if is_next_target and qty == 0:
                btn_label = "👉 + Add"
            else:
                btn_label = f"Add ({qty}) +" if qty > 0 else "+ Add"
            if st.button(
                btn_label,
                key=f"btn_pdp_add_{prod['id']}",
                type="primary",
                use_container_width=True,
            ):
                st.session_state.cart.append(prod)
                st.rerun()
        else:
            st.button(
                "+ Add",
                key=f"btn_pdp_add_disabled_{prod['id']}",
                disabled=True,
                use_container_width=True,
            )


# 11. Render Screen 3: Product Listing (PDP)
def render_screen_3_product_listing():
    render_phone_status_bar()

    scenario_id = st.session_state.get("selected_scenario") or "cooking"
    sc = st.session_state.get("scenario_data") or SCENARIOS.get(scenario_id, {})
    subcat = st.session_state.get("selected_subcat") or st.session_state.get("active_subcat")
    if not subcat:
        guided = SCENARIO_GUIDED_SUBCATEGORIES.get(scenario_id, [])
        subcat = guided[0] if guided else "Products"
        st.session_state.selected_subcat = subcat

    valid_products = get_valid_products_for_subcat(scenario_id, subcat)
    eligible_pids = SCENARIO_SELECTED_PRODUCTS.get(scenario_id, set())

    # Display eligible products first, followed by ineligible products
    valid_products = sorted(valid_products, key=lambda p: 0 if p.get("id") in eligible_pids else 1)

    guidance = get_scenario_guidance(scenario_id, st.session_state.cart)
    next_step = guidance["next_step"]
    all_added = guidance["all_added"]
    subcat_item = next((it for it in guidance["scenario_items"] if it["subcategory"] == subcat), None)
    is_current_subcat_done = subcat_item["is_added"] if subcat_item else False

    # Top Header Navigation Row
    col_back, col_title = st.columns([1, 4], vertical_alignment="center")
    with col_back:
        if st.button("←", key="btn_pdp_back_top", type="secondary", use_container_width=True):
            st.session_state.current_screen = "home"
            st.rerun()
    with col_title:
        item_count_text = f"{len(valid_products)} product{'s' if len(valid_products) != 1 else ''}"
        st.markdown(
            clean_html(f"""
            <div class="pdp-header-text">
                <div class="pdp-header-title">{subcat}</div>
                <div class="pdp-header-subtitle">{sc.get('short_name', '')} · {item_count_text}</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # Contextual Animated Guidance Banner for Screen 3
    if all_added:
        pdp_guidance_html = """
        <div class="guidance-pdp-banner guidance-pdp-banner-done">
            ✨ <strong>All scenario items added!</strong> Tap <strong>View Cart</strong> below to complete your order.
        </div>
        """
    elif is_current_subcat_done and subcat_item:
        if next_step:
            pdp_guidance_html = f"""
            <div class="guidance-pdp-banner guidance-pdp-banner-done">
                ✅ <strong>{subcat_item['product_name']}</strong> is in your cart! Tap <strong>← Back to Categories</strong> to add <strong>{next_step['product_name']}</strong> from <strong>{next_step['subcategory']}</strong>.
            </div>
            """
        else:
            pdp_guidance_html = f"""
            <div class="guidance-pdp-banner guidance-pdp-banner-done">
                ✅ <strong>{subcat_item['product_name']}</strong> is in your cart! Tap <strong>View Cart</strong> below.
            </div>
            """
    elif subcat_item and next_step and next_step["product_id"] == subcat_item["product_id"]:
        pdp_guidance_html = f"""
        <div class="guidance-pdp-banner">
            👉 Tap <strong>+ Add</strong> on <strong>{subcat_item['product_name']}</strong> below to continue your mission.
        </div>
        """
    else:
        pdp_guidance_html = ""

    if pdp_guidance_html:
        st.markdown(clean_html(pdp_guidance_html), unsafe_allow_html=True)

    # Product Cards (Consistent Two-Column Shopping Grid)
    if valid_products:
        # Render all products in 2-column shopping grid (eligible products appear first)
        for i in range(0, len(valid_products), 2):
            pair = valid_products[i:i + 2]
            cols = st.columns(2)
            for c_idx, prod in enumerate(pair):
                with cols[c_idx]:
                    is_target = (next_step is not None and prod.get("id") == next_step["product_id"])
                    render_product_card(
                        prod,
                        is_eligible=(prod.get("id") in eligible_pids),
                        is_next_target=is_target,
                    )
    else:
        st.markdown(
            clean_html("""
            <div class="placeholder-card">
                <div style="font-size: 30px; margin-bottom: 8px;">📦</div>
                <div class="placeholder-title">No products available</div>
                <div class="placeholder-detail">There are no products matching this category for the current scenario.</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # Back Navigation Button
    st.write("")
    if st.button("← Back to Categories", key="btn_pdp_back_bottom", type="secondary", use_container_width=True):
        st.session_state.current_screen = "home"
        st.rerun()

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="categories")

    # Fixed Floating View Cart Bar if items exist
    render_floating_cart_bar()

    # Subtle Demo Disclaimer
    st.markdown(
        clean_html("""
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """),
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()


# 11b. Render Screen 4: View Cart & Complete Your Moment Recommendations
def render_screen_4_view_cart():
    render_phone_status_bar()

    scenario_id = st.session_state.get("selected_scenario") or "cooking"
    sc = st.session_state.get("scenario_data") or SCENARIOS.get(scenario_id, {})
    cart_count = len(st.session_state.cart)
    item_label = "item" if cart_count == 1 else "items"

    # Top Header Navigation Row
    col_back, col_title = st.columns([1, 4], vertical_alignment="center")
    with col_back:
        if st.button("←", key="btn_cart_back_top", type="secondary", use_container_width=True):
            st.session_state.current_screen = "product_listing" if st.session_state.get("selected_subcat") else "home"
            st.rerun()
    with col_title:
        st.markdown(
            f"""
            <div class="cart-header-text">
                <div class="cart-header-title">Your Cart</div>
                <div class="cart-header-subtitle">{sc.get('short_name', '')} · {cart_count} {item_label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # If Cart is Empty
    if not st.session_state.cart:
        st.markdown(
            """
            <div class="cart-empty-card">
                <div style="font-size: 34px; margin-bottom: 8px;">🛒</div>
                <div class="cart-empty-title">Your cart is empty</div>
                <div class="cart-empty-desc">Explore categories and add products to start your shopping journey.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("← Back to Shopping", key="btn_empty_back_shop", type="primary", use_container_width=True):
            st.session_state.current_screen = "product_listing" if st.session_state.get("selected_subcat") else "home"
            st.rerun()
    else:
        # Grouped Cart Items with Quantities and Controls
        unique_pids = []
        for item in st.session_state.cart:
            pid = item.get("id")
            if pid and pid not in unique_pids:
                unique_pids.append(pid)

        for pid in unique_pids:
            prod = PRODUCT_BY_ID.get(pid)
            if not prod:
                continue
            qty = sum(1 for item in st.session_state.cart if item.get("id") == pid)
            unit_price = prod.get("price", 0)
            line_total = unit_price * qty

            with st.container(border=True):
                col_info, col_ctrl, col_total = st.columns([5, 4, 3], vertical_alignment="center")
                with col_info:
                    st.markdown(
                        f"""
                        <div class="cart-item-info">
                            <span class="cart-item-icon">{prod.get("icon", "📦")}</span>
                            <div class="cart-item-text">
                                <div class="cart-item-name" title="{prod['name']}">{prod['name']}</div>
                                <div class="cart-item-meta">{prod.get("weight", "")} · ₹{unit_price} each</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                with col_ctrl:
                    col_m, col_q, col_p = st.columns([1, 1, 1], vertical_alignment="center")
                    with col_m:
                        if st.button("−", key=f"btn_cart_dec_{pid}", help="Decrease quantity", use_container_width=True):
                            for idx, itm in enumerate(st.session_state.cart):
                                if itm.get("id") == pid:
                                    st.session_state.cart.pop(idx)
                                    break
                            st.rerun()
                    with col_q:
                        st.markdown(f'<div class="cart-qty-display">{qty}</div>', unsafe_allow_html=True)
                    with col_p:
                        if st.button("+", key=f"btn_cart_inc_{pid}", help="Increase quantity", use_container_width=True):
                            st.session_state.cart.append(prod)
                            st.rerun()
                with col_total:
                    st.markdown(f'<div class="cart-line-total">₹{line_total}</div>', unsafe_allow_html=True)

        # Calculated Subtotal
        subtotal = sum(p.get("price", 0) for p in st.session_state.cart)
        st.markdown(
            f"""
            <div class="cart-subtotal-card">
                <div class="cart-subtotal-row">
                    <span class="cart-subtotal-label">Subtotal ({cart_count} {item_label})</span>
                    <span class="cart-subtotal-value">₹{subtotal}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Recommendation Section
    st.markdown(
        """
        <div class="recommendation-header-box">
            <div class="recommendation-title">Complete Your Moment</div>
            <div class="recommendation-subtitle">Things You May Like</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    recs = get_cart_recommendations(scenario_id, st.session_state.cart)
    if recs:
        # Two-column recommendation grid
        for i in range(0, len(recs), 2):
            pair = recs[i:i + 2]
            cols = st.columns(2)
            for c_idx, rec in enumerate(pair):
                with cols[c_idx]:
                    with st.container(border=True):
                        card_html = (
                            f'<div class="pdp-grid-card">'
                            f'<div class="pdp-grid-img-box"><span class="pdp-grid-emoji">{rec.get("icon", "📦")}</span></div>'
                            f'<div class="pdp-grid-info">'
                            f'<div class="pdp-grid-name" title="{rec["name"]}">{rec["name"]}</div>'
                            f'<div class="pdp-grid-weight">{rec.get("weight", "")}</div>'
                            f'<div class="pdp-grid-price">₹{rec.get("price", 0)}</div>'
                            f'<div class="rec-why-this-box">{rec["why_this"]}</div>'
                            f'</div>'
                            f'</div>'
                        )
                        st.markdown(card_html, unsafe_allow_html=True)
                        if st.button("+ Add", key=f"btn_rec_add_{rec['id']}", type="primary", use_container_width=True):
                            st.session_state.cart.append(rec["product"])
                            st.rerun()
    else:
        st.markdown(
            """
            <div class="rec-empty-box">
                <div style="font-size: 22px; margin-bottom: 4px;">✨</div>
                <div class="rec-empty-text">No suitable suggestions for this shopping moment right now.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------------------
    # The Usuals Section (Immediately below Complete Your Moment)
    # -------------------------------------------------------------------------
    usuals_products, missing_usuals = get_the_usuals_products()

    st.markdown(
        clean_html("""
        <div class="recommendation-header-box usuals-header-box">
            <div class="recommendation-title">The Usuals</div>
            <div class="recommendation-subtitle">From your regular essentials</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    if usuals_products:
        # Two-column compact grid consistent with View Cart design
        for i in range(0, len(usuals_products), 2):
            pair = usuals_products[i:i + 2]
            cols = st.columns(2)
            for c_idx, u_prod in enumerate(pair):
                with cols[c_idx]:
                    with st.container(border=True):
                        card_html = (
                            f'<div class="pdp-grid-card">'
                            f'<div class="pdp-grid-img-box"><span class="pdp-grid-emoji">{u_prod.get("icon", "📦")}</span></div>'
                            f'<div class="pdp-grid-info">'
                            f'<div class="pdp-grid-name" title="{u_prod["name"]}">{u_prod["name"]}</div>'
                            f'<div class="pdp-grid-weight">{u_prod.get("weight", "")}</div>'
                            f'<div class="pdp-grid-price">₹{u_prod.get("price", 0)}</div>'
                            f'</div>'
                            f'</div>'
                        )
                        st.markdown(clean_html(card_html), unsafe_allow_html=True)

                        qty = sum(1 for item in st.session_state.cart if item.get("id") == u_prod["id"])
                        btn_label = f"Add ({qty}) +" if qty > 0 else "+ Add"
                        if st.button(
                            btn_label,
                            key=f"btn_usuals_add_{u_prod['id']}",
                            type="primary",
                            use_container_width=True,
                        ):
                            st.session_state.cart.append(u_prod["product"])
                            st.rerun()

    # Accessible Floating Bottom Action Area (Visible while screen scrolls)
    if st.session_state.cart:
        subtotal = sum(p.get("price", 0) for p in st.session_state.cart)
        with st.container():
            st.markdown('<div class="cart-checkout-anchor"></div>', unsafe_allow_html=True)
            if st.button(
                f"Place Order  ·  ₹{subtotal} →",
                key="btn_cart_checkout_bottom",
                type="primary",
                use_container_width=True,
            ):
                new_order = create_simulated_order(scenario_id, st.session_state.cart)
                if new_order:
                    st.session_state.current_order = new_order
                    st.session_state.simulated_orders.append(new_order)
                    st.session_state.cart = []
                    st.session_state.order_flow_stage = "confirmation"
                    st.session_state.auto_navigated_to_tracking = False
                    st.session_state.current_screen = "order_confirmation"
                    st.rerun()
                else:
                    st.error("Cart is empty or contains invalid items.")

    # Continue Shopping Button
    st.write("")
    if st.button("← Continue Shopping", key="btn_cart_continue_shopping", type="secondary", use_container_width=True):
        st.session_state.current_screen = "product_listing" if st.session_state.get("selected_subcat") else "home"
        st.rerun()

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="cart")

    # Subtle Demo Disclaimer
    st.markdown(
        """
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()




# 11c. Render Screen 5a: Dedicated Order Confirmation (Success Animation & Auto-Navigation)
def render_screen_5_order_confirmation():
    render_phone_status_bar()

    order = st.session_state.get("current_order")
    if not order:
        st.markdown(
            clean_html("""
            <div class="cart-empty-card">
                <div style="font-size: 34px; margin-bottom: 8px;">📦</div>
                <div class="cart-empty-title">No Active Order Found</div>
                <div class="cart-empty-desc">Explore categories and place an order to view tracking.</div>
            </div>
            """),
            unsafe_allow_html=True,
        )
        if st.button("← Back to Home", key="btn_order_fallback_home", type="primary", use_container_width=True):
            st.session_state.current_screen = "home"
            st.rerun()
        render_phone_bottom_nav(active_tab="home")
        render_phone_home_indicator()
        return

    # Temporary, clean, and uncluttered confirmation screen
    st.markdown(
        clean_html(f"""
        <div class="confirm-screen-container">
            <div class="confirm-icon-outer">
                <svg class="confirm-svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12" class="confirm-polyline"></polyline>
                </svg>
            </div>
            <div class="confirm-title">Your order is placed!</div>
            <div class="confirm-subtitle">Your order has been confirmed.</div>
            <div class="confirm-card-box">
                <div class="confirm-badge-row">
                    <span style="color: #666; font-weight: 600;">ORDER ID</span>
                    <span style="color: #1F1F1F; font-weight: 800; font-family: monospace;">{order['order_id']}</span>
                </div>
                <div class="confirm-divider"></div>
                <div class="confirm-badge-row">
                    <span style="color: #666; font-weight: 600;">ESTIMATED ARRIVAL</span>
                    <span style="color: #0C831F; font-weight: 800;">⚡ {order.get('estimated_delivery', '18–25 mins')}</span>
                </div>
                <div class="confirm-divider"></div>
                <div class="confirm-badge-row">
                    <span style="color: #666; font-weight: 600;">AMOUNT PAID</span>
                    <span style="color: #1F1F1F; font-weight: 800;">₹{order['total']} (Pre-paid)</span>
                </div>
            </div>
            <div class="confirm-auto-redirect-note">
                <span class="confirm-spinner-dot"></span> Redirecting to live tracking...
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Track Order fallback button
    if st.button("Track Order →", key="btn_confirm_track_order", type="primary", use_container_width=True):
        st.session_state.auto_navigated_to_tracking = True
        st.session_state.order_flow_stage = "tracking"
        st.session_state.current_screen = "order_tracking"
        st.rerun()

    # Subtle Demo Disclaimer
    st.markdown(
        clean_html("""
        <div class="demo-disclaimer" style="margin-top: 14px;">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """),
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()

    # Bounded automatic transition to order_tracking after ~1.8 seconds
    if not st.session_state.get("auto_navigated_to_tracking", False):
        import time
        time.sleep(1.8)
        st.session_state.auto_navigated_to_tracking = True
        st.session_state.order_flow_stage = "tracking"
        st.session_state.current_screen = "order_tracking"
        st.rerun()


# 11d. Render Screen 5b: Dedicated Order Tracking (Inspired by Reference Image)
def render_screen_5b_order_tracking():
    render_phone_status_bar()

    order = st.session_state.get("current_order")
    if not order:
        st.markdown(
            clean_html("""
            <div class="cart-empty-card">
                <div style="font-size: 34px; margin-bottom: 8px;">📦</div>
                <div class="cart-empty-title">No Active Order Found</div>
                <div class="cart-empty-desc">Explore categories and place an order to view tracking.</div>
            </div>
            """),
            unsafe_allow_html=True,
        )
        if st.button("← Back to Home", key="btn_tracking_fallback_home", type="primary", use_container_width=True):
            st.session_state.current_screen = "home"
            st.rerun()
        render_phone_bottom_nav(active_tab="home")
        render_phone_home_indicator()
        return

    stage_idx = order.get("tracking_stage_index", 0)

    # Dynamic status headlines based on stage
    stage_meta = [
        {"sub": "Order confirmed", "head": f"Arriving in {order.get('estimated_delivery', '18–25 mins').split(' ')[0]}", "speech": "Your order is confirmed and being prepared at the dark store."},
        {"sub": "Preparing your order", "head": "Arriving in 15 minutes", "speech": "Dark store partner is packing your items with care."},
        {"sub": "Delivery partner assigned", "head": "Arriving in 8 minutes", "speech": "Shekhar is reaching the dark store to pick up your order."},
        {"sub": "Order is on the way", "head": "Arriving in 2 minutes", "speech": "I have picked up your order, and I am on the way to your location"},
        {"sub": "Delivered", "head": "Delivered to your doorstep", "speech": "Order successfully delivered! Thank you for ordering with BlinkitSense."},
    ]
    cur_meta = stage_meta[min(stage_idx, 4)]

    # Top Navigation Row (White back arrow)
    col_back, col_space = st.columns([1, 4], vertical_alignment="center")
    with col_back:
        if st.button("←", key="btn_tracking_top_back", type="secondary", use_container_width=True):
            st.session_state.current_screen = "home"
            st.rerun()
    with col_space:
        st.markdown(
            clean_html(f'<div style="font-size: 11px; font-weight: 700; color: #666; text-align: right; padding-right: 4px;">ORDER #{order["order_id"]}</div>'),
            unsafe_allow_html=True,
        )

    # A. Top Green Header Banner (Inspired by Reference Image)
    st.markdown(
        clean_html(f"""
        <div class="tracking-header-green">
            <div class="tracking-header-top-row">
                <div class="tracking-status-sub">{cur_meta['sub']}</div>
                <div class="tracking-order-id-chip">SIMULATED DEMO</div>
            </div>
            <div class="tracking-status-main">{cur_meta['head']}</div>
            <div style="font-size: 10.5px; color: rgba(255,255,255,0.85); font-weight: 500;">
                ⚡ {order.get('scenario_name', '')} · {order.get('estimated_delivery', 'Bengaluru')}
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # B. Simulated Map Card with Google watermark and route (Inspired by Reference Image)
    st.markdown(
        clean_html("""
        <div class="tracking-map-card">
            <div class="tracking-map-graphic">
                <svg width="100%" height="180" viewBox="0 0 340 180" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="340" height="180" fill="#EBEAE6"/>
                    <rect x="15" y="12" width="45" height="48" rx="4" fill="#DDDCD5"/>
                    <rect x="68" y="12" width="55" height="28" rx="4" fill="#DDDCD5"/>
                    <rect x="131" y="12" width="60" height="35" rx="4" fill="#DDDCD5"/>
                    <rect x="199" y="12" width="126" height="40" rx="4" fill="#DDDCD5"/>
                    <rect x="15" y="72" width="38" height="98" rx="4" fill="#DDDCD5"/>
                    <rect x="63" y="112" width="50" height="58" rx="4" fill="#DDDCD5"/>
                    <rect x="123" y="112" width="65" height="58" rx="4" fill="#DDDCD5"/>
                    <rect x="198" y="102" width="55" height="68" rx="4" fill="#DDDCD5"/>
                    <rect x="263" y="82" width="62" height="88" rx="4" fill="#DDDCD5"/>
                    <path d="M 0 55 L 340 55" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>
                    <path d="M 58 55 L 58 180" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
                    <path d="M 125 0 L 125 180" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>
                    <path d="M 190 55 L 190 180" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
                    <path d="M 260 0 L 260 180" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>
                    <path d="M 58 105 L 340 105" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>
                    <path d="M 275 55 L 68 55 Q 58 55 58 65 L 58 102" stroke="#2A75D3" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <ellipse cx="58" cy="116" rx="8" ry="3" fill="rgba(0,0,0,0.18)"/>
                    <path d="M 58 86 C 50 86 44 92 44 100 C 44 110 58 120 58 120 C 58 120 72 110 72 100 C 72 92 66 86 58 86 Z" fill="#FFFFFF" stroke="#D0D0D0" stroke-width="1.5"/>
                    <circle cx="58" cy="99" r="5" fill="#F8CB46" stroke="#2A75D3" stroke-width="2.5"/>
                    <g transform="translate(254, 30)">
                        <circle cx="8" cy="29" r="5" fill="#2A2A2A"/>
                        <circle cx="28" cy="29" r="5" fill="#2A2A2A"/>
                        <circle cx="8" cy="29" r="2.5" fill="#A0A0A0"/>
                        <circle cx="28" cy="29" r="2.5" fill="#A0A0A0"/>
                        <path d="M 6 27 L 15 27 L 22 21 L 28 27" stroke="#F8CB46" stroke-width="3" stroke-linecap="round"/>
                        <path d="M 20 21 L 23 13" stroke="#F8CB46" stroke-width="2.5" stroke-linecap="round"/>
                        <circle cx="16" cy="14" r="5" fill="#E53935"/>
                        <rect x="7" y="10" width="8" height="11" rx="2" fill="#0C831F"/>
                        <circle cx="17" cy="8" r="5.5" fill="#F8CB46"/>
                        <path d="M 19 8 L 23 8" stroke="#1F1F1F" stroke-width="2" stroke-linecap="round"/>
                    </g>
                    <text x="14" y="170" font-family="-apple-system, Roboto, sans-serif" font-weight="700" font-size="12" fill="#999999" letter-spacing="-0.3">Google</text>
                    <circle cx="318" cy="22" r="11" fill="#FFFFFF" opacity="0.9" stroke="#E0E0E0" stroke-width="0.8"/>
                    <path d="M 314 20 L 314 18 L 316 18 M 322 18 L 324 18 L 324 20 M 324 24 L 324 26 L 322 26 M 316 26 L 314 26 L 314 24" stroke="#555555" stroke-width="1.2" stroke-linecap="round"/>
                </svg>
            </div>
            <div style="padding: 7px 12px; background: #FFFFFF; font-size: 11px; color: #555; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #ECECEC;">
                <span>📍 Blinkit Store: <strong>0.5 km away</strong></span>
                <span style="color: #0C831F; font-weight: 700;">Simulated Demo Route</span>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # C. Delivery-Partner Card (Shekhar) & Tipping Widget (Inspired by Reference Image)
    st.markdown(
        clean_html(f"""
        <div class="tracking-partner-card">
            <div class="tracking-partner-top">
                <div class="tracking-partner-profile">
                    <div class="tracking-partner-avatar-wrap">🛵</div>
                    <div>
                        <div class="tracking-partner-name-row">I'm Shekhar, your delivery partner</div>
                        <div class="tracking-partner-badge-demo">Demo Delivery Partner · Assigned</div>
                    </div>
                </div>
                <div class="tracking-call-btn" title="Decorative control · Simulated partner">📞</div>
            </div>
            <div class="tracking-speech-bubble">
                "{cur_meta['speech']}"
            </div>
            <div class="tracking-tip-section">
                <div class="tracking-tip-header-row">
                    <div>
                        <div class="tracking-tip-heading">Delivering happiness at your doorstep!</div>
                        <div class="tracking-tip-subheading">Thank them by leaving a tip</div>
                    </div>
                    <div style="font-size: 26px;">🛵🎁</div>
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Interactive Tip Buttons
    t1, t2, t3, t4 = st.columns(4)
    tip_sel = st.session_state.get("demo_tip_selected")
    with t1:
        if st.button("🍪 ₹20", key="btn_tip_20", type="secondary", use_container_width=True):
            st.session_state.demo_tip_selected = 20
            st.rerun()
    with t2:
        if st.button("🧦 ₹30 ⭐", key="btn_tip_30", type="primary" if tip_sel == 30 else "secondary", use_container_width=True):
            st.session_state.demo_tip_selected = 30
            st.rerun()
    with t3:
        if st.button("🪙 ₹50", key="btn_tip_50", type="secondary", use_container_width=True):
            st.session_state.demo_tip_selected = 50
            st.rerun()
    with t4:
        if st.button("👏 Other", key="btn_tip_other", type="secondary", use_container_width=True):
            st.session_state.demo_tip_selected = "Custom"
            st.rerun()

    if tip_sel:
        st.markdown(
            clean_html(f'<div style="font-size: 11px; color: #0C831F; font-weight: 700; text-align: center; margin-bottom: 8px;">🎉 Demo tip of ₹{tip_sel} added for Shekhar!</div>'),
            unsafe_allow_html=True,
        )

    # Store Safety Banner
    st.markdown(
        clean_html("""
        <div style="background-color: #FFFFFF; border: 1px solid #E8E8E8; border-radius: 12px; padding: 10px 14px; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
            <div style="font-size: 18px;">🛡️</div>
            <div style="flex: 1;">
                <div style="font-size: 11.5px; font-weight: 700; color: #1F1F1F;">Your Blinkit store is only 0.5 km away</div>
                <div style="font-size: 9.5px; color: #666666;">Learn about delivery partner safety &gt;</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # D. Simulated Delivery Progress (5 Stages)
    st.markdown(
        clean_html("""
        <div class="order-section-title">
            <span>Simulated Delivery Progress</span>
            <span class="order-status-live-pill">● Demo Tracking</span>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Stage advancement control
    col_adv, col_stage_info = st.columns([3, 2], vertical_alignment="center")
    with col_adv:
        if stage_idx < 4:
            next_name = order["delivery_state"]["steps"][stage_idx + 1]["name"]
            if st.button(f"Advance Stage ⏩ ({next_name})", key="btn_advance_stage", type="secondary", use_container_width=True):
                order["tracking_stage_index"] = stage_idx + 1
                for i, s in enumerate(order["delivery_state"]["steps"]):
                    if i < order["tracking_stage_index"]:
                        s["status"] = "completed"
                    elif i == order["tracking_stage_index"]:
                        s["status"] = "current"
                    else:
                        s["status"] = "pending"
                st.rerun()
        else:
            st.button("✅ Delivered (Demo completed)", key="btn_stage_done", disabled=True, use_container_width=True)
    with col_stage_info:
        st.markdown(clean_html(f'<div style="text-align: right; font-size: 11px; color: #666; font-weight: 600;">Stage {stage_idx + 1} of 5</div>'), unsafe_allow_html=True)

    # Stepper rendering
    stepper_html = ['<div class="delivery-stepper-box">']
    steps = order["delivery_state"]["steps"]
    total_steps = len(steps)

    for idx, step in enumerate(steps):
        status = step["status"]
        is_last = (idx == total_steps - 1)
        line_class = "stepper-line-completed" if status == "completed" else "stepper-line-pending"

        if status == "completed":
            dot_html = """
            <div class="stepper-dot-circle stepper-dot-done">
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            """
            item_class = "stepper-item-done"
            status_tag = '<span class="stepper-tag-done">Done</span>'
        elif status == "current":
            dot_html = """
            <div class="stepper-dot-circle stepper-dot-current">
                <div class="stepper-pulse-dot"></div>
            </div>
            """
            item_class = "stepper-item-current"
            status_tag = '<span class="stepper-tag-current">Current</span>'
        else:
            dot_html = """
            <div class="stepper-dot-circle stepper-dot-pending">
                <div class="stepper-hollow-dot"></div>
            </div>
            """
            item_class = "stepper-item-pending"
            status_tag = '<span class="stepper-tag-pending">Pending</span>'

        line_elem = "" if is_last else f'<div class="stepper-line {line_class}"></div>'

        stepper_html.append(
            f"""
            <div class="stepper-row {item_class}">
                <div class="stepper-left-col">
                    {dot_html}
                    {line_elem}
                </div>
                <div class="stepper-right-col">
                    <div class="stepper-header-row">
                        <span class="stepper-name">{step['name']}</span>
                        {status_tag}
                    </div>
                    <div class="stepper-desc">{step['desc']}</div>
                </div>
            </div>
            """
        )

    stepper_html.append('</div>')
    st.markdown(clean_html("".join(stepper_html)), unsafe_allow_html=True)

    # E. Pay / Bill Banner matching Reference Image
    st.markdown(
        clean_html(f"""
        <div class="tracking-pay-card">
            <div>
                <div class="tracking-pay-title">Pay ₹{order['total']} before or on delivery</div>
                <div class="tracking-pay-sub">Pre-paid Online · Simulated demo transaction</div>
            </div>
            <div class="tracking-pay-pill">PAID (DEMO)</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # F. Items in your order
    item_count = order["item_count"]
    item_label = "item" if item_count == 1 else "items"
    st.markdown(
        clean_html(f"""
        <div class="order-section-title">
            <span>Items in your order</span>
            <span class="order-section-badge">{item_count} {item_label}</span>
        </div>
        """),
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        items_html = []
        for itm in order["items"]:
            items_html.append(
                f"""
                <div class="order-item-card">
                    <div class="order-item-icon-box">{itm.get('icon', '📦')}</div>
                    <div class="order-item-info">
                        <div class="order-item-name" title="{itm['name']}">{itm['name']}</div>
                        <div class="order-item-meta">{itm.get('weight', '')} · ₹{itm['price']} each</div>
                    </div>
                    <div class="order-item-qty">Qty: {itm['qty']}</div>
                    <div class="order-item-total">₹{itm['line_total']}</div>
                </div>
                """
            )
        st.markdown(clean_html("".join(items_html)), unsafe_allow_html=True)

    # G. Reconciled Bill Summary
    st.markdown(
        clean_html("""
        <div class="order-section-title">
            <span>Bill Summary</span>
            <span class="order-section-badge">Paid</span>
        </div>
        """),
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            clean_html(f"""
            <div class="order-bill-card">
                <div class="order-bill-row">
                    <span class="order-bill-label">Item Total</span>
                    <span class="order-bill-val">₹{order['subtotal']}</span>
                </div>
                <div class="order-bill-row">
                    <span class="order-bill-label">Delivery Partner Fee</span>
                    <span class="order-bill-free">FREE</span>
                </div>
                <div class="order-bill-row">
                    <span class="order-bill-label">Handling & Packaging</span>
                    <span class="order-bill-free">FREE</span>
                </div>
                <div class="order-bill-divider"></div>
                <div class="order-bill-total-row">
                    <span class="order-bill-total-label">Grand Total</span>
                    <span class="order-bill-total-val">₹{order['total']}</span>
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # H. Delivery Destination
    st.markdown(
        clean_html("""
        <div class="order-section-title">
            <span>Delivery Address</span>
        </div>
        """),
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            clean_html(f"""
            <div class="order-address-card">
                <div class="order-address-icon">📍</div>
                <div class="order-address-details">
                    <div class="order-address-title">{order['delivery_address']}</div>
                    <div class="order-address-sub">Illustrative demo location · Simulated delivery</div>
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # I. Back to Home action
    st.write("")
    if st.button("← Back to Home", key="btn_tracking_back_home", type="primary", use_container_width=True):
        st.session_state.current_screen = "home"
        st.rerun()

    # Bottom Navigation Bar
    render_phone_bottom_nav(active_tab="home")

    # Subtle Demo Disclaimer
    st.markdown(
        clean_html("""
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """),
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()


# 11d. Render Orders Screen: Rohan's Historical Purchase History (Read-Only)
def render_screen_orders():
    render_phone_status_bar()

    # Top Header Navigation Row
    col_back, col_title = st.columns([1, 4], vertical_alignment="center")
    with col_back:
        if st.button("←", key="btn_orders_back_top", type="secondary", use_container_width=True):
            st.session_state.current_screen = "home"
            st.rerun()
    with col_title:
        st.markdown(
            clean_html("""
            <div class="orders-header-text">
                <div class="orders-header-title">Past Orders</div>
                <div class="orders-header-subtitle">Rohan Mehta · 8 Orders History</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # Historical summary pill
    st.markdown(
        clean_html("""
        <div class="orders-summary-banner">
            <span class="orders-summary-icon">📦</span>
            <div class="orders-summary-content">
                <div class="orders-summary-title">8 Completed Weekly Deliveries</div>
                <div class="orders-summary-desc">Read-only historical purchase log for Bengaluru residence</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Render each of the 8 historical orders
    for order in HISTORICAL_ORDERS:
        week_num = order.get("week")
        order_id = order.get("order_id", f"ORD_{week_num:03d}")
        order_total = order.get("total", 0)
        items = order.get("items", [])
        item_count = sum(itm.get("qty", 1) for itm in items)

        with st.container(border=True):
            # Order card header
            st.markdown(
                clean_html(f"""
                <div class="order-hist-card-header">
                    <div class="order-hist-title-group">
                        <span class="order-hist-week-pill">Week {week_num}</span>
                        <span class="order-hist-id">#{order_id}</span>
                    </div>
                    <div class="order-hist-total">₹{order_total}</div>
                </div>
                <div class="order-hist-meta-row">
                    <span class="order-hist-status">✅ Delivered</span>
                    <span class="order-hist-items-count">{item_count} items</span>
                </div>
                <div class="order-hist-divider"></div>
                """),
                unsafe_allow_html=True,
            )

            # Order items breakdown
            items_html_list = []
            for itm in items:
                name = itm.get("name", "Item")
                qty = itm.get("qty", 1)
                price = itm.get("price", 0)
                subcat = itm.get("subcategory", "")
                subcat_badge = f'<span class="order-item-subcat">{subcat}</span>' if subcat else ""

                items_html_list.append(
                    f'<div class="order-hist-item-row">'
                    f'<div class="order-hist-item-left">'
                    f'<span class="order-hist-item-qty">{qty}x</span>'
                    f'<span class="order-hist-item-name">{name}</span>'
                    f'{subcat_badge}'
                    f'</div>'
                    f'<div class="order-hist-item-price">₹{price * qty}</div>'
                    f'</div>'
                )

            items_block = '<div class="order-hist-items-list">' + "".join(items_html_list) + '</div>'
            st.markdown(clean_html(items_block), unsafe_allow_html=True)

    # Back to Home Action
    st.write("")
    if st.button("← Back to Home", key="btn_orders_back_bottom", type="secondary", use_container_width=True):
        st.session_state.current_screen = "home"
        st.rerun()

    # Bottom Navigation Bar (Orders tab active)
    render_phone_bottom_nav(active_tab="orders")

    # Subtle Demo Disclaimer
    st.markdown(
        clean_html("""
        <div class="demo-disclaimer">
            BlinkitSense is a fictional concept demo · Not an official Blinkit feature
        </div>
        """),
        unsafe_allow_html=True,
    )

    render_phone_home_indicator()


# 12. Main Application Router
def main():
    if st.session_state.current_screen == "home":
        render_screen_2_home()
    elif st.session_state.current_screen == "product_listing":
        render_screen_3_product_listing()
    elif st.session_state.current_screen == "view_cart":
        render_screen_4_view_cart()
    elif st.session_state.current_screen == "orders":
        render_screen_orders()
    elif st.session_state.current_screen == "order_confirmation":
        render_screen_5_order_confirmation()
    elif st.session_state.current_screen == "order_tracking":
        render_screen_5b_order_tracking()
    elif st.session_state.current_screen == "scenario_confirmation":
        render_scenario_confirmation()
    else:
        render_scenario_selection()


if __name__ == "__main__":
    main()


