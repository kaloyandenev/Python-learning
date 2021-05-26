import math
fan_name = input()
budget = float(input())
beer_quantity = int(input())
chips_quantity = int(input())
total_beer_price = beer_quantity * 1.20
chips_price = (total_beer_price * 0.45)
total_chips_price = math.ceil(chips_price * chips_quantity)
total_price = total_beer_price + total_chips_price
difference = abs(budget - total_price)
if total_price <= budget:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")