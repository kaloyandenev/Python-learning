# input_list = input().split()
# input_list = [int(n) for n in input_list]
# average_number = sum(input_list) / len(input_list)
# if average_number == input_list[0]:
#     print("No")
# else:
#     greater_than_average = [n for n in input_list if n > average_number]
#     greater_than_average.sort(reverse=True)
#     if len(greater_than_average) < 5:
#         top_five = [greater_than_average[nums] for nums in range(len(greater_than_average))]
#     else:
#         top_five = [greater_than_average[nums] for nums in range(5)]
#     top_five = [str(el) for el in top_five]
#     print(f"{' '.join(top_five)}")

test_list = [1, 2, 3, 4]
last_element = test_list.pop(1)
print(last_element)
print(test_list)
