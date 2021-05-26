import re
pattern = r"^(\$|\%)(?P<tag>[A-Z][a-z]{2,})\1:\s(\[(?P<num1>\d+)\]\|)(\[(?P<num2>\d+)\]\|)(\[(?P<num3>\d+)\]\|)$"
input_count = int(input())

for _ in range(input_count):
    message = input()
    if re.match(pattern, message):
        matches = (el.groupdict() for el in re.finditer(pattern, message))
        for match in matches:
            print(f"{match['tag']}: {chr(int(match['num1']))}{chr(int(match['num2']))}{chr(int(match['num3']))}")

    else:
        print("Valid message not found!")
