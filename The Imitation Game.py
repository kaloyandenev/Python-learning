message = input()

command = input()

while not command == "Decode":
    if command.startswith("ChangeAll"):
        substring, replacement = command.split("|")[1:]
        message = message.replace(substring, replacement)
    elif command.startswith("Insert"):
        index, value = command.split("|")[1:]
        index = int(index)
        message = message[:index] + value + message[index:]
    elif command.startswith("Move"):
        command, number = command.split("|")
        number = int(number)
        message = message[number:] + message[:number]
    command = input()
print(f"The decrypted message is: {message}")
