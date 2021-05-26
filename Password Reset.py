password = input()
modified_password = ""
command = input()

while not command == "Done":
    if command == "TakeOdd":
        modified_password = ""
        for index in range(len(password)):
            if not index % 2 == 0:
                modified_password += password[index]
        password = modified_password
        print(modified_password)
    elif command.startswith("Cut"):
        index, length = command.split()[1:]
        index = int(index)
        length = int(length)
        left_pass = password[:index]
        right_pass = password[index + length:]
        modified_password = left_pass + right_pass
        print(modified_password)
        password = modified_password
    elif command.startswith("Substitute"):
        substring, substitute = command.split()[1:]
        if substring in password:
            modified_password = password.replace(substring, substitute)
            print(modified_password)
            password = modified_password
        else:
            print("Nothing to replace!")
    command = input()

if not modified_password:
    print(f"Your password is: {password}")
else:
    print(f"Your password is: {modified_password}")
