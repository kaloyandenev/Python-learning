prices = input()
total_net = 0
total_with_tax = 0
discounted_price = 0

while not prices == "special" and not prices == "regular":
    prices = float(prices)
    if prices >= 0:
        total_net += prices
    else:
        print("Invalid price!")

    prices = input()

if prices == "special":
    discounted_price = total_net * 1.2 * 0.9
else:
    discounted_price = total_net * 1.2
if total_net <= 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {(total_net):.2f}$\nTaxes: {(total_net * 1.2 - total_net):.2f}$\n-----------\nTotal price: {(discounted_price):.2f}$" )
