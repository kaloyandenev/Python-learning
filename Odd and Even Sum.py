def sum_even_and_odd(input_str):
    sum_odd = 0
    sum_even = 0
    for element in input_str:
        element = int(element)
        if element % 2 == 0:
            sum_even += element
        else:
            sum_odd += element
    return sum_odd, sum_even


number_input_str = input()
result = sum_even_and_odd(number_input_str)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
