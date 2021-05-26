def exchange(list_input, value):
    left_list = list_input[:value]
    right_list = list_input[value:]
    exchanged_list = right_list + left_list
    exchanged_list = [int(i) for i in exchanged_list]
    return exchanged_list


def max_even_odd(list_input):
    max_even = [i for i in list_input if not i % 2][::-1]
    if len(max_even) > 0:
        max_even = max(max_even)
        max_even_index = len(list_input) - list_input.index(max_even)
    else:
        max_even_index = "No matches"
    max_odd = [i for i in list_input if i % 2][::-1]
    if len(max_odd) > 0:
        max_odd = max(max_odd)
        max_odd_index = len(list_input) - list_input.index(max_odd)
    else:
        max_odd_index = "No matches"
    return max_even_index, max_odd_index


def min_even_odd(list_input):
    min_even = [i for i in list_input if not i % 2][::-1]
    if len(min_even) > 0:
        min_even = min(min_even)
        min_even_index = len(list_input) - list_input.index(min_even)
    else:
        min_even_index = "No matches"
    min_odd = [i for i in list_input if i % 2][::-1]
    if len(min_odd) > 0:
        min_odd = min(min_odd)
        min_odd_index = len(list_input) - list_input.index(min_odd)
    else:
        min_odd_index = "No matches"
    return min_even_index, min_odd_index


def first_even_odd(list_input, value):
    first_even = []
    first_odd = []
    last_even = []
    last_odd = []
    if value > len(list_input):
        return "Invalid count"
    else:
        for index in range(len(list_input)):
            for _ in range(value):
                if list_input[index] % 2 == 0:
                    first_even.append(list_input[index])
                else:
                    first_odd.append(list_input[index])
        for index in range(len(list_input)):
            if list_input[index] % 2 == 0:
                last_even.append(list_input[index])
                last_even = last_even[value:-1:1]
            else:
                last_odd.append(list_input[index])
                last_odd = last_odd[value:-1:1]
        return first_even, first_odd, last_even, last_odd

input_list = input().split()
command = input()
exchanged_list = input_list
while command != "end":
    command_list = command.split()
    command = command_list[0]
    if command == "exchange":
        index_value = int(command_list[1])
        if index_value > len(input_list):
            print("Invalid index")
        else:
            exchanged_list = exchange(exchanged_list, index_value)
            print(exchanged_list)
    elif command == "max":
        if command_list[1] == "odd":
            print(max_even_odd(exchanged_list)[1])
        elif command_list[1] == "even":
            print(max_even_odd(exchanged_list)[0])
    elif command == "min":
        if command_list[1] == "odd":
            print(min_even_odd(exchanged_list)[1])
        elif command_list[1] == "even":
            print(min_even_odd(exchanged_list)[0])
    elif command == "first":
        pass
    elif command == "last":
        pass
    command = input()
