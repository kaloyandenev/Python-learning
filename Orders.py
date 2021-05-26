def order_calculation(product_input, quantity):
    if product_input == "coffee":
        return quantity * 1.50
    elif product_input == "water":
        return quantity * 1.00
    elif product_input == "coke":
        return quantity * 1.40
    elif product_input == "snacks":
        return quantity * 2.00


product = input()
price = float(input())
print(f"{order_calculation(product, price):.2f}")
