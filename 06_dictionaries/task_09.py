"""
Given the dictionary:

products = {
    "apple": 30,
    "banana": 25,
    "orange": 40
}

The user enters a product name.

If the product exists:

The user enters a new price.

Update it.

Then, print the entire dictionary.

If the product does not exist:

Product not found.
"""
products = {
    "apple": 30,
    "banana": 25,
    "orange": 40
}

user_product = input("Enter product: ")

if user_product in products:
    products[user_product] = int(input("Enter new price: "))
    print(products)
else:
    print("Product not found.")
