first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
people_to_serve = int(input())
working_hours = 0

while people_to_serve > 0:
    working_hours += 1
    people_to_serve -= first_employee_capacity + second_employee_capacity + third_employee_capacity
    if working_hours % 4 == 0:
        working_hours += 1
print(f"Time needed: {working_hours}h.")
