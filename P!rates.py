command = input()
cities = {}
while not command == "Sail":
    town, population, gold = command.split("||")
    gold = int(gold)
    population = int(population)
    if town in cities:
        cities[town]["population"] += population
        cities[town]["gold"] += gold
    else:
        cities[town] = {"population": population, "gold": gold}

    command = input()

command = input()

while not command == "End":
    if command.startswith("Plunder"):
        town, people, gold = command.split("=>")[1:]
        if town in cities:
            people = int(people)
            gold = int(gold)
            cities[town]["population"] -= people
            cities[town]["gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
                cities.pop(town)
                print(f"{town} has been wiped off the map!")
    elif command.startswith("Prosper"):
        town, gold = command.split("=>")[1:]
        gold = int(gold)
        if town in cities:
            if gold >= 0:
                cities[town]["gold"] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
            else:
                print("Gold added cannot be a negative number!")

    command = input()
# sorted_towns = cities.items()
sorted_towns = dict(sorted(cities.items(), key=lambda tkvp: (-tkvp[1]["gold"], tkvp[0])))
print(f"Ahoy, Captain! There are {len(sorted_towns)} wealthy settlements to go to:")
if sorted_towns:
    for town in sorted_towns:
        print(f"{town} -> Population: {sorted_towns[town]['population']} citizens, Gold: {sorted_towns[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
