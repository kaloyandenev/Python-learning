budget = float(input())
season = input()
price = 0.00
destination = ""
type_vacation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_vacation = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        type_vacation = "Hotel"
        price = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_vacation = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        type_vacation = "Hotel"
        price = 0.8 * budget
elif budget > 1000:
    type_vacation = "Hotel"
    destination = "Europe"
    price = 0.9 * budget
print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price:.2f}")
