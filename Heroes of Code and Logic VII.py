number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    heroes[hero_name] = {"hp": hp, "mp": mp}

command = input()
while not command == "End":
    if command.startswith("Heal"):
        hero_name, amount = command.split(" - ")[1:]
        amount = int(amount)
        heroes[hero_name]["hp"] += amount
        healing_amount = 0
        if heroes[hero_name]["hp"] > 100:
            healing_amount = amount - (heroes[hero_name]["hp"] - 100)
            heroes[hero_name]["hp"] = 100
        else:
            healing_amount = amount
        print(f"{hero_name} healed for {healing_amount} HP!")
    elif command.startswith("Recharge"):
        hero_name, amount = command.split(" - ")[1:]
        amount = int(amount)
        heroes[hero_name]["mp"] += amount
        amount_recovered = 0
        if heroes[hero_name]["mp"] > 200:
            amount_recovered = amount - (heroes[hero_name]["mp"] - 200)
            heroes[hero_name]["mp"] = 200
        else:
            amount_recovered = amount
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif command.startswith("TakeDamage"):
        hero_name, damage, attacker = command.split(" - ")[1:]
        damage = int(damage)
        heroes[hero_name]["hp"] -= damage
        if heroes[hero_name]["hp"] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    elif command.startswith("CastSpell"):
        hero_name, mp_needed, spell_name = command.split(" - ")[1:]
        mp_needed = int(mp_needed)
        if heroes[hero_name]["mp"] >= mp_needed:
            heroes[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))


for hero, values_dict in sorted_heroes:
    print(hero)
    print(f"  HP: {values_dict['hp']}")
    print(f"  MP: {values_dict['mp']}")
