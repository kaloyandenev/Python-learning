n1 = int(input())
n2 = int(input())
operator = input()
result = 0.00
result_type = ""
if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
if result % 2 == 0:
    result_type = "even"
else:
    result_type = "odd"
if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {result_type}")
elif operator == "/" and n2 != 0:
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%" and n2 != 0:
    print(f"{n1} % {n2} = {result}")

