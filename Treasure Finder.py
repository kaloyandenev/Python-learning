key = input().split()
key = [int(n) for n in key]

string = input()
index = 0
while not string == "find":
    current_string = ""
    for char in string:
        current_string += chr(ord(char) - key[index])
        index += 1
        if index >= len(key):
            index = 0
    treasure_start_index = current_string.index("&") + 1
    treasure_end_index = len(current_string) - current_string[::-1].index("&") - 1
    treasure_type = current_string[treasure_start_index:treasure_end_index]
    coordinates_start = current_string.index("<") + 1
    coordinates_end = len(current_string) - current_string[::-1].index(">") - 1
    coordinates = current_string[coordinates_start:coordinates_end]
    print(f"Found {treasure_type} at {coordinates}")
    index = 0
    string = input()
