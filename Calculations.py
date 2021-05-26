def calculator(opr, num1, num2):
    if opr == "multiply":
        return num1 * num2
    elif opr == "divide":
        return num1 // num2
    elif opr == "add":
        return num1 + num2
    elif opr == "subtract":
        return num1 - num2


operator = input()
num_1 = int(input())
num_2 = int(input())
print(calculator(operator, num_1, num_2))
