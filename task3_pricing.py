#1
price_dict = {
    "Laptop": 75000,
    "Mobile": 30000,
    "Tablet": 20000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800
}
print("Price Dictionary:", price_dict)

#2
price_dict["Monitor"] = 12000 #Adding
print("After Adding Monitor:", price_dict)

price_dict["Mobile"] = 28000  #Updating
print("After Updating Mobile Price:", price_dict)

product_to_remove = "Tablet"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"{product_to_remove} removed.")
else:
    print(f"{product_to_remove} not found.")

print("After Removal:", price_dict) #After removal
#3
total = sum(price_dict.values())
count = len(price_dict)

average_price = total / count

print("Average Price:", average_price)

#extra
# Product with max price
max_product = max(price_dict, key=price_dict.get)

# Product with min price
min_product = min(price_dict, key=price_dict.get)

print("Highest Price Product:", max_product, price_dict[max_product])
print("Lowest Price Product:", min_product, price_dict[min_product])






