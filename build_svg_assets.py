"""
Script to generate dedicated, highly detailed SVG assets for all 30 subcategories of BlinkitSense.
Assets are saved in assets/subcategories/*.svg and catalogued in assets/subcategory_assets.py.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets" / "subcategories"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

SVG_DATA = {}

# 1. Vegetables & Fruits
SVG_DATA["vegetables_fruits"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="banana-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE066" />
      <stop offset="70%" stop-color="#F5BA13" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <linearGradient id="leaf-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#34D399" />
      <stop offset="60%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <radialGradient id="tomato-grad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FF6B6B" />
      <stop offset="65%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#B91C1C" />
    </radialGradient>
    <filter id="subcat-glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="1.5" flood-opacity="0.15" />
    </filter>
  </defs>
  <g filter="url(#subcat-glow)" class="subcat-anim-float">
    <!-- Banana bunch -->
    <path d="M12 44 C8 32 14 20 25 14 C27 13 29 14 28 16 C20 22 17 32 18 42 C18 45 14 46 12 44 Z" fill="url(#banana-grad)" />
    <path d="M17 46 C12 36 17 25 28 18 C30 17 31 19 30 21 C22 27 19 36 21 45 C21 47 18 48 17 46 Z" fill="url(#banana-grad)" />
    <path d="M22 20 C23 18 26 17 27 19" stroke="#92400E" stroke-width="1.8" stroke-linecap="round" />
    <!-- Spinach / Leafy greens -->
    <path d="M30 48 C28 34 32 20 40 10 C46 20 47 34 42 48 Z" fill="url(#leaf-grad)" />
    <path d="M36 48 C37 38 41 28 48 16 C53 26 51 38 46 48 Z" fill="#059669" opacity="0.9" />
    <path d="M36 48 Q39 30 40 12" stroke="#A7F3D0" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.7" />
    <!-- Tomato -->
    <circle cx="43" cy="45" r="13" fill="url(#tomato-grad)" />
    <ellipse cx="40" cy="39" rx="3.5" ry="2" fill="#FFFFFF" opacity="0.35" transform="rotate(-20 40 39)" />
    <!-- Tomato stem -->
    <path d="M43 32 L41 28 M43 32 L46 28 M43 32 L43 27 M43 32 L39 33 M43 32 L47 34" stroke="#15803D" stroke-width="2" stroke-linecap="round" />
  </g>
</svg>"""

