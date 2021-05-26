import math
total_cats_months = 0
breed = input()
gender = input()
if breed != "British Shorthair" and breed != "Siamese" and breed != "Persian" and breed != "Ragdoll" and breed != "American Shorthair" and breed != "Siberian":
    print(f"{breed} is invalid cat!")
else:
    if breed == "British Shorthair":
        if gender == "m":
            total_cats_months = 13 * 12
        else:
            total_cats_months = 14 * 12
    elif breed == "Siamese":
        if gender == "m":
            total_cats_months = 15 * 12
        else:
            total_cats_months = 16 * 12
    elif breed == "Persian":
        if gender == "m":
            total_cats_months = 14 * 12
        else:
             total_cats_months = 15 * 12
    elif breed == "Ragdoll":
        if gender == "m":
            total_cats_months = 16 * 12
        else:
            total_cats_months = 17 * 12
    elif breed == "American Shorthair":
        if gender == "m":
            total_cats_months = 12 * 12
        else:
            total_cats_months = 13 * 12
    elif breed == "Siberian":
        if gender == "m":
            total_cats_months = 11 * 12
        else:
            total_cats_months = 12 * 12
    cats_years = math.floor(total_cats_months / 6)
    print(f"{cats_years} cat months")