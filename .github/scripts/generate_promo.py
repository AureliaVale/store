import json
import random
import datetime

# Load your products catalog
try:
    with open('products.json', 'r') as f:
        products = json.load(f)
except Exception as e:
    products = []

if products:
    # Pick a random product to spotlight
    product = random.choice(products)

    # Format a clean promotional post
    promo_text = f"""# Spotlight: {product['title']}

{product['description']}

Get it here: {product['checkout_url']}
"""

    # Save it to a markdown file in a promos folder
    today = datetime.date.today().isoformat()
    # Ensure promos folder exists via python
    import os
    os.makedirs('promos', exist_ok=True)
    
    filename = f"promos/promo-{today}.md"
    with open(filename, 'w') as f_out:
        f_out.write(promo_text)
    
    print(f"Successfully generated: {filename}")
else:
    print("No products found to promote.")
