food_eaten = 0.00
small_cats = 0
big_cats = 0
huge_cats = 0
cat_number = int(input())
for cats in range(cat_number):
    food_eaten_per_cat = float(input())
    if 100 <= food_eaten_per_cat < 200:
        small_cats += 1
    elif 200 <= food_eaten_per_cat < 300:
        big_cats += 1
    elif 300 <= food_eaten_per_cat < 400:
        huge_cats += 1
    food_eaten += food_eaten_per_cat
price = (food_eaten / 1000) * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {price:.2f} lv.")