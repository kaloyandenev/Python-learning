from collections import ChainMap
input_line = input()
left_side = {}
right_side = {}
last_side = ""
trigger = True
force_users = []
while not input_line == "Lumpawaroo":
    if "|" in input_line:
        force_side, force_user = input_line.split(" | ")
        force_users += [force_user]
        if trigger:
            last_side = force_side
            trigger = False
        if force_side not in left_side and force_side not in right_side:
            if not force_side == last_side:
                right_side[force_side] = [force_user]
            else:
                left_side[force_side] = [force_user]
        else:
            if force_side in left_side:
                left_side[force_side] += [force_user]
            else:
                right_side[force_side] += [force_user]
        last_side = force_side

    elif "->" in input_line:
        force_user, force_side = input_line.split(" -> ")
        if force_user in force_users:
            for side in left_side:
                for users in left_side[side]:
                    if force_user == users:
                        left_side[side].remove(force_user)
                        right_side[force_side] += [force_user]
                        print(f"{force_user} joins the {force_side} side!")
            for side in right_side:
                for users in right_side[side]:
                    if force_user == users:
                        right_side[side].remove(force_user)
                        left_side[force_side] += [force_user]
                        print(f"{force_user} joins the {force_side} side!")
        else:
            if force_side in left_side:
                left_side[force_side] += [force_user]
                print(f"{force_user} joins the {force_side} side!")
            else:
                right_side[force_user] += [force_user]
                print(f"{force_user} joins the {force_side} side!")
    input_line = input()

for key in left_side:
    left_side[key].sort()
for key in right_side:
    right_side[key].sort()

all_sides = dict(ChainMap({}, left_side, right_side))
all_sides_sorted = sorted(all_sides.items(), key=lambda kvp: len(kvp[1]), reverse=True)
all_sides_sorted = sorted(all_sides.items(), key=lambda kvp: kvp[0])

for element in all_sides_sorted:
    if not len(element[1]) == 0:
        print(f"Side: {element[0]}, Members: {len(element[1])}")
        for user in element[1]:
            print(f"! {user}")


