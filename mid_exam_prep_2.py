input_weapon = input().split("|")
command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "Move":
        index = int(command[2])
        if command[1] == "Left":
            if index - 1 in range(len(input_weapon)):
                input_weapon[index], input_weapon[index - 1] = input_weapon[index - 1], input_weapon[index]
        elif command[1] == "Right":
            if index + 1 in range(len(input_weapon)):
                input_weapon[index], input_weapon[index + 1] = input_weapon[index + 1], input_weapon[index]
    elif command[0] == "Check":
        if command[1] == "Even":
            even_positions = [input_weapon[index] for index in range(len(input_weapon)) if index % 2 == 0]
            print(f"{' '.join(even_positions)}")
        elif command[1] == "Odd":
            odd_positions = [input_weapon[index] for index in range(len(input_weapon)) if not index % 2 == 0]
            print(f"{' '.join(odd_positions)}")
    command = input()

print(f"You crafted {''.join(input_weapon)}!")
