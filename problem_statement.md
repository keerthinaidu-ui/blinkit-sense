Writing

# BlinkitSense — Problem Statement

## 1\. Product Overview

**Product:** Blinkit\
**Concept:** BlinkitSense\
**Purpose:** Demonstrate how contextual product discovery can encourage habitual customers to try relevant products from new categories during their existing shopping journeys.

BlinkitSense is a fictional, mobile-first shopping prototype using predefined demo data. It is not an official Blinkit feature and does not connect to Blinkit's production systems.

## 2\. Problem Hypothesis

Frequent quick-commerce customers often repeatedly purchase products from familiar categories without exploring others. During urgent purchases, speed and availability dominate. During routine purchases, established habits and familiar products reduce experimentation.

**Hypothesis:** Relevant, context-aware product recommendations, supported by clear explanations, can encourage customers to try products from categories they have not previously adopted.

**How might we help habitual Blinkit customers discover relevant new-category products without disrupting their existing shopping journeys or forcing irrelevant recommendations?**

## 3\. Demo Persona

Rohan Mehta is a fictional Blinkit customer used consistently across all three scenarios.

| Attribute | Demo value |
| --- | --- |
| Age | 29 |
| Location | Bengaluru |
| Occupation | Product Manager |
| Household | Lives alone |
| Blinkit tenure | 2 years |
| Monthly orders | 4–6 |
| Typical order value | ₹600–₹800 |

These attributes and behavioral preferences are illustrative, not actual customer research findings.

### Shopping preferences

- Generally prefers products under ₹500.
- Prefers products rated 4 stars or above.
- Values substantial review counts and familiar, value-oriented brands.
- Is more willing to try unfamiliar products when their benefits are clear.

### Search and browsing history

The configured demo history includes searches for:

- Pasta recipes
- Chilli flakes
- Pasta strainer
- Baking paper
- Quick healthy breakfast
- Protein breakfast
- Easy dinner ideas

Browsed products and categories include pasta sauces, cheese, cooking ingredients, pasta strainers, coffee, yogurt and granola.

These signals may influence recommendations only when relevant to the selected shopping mission.

## 4\. Historical Orders and Habit Memory

Rohan has the following eight historical orders. This history remains identical across all three scenarios.

| Week | Order total | Products |
| --- | --- | --- |
| 1 | ₹612 | Milk, eggs, bread, bananas, pasta, pasta sauce, chips, Coke |
| 2 | ₹487 | Milk, eggs, bread, chicken, onions, tomatoes, coffee, biscuits |
| 3 | ₹731 | Milk, eggs, vegetables, pasta, pasta sauce, cheese, chilli flakes, Coke, Maggi |
| 4 | ₹563 | Milk, eggs, bread, chicken, rice, dal, coffee, chips |
| 5 | ₹804 | Milk, eggs, vegetables, pasta, pasta sauce, mushrooms, cheese, coffee, Coke |
| 6 | **₹628** | Milk, bread, eggs, bananas, Maggi, biscuits, chips, shampoo |
| 7 | ₹692 | Milk, eggs, chicken, onions, tomatoes, pasta, cheese, pasta sauce, Coke |
| 8 | ₹618 | Milk, eggs, bread, mushrooms, pasta, pasta sauce, cheese, coffee, biscuits |

**Week 6 total:** ₹429 + ₹199 for shampoo = **₹628**.

The Week 6 historical order must contain shampoo as a separate line item priced at ₹199. Its line-item totals must reconcile to ₹628. The other seven order totals must remain unchanged.

Use a single structured historical dataset containing order IDs, weeks, product IDs, product names, categories, quantities, unit prices, line totals and order totals. Where exact historical line-item prices are unavailable, use clearly labelled illustrative values and reconcile them to the specified order totals.

### Established purchase patterns

- **Routine essentials:** Milk, eggs, bread and fruit.
- **Weekend cooking:** Pasta, pasta sauce, cheese, mushrooms, chicken and vegetables.
- **Snacks and beverages:** Coffee, Coke, chips, biscuits and Maggi.

### Category adoption

Category adoption must be derived from the product-level historical records using a consistent rule: a category is adopted if at least one product belonging to that category appears in the historical orders.

Do not invent exact category order counts or claim a category is new when the historical records show otherwise. If a product's category mapping is ambiguous, configure its category explicitly before calculating adoption.

A new product and a new category are different: an unfamiliar product does not qualify as new-category discovery if its category has already been adopted.

### Habit Memory

Habit Memory is derived from Rohan's historical orders, not the selected scenario. It must remain unchanged throughout the demo.

The cart page includes an **Order Again** section that prioritizes suitable previously tried products when justified, followed by familiar repeat purchases.

