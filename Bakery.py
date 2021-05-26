input_data = input().split()
products_dictionary = {}
for index in range(0, len(input_data), 2):
    products_dictionary[input_data[index]] = input_data[index + 1]
print(products_dictionary)




# products_dictionary[key] = value
