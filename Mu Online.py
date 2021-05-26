health = 100
bitcoins = 0
dungeons_rooms = input().split("|")
best_room = 0
for room in dungeons_rooms:
    best_room += 1
    command, number_str = room.split()
    if command == "potion":
        current_health = health
        health += int(number_str)
        healing_amount = int(number_str)
        if health > 100:
            healing_amount = 100 - current_health
            health = 100
        print(f"You healed for {healing_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        if health > 0:
            bitcoins += int(number_str)
            print(f"You found {int(number_str)} bitcoins.")
    else:
        health -= int(number_str)
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
        else:
            print(f"You slayed {command}.")


if health > 0:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