- Shampoo is a previously tried product, not a new product discovery.
- Do not automatically recommend shampoo simply because it appears in Week 6.
- Recommend replenishment only when supported by product type, recorded purchase frequency, elapsed time and reasonable, explicitly configured usage assumptions.
- Do not automatically recommend durable products, such as a pasta strainer, for replenishment.
- If no previously tried product is suitable for replenishment, show familiar repeat purchases.
- Do not claim that Rohan enjoyed or positively rated a product without supporting data.

## 5\. Scenario Independence

All three scenarios use the same persona and persistent historical order history, but each has its own independent shopping session.

When a scenario is selected:

- Start with an empty active cart.
- Reset scenario-specific search, browsing and temporary selections.
- Load that scenario's context and relevant shopping journey.
- Preserve all eight historical orders and Habit Memory.

Products added to one scenario's cart must never appear in another scenario's cart or be added to historical Orders. Only a separately simulated checkout may display a completion state; it must not silently rewrite the predefined historical order dataset.

## 6\. Home-Screen Category Taxonomy

The home screen displays the following four top-level categories and their subcategories. All category and subcategory labels remain visible in every scenario.

Only categories, subcategories and catalogue products relevant to the selected guided scenario are highlighted and clickable. Other items remain visible but non-interactive. BlinkitSense recommendation products are clickable **only on the cart page**, never on the home screen.

### Grocery & Kitchen

- Vegetables & Fruits
- Atta, Rice & Dal
- Oil, Ghee & Masala
- Dairy, Bread & Eggs
- Bakery & Biscuits
- Dry Fruits & Cereals
- Chicken, Meat & Fish
- Kitchenware & Appliances

### Snacks & Drinks

- Chips & Namkeen
- Sweets & Chocolates
- Drinks & Juices
- Tea, Coffee & Milk Drinks
- Instant Food
- Sauces & Spreads
- Paan Corner
- Ice Creams & More

### Beauty & Personal Care

- Bath & Body
- Hair
- Skin & Face
- Beauty & Cosmetics
- Feminine Hygiene
- Baby Care
- Health & Pharma
- Sexual Wellness

### Household Essentials

- Home & Lifestyle
- Cleaners & Repellents
- Electronics
- Stationery & Games
- Stores
- E-Cards

### Guided product mappings

**Scenario 1 — Cooking at Home**

- Pasta → Instant Food
- Pasta sauce → Sauces & Spreads
- Mushrooms → Vegetables & Fruits
- Cheese → Dairy, Bread & Eggs
- Chilli flakes → Oil, Ghee & Masala

**Scenario 2 — Quick Breakfast**

- Bananas → Vegetables & Fruits
- Greek yogurt → Dairy, Bread & Eggs
- Granola → Instant Food
- Orange juice → Drinks & Juices

**Scenario 3 — First-Time Period Care**

- Sanitary pads → Feminine Hygiene
- Dark chocolate → Sweets & Chocolates
- Ice cream → Ice Creams & More

These mappings are authoritative for the guided demo. Each product must exist in the configured catalogue, have a stable product ID and belong to its assigned subcategory. Do not display unavailable products as selectable items.

## 7\. Scenario 1 — Saturday Evening: Cooking at Home

**Context:** Saturday, 7:05 PM, Bengaluru, heavy rain.

**Mission:** Prepare dinner at home.

The cart starts empty. The evaluator can navigate relevant categories and add pasta, pasta sauce, mushrooms, cheese and chilli flakes through the shopping interface.

Potential BlinkitSense discovery candidates:

| Product | Demo price | Category |
| --- | --- | --- |
| Silicone Pasta Colander | ₹249 | Kitchenware & Appliances |
| Hot Chocolate | ₹199 | Tea, Coffee & Milk Drinks |
| Garlic Bread | ₹129 | Bakery & Biscuits |

These are illustrative demo candidates, not verified live Blinkit listings. Show a candidate only if its category has not already been adopted, its catalogue data is complete and its relevance to the current mission is defensible.

## 8\. Scenario 2 — Monday Morning: Quick Breakfast

**Context:** Monday, 8:15 AM, Bengaluru, hot and sunny. Rohan has a 9:30 AM meeting.

**Mission:** Find a quick, low-effort breakfast before work.

The cart starts empty. The evaluator can add bananas, Greek yogurt, granola and orange juice.

Potential BlinkitSense discovery candidates:

| Product | Demo price | Category |
| --- | --- | --- |
| Protein Breakfast Bar | ₹149 | Chips & Namkeen |
| Overnight Oats Cup | ₹179 | Instant Food |
| Coconut Water | ₹99 | Drinks & Juices |

All prices are illustrative. Product descriptions and category assignments must be configured consistently in the catalogue. Only candidates from eligible, unadopted categories may count as new-category discovery.

