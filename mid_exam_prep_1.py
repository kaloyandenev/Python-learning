import math
budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_packages_of_flour = students // 5
flour_total_price = flour_price * (students - free_packages_of_flour)
eggs_price = 10 * egg_price * students
aprons_price = math.ceil(students * 1.2) * apron_price
total_price = flour_total_price + aprons_price + eggs_price
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{(total_price - budget):.2f}$ more needed.")
