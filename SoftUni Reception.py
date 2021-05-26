first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
customers = int(input())
hours = 0
while customers > 0:
    hours += 1
    customers -= first_employee + second_employee + third_employee
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")

