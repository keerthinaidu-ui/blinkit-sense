"""
Subcategory Assets Module for BlinkitSense.
Maps each subcategory to its dedicated SVG illustration, short 2-line label, category group, and fallback.
"""

from pathlib import Path
from functools import lru_cache

ASSETS_DIR = Path(__file__).parent / "subcategories"

# Master configuration for all 30 subcategories
SUBCATEGORY_METADATA = {
    # 1. Grocery & Kitchen (8)
    "Vegetables & Fruits": {
        "slug": "vegetables_fruits",
        "category": "Grocery & Kitchen",
        "short_label": "Vegetables &<br>Fruits",
        "fallback_icon": "🥦",
        "color_accent": "#EBF7ED",
    },
    "Atta, Rice & Dal": {
        "slug": "atta_rice_dal",
        "category": "Grocery & Kitchen",
        "short_label": "Atta, Rice<br>& Dal",
        "fallback_icon": "🌾",
        "color_accent": "#FEF3C7",
    },
    "Oil, Ghee & Masala": {
        "slug": "oil_ghee_masala",
        "category": "Grocery & Kitchen",
        "short_label": "Oil, Ghee<br>& Masala",
        "fallback_icon": "🫒",
        "color_accent": "#FFFBEB",
    },
    "Dairy, Bread & Eggs": {
        "slug": "dairy_bread_eggs",
        "category": "Grocery & Kitchen",
        "short_label": "Dairy, Bread<br>& Eggs",
        "fallback_icon": "🥛",
        "color_accent": "#EFF6FF",
    },
    "Bakery & Biscuits": {
        "slug": "bakery_biscuits",
        "category": "Grocery & Kitchen",
        "short_label": "Bakery &<br>Biscuits",
        "fallback_icon": "🥐",
        "color_accent": "#FEF3C7",
    },
    "Dry Fruits & Cereals": {
        "slug": "dry_fruits_cereals",
        "category": "Grocery & Kitchen",
        "short_label": "Dry Fruits<br>& Cereals",
        "fallback_icon": "🥜",
        "color_accent": "#FFF7ED",
    },
    "Chicken, Meat & Fish": {
        "slug": "chicken_meat_fish",
        "category": "Grocery & Kitchen",
        "short_label": "Chicken, Meat<br>& Fish",
        "fallback_icon": "🍗",
        "color_accent": "#FEF2F2",
    },
    "Kitchenware & Appliances": {
        "slug": "kitchenware_appliances",
        "category": "Grocery & Kitchen",
        "short_label": "Kitchenware<br>& Appliances",
        "fallback_icon": "🍳",
        "color_accent": "#F0FDFA",
    },

    # 2. Snacks & Drinks (8)
    "Chips & Namkeen": {
        "slug": "chips_namkeen",
        "category": "Snacks & Drinks",
        "short_label": "Chips &<br>Namkeen",
        "fallback_icon": "🥔",
        "color_accent": "#FEF3C7",
    },
    "Sweets & Chocolates": {
        "slug": "sweets_chocolates",
        "category": "Snacks & Drinks",
        "short_label": "Sweets &<br>Chocolates",
        "fallback_icon": "🍫",
        "color_accent": "#F5F3FF",
    },
    "Drinks & Juices": {
        "slug": "drinks_juices",
        "category": "Snacks & Drinks",
        "short_label": "Drinks &<br>Juices",
        "fallback_icon": "🥤",
        "color_accent": "#EFF6FF",
    },
    "Tea, Coffee & Milk Drinks": {
        "slug": "tea_coffee_milk_drinks",
        "category": "Snacks & Drinks",
        "short_label": "Tea, Coffee<br>& Drinks",
        "fallback_icon": "☕",
        "color_accent": "#FFFBEB",
    },
    "Instant Food": {
        "slug": "instant_food",
        "category": "Snacks & Drinks",
        "short_label": "Instant<br>Food",
        "fallback_icon": "🍜",
        "color_accent": "#FEF2F2",
    },
    "Sauces & Spreads": {
        "slug": "sauces_spreads",
        "category": "Snacks & Drinks",
        "short_label": "Sauces &<br>Spreads",
        "fallback_icon": "🥫",
        "color_accent": "#FFF1F2",
    },
    "Paan Corner": {
        "slug": "paan_corner",
        "category": "Snacks & Drinks",
        "short_label": "Paan<br>Corner",
        "fallback_icon": "🍃",
        "color_accent": "#F0FDF4",
    },
    "Ice Creams & More": {
        "slug": "ice_creams_more",
        "category": "Snacks & Drinks",
        "short_label": "Ice Creams<br>& More",
        "fallback_icon": "🍦",
        "color_accent": "#FFF1F2",
    },

    # 3. Beauty & Personal Care (8)
    "Bath & Body": {
        "slug": "bath_body",
        "category": "Beauty & Personal Care",
        "short_label": "Bath &<br>Body",
        "fallback_icon": "🧴",
        "color_accent": "#F0FDFA",
    },
    "Hair": {
        "slug": "hair",
        "category": "Beauty & Personal Care",
        "short_label": "Hair<br>Care",
        "fallback_icon": "💇",
        "color_accent": "#ECFDF5",
    },
    "Skin & Face": {
        "slug": "skin_face",
        "category": "Beauty & Personal Care",
        "short_label": "Skin &<br>Face",
        "fallback_icon": "✨",
        "color_accent": "#FFF1F2",
    },
    "Beauty & Cosmetics": {
        "slug": "beauty_cosmetics",
        "category": "Beauty & Personal Care",
        "short_label": "Beauty &<br>Cosmetics",
        "fallback_icon": "💄",
        "color_accent": "#FDF2F8",
    },
    "Feminine Hygiene": {
        "slug": "feminine_hygiene",
        "category": "Beauty & Personal Care",
        "short_label": "Feminine<br>Hygiene",
        "fallback_icon": "🌸",
        "color_accent": "#FDF2F8",
    },
    "Baby Care": {
        "slug": "baby_care",
        "category": "Beauty & Personal Care",
        "short_label": "Baby<br>Care",
        "fallback_icon": "🍼",
        "color_accent": "#F0F9FF",
    },
    "Health & Pharma": {
        "slug": "health_pharma",
        "category": "Beauty & Personal Care",
        "short_label": "Health &<br>Pharma",
        "fallback_icon": "💊",
        "color_accent": "#FEF2F2",
    },
    "Sexual Wellness": {
        "slug": "sexual_wellness",
        "category": "Beauty & Personal Care",
        "short_label": "Sexual<br>Wellness",
        "fallback_icon": "🛡️",
        "color_accent": "#EEF2FF",
    },

    # 4. Household Essentials (6)
    "Home & Lifestyle": {
        "slug": "home_lifestyle",
        "category": "Household Essentials",
        "short_label": "Home &<br>Lifestyle",
        "fallback_icon": "🕯️",
        "color_accent": "#FFFBEB",
    },
    "Cleaners & Repellents": {
        "slug": "cleaners_repellents",
        "category": "Household Essentials",
        "short_label": "Cleaners &<br>Repellents",
        "fallback_icon": "🧼",
        "color_accent": "#F0F9FF",
    },
    "Electronics": {
        "slug": "electronics",
        "category": "Household Essentials",
        "short_label": "Electronics<br>& Cables",
        "fallback_icon": "🎧",
        "color_accent": "#F8FAFC",
    },
    "Stationery & Games": {
        "slug": "stationery_games",
        "category": "Household Essentials",
        "short_label": "Stationery<br>& Games",
        "fallback_icon": "📓",
        "color_accent": "#FEF3C7",
    },
    "Stores": {
        "slug": "stores",
        "category": "Household Essentials",
        "short_label": "Specialty<br>Stores",
        "fallback_icon": "⚡",
        "color_accent": "#FEF9C3",
    },
    "E-Cards": {
        "slug": "e_cards",
        "category": "Household Essentials",
        "short_label": "Gift<br>E-Cards",
        "fallback_icon": "🎁",
        "color_accent": "#FEF3C7",
    },
}


