# def is_number_perfect(number):
#     divisors_sum = 0
#     for element in range(1, number):
#         if number % element == 0:
#             divisors_sum += element
#     if number == divisors_sum:
#         return True
#     else:
#         return False
#
# input_number = int(input())
# number_is_perfect = is_number_perfect(input_number)
# if number_is_perfect:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")
list_input = [2, 5, 7, 12, 121, 89]
value = 2
first_even = []
first_odd = []
last_even = []
last_odd = []
if value > len(list_input):
    print("Invalid count")
else:
    for index in range(len(list_input)):
        if list_input[index] % 2 == 0:
            first_even.append(list_input[index])
        else:
            first_odd.append(list_input[index])
    cutting_range = len(first_odd)-value
    last_odd = first_odd[cutting_range:]
    last_even = first_even[cutting_range:]
print(first_odd, first_even, last_odd, last_even)
