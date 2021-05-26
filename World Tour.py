stops = input()
command = input()
current_string = ""
while not command == "Travel":
    if command.startswith("Add Stop"):
        index, string = command.split(":")[1:]
        index = int(index)
        if index in range(0, len(stops)):
            current_string = stops[:index] + string + stops[index:]
            stops = current_string
        print(stops)
    elif command.startswith("Remove Stop"):
        start_index, end_index = command.split(":")[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if end_index in range(0, len(stops)) and start_index in range(0, len(stops)) and start_index <= end_index:
            current_string = stops[:start_index] + stops[end_index+1:]
            stops = current_string
        print(stops)
    elif command.startswith("Switch"):
        old_string, new_string = command.split(":")[1:]
        if old_string in stops:
            current_string = stops.replace(old_string, new_string)
            stops = current_string
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
