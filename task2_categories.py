#1
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse"]
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories"]
categories_set = set(categories) #creating set
print("Categories Set:", categories_set)

#2
categories_set.add("Gaming")
categories_set.add("Electronics")  # duplicate
print("After Adding:", categories_set)

#3
print("Is 'Electronics' present?", "Electronics" in categories_set)
print("Is 'Clothing' present?", "Clothing" in categories_set)

#extra
print("Total Unique Categories:", len(categories_set))





