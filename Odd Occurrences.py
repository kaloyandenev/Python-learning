data_list = input().split()
data_dict = {}
data_list = [element.lower() for element in data_list]
for element in data_list:
    if element in data_dict:
        data_dict[element] += 1
    else:
        data_dict[element] = 1
for element in data_dict.items():
    if element[1] % 2 != 0:
        print(f"{element[0]}", end=" ")

