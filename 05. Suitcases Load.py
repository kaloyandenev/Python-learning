capacity = float(input())
command = input()
current_counter = 0
total_suitcases = 0
total_suitcases_counter = 0
while command != "End":
    suitcase_volume = float(command)
    current_counter += 1
    if current_counter == 3:
        suitcase_volume *= 1.10
        current_counter = 0
    total_suitcases += suitcase_volume
    if total_suitcases <= capacity:
        total_suitcases_counter += 1
        command = input()
    else:
        break
if command == "End":
    print(f"Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {total_suitcases_counter} suitcases loaded.")
