def swap(list_input, index_1, index_2):
    list_input[index_1], list_input[index_2] = list_input[index_2], list_input[index_1]
    return list_input


def multiply(list_input, index_1, index_2):
    list_input[index_1] = list_input[index_1] * list_input[index_2]
    return list_input


def decrease(list_input):
    return [el - 1 for el in list_input]


list_to_modify = input().split()
list_to_modify = [int(n) for n in list_to_modify]
command = input()

while command != "end":
    command = command.split()
    if command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        list_to_modify = swap(list_to_modify, first_index, second_index)
    elif command[0] == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        list_to_modify = multiply(list_to_modify, first_index, second_index)
    elif command[0] == "decrease":
        list_to_modify = decrease(list_to_modify)
    command = input()

list_to_modify = [str(el) for el in list_to_modify]
result = ', '.join(list_to_modify)
print(result)
