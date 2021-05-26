def calc_factorial(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return int(result)

num_1 = int(input())
num_2 = int(input())
result = calc_factorial(num_1) / calc_factorial(num_2)
print(f"{result:.2f}")
