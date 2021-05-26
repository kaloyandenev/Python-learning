string = input()
string_dictionary = {}
for character in string:
    if not character == " ":
        if character in string_dictionary:
            string_dictionary[character] += 1
        else:
            string_dictionary[character] = 1
for element in string_dictionary:
    print(f"{element} -> {string_dictionary[element]}")
