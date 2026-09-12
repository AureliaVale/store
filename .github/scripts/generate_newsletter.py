import json
import os
from datetime import datetime

# Load products catalog
try:
    with open('products.json', 'r') as f:
        products = json.load(f)
except Exception as e:
    products = []

store_base_url = "https://aureliavale.github.io/store/"
today_date = datetime.now().strftime("%B %d, %Y")
file_date_str = datetime.now().strftime('%Y-%m-%d')

# Build a clean markdown newsletter template
newsletter_content = f"""# Quiet Store Weekly Dispatch
*Date: {today_date}*

Welcome to this week's update from Aurelia Vale's digital shelf. Here is what is fresh, focused, and available to support your workflow this week.

---

## 🌟 Featured Digital Products
"""

for product in products[:3]: # Pull top products
    title = product.get('title', 'Digital Product')
    desc = product.get('description', '')
    url = product.get('checkout_url', store_base_url)
    
    newsletter_content += f"""
### [{title}]({url})
{desc}
👉 [Get instant access here]({url})
"""

newsletter_content += f"""
---
*Thank you for supporting independent digital publishing. You can explore the full collection anytime at [The Quiet Store]({store_base_url}).*
"""

# Ensure a newsletters directory exists
os.makedirs('newsletters', exist_ok=True)

# Save the newsletter file
filename = f"newsletters/newsletter-{file_date_str}.md"
with open(filename, 'w', encoding='utf-8') as f:
    f.write(newsletter_content)

print(f"Successfully generated newsletter: {filename}")

# Optional: Automatically update index.html if you have a specific placeholder or section for it
# For now, we ensure the build script commits any new dispatches so your static site generator or index can read them.
