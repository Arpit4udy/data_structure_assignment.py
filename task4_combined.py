#1
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse"]

categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories"]

price_dict = {
    "Laptop": 75000,
    "Mobile": 28000,
    "Tablet": 20000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800
}

# Create catalog
catalog = []

for i in range(len(products)):
    product_name = products[i]
    price = price_dict[product_name]
    category = categories[i]
    
    catalog.append((product_name, price, category))

print("Catalog:", catalog)

#2
category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    
    category_to_products[category].append(product_name)

print("Category to Products:", category_to_products)

#3
# Find category with maximum products
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print("Category with maximum products:", max_category)

print("Products in that category:")
for product in category_to_products[max_category]:
    print(product)




