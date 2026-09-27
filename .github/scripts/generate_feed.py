import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Load your products catalog
try:
    with open('products.json', 'r') as f:
        products = json.load(f)
except Exception as e:
    products = []

# Base URL for your store
store_base_url = "https://aureliavale.github.io/store/"

# Create root RSS element with required Google/Pinterest namespace
rss = ET.Element('rss', version='2.0')
rss.set('xmlns:g', 'http://base.google.com/ns/1.0')

channel = ET.SubElement(rss, 'channel')
ET.SubElement(channel, 'title').text = "Aurelia Vale Digital Store Catalog"
ET.SubElement(channel, 'link').text = store_base_url
ET.SubElement(channel, 'description').text = "Automated product catalog for Pinterest and search feeds."

for product in products:
    item = ET.SubElement(channel, 'item')
    
    # Required Pinterest / Google Merchant fields
    ET.SubElement(item, 'g:id').text = str(product.get('id', 'item'))
    ET.SubElement(item, 'title').text = product.get('title', '')
    ET.SubElement(item, 'g:title').text = product.get('title', '')
    ET.SubElement(item, 'description').text = product.get('description', '')
    ET.SubElement(item, 'g:description').text = product.get('description', '')
    
    # Use checkout url or store url for the link
    checkout_url = product.get('checkout_url', store_base_url)
    ET.SubElement(item, 'link').text = checkout_url
    ET.SubElement(item, 'g:link').text = checkout_url
    
    # Availability & Price (real price from products.json, with currency detection)
    ET.SubElement(item, 'g:availability').text = 'in stock'
    raw_price = str(product.get('price', '')).strip()
    if raw_price.lower() in ('free', '0', '0.00', '€0.00', '$0.00'):
        price_value = '0.00'
    else:
        digits = ''.join(c for c in raw_price if c.isdigit() or c == '.')
        price_value = digits if digits else '0.00'
    currency = 'USD' if raw_price.startswith('$') else 'EUR'
    ET.SubElement(item, 'g:price').text = f'{price_value} {currency}'

    # Fallback image (Pinterest requires an image link)
    ET.SubElement(item, 'g:image_link').text = "https://aureliavale.github.io/store/assets/preview.png"

# Pretty-print the XML
xml_str = minidom.parseString(ET.tostring(rss)).toprettyxml(indent="    ")

# Save as catalog.xml in the root of the repo so GitHub Pages publishes it live
with open('catalog.xml', 'w', encoding='utf-8') as f:
    f.write(xml_str)

print("Successfully generated catalog.xml for Pinterest!")
