# A program to look up the price of products
products = {
    "bananas": 0.59,
    "bread": 2.49,
    "eggs": 3.29,
    "milk": 3.89,
    "cereal": 4.19
}

print("Welcome to the price lookup system.")

while True:
    product_name = input("Enter a product name: ")

    if product_name.lower() == "quit":
        break
    elif product_name.lower() in products:
        price = products[product_name.lower()]
        print(f'The price of {product_name} is ${price:.2f}.')
    else:
        print(f'Unknown product "{product_name}".  Please try again.')

print("Have a nice day!")