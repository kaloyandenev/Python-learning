string = input()

command = input()

while not command == "Finish":
    if command.startswith("Replace"):
        current_char, new_char = command.split()[1:]
        if current_char in string:
            string = string.replace(current_char, new_char)
        print(string)
    elif command.startswith("Make"):
        command, action = command.split()
        if action == "Upper":
            string = string.upper()
        elif action == "Lower":
            string = string.lower()
        print(string)
    elif command.startswith("Check"):
        command, message = command.split()
        if message in string:
            print(f"Message contains {message}")
        else:
            print(f"Message doesn't contain {message}")
    elif command.startswith("Sum"):
        start_index, end_index = command.split()[1:]
        start_index = int(start_index)
        end_index = int(end_index) + 1
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            if start_index <= end_index:
                sum_asci = 0
                for char in string[start_index:end_index]:
                    sum_asci += ord(char)
                print(sum_asci)
            else:
                print("Invalid indices!")
        else:
            print("Invalid indices!")
    elif command.startswith("Cut"):
        start_index, end_index = command.split()[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            if start_index <= end_index:
                string = string[:start_index] + string[end_index + 1:]
                print(string)
            # elif start_index == end_index:
            #     string = string[:start_index] + string[end_index + 1:]
            #     print(string)
            else:
                print("Invalid indices!")
        else:
            print("Invalid indices!")

    command = input()
