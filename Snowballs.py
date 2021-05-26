number_of_snowballs = int(input())
max_value = 0
snow = 0
time = 0
quality = 0
max_snow = 0
max_time = 0
max_quality = 0
for balls in range(1, number_of_snowballs + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    current_value = int((snow / time) ** quality)
    if current_value > max_value:
        max_value = current_value
        max_snow = snow
        max_time = time
        max_quality = quality
print(f"{max_snow} : {max_time} = {max_value} ({max_quality})")
