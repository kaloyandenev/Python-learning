calories_per_minute = 5
minutes_for_walking = int(input())
walkings_per_day = int(input())
calories_per_day = int(input())

burned_calories_per_day = calories_per_minute * minutes_for_walking * walkings_per_day
if burned_calories_per_day >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories_per_day}.")