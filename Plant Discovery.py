number = int(input())
plants = {}
for _ in range(number):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant] = {"rarity": rarity, "rating": []}

command = input()
while not command == "Exhibition":
    if command.startswith("Rate"):
        command = command.split(":")
        plant, rating = command[1].split(" - ")
        plant = plant.strip()
        if plant in plants:
            rating = int(rating)
            plants[plant]["rating"].append(rating)
        else:
            print("error")
    elif command.startswith("Update"):
        command = command.split(":")
        plant, rarity = command[1].split(" - ")
        plant = plant.strip()
        if plant in plants:
            rarity = int(rarity)
            plants[plant]["rarity"] = rarity
        else:
            print("error")
    elif command.startswith("Reset"):
        command = command.split(":")
        plant = command[1].strip()
        if plant in plants:
            plants[plant]["rating"].clear()
        else:
            print("error")
    command = input()

for plant in plants:
    if plants[plant]["rating"]:
        avg = sum(plants[plant]["rating"]) / len(plants[plant]["rating"])
    else:
        avg = 0
    plants[plant]["average"] = avg

sorted_plants = sorted(plants.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["average"]))
print("Plants for the exhibition:")

for plant in sorted_plants:
    print(f"- {plant[0]}; Rarity: {plant[1]['rarity']}; Rating: {plant[1]['average']:.2f}")