## 9\. Scenario 3 — Wednesday Evening: First-Time Period Care

**Context:** Wednesday, 8:20 PM, Bengaluru, warm evening.

**Mission:** Period-care shopping initiated through explicit user actions.

The cart starts empty. The evaluator searches for "sanitary pads", selects an available demo product and adds it to the cart. Dark chocolate and ice cream can be added separately.

Potential BlinkitSense discovery candidates:

| Product | Demo price | Category |
| --- | --- | --- |
| Period Heat Patch | ₹199 | Requires explicit catalogue classification |
| Pain Relief Balm | ₹149 | Requires explicit catalogue classification |
| Flowers | ₹249 | Gifting, only if configured |

Do not infer who the products are for, whether anyone is experiencing pain, or any medical, relationship or personal circumstance. Do not make medical claims. Exclude candidates whose category, intended use or relevance cannot be established from the configured data. Flowers must remain optional.

## 10\. BlinkitSense Recommendation Engine

Implement deterministic, explainable contextual recommendation rules using the local demo dataset. No external AI service is required.

The engine evaluates:

1. Current scenario and shopping mission.
2. Current cart and explicit search intent.
3. Historical purchases and category adoption.
4. Relevant configured search and browsing history.
5. Configured user preferences.
6. Time, weather and occasion where relevant.

The engine must first identify eligible unadopted categories, then evaluate catalogue candidates for relevance and rank the strongest matches. It must exclude candidates with missing data, unsupported assumptions, unjustified relevance, duplicate cart items without a clear reason, or ineligible category-adoption status.

Display up to three recommendations on the cart page. Each card may show:

- Product name, configured price and category.
- Image or placeholder.
- Rating and review count only when explicitly configured.
- "New for you" only when historical data supports the label.
- A concise "Why this?" explanation grounded in actual demo signals.
- An Add button.

Adding a recommendation updates the active cart only. It does not change historical purchases or automatically mark the product or category as adopted. If no suitable candidate exists, display an appropriate no-recommendation state instead of forcing discovery.

## 11\. Required Screens and Interactions

### Home

- Compact delivery-location header and search bar.
- Four top-level categories and their subcategories.
- Scenario-specific highlights and clickability.
- Product browsing and add-to-cart actions for relevant catalogue products.
- Live cart count.
- Bottom navigation for Home, Orders and Cart.
- Visible selected-scenario indicator.

### Cart

- Current cart items, quantities, removal controls and calculated subtotal.
- Habit Memory and Order Again.
- Contextual BlinkitSense recommendations.
- Simulated checkout with a completion summary.

### Orders

- All eight historical orders, their weeks, totals and products.
- Week 6 shampoo at ₹199 and order total ₹628.
- An Order Again action where supported by the catalogue.

The Orders screen and Habit Memory must use the same historical dataset. Cart changes must never mutate historical orders. If an historical product is absent from the catalogue, explain that it cannot be added rather than substituting another product.

## 12\. Technical Constraints

- Python and Streamlit.
- Local JSON or Python files for the persona, product catalogue, scenarios and historical orders.
- Streamlit session state for navigation, selected scenario, active cart, search and temporary interaction state.
- Custom CSS for a mobile-first, Blinkit-inspired interface.
- Streamlit Community Cloud as the sole deployment target.
- No mandatory API keys, paid services, external database or live Blinkit integration.

Use stable product IDs, a single source of truth for historical orders, validated scenario-to-product mappings and calculated cart totals. Switching scenarios must reset the cart and temporary state without clearing the persistent order history. Streamlit reruns must not unexpectedly empty the active cart.

The interface may use Blinkit-inspired colours and shopping patterns but must not imply official affiliation. Product photography, availability, ratings, review counts and customer feedback must not be fabricated or presented as verified live data.

## 13\. Acceptance Criteria

- The app opens on scenario selection, and all three scenarios work.
- Every scenario starts with an empty cart.
- Scenario carts remain independent; historical orders and Habit Memory persist.
- The home screen follows the specified taxonomy and clickability rules.
- Recommendation products are interactive only on the cart page.
- Relevant products can be browsed and added to the cart.
- Cart quantities, removals and totals update correctly.
- Recommendations differ appropriately by scenario and include defensible explanations.
- Week 6 contains shampoo priced at ₹199 and totals ₹628.
- Every historical order total reconciles with its configured line items.
- Shampoo and durable products are not automatically recommended for replenishment without adequate justification.
- Adding recommendations never falsely records historical purchases.
- Simulated checkout does not claim an actual Blinkit order was placed.
- The application runs without external credentials and can be deployed through Streamlit Community Cloud.

**Product principle:** Habit Memory supports established behavior. BlinkitSense enables relevant new-category discovery when the current shopping mission genuinely supports it.