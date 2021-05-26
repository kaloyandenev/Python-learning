strings_number = int(input())

for _ in range(strings_number):
    data_string = input()
    start_index_name = data_string.index("@") + 1
    end_index_name = data_string.index("|")
    start_index_age = data_string.index("#") + 1
    end_index_age = data_string.index("*")
    name = data_string[start_index_name:end_index_name]
    age = data_string[start_index_age:end_index_age]
    print(f"{name} is {age} years old.")

