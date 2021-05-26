def loading_bar(percent):
    bar_list = []
    percent = int(percent / 10)
    for element in range(0, percent):
        bar_list.append('%')
    for element in range(percent, 10):
        bar_list.append(".")
    return bar_list


number = int(input())
if number % 10 == 0:
    result = loading_bar(number)
    result = "".join(result)
    if number == 100:
        print("100% Complete!")
        print(f"[{result}]")
    else:
        print(f"{number}% [{result}]")
        print("Still loading...")