# 2. Atta, Rice & Dal
SVG_DATA["atta_rice_dal"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="atta-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" />
      <stop offset="50%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#B91C1C" />
    </linearGradient>
    <linearGradient id="rice-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="50%" stop-color="#3B82F6" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <radialGradient id="dal-grad" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="70%" stop-color="#EAB308" />
      <stop offset="100%" stop-color="#CA8A04" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Rice Sack (Back Left) -->
    <path d="M12 24 C12 20 16 19 23 19 C30 19 34 20 34 24 L32 50 C32 53 29 55 23 55 C17 55 14 53 14 50 Z" fill="url(#rice-grad)" />
    <path d="M16 23 Q23 20 30 23" stroke="#93C5FD" stroke-width="1.5" fill="none" />
    <rect x="17" y="28" width="12" height="12" rx="2" fill="#FFFFFF" opacity="0.9" />
    <path d="M20 34 L26 34" stroke="#1D4ED8" stroke-width="1.5" stroke-linecap="round" />
    <circle cx="23" cy="32" r="1.5" fill="#EAB308" />

    <!-- Atta Sack (Center Right) -->
    <path d="M27 18 C27 14 32 13 41 13 C50 13 55 14 55 18 L53 50 C53 53 49 55 41 55 C33 55 29 53 29 50 Z" fill="url(#atta-grad)" />
    <path d="M31 17 Q41 14 51 17" stroke="#FCA5A5" stroke-width="1.8" fill="none" />
    <!-- Wheat emblem on atta -->
    <circle cx="41" cy="31" r="7.5" fill="#FEF3C7" />
    <path d="M41 26 L41 36 M38 29 L41 31 L44 29 M38 32 L41 34 L44 32" stroke="#D97706" stroke-width="1.2" stroke-linecap="round" />
    
    <!-- Bowl of yellow dal (Front Left) -->
    <ellipse cx="22" cy="50" rx="14" ry="5.5" fill="#78350F" />
    <ellipse cx="22" cy="48" rx="13" ry="5" fill="url(#dal-grad)" />
    <circle cx="18" cy="47" r="1.2" fill="#B45309" />
    <circle cx="22" cy="46" r="1.2" fill="#B45309" />
    <circle cx="26" cy="48" r="1.2" fill="#B45309" />
  </g>
</svg>"""

# 3. Oil, Ghee & Masala
SVG_DATA["oil_ghee_masala"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="oil-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="50%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <linearGradient id="ghee-pot" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FBBF24" />
      <stop offset="70%" stop-color="#FDE68A" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Oil Bottle (Left) -->
    <path d="M19 12 L23 12 L23 16 L27 21 L27 48 C27 52 25 54 21 54 C17 54 15 52 15 48 L15 21 L19 16 Z" fill="url(#oil-grad)" opacity="0.9" />
    <!-- Bottle neck and red cap -->
    <rect x="18" y="9" width="6" height="4" rx="1" fill="#DC2626" />
    <!-- Oil reflection -->
    <path d="M17 24 L17 48" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" opacity="0.6" />
    <rect x="17" y="30" width="8" height="10" rx="1" fill="#FFFFFF" opacity="0.85" />
    <circle cx="21" cy="35" r="2" fill="#EAB308" />

    <!-- Ghee Jar (Right) -->
    <path d="M33 26 C33 24 37 23 44 23 C51 23 55 24 55 26 L55 46 C55 52 50 54 44 54 C38 54 33 52 33 46 Z" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1" />
    <path d="M34 33 C34 33 39 31 44 31 C49 31 54 33 54 33 L54 46 C54 51 49 53 44 53 C39 53 34 51 34 46 Z" fill="url(#ghee-pot)" />
    <!-- Jar gold lid -->
    <ellipse cx="44" cy="23" rx="11" ry="3.5" fill="#D97706" />
    <ellipse cx="44" cy="22" rx="11" ry="3.5" fill="#FBBF24" />
    <!-- Red Chilli Pepper (Front) -->
    <path d="M26 51 C32 46 38 48 46 45 C41 53 32 55 26 51 Z" fill="#DC2626" />
    <path d="M26 51 Q23 50 22 47" stroke="#15803D" stroke-width="2" stroke-linecap="round" fill="none" />
  </g>
</svg>"""

# 4. Dairy, Bread & Eggs
SVG_DATA["dairy_bread_eggs"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="milk-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="60%" stop-color="#3B82F6" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <linearGradient id="bread-crust" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#B45309" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <radialGradient id="egg-grad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FFFBEB" />
      <stop offset="70%" stop-color="#FDE68A" />
      <stop offset="100%" stop-color="#F59E0B" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Bread Loaf Pack (Back Right) -->
    <path d="M30 18 C30 14 36 12 46 12 C56 12 60 14 60 18 L58 46 C58 49 54 51 45 51 C36 51 32 49 32 46 Z" fill="#FDF6B2" stroke="#F59E0B" stroke-width="1.2" />
    <path d="M33 16 C35 14 40 13 46 13 C52 13 57 14 58 16" stroke="url(#bread-crust)" stroke-width="3" stroke-linecap="round" />
    <rect x="36" y="24" width="18" height="15" rx="2" fill="#EF4444" />
    <path d="M40 31 L50 31" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
    <!-- Slices texture -->
    <path d="M36 42 L54 42 M37 46 L53 46" stroke="#D97706" stroke-width="1" stroke-linecap="round" opacity="0.6" />

    <!-- Milk Carton (Left) -->
    <path d="M12 24 L20 18 L28 24 L28 50 C28 53 26 54 20 54 C14 54 12 53 12 50 Z" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <path d="M12 24 L20 18 L28 24" fill="url(#milk-grad)" />
    <!-- Milk blue wave band -->
    <path d="M12 34 Q20 38 28 34 L28 44 Q20 48 12 44 Z" fill="url(#milk-grad)" />
    <path d="M19 14 L21 14 L21 18 L19 18 Z" fill="#3B82F6" />
    <ellipse cx="20" cy="30" rx="3" ry="2" fill="#3B82F6" />

    <!-- Eggs (Front Center) -->
    <ellipse cx="27" cy="49" rx="5" ry="6.5" fill="url(#egg-grad)" transform="rotate(-15 27 49)" />
    <ellipse cx="36" cy="48" rx="5" ry="6.5" fill="url(#egg-grad)" transform="rotate(10 36 48)" />
  </g>
</svg>"""

# 5. Bakery & Biscuits
SVG_DATA["bakery_biscuits"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="croissant-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBBF24" />
      <stop offset="50%" stop-color="#D97706" />
      <stop offset="100%" stop-color="#92400E" />
    </linearGradient>
    <radialGradient id="cookie-grad" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FDE68A" />
      <stop offset="65%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#B45309" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Biscuit Roll Pack (Back) -->
    <rect x="8" y="20" width="46" height="15" rx="7.5" fill="#2563EB" />
    <rect x="12" y="20" width="38" height="15" fill="#1D4ED8" />
    <ellipse cx="54" cy="27.5" rx="3.5" ry="7.5" fill="#60A5FA" />
    <path d="M16 27.5 L46 27.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
    <circle cx="31" cy="27.5" r="4" fill="#FBBF24" />

    <!-- Golden Croissant (Left) -->
    <path d="M10 48 C8 42 14 34 26 35 C38 36 44 44 42 49 C36 47 30 45 26 45 C20 45 14 47 10 48 Z" fill="url(#croissant-grad)" />
    <path d="M16 43 C18 38 23 38 26 45" stroke="#78350F" stroke-width="1.2" stroke-linecap="round" fill="none" />
    <path d="M26 45 C29 38 34 38 36 44" stroke="#78350F" stroke-width="1.2" stroke-linecap="round" fill="none" />

    <!-- Choco-chip Cookie (Right) -->
    <circle cx="45" cy="46" r="11" fill="url(#cookie-grad)" />
    <!-- Chocolate chips -->
    <circle cx="41" cy="42" r="1.8" fill="#451A03" />
    <circle cx="48" cy="41" r="1.6" fill="#451A03" />
    <circle cx="44" cy="47" r="2" fill="#451A03" />
    <circle cx="50" cy="48" r="1.5" fill="#451A03" />
    <circle cx="40" cy="50" r="1.6" fill="#451A03" />
  </g>
</svg>"""

# 6. Dry Fruits & Cereals
SVG_DATA["dry_fruits_cereals"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="jar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E2E8F0" />
      <stop offset="50%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#CBD5E1" />
    </linearGradient>
    <linearGradient id="cereal-box" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EA580C" />
      <stop offset="60%" stop-color="#F97316" />
      <stop offset="100%" stop-color="#C2410C" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Cereal Box (Right) -->
    <path d="M30 16 L48 12 L56 15 L56 50 L38 54 L30 50 Z" fill="url(#cereal-box)" />
    <path d="M30 16 L38 20 L56 15" stroke="#FED7AA" stroke-width="1" fill="none" />
    <!-- Sunburst on cereal -->
    <circle cx="44" cy="32" r="6" fill="#FDE047" />
    <ellipse cx="44" cy="43" rx="8" ry="4" fill="#FEF08A" />

    <!-- Glass Jar of Almonds/Cashews (Left) -->
    <rect x="12" y="24" width="22" height="28" rx="4" fill="url(#jar-grad)" stroke="#94A3B8" stroke-width="1" opacity="0.9" />
    <!-- Metal lid -->
    <rect x="14" y="20" width="18" height="5" rx="1.5" fill="#D97706" />
    <!-- Almonds & Nuts inside -->
    <ellipse cx="18" cy="34" rx="3.5" ry="2" fill="#92400E" transform="rotate(-30 18 34)" />
    <ellipse cx="27" cy="33" rx="3" ry="2.2" fill="#D97706" transform="rotate(20 27 33)" />
    <ellipse cx="22" cy="40" rx="3.5" ry="2.2" fill="#B45309" transform="rotate(10 22 40)" />
    <ellipse cx="17" cy="45" rx="3" ry="2" fill="#D97706" transform="rotate(-15 17 45)" />
    <ellipse cx="27" cy="45" rx="3.5" ry="2" fill="#92400E" transform="rotate(25 27 45)" />
  </g>
</svg>"""

# 7. Chicken, Meat & Fish
SVG_DATA["chicken_meat_fish"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="drumstick-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="60%" stop-color="#D97706" />
      <stop offset="100%" stop-color="#92400E" />
    </linearGradient>
    <linearGradient id="fish-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#0369A1" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Fresh Fish (Top Right) -->
    <path d="M26 22 C32 16 46 16 56 22 C52 26 48 29 42 29 C34 29 28 26 26 22 Z" fill="url(#fish-grad)" />
    <!-- Fish Tail -->
    <path d="M54 22 L62 16 L60 22 L62 28 Z" fill="#0284C7" />
    <circle cx="31" cy="21" r="1.5" fill="#FFFFFF" />
    <circle cx="31" cy="21" r="0.8" fill="#0F172A" />
    <path d="M37 20 Q40 24 37 27 M42 20 Q45 24 42 27" stroke="#BAE6FD" stroke-width="1.2" stroke-linecap="round" fill="none" />

    <!-- Chicken Drumstick (Center Left) -->
    <path d="M12 48 C8 42 12 32 22 30 C30 28 36 34 34 44 C32 50 20 54 12 48 Z" fill="url(#drumstick-grad)" />
    <!-- Bone -->
    <path d="M30 40 L40 48" stroke="#E2E8F0" stroke-width="4" stroke-linecap="round" />
    <circle cx="41" cy="46" r="2.5" fill="#E2E8F0" />
    <circle cx="43" cy="50" r="2.5" fill="#E2E8F0" />

    <!-- Steak Cutlet (Bottom Right) -->
    <path d="M26 46 C28 42 38 41 46 45 C52 48 50 54 44 56 C36 58 24 54 26 46 Z" fill="#DC2626" />
    <path d="M32 45 Q36 49 42 47" stroke="#FCA5A5" stroke-width="1.8" stroke-linecap="round" fill="none" />
  </g>
</svg>"""

# 8. Kitchenware & Appliances
SVG_DATA["kitchenware_appliances"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="pan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="50%" stop-color="#475569" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>
    <linearGradient id="kettle-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0D9488" />
      <stop offset="60%" stop-color="#14B8A6" />
      <stop offset="100%" stop-color="#0F766E" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Electric Kettle (Right) -->
    <path d="M32 25 L48 23 C52 23 54 26 54 30 L52 48 C52 52 48 54 42 54 L34 54 C30 54 28 51 28 47 L30 30 C30 26 31 25 32 25 Z" fill="url(#kettle-grad)" />
    <!-- Lid & Spout -->
    <path d="M36 23 L44 23 L42 19 L38 19 Z" fill="#1E293B" />
    <path d="M30 28 L24 25 L25 32 Z" fill="#0D9488" />
    <!-- Kettle Handle -->
    <path d="M51 27 C57 27 58 35 57 42 C56 46 52 47 51 47" stroke="#1E293B" stroke-width="3" stroke-linecap="round" fill="none" />
    <rect x="36" y="34" width="8" height="12" rx="1.5" fill="#CCFBF1" opacity="0.8" />
    <circle cx="40" cy="50" r="1.5" fill="#F87171" />

    <!-- Frying Pan (Front Left) -->
    <ellipse cx="22" cy="46" rx="14" ry="7" fill="url(#pan-grad)" />
    <ellipse cx="22" cy="45" rx="12" ry="5.5" fill="#0F172A" />
    <!-- Pan handle -->
    <path d="M10 46 L2 42" stroke="#1E293B" stroke-width="3.5" stroke-linecap="round" />
    <!-- Wooden Spatula -->
    <path d="M22 20 L27 38 M21 16 L25 22" stroke="#B45309" stroke-width="2.5" stroke-linecap="round" />
  </g>
</svg>"""

# 9. Chips & Namkeen
SVG_DATA["chips_namkeen"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="chips-bag" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="60%" stop-color="#1D4ED8" />
      <stop offset="100%" stop-color="#1E3A8A" />
    </linearGradient>
    <linearGradient id="namkeen-bag" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F97316" />
      <stop offset="70%" stop-color="#EA580C" />
      <stop offset="100%" stop-color="#C2410C" />
    </linearGradient>
    <radialGradient id="chip-gold" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FEF08A" />
      <stop offset="60%" stop-color="#FBBF24" />
      <stop offset="100%" stop-color="#D97706" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Namkeen Bag (Back Left) -->
    <path d="M12 22 L28 17 L36 44 L20 48 Z" fill="url(#namkeen-bag)" />
    <path d="M12 22 L28 17" stroke="#FDE047" stroke-width="2" stroke-linecap="round" />
    <circle cx="23" cy="32" r="5" fill="#FEF08A" />
    <circle cx="23" cy="32" r="3" fill="#DC2626" />

    <!-- Lay's Chips Bag (Center Right) -->
    <path d="M24 16 C28 13 38 13 42 16 L52 46 C50 49 42 51 36 51 C30 51 24 49 22 46 Z" fill="url(#chips-bag)" />
    <path d="M25 16 Q33 13 41 16" stroke="#93C5FD" stroke-width="2" fill="none" />
    <!-- Yellow sun logo -->
    <circle cx="34" cy="29" r="7" fill="#FACC15" />
    <rect x="26" y="27" width="16" height="4" rx="2" fill="#DC2626" />

    <!-- Crispy Potato Chips Spilling (Front) -->
    <ellipse cx="44" cy="45" rx="6" ry="4" fill="url(#chip-gold)" transform="rotate(-20 44 45)" />
    <ellipse cx="32" cy="49" rx="6" ry="3.5" fill="url(#chip-gold)" transform="rotate(15 32 49)" />
    <ellipse cx="48" cy="50" rx="5" ry="3" fill="url(#chip-gold)" transform="rotate(5 48 50)" />
  </g>
</svg>"""

# 10. Sweets & Chocolates
SVG_DATA["sweets_chocolates"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="choco-wrap" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED" />
      <stop offset="60%" stop-color="#6D28D9" />
      <stop offset="100%" stop-color="#4C1D95" />
    </linearGradient>
    <linearGradient id="choco-bar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#58260F" />
      <stop offset="50%" stop-color="#78350F" />
      <stop offset="100%" stop-color="#451A03" />
    </linearGradient>
    <radialGradient id="ladoo-grad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="60%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Chocolate Bar (Left Slanted) -->
    <rect x="14" y="22" width="22" height="32" rx="3" fill="url(#choco-wrap)" transform="rotate(-15 25 38)" />
    <!-- Peeling silver foil -->
    <path d="M14 24 L28 17 L25 11 L11 18 Z" fill="#E2E8F0" stroke="#94A3B8" stroke-width="0.8" />
    <!-- Exposed chocolate cubes -->
    <rect x="14" y="14" width="12" height="12" rx="1.5" fill="url(#choco-bar)" transform="rotate(-15 20 20)" />
    <path d="M16 18 L24 16 M20 15 L18 23" stroke="#451A03" stroke-width="1" />
    <!-- Gold script on wrapper -->
    <path d="M20 34 Q24 32 28 35" stroke="#FDE047" stroke-width="2" stroke-linecap="round" fill="none" />

    <!-- Indian Mithai / Motichoor Ladoo (Right) -->
    <circle cx="45" cy="43" r="11" fill="url(#ladoo-grad)" />
    <circle cx="39" cy="39" r="1.2" fill="#15803D" /> <!-- Pista -->
    <circle cx="48" cy="38" r="1.2" fill="#15803D" />
    <circle cx="44" cy="46" r="1.2" fill="#DC2626" /> <!-- Saffron/Kesar -->
    <circle cx="49" cy="45" r="1" fill="#15803D" />
  </g>
</svg>"""

# 11. Drinks & Juices
SVG_DATA["drinks_juices"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="cola-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A" />
      <stop offset="60%" stop-color="#2563EB" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <linearGradient id="juice-box" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F97316" />
      <stop offset="50%" stop-color="#FB923C" />
      <stop offset="100%" stop-color="#EA580C" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Juice Tetra-Pak (Left) -->
    <rect x="12" y="22" width="18" height="30" rx="3" fill="url(#juice-box)" />
    <!-- Mango on box -->
    <ellipse cx="21" cy="35" rx="5" ry="6" fill="#FACC15" />
    <path d="M21 29 Q23 27 24 28" stroke="#15803D" stroke-width="1.2" fill="none" />
    <!-- Straw -->
    <path d="M24 22 L28 11 L32 11" stroke="#EF4444" stroke-width="2" stroke-linecap="round" fill="none" />

    <!-- Soda Bottle (Right) -->
    <path d="M42 12 L46 12 L47 18 L51 24 L51 48 C51 52 49 54 44 54 C39 54 37 52 37 48 L37 24 L41 18 Z" fill="#0F172A" />
    <!-- Bottle cap -->
    <rect x="42" y="9" width="4" height="4" rx="1" fill="#DC2626" />
    <!-- Blue/Red Cola Label -->
    <rect x="37" y="28" width="14" height="12" fill="url(#cola-grad)" />
    <path d="M39 34 Q44 32 49 34" stroke="#DC2626" stroke-width="2" fill="none" />
    <!-- Carbonation bubbles -->
    <circle cx="41" cy="44" r="1.2" fill="#FFFFFF" opacity="0.6" class="subcat-anim-bubble" />
    <circle cx="45" cy="46" r="1" fill="#FFFFFF" opacity="0.6" class="subcat-anim-bubble" />
    <circle cx="46" cy="42" r="1.4" fill="#FFFFFF" opacity="0.7" class="subcat-anim-bubble" />
  </g>
</svg>"""

# 12. Tea, Coffee & Milk Drinks
SVG_DATA["tea_coffee_milk_drinks"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="mug-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" />
      <stop offset="50%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#B91C1C" />
    </linearGradient>
    <linearGradient id="tea-pack" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#15803D" />
      <stop offset="50%" stop-color="#22C55E" />
      <stop offset="100%" stop-color="#166534" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Green Tea Pack (Back Left) -->
    <path d="M12 20 L26 16 L32 46 L18 50 Z" fill="url(#tea-pack)" />
    <circle cx="21" cy="32" r="4.5" fill="#FEF08A" />
    <!-- Tea leaf emblem -->
    <path d="M21 29 C24 30 25 35 21 35 C17 35 18 30 21 29 Z" fill="#15803D" />

    <!-- Coffee Mug (Right) -->
    <path d="M32 28 C32 28 34 50 44 50 C54 50 56 28 56 28 Z" fill="url(#mug-grad)" />
    <!-- Mug Handle -->
    <path d="M53 32 C58 32 60 38 58 43 C56 46 52 46 51 45" stroke="#B91C1C" stroke-width="3" stroke-linecap="round" fill="none" />
    <!-- Hot dark coffee top -->
    <ellipse cx="44" cy="28" rx="11" ry="3.5" fill="#451A03" />
    <ellipse cx="44" cy="28" rx="8" ry="2" fill="#78350F" />
    <!-- Steam curls -->
    <path d="M40 23 Q38 17 42 13" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round" fill="none" class="subcat-anim-steam" />
    <path d="M46 23 Q48 18 45 13" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round" fill="none" class="subcat-anim-steam" />
  </g>
</svg>"""

# 13. Instant Food
SVG_DATA["instant_food"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="noodle-bowl" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" />
      <stop offset="50%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#B91C1C" />
    </linearGradient>
    <linearGradient id="noodle-gold" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FEF08A" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Noodle Cup/Bowl -->
    <path d="M14 28 L20 52 C21 55 24 56 32 56 C40 56 43 55 44 52 L50 28 Z" fill="url(#noodle-bowl)" />
    <!-- Yellow banner band -->
    <path d="M16 34 L48 34 L46 42 L18 42 Z" fill="#FACC15" />
    <text x="32" y="40" font-size="6" font-weight="900" fill="#DC2626" text-anchor="middle" font-family="sans-serif">2-MIN</text>

    <!-- Wavy Noodles Mound -->
    <ellipse cx="32" cy="28" rx="17" ry="6" fill="url(#noodle-gold)" />
    <path d="M19 27 Q22 23 26 27 Q30 30 34 26 Q38 22 42 27" stroke="#D97706" stroke-width="2" stroke-linecap="round" fill="none" />
    <path d="M23 25 Q27 21 31 25 Q35 28 39 24" stroke="#D97706" stroke-width="2" stroke-linecap="round" fill="none" />

    <!-- Chopsticks lifting noodles -->
    <path d="M46 10 L28 22 M52 11 L28 24" stroke="#78350F" stroke-width="2" stroke-linecap="round" />
    <!-- Green peas & carrot garnish -->
    <circle cx="28" cy="27" r="1.5" fill="#15803D" />
    <circle cx="36" cy="26" r="1.5" fill="#15803D" />
    <rect x="31" y="27" width="2" height="2" fill="#EA580C" />
  </g>
</svg>"""

# 14. Sauces & Spreads
SVG_DATA["sauces_spreads"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="ketchup-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#B91C1C" />
      <stop offset="40%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#991B1B" />
    </linearGradient>
    <linearGradient id="mayo-jar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FEF08A" />
      <stop offset="50%" stop-color="#FFFBEB" />
      <stop offset="100%" stop-color="#FDE047" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Mayo / Peanut Butter Jar (Right) -->
    <rect x="33" y="24" width="22" height="28" rx="4" fill="url(#mayo-jar)" stroke="#F59E0B" stroke-width="1" />
    <!-- Blue lid -->
    <ellipse cx="44" cy="23" rx="10" ry="3" fill="#2563EB" />
    <!-- Label -->
    <rect x="35" y="32" width="18" height="12" rx="2" fill="#FFFFFF" />
    <circle cx="44" cy="38" r="3" fill="#D97706" />

    <!-- Ketchup Squeeze Bottle (Left) -->
    <path d="M16 20 C16 18 19 16 23 16 C27 16 30 18 30 20 L31 48 C31 52 28 54 23 54 C18 54 15 52 15 48 Z" fill="url(#ketchup-grad)" />
    <!-- Yellow spout cap -->
    <path d="M21 16 L25 16 L24 10 L22 10 Z" fill="#FACC15" />
    <!-- White label with tomato -->
    <ellipse cx="23" cy="35" rx="5" ry="6" fill="#FFFFFF" />
    <circle cx="23" cy="36" r="3" fill="#DC2626" />
    <path d="M23 32 L23 33" stroke="#15803D" stroke-width="1.5" stroke-linecap="round" />
  </g>
</svg>"""

# 15. Paan Corner
SVG_DATA["paan_corner"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="paan-leaf" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22C55E" />
      <stop offset="60%" stop-color="#16A34A" />
      <stop offset="100%" stop-color="#14532D" />
    </linearGradient>
    <linearGradient id="brass-tin" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D97706" />
      <stop offset="50%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Traditional Brass Mukhwas Tin (Right) -->
    <ellipse cx="44" cy="38" rx="14" ry="7" fill="url(#brass-tin)" />
    <path d="M30 38 L30 46 C30 50 36 53 44 53 C52 53 58 50 58 46 L58 38 Z" fill="#B45309" />
    <ellipse cx="44" cy="36" rx="12" ry="5" fill="#FEF08A" />
    <!-- Fennel seeds / Saunf -->
    <ellipse cx="41" cy="35" rx="1.5" ry="0.8" fill="#16A34A" transform="rotate(30 41 35)" />
    <ellipse cx="46" cy="36" rx="1.5" ry="0.8" fill="#EC4899" transform="rotate(-20 46 36)" />
    <ellipse cx="43" cy="37" rx="1.5" ry="0.8" fill="#FFFFFF" transform="rotate(10 43 37)" />

    <!-- Folded Meetha Paan Triangle (Left) -->
    <path d="M12 44 L28 16 L38 38 Z" fill="url(#paan-leaf)" />
    <!-- Silver vark foil -->
    <polygon points="24,26 31,23 29,32 23,30" fill="#E2E8F0" opacity="0.85" />
    <!-- Red Cherry Clove on top -->
    <circle cx="26" cy="22" r="3.5" fill="#DC2626" />
    <circle cx="25" cy="21" r="1" fill="#FFFFFF" opacity="0.7" />
    <path d="M26 19 L27 16" stroke="#451A03" stroke-width="1.5" stroke-linecap="round" />
  </g>
</svg>"""

# 16. Ice Creams & More
SVG_DATA["ice_creams_more"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="cone-waffle" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="50%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <radialGradient id="strawberry-scoop" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#FDA4AF" />
      <stop offset="60%" stop-color="#F43F5E" />
      <stop offset="100%" stop-color="#BE123C" />
    </radialGradient>
    <linearGradient id="bar-choco" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#58260F" />
      <stop offset="60%" stop-color="#78350F" />
      <stop offset="100%" stop-color="#451A03" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Chocolate Popsicle Bar (Right) -->
    <rect x="36" y="16" width="18" height="26" rx="9" fill="url(#bar-choco)" />
    <!-- Stick -->
    <rect x="42" y="42" width="6" height="12" rx="2" fill="#FDE047" stroke="#D97706" stroke-width="0.8" />
    <!-- White bite mark -->
    <circle cx="52" cy="19" r="4.5" fill="#FAF5EF" />

    <!-- Waffle Cone (Left) -->
    <polygon points="12,32 28,32 20,54" fill="url(#cone-waffle)" />
    <path d="M14 36 L24 48 M16 42 L22 50 M26 36 L16 48" stroke="#92400E" stroke-width="0.8" stroke-linecap="round" />
    <!-- Strawberry Scoop -->
    <circle cx="20" cy="24" r="10" fill="url(#strawberry-scoop)" />
    <!-- Chocolate Drizzle & Cherry -->
    <path d="M14 24 Q17 28 20 25 Q23 28 26 24" stroke="#451A03" stroke-width="2" fill="none" />
    <circle cx="20" cy="13" r="3" fill="#DC2626" />
    <path d="M21 11 Q24 8 26 9" stroke="#15803D" stroke-width="1.2" fill="none" />
  </g>
</svg>"""

# 17. Bath & Body
SVG_DATA["bath_body"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="bottle-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0D9488" />
      <stop offset="50%" stop-color="#14B8A6" />
      <stop offset="100%" stop-color="#0F766E" />
    </linearGradient>
    <radialGradient id="soap-bar" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#E0F2FE" />
      <stop offset="60%" stop-color="#BAE6FD" />
      <stop offset="100%" stop-color="#38BDF8" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Body Wash Pump Bottle (Left) -->
    <rect x="14" y="22" width="20" height="30" rx="6" fill="url(#bottle-grad)" />
    <!-- Pump Dispenser -->
    <rect x="22" y="16" width="4" height="6" fill="#E2E8F0" />
    <path d="M18 16 L28 16 L31 18 L28 18 L28 20 L22 20 Z" fill="#475569" />
    <!-- Bottle label -->
    <rect x="18" y="30" width="12" height="14" rx="2" fill="#FFFFFF" opacity="0.9" />
    <path d="M21 37 L27 37" stroke="#0D9488" stroke-width="1.8" stroke-linecap="round" />

    <!-- Organic Soap Bar (Right) -->
    <rect x="36" y="34" width="22" height="15" rx="5" fill="url(#soap-bar)" stroke="#0284C7" stroke-width="0.8" />
    <ellipse cx="47" cy="41.5" rx="6" ry="3" fill="#FFFFFF" opacity="0.5" />
    <!-- Floating Lather Bubbles -->
    <circle cx="42" cy="26" r="3.5" fill="#E0F2FE" stroke="#38BDF8" stroke-width="0.8" opacity="0.8" class="subcat-anim-bubble" />
    <circle cx="49" cy="22" r="2.5" fill="#E0F2FE" stroke="#38BDF8" stroke-width="0.8" opacity="0.8" class="subcat-anim-bubble" />
    <circle cx="36" cy="28" r="2" fill="#E0F2FE" stroke="#38BDF8" stroke-width="0.8" opacity="0.8" class="subcat-anim-bubble" />
  </g>
</svg>"""

# 18. Hair
SVG_DATA["hair"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="shampoo-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="50%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="oil-hair" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="50%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Shampoo Bottle (Center Left) -->
    <path d="M16 20 C16 16 20 14 26 14 C32 14 36 16 36 20 L35 48 C35 52 31 54 26 54 C21 54 17 52 17 48 Z" fill="url(#shampoo-grad)" />
    <!-- Flip cap -->
    <rect x="22" y="10" width="8" height="4" rx="2" fill="#047857" />
    <!-- Sleek shine stripe -->
    <path d="M21 22 L19 46" stroke="#A7F3D0" stroke-width="1.8" stroke-linecap="round" opacity="0.7" />

    <!-- Nourishing Hair Oil Bottle (Right) -->
    <path d="M40 25 L48 25 L48 48 C48 51 45 53 44 53 C43 53 40 51 40 48 Z" fill="url(#oil-hair)" opacity="0.9" />
    <rect x="42" y="21" width="4" height="4" fill="#D97706" />
    <!-- Oil Droplet -->
    <path d="M44 14 C44 14 47 18 47 19 C47 20.5 45.5 22 44 22 C42.5 22 41 20.5 41 19 C41 18 44 14 44 14 Z" fill="#F59E0B" />

    <!-- Wide Tooth Comb (Foreground) -->
    <rect x="12" y="47" width="28" height="4" rx="1.5" fill="#451A03" />
    <path d="M15 47 L15 53 M19 47 L19 53 M23 47 L23 53 M27 47 L27 53 M31 47 L31 53 M35 47 L35 53" stroke="#451A03" stroke-width="1.5" stroke-linecap="round" />
  </g>
</svg>"""

# 19. Skin & Face
SVG_DATA["skin_face"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="serum-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F43F5E" />
      <stop offset="50%" stop-color="#FB7185" />
      <stop offset="100%" stop-color="#E11D48" />
    </linearGradient>
    <linearGradient id="cream-jar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFBEB" />
      <stop offset="60%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#FEF3C7" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Luxury Face Cream Jar (Right) -->
    <rect x="30" y="32" width="26" height="20" rx="5" fill="url(#cream-jar)" stroke="#FDE68A" stroke-width="1" />
    <!-- Rose gold lid -->
    <ellipse cx="43" cy="31" rx="13" ry="4" fill="#F59E0B" />
    <ellipse cx="43" cy="30" rx="13" ry="4" fill="#FCD34D" />

    <!-- Serum Dropper Bottle (Left) -->
    <rect x="12" y="24" width="16" height="28" rx="4" fill="url(#serum-grad)" />
    <!-- Pipette Dropper Top -->
    <rect x="17" y="19" width="6" height="5" fill="#1F2937" />
    <path d="M18 19 C18 14 22 14 22 19 Z" fill="#4B5563" />
    <!-- Dropper Pipette Glass Tip -->
    <circle cx="20" cy="11" r="1.5" fill="#FB7185" />
    <!-- Label -->
    <rect x="14" y="32" width="12" height="12" rx="1.5" fill="#FFFFFF" opacity="0.9" />
    <circle cx="20" cy="38" r="2.5" fill="#F43F5E" />
  </g>
</svg>"""

# 20. Beauty & Cosmetics
SVG_DATA["beauty_cosmetics"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="lipstick-bullet" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#BE123C" />
      <stop offset="50%" stop-color="#E11D48" />
      <stop offset="100%" stop-color="#9F1239" />
    </linearGradient>
    <linearGradient id="gold-casing" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D97706" />
      <stop offset="50%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Compact Blush Powder (Right) -->
    <circle cx="44" cy="41" r="13" fill="#1F2937" />
    <circle cx="44" cy="41" r="10.5" fill="#FDA4AF" />
    <ellipse cx="44" cy="41" rx="8" ry="5" fill="#F43F5E" opacity="0.8" />

    <!-- Lipstick (Left) -->
    <rect x="16" y="36" width="12" height="18" rx="2" fill="#1F2937" />
    <rect x="17" y="27" width="10" height="9" fill="url(#gold-casing)" />
    <!-- Angled Bullet -->
    <path d="M18 27 L18 19 C18 15 22 13 24 13 L26 19 L26 27 Z" fill="url(#lipstick-bullet)" />

    <!-- Mascara Wand (Top Right) -->
    <path d="M38 12 L54 26" stroke="#4B5563" stroke-width="2.5" stroke-linecap="round" />
    <path d="M34 9 L38 12" stroke="#1F2937" stroke-width="4.5" stroke-linecap="round" />
  </g>
</svg>"""

# 21. Feminine Hygiene
SVG_DATA["feminine_hygiene"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="pad-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="50%" stop-color="#FCE7F3" />
      <stop offset="100%" stop-color="#FBCFE8" />
    </linearGradient>
    <radialGradient id="flower-center" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#F472B6" />
      <stop offset="100%" stop-color="#DB2777" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Sanitary Pad with Wings -->
    <path d="M24 12 C18 12 14 18 15 26 C15 30 13 32 10 33 C13 34 15 36 15 40 C14 48 18 54 24 54 C30 54 34 48 33 40 C33 36 35 34 38 33 C35 32 33 30 33 26 C34 18 30 12 24 12 Z" fill="url(#pad-grad)" stroke="#F472B6" stroke-width="1.2" />
    <!-- Embossed contour channels -->
    <path d="M22 18 C20 24 20 42 22 48 M26 18 C28 24 28 42 26 48" stroke="#F472B6" stroke-width="1" stroke-linecap="round" fill="none" opacity="0.6" />

    <!-- Soft Cotton Blossom / Flower (Right) -->
    <g transform="translate(42, 38)">
      <circle cx="0" cy="-6" r="5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" />
      <circle cx="6" cy="-2" r="5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" />
      <circle cx="4" cy="5" r="5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" />
      <circle cx="-4" cy="5" r="5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" />
      <circle cx="-6" cy="-2" r="5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" />
      <circle cx="0" cy="0" r="4" fill="url(#flower-center)" />
    </g>
  </g>
</svg>"""

# 22. Baby Care
SVG_DATA["baby_care"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="feeding-bottle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E0F2FE" />
      <stop offset="50%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#BAE6FD" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Baby Milk Bottle (Left) -->
    <rect x="16" y="24" width="18" height="28" rx="5" fill="url(#feeding-bottle)" stroke="#38BDF8" stroke-width="1" />
    <!-- Collar & Teat -->
    <rect x="18" y="18" width="14" height="6" rx="2" fill="#FDE047" />
    <path d="M22 18 C22 13 28 13 28 18 Z" fill="#FBBF24" opacity="0.9" />
    <!-- Measurement lines -->
    <path d="M19 32 L24 32 M19 37 L23 37 M19 42 L24 42" stroke="#0284C7" stroke-width="1.2" stroke-linecap="round" />

    <!-- Pastel Baby Rattle (Right) -->
    <circle cx="44" cy="26" r="10" fill="#F472B6" />
    <circle cx="44" cy="26" r="6" fill="#FDF2F8" />
    <!-- Rattle Handle -->
    <path d="M44 36 L44 50" stroke="#38BDF8" stroke-width="3" stroke-linecap="round" />
    <circle cx="44" cy="52" r="3" fill="#FACC15" />
    <!-- Soft rattle beads -->
    <circle cx="44" cy="26" r="2.5" fill="#F43F5E" />
  </g>
</svg>"""

# 23. Health & Pharma
SVG_DATA["health_pharma"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="medicine-bottle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E2E8F0" />
      <stop offset="50%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#CBD5E1" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Medicine Bottle (Left) -->
    <rect x="12" y="22" width="20" height="30" rx="4" fill="url(#medicine-bottle)" stroke="#94A3B8" stroke-width="1" />
    <rect x="16" y="16" width="12" height="6" rx="2" fill="#DC2626" />
    <!-- First Aid Red Cross on bottle -->
    <rect x="16" y="28" width="12" height="12" rx="2" fill="#DC2626" />
    <path d="M22 31 L22 37 M19 34 L25 34" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />

    <!-- Capsule Blister Strip (Right) -->
    <rect x="34" y="20" width="20" height="32" rx="3" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1" />
    <!-- Capsules -->
    <g transform="translate(39, 26)">
      <rect x="0" y="0" width="10" height="4" rx="2" fill="#2563EB" />
      <rect x="5" y="0" width="5" height="4" rx="2" fill="#EF4444" />
    </g>
    <g transform="translate(39, 34)">
      <rect x="0" y="0" width="10" height="4" rx="2" fill="#10B981" />
      <rect x="5" y="0" width="5" height="4" rx="2" fill="#FBBF24" />
    </g>
    <g transform="translate(39, 42)">
      <rect x="0" y="0" width="10" height="4" rx="2" fill="#EF4444" />
      <rect x="5" y="0" width="5" height="4" rx="2" fill="#FFFFFF" stroke="#EF4444" stroke-width="0.5" />
    </g>
  </g>
</svg>"""

# 24. Sexual Wellness
SVG_DATA["sexual_wellness"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="shield-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#818CF8" />
      <stop offset="50%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#4338CA" />
    </linearGradient>
    <linearGradient id="feather-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E879F9" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Wellness Shield (Center) -->
    <path d="M32 14 C42 14 46 20 46 30 C46 42 36 50 32 54 C28 50 18 42 18 30 C18 20 22 14 32 14 Z" fill="url(#shield-grad)" />
    <!-- Inner heart/care emblem -->
    <path d="M32 25 C30 22 26 22 24 25 C22 28 24 33 32 38 C40 33 42 28 40 25 C38 22 34 22 32 25 Z" fill="#FDF4FF" opacity="0.9" />

    <!-- Soft Feather (Floating on right) -->
    <path d="M40 28 C48 24 54 30 50 38 C47 43 42 42 40 28 Z" fill="url(#feather-grad)" opacity="0.85" />
    <path d="M40 28 L49 39" stroke="#FFFFFF" stroke-width="1" stroke-linecap="round" opacity="0.7" />
  </g>
</svg>"""

# 25. Home & Lifestyle
SVG_DATA["home_lifestyle"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="candle-jar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FEF3C7" />
      <stop offset="50%" stop-color="#FFFBEB" />
      <stop offset="100%" stop-color="#FDE68A" />
    </linearGradient>
    <radialGradient id="flame-grad" cx="40%" cy="60%" r="60%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="40%" stop-color="#FDE047" />
      <stop offset="80%" stop-color="#F97316" />
      <stop offset="100%" stop-color="#DC2626" />
    </radialGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Aromatic Candle Jar (Left) -->
    <rect x="14" y="28" width="20" height="24" rx="4" fill="url(#candle-jar)" stroke="#D97706" stroke-width="1" />
    <path d="M24 28 L24 24" stroke="#451A03" stroke-width="1.8" stroke-linecap="round" />
    <!-- Candle Flame -->
    <path d="M24 14 C21 18 21 23 24 24 C27 23 27 18 24 14 Z" fill="url(#flame-grad)" class="subcat-anim-flicker" />

    <!-- Potted Indoor Succulent Plant (Right) -->
    <!-- Ceramic Terracotta Pot -->
    <polygon points="38,36 54,36 51,52 41,52" fill="#D97706" />
    <rect x="36" y="34" width="20" height="4" rx="1.5" fill="#B45309" />
    <!-- Green Succulent Leaves -->
    <path d="M46 34 C44 26 40 22 43 20 C46 22 48 26 46 34 Z" fill="#15803D" />
    <path d="M46 34 C41 29 36 28 36 31 C38 34 43 34 46 34 Z" fill="#16A34A" />
    <path d="M46 34 C51 29 56 28 56 31 C54 34 49 34 46 34 Z" fill="#22C55E" />
  </g>
</svg>"""

# 26. Cleaners & Repellents
SVG_DATA["cleaners_repellents"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="spray-bottle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" />
      <stop offset="50%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#0369A1" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Spray Cleaner Bottle (Left) -->
    <path d="M16 26 L26 26 L27 52 C27 54 25 55 21 55 C17 55 15 54 15 52 Z" fill="url(#spray-bottle)" />
    <!-- Trigger Spray Head -->
    <rect x="18" y="22" width="6" height="4" fill="#E2E8F0" />
    <path d="M14 20 L28 17 L28 22 L24 22 L23 26 L17 26 Z" fill="#1E293B" />
    <path d="M14 20 L11 20" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round" />
    <!-- Spray Mist droplets -->
    <circle cx="8" cy="18" r="1" fill="#38BDF8" class="subcat-anim-bubble" />
    <circle cx="6" cy="22" r="1.2" fill="#38BDF8" class="subcat-anim-bubble" />

    <!-- Mosquito Repellent Vaporizer (Right) -->
    <rect x="36" y="32" width="18" height="20" rx="4" fill="#6366F1" />
    <rect x="39" y="27" width="12" height="5" rx="1.5" fill="#818CF8" />
    <!-- Blue Glow Lamp -->
    <circle cx="45" cy="40" r="4" fill="#C7D2FE" />
    <circle cx="45" cy="40" r="2" fill="#FFFFFF" />
  </g>
</svg>"""

# 27. Electronics
SVG_DATA["electronics"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="earbuds-case" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="60%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Wireless Earbuds Case (Left) -->
    <rect x="12" y="24" width="24" height="22" rx="9" fill="url(#earbuds-case)" stroke="#CBD5E1" stroke-width="1" />
    <line x1="12" y1="33" x2="36" y2="33" stroke="#94A3B8" stroke-width="0.8" />
    <!-- Green LED battery indicator -->
    <circle cx="24" cy="38" r="1.5" fill="#10B981" />

    <!-- AA Battery Cell (Right) -->
    <rect x="42" y="24" width="12" height="24" rx="2" fill="#1E293B" />
    <rect x="42" y="24" width="12" height="8" rx="1" fill="#F59E0B" />
    <!-- Positive terminal nipple -->
    <rect x="46" y="21" width="4" height="3" rx="1" fill="#94A3B8" />
    <text x="48" y="44" font-size="6" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="sans-serif">+</text>

    <!-- Braided USB Cable Curve -->
    <path d="M18 50 C26 58 38 58 46 52" stroke="#3B82F6" stroke-width="2.5" stroke-linecap="round" fill="none" />
  </g>
</svg>"""

# 28. Stationery & Games
SVG_DATA["stationery_games"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="notebook-cover" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="50%" stop-color="#FBBF24" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Spiral Notebook (Left) -->
    <rect x="14" y="18" width="24" height="34" rx="3" fill="url(#notebook-cover)" />
    <rect x="18" y="18" width="20" height="34" fill="#FEF3C7" />
    <!-- Notebook lines -->
    <line x1="22" y1="26" x2="34" y2="26" stroke="#D97706" stroke-width="1" />
    <line x1="22" y1="32" x2="34" y2="32" stroke="#D97706" stroke-width="1" />
    <line x1="22" y1="38" x2="34" y2="38" stroke="#D97706" stroke-width="1" />
    <!-- Spiral coils -->
    <circle cx="14" cy="22" r="1.5" fill="#475569" />
    <circle cx="14" cy="28" r="1.5" fill="#475569" />
    <circle cx="14" cy="34" r="1.5" fill="#475569" />
    <circle cx="14" cy="40" r="1.5" fill="#475569" />

    <!-- Gaming Controller / Dice (Right) -->
    <rect x="36" y="28" width="18" height="18" rx="4" fill="#8B5CF6" />
    <!-- White pips for dice or controller buttons -->
    <circle cx="41" cy="33" r="1.8" fill="#FFFFFF" />
    <circle cx="49" cy="33" r="1.8" fill="#F43F5E" />
    <circle cx="45" cy="37" r="1.8" fill="#10B981" />
    <circle cx="41" cy="41" r="1.8" fill="#FACC15" />
    <circle cx="49" cy="41" r="1.8" fill="#FFFFFF" />
  </g>
</svg>"""

# 29. Stores
SVG_DATA["stores"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="bag-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="60%" stop-color="#F8CB46" />
      <stop offset="100%" stop-color="#EAB308" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Blinkit Yellow Delivery Bag -->
    <path d="M15 24 L49 24 L46 54 L18 54 Z" fill="url(#bag-grad)" />
    <!-- Bag handles -->
    <path d="M25 24 C25 15 39 15 39 24" stroke="#0C831F" stroke-width="3" stroke-linecap="round" fill="none" />
    <!-- Store Awning on top -->
    <path d="M12 24 L52 24 L49 18 L15 18 Z" fill="#0C831F" />
    <!-- Electric Speedy Lightning Bolt in center -->
    <polygon points="34,28 26,38 32,38 30,48 38,36 32,36" fill="#1F1F1F" />
    <!-- Green Accent Tag -->
    <rect x="22" y="49" width="20" height="3" rx="1.5" fill="#0C831F" />
  </g>
</svg>"""

# 30. E-Cards
SVG_DATA["e_cards"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">
  <defs>
    <linearGradient id="card-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FEF08A" />
      <stop offset="50%" stop-color="#F8CB46" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
  </defs>
  <g class="subcat-anim-float">
    <!-- Gift Card Rectangle (Sleek angle) -->
    <rect x="10" y="20" width="44" height="28" rx="5" fill="url(#card-gold)" stroke="#B45309" stroke-width="1" />
    <!-- Satin Red Ribbon horizontal & vertical -->
    <rect x="10" y="31" width="44" height="6" fill="#DC2626" />
    <rect x="28" y="20" width="6" height="28" fill="#DC2626" />
    <!-- Ribbon Bow loops -->
    <circle cx="28" cy="28" r="4.5" fill="#EF4444" />
    <circle cx="34" cy="28" r="4.5" fill="#EF4444" />
    <circle cx="31" cy="28" r="2.5" fill="#B91C1C" />

    <!-- Sparkles -->
    <path d="M46 14 L47 17 L50 18 L47 19 L46 22 L45 19 L42 18 L45 17 Z" fill="#FBBF24" class="subcat-anim-sparkle" />
    <path d="M14 44 L15 46 L17 47 L15 48 L14 50 L13 48 L11 47 L13 46 Z" fill="#FBBF24" class="subcat-anim-sparkle" />
  </g>
</svg>"""

# Write each SVG to file
for slug, svg_content in SVG_DATA.items():
    file_path = ASSETS_DIR / f"{slug}.svg"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Wrote {file_path}")

print(f"Successfully generated {len(SVG_DATA)} SVG assets!")