import base64
import re

@lru_cache(maxsize=64)
def get_subcategory_data_uri(subcat_name: str) -> str:
    """
    Returns base64 data URI of the SVG illustration.
    Using data URI in an <img> tag is 100% resilient against CommonMark markdown parsing.
    """
    meta = SUBCATEGORY_METADATA.get(subcat_name)
    if not meta:
        fallback_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><text x="32" y="38" font-size="28" text-anchor="middle">📦</text></svg>'
        return f"data:image/svg+xml;base64,{base64.b64encode(fallback_svg.encode()).decode()}"
    
    slug = meta["slug"]
    svg_file = ASSETS_DIR / f"{slug}.svg"
    svg_bytes = b""
    if svg_file.exists():
        try:
            svg_bytes = svg_file.read_bytes()
        except Exception:
            pass
            
    if not svg_bytes:
        fallback_icon = meta.get("fallback_icon", "🛍️")
        fallback_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="8" y="8" width="48" height="48" rx="14" fill="#F5F5F5" /><text x="32" y="39" font-size="26" text-anchor="middle">{fallback_icon}</text></svg>'
        svg_bytes = fallback_svg.encode("utf-8")

    b64 = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"


@lru_cache(maxsize=64)
def get_subcategory_svg(subcat_name: str) -> str:
    """
    Returns the SVG content for a given subcategory.
    Falls back to a styled SVG with the fallback icon if file missing.
    Strips XML comments and leading whitespace to prevent CommonMark code block parsing.
    """
    meta = SUBCATEGORY_METADATA.get(subcat_name)
    if not meta:
        return '<svg viewBox="0 0 64 64" width="100%" height="100%"><text x="32" y="38" font-size="28" text-anchor="middle">📦</text></svg>'
    
    slug = meta["slug"]
    svg_file = ASSETS_DIR / f"{slug}.svg"
    raw_svg = ""
    if svg_file.exists():
        try:
            raw_svg = svg_file.read_text(encoding="utf-8")
        except Exception:
            pass
            
    if not raw_svg:
        fallback_icon = meta.get("fallback_icon", "🛍️")
        raw_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%"><rect x="8" y="8" width="48" height="48" rx="14" fill="#F5F5F5" /><text x="32" y="39" font-size="26" text-anchor="middle">{fallback_icon}</text></svg>"""

    # Strip XML comments
    cleaned = re.sub(r"<!--.*?-->", "", raw_svg, flags=re.DOTALL)
    # Minify into single unindented string so markdown parser never treats it as a code block
    minified = " ".join(line.strip() for line in cleaned.splitlines() if line.strip())
    return minified


def get_subcategory_meta(subcat_name: str) -> dict:
    """Returns metadata for the subcategory."""
    return SUBCATEGORY_METADATA.get(subcat_name, {
        "slug": "unknown",
        "category": "General",
        "short_label": subcat_name,
        "fallback_icon": "🛍️",
        "color_accent": "#F5F5F5",
    })
