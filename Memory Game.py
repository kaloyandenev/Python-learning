def index_is_valid(input_list, index):
    if index in range(len(input_list)):
        return True
    return False


moves_counter = 0
list_input = input().split()
command = input()

while command != "end" and len(list_input):
    moves_counter += 1
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)
    current_index_value = list_input[index_1]
    if index_is_valid(list_input, index_1) and index_is_valid(list_input, index_2):
        if list_input[index_1] != list_input[index_2]:
            print("Try again!")
        else:
            print(f"Congrats! You have found matching elements - {list_input[index_1]}!")
            list_input.remove(current_index_value)
            list_input.remove(current_index_value)
    else:
        list_middle = len(list_input) // 2
        list_input.insert(list_middle, f"-{moves_counter}a")
        list_input.insert(list_middle, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")

    command = input()


if len(list_input) == 0:
    print(f"You have won in {moves_counter} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(list_input)}")
