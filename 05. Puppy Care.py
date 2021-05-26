bought_food = int(input())
bought_food_in_grams = bought_food * 1000
eaten_food_grams = 0
command = input()

while command != "Adopted":
    grams_eaten_per_feed = int(command)
    eaten_food_grams += grams_eaten_per_feed
    command = input()
difference = abs(bought_food_in_grams - eaten_food_grams)
if eaten_food_grams <= bought_food_in_grams:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
