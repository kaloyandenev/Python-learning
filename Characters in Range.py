def return_char_in_range(character1, character2):
    range_list = []
    for char in range(ord(character1)+1, ord(character2)):
        range_list.append(chr(char))
    return range_list


char_1 = input()
char_2 = input()
result = return_char_in_range(char_1, char_2)
result = " ".join(result)
print(result)
