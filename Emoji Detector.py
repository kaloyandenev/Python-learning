import re
pattern = r"(\:\:|\*\*)[A-Z][a-z]{2,}\1|\d"
string_input = input()
emojis = []
numbers = []
cool_emojis = []
matches_list = [el.group() for el in re.finditer(pattern, string_input)]
for el in matches_list:
    if el.isdigit():
        numbers.append(int(el))
    else:
        emojis.append(el)
coolnes = 1
emoji_coolnes = 0
for num in numbers:
    coolnes *= num
for emoji in emojis:
    emoji_stripped = emoji[2:-2]
    for char in emoji_stripped:
        emoji_coolnes += ord(char)
    if emoji_coolnes >= coolnes:
        cool_emojis.append(emoji)
    emoji_coolnes = 0


print(f"Cool threshold: {coolnes}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for match in cool_emojis:
    print(match)
