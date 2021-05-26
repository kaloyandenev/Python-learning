import re
participants = input().split(", ")
pattern = r"\w"
runner_info = input()
runners_dict = {el: 0 for el in participants}
while not runner_info == "end of race":
    matches = re.findall(pattern, runner_info)
    name = [letter for letter in matches if letter.isalpha()]
    name_str = ""
    for char in name:
        name_str += char
    distance = sum([int(num) for num in matches if num.isdigit()])
    if name_str in runners_dict:
        runners_dict[name_str] += distance

    runner_info = input()
sorted_runners = sorted(runners_dict.items(), key=lambda kvp: -kvp[1])
print(f"1st place: {sorted_runners[0][0]}")
print(f"2nd place: {sorted_runners[1][0]}")
print(f"3rd place: {sorted_runners[2][0]}")
