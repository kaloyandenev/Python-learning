import math
party_size = int(input())
period = int(input())
party_earnings = 0
spendings = 0
earnings = 0
for days in range(1, period + 1):
    if days % 10 == 0:
        party_size -= 2
    if days % 15 == 0:
        party_size += 5
    party_earnings += 50
    spendings += 2 * party_size
    if days % 3 == 0:
        spendings += 3 * party_size
    if days % 5 == 0:
        earnings += 20 * party_size
        if days % 3 == 0:
            spendings += 2 * party_size
total_per_companion = int(math.floor(party_earnings + earnings - spendings) / party_size)
print(f"{party_size} companions received {total_per_companion} coins each.")
