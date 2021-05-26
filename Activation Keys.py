activation_key = input()
instructions = input()
while not instructions == "Generate":
    if instructions.startswith("Contains"):
        command, substring = instructions.split(">>>")
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instructions.startswith("Flip"):
        command, start_index, end_index = instructions.split(">>>")[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        first_part = activation_key[:start_index]
        end_part = activation_key[end_index:]
        if command == "Upper":
            activation_key = first_part + activation_key[start_index:end_index].upper() + end_part
            print(activation_key)
        elif command == "Lower":
            activation_key = first_part + activation_key[start_index:end_index].lower() + end_part
            print(activation_key)
    elif instructions.startswith("Slice"):
        command, start_index, end_index = instructions.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        first_part = activation_key[:start_index]
        end_part = activation_key[end_index:]
        activation_key = first_part + end_part
        print(activation_key)
    instructions = input()
print(f"Your activation key is: {activation_key}")
