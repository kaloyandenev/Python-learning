goods = {}
command = input()

while command != "stop":
    value = input()
    if command in goods:
        goods[command] += int(value)
    else:
        goods[command] = int(value)
    command = input()

for element in goods:
    print(f"{element} -> {goods[element]}")
