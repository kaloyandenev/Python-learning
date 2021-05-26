input_line = input()
sides = {}
last_side = ""
trigger = True
force_users = []
while not input_line == "Lumpawaroo":
    if "|" in input_line:
        force_side, force_user = input_line.split(" | ")
        if force_user not in force_users:
            force_users.append(force_user)
            if trigger:
                last_side = force_side
                trigger = False
            if force_side not in sides:
                sides[force_side] = [force_user]
            else:
                sides[force_side].append(force_user)
            last_side = force_side

    elif "->" in input_line:
        force_user, force_side = input_line.split(" -> ")
        if force_user in force_users:
            for side in sides:
                if force_user not in sides[side]:
                    sides[side].append(force_user)
                    print(f"{force_user} joins the {force_side} side!")
                else:
                    sides[side].remove(force_user)
        else:
            if force_side in sides.keys():
                sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
                force_users.append(force_user)

    input_line = input()

for key in sides:
    sides[key].sort()
for key in sides:
    sides[key].sort()

all_sides_sorted = dict(sorted(sides.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
for element in all_sides_sorted:
    if not len(all_sides_sorted[element]) == 0:
        print(f"Side: {element}, Members: {len(all_sides_sorted[element])}")
        for user in all_sides_sorted[element]:
            print(f"! {user}")


