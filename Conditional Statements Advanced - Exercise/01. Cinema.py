premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00
total_income = 0
type_projection = input()
rows = int(input())
columns = int(input())
if type_projection == "Premiere":
    total_income = premiere_price * rows * columns
elif type_projection == "Normal":
    total_income = normal_price * rows * columns
elif type_projection == "Discount":
    total_income = discount_price * rows * columns

print(f"{total_income:.2f} leva")