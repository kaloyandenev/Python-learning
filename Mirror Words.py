import re
pattern = r"(@|#)(?P<first_word>([a-zA-Z]{3,}))\1(@|#)(?P<second_word>([a-zA-Z]{3,}))\1"

string = input()
matched = [el.groupdict() for el in re.finditer(pattern, string)]
mirror_words = []
for match in matched:
    if match["first_word"] == match["second_word"][::-1]:
        mirror_words.append(match)
if not matched:
    print("No word pairs found!")
else:
    print(f"{len(matched)} word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
mirror_words = [el['first_word'] + " <=> " + el['second_word'] for el in mirror_words]
print(", ".join(mirror_words))
