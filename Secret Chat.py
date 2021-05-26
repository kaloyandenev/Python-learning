concealed_message = input()
current_message = ""

command = input()

while not command == "Reveal":
    if command.startswith("InsertSpace"):
        command, index = command.split(":|:")
        index = int(index)
        current_message = concealed_message[:index] + " " + concealed_message[index:]
        concealed_message = current_message
        print(concealed_message)
    elif command.startswith("Reverse"):
        command, substring = command.split(":|:")
        if substring in concealed_message:
            current_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = current_message + substring
            print(concealed_message)
        else:
            print("error")
    elif command.startswith("ChangeAll"):
        substring, replacement = command.split(":|:")[1:]
        if substring in concealed_message:
            current_message = concealed_message.replace(substring, replacement)
            concealed_message = current_message
            print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")
