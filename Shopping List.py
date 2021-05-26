initial_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    command = command.split()
    action = command[0]
    product_one = command[1]
    if action == "Urgent":
        if product_one not in initial_list:
            initial_list.insert(0, product_one)
    elif action == "Unnecessary":
        if product_one in initial_list:
            initial_list.remove(product_one)
    elif action == "Correct":
        product_two = command[2]
        if product_one in initial_list:
            index = initial_list.index(product_one)
            initial_list[index] = product_two
    elif action == "Rearrange":
        if product_one in initial_list:
            initial_list.remove(product_one)
            initial_list.append(product_one)
    command = input()

print(", ".join(initial_list))
