import re
pattern = r"(\||#)(?P<item_name>[a-zA-Z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{,3}|10000)\1"
food_data = input()
matched_food = [el.groupdict() for el in re.finditer(pattern, food_data)]
total_calories = 0
for food in matched_food:
    total_calories += int(food["calories"])
days_to_last = total_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")
for food in matched_food:
    print(f"Item: {food['item_name']}, Best before: {food['expiration_date']}, Nutrition: {food['calories']}")
# import re
# pattern = r"(\||#)(?P<item_name>[a-zA-Z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{,3}|10000)\1"
# food_data = input()
# matches = re.finditer(pattern, food_data)
# food_list = []
# total_calories = 0
# for food in matches:
#     object_dict = food.groupdict()
#     food_list.append(object_dict)
#     total_calories += int(object_dict["calories"])
# days_to_last = total_calories // 2000
# print(f"You have food to last you for: {days_to_last} days!")
# for food in food_list:
#     print(f"Item: {food['item_name']}, Best before: {food['expiration_date']}, Nutrition: {food['calories']}")
