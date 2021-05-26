shield_counter = 0
helmet_counter = 0
sword_counter = 0
armor_counter = 0
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
for lost_day in range(1, lost_fights_count + 1):
    if lost_day % 2 == 0:
        helmet_counter += 1
    if lost_day % 3 == 0:
        sword_counter += 1
    # как да го направя с проверка на счупванията
    if lost_day % 3 == 0 and lost_day % 2 == 0:
        shield_counter += 1
        if shield_counter % 2 == 0:
            armor_counter += 1
expenses = helmet_counter * helmet_price + sword_counter * sword_price + shield_counter * shield_price + armor_counter * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
