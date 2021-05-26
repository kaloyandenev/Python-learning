roses_price = 5.00
dahlias_price = 3.80
tulips = 2.80
narcissus = 3.00
gladiolus = 2.50
type_of_flowers = input()
quantity = int(input())
budget = int(input())
if type_of_flowers == "Roses" and quantity > 80:
    roses_price *= 0.9
if type_of_flowers == "Dahlias" and quantity > 90:
    dahlias_price *= 0.85
if type_of_flowers == "Tulips" and quantity > 80:
    tulips *= 0.85
if type_of_flowers == "Narcissus" and quantity < 120:
    narcissus *= 1.15
if type_of_flowers == "Gladiolus" and quantity < 80:
    gladiolus *= 1.20

if type_of_flowers == "Roses":
    total = quantity * roses_price
elif type_of_flowers == "Dahlias":
    total = quantity * dahlias_price
elif type_of_flowers == "Tulips":
    total = quantity * tulips
elif type_of_flowers == "Narcissus":
    total = narcissus * quantity
elif type_of_flowers == "Gladiolus":
    total = gladiolus * quantity
difference = abs(total - budget)
if total <= budget:
    print(f"Hey, you have a great garden with {quantity} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")