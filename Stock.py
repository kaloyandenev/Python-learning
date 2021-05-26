data = input().split()
products = {}
searched_products = input().split()
for index in range(0, len(data), 2):
    products[data[index]] = data[index + 1]

for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
