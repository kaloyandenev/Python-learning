def find_smallest_number(n1, n2, n3):
    list_of_numbers = [n1, n2, n3]
    min_num = min(list_of_numbers)
    return min_num


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(find_smallest_number(num_one, num_two, num_three))
