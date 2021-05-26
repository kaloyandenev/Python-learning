items = input().split()
items = [int(item) for item in items]
entry_index = int(input())
type_of_item = input()
left_items = items[:entry_index]
right_items = items[entry_index + 1:]
entry_value = items[entry_index]
sum_left = 0
sum_right = 0
if type_of_item == "cheap":
    cheap_left_items = [item for item in left_items if item < entry_value]
    cheap_right_items = [item for item in right_items if item < entry_value]
    sum_left = sum(cheap_left_items)
    sum_right = sum(cheap_right_items)
elif type_of_item == "expensive":
    expensive_left_items = [item for item in left_items if item >= entry_value]
    expensive_right_items = [item for item in right_items if item >= entry_value]
    sum_left = sum(expensive_left_items)
    sum_right = sum(expensive_right_items)

if sum_left >= sum_right:
    print(f"Left - {sum_left}")
else:
    print(f"Right - {sum_right}")

