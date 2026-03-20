#1
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse"]
print("Products List:", products)

#2
sample_product = ("Laptop", 75000, "Electronics")
print("Sample Product:", sample_product)

#3
print("2nd Product:", products[1])
print("Last Product:", products[-1])

#4
products.append("Monitor")
products.append("Printer")
print("Updated Products List:", products)

#extra

temp_list = list(sample_product) # Convert tuple to list
temp_list[1] = 70000 # Change price
sample_product = tuple(temp_list)  # Convert back to tuple
print("Updated Sample Product:", sample_product)





