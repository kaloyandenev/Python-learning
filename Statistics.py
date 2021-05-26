products = {}
command = input()

while not command == "statistics":
    key, value = command.split(": ")
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    command = input()
print(f"Products in stock:")
for key in products:
    print(f"- {key}: {products[key]}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
