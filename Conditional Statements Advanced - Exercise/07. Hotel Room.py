studio_price = 0.00
apartment_price = 0.00
month = input()
nights = int(input())
if month == "May" or month == "October":
    studio_price = 50.00
    apartment_price = 65.00
    if nights > 14:
        studio_price *= 0.7
    elif nights > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76.00
    apartment_price = 77.00
if nights > 14:
    apartment_price *= 0.9
total_apartment_price = apartment_price * nights
total_studio_price = studio_price * nights
print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")