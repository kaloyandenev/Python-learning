battles_won = 0
energy = int(input())
command = input()

while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        battles_won += 1
        energy -= distance
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break
    if battles_won % 3 == 0:
        energy += battles_won
    command = input()

if command == "End of battle":
    print(f"Won battles: {battles_won}. Energy left: {energy}")
