# capacity = 255
# lines = int(input())
# liters_to_pour = int(input())
# total_pour = 0
# total_pour += liters_to_pour
# if liters_to_pour > capacity:
#         print(f"Insufficient capacity!")
#         total_pour = 0
# for pours in range(lines - 1):
#     liters_to_pour = int(input())
#     if liters_to_pour > capacity - total_pour:
#         print(f"Insufficient capacity!")
#         continue
#     total_pour += liters_to_pour
# print(total_pour)
capacity = 255
current_capacity = 0
lines = int(input())
for _ in range(lines):
    pour = int(input())
    if pour + current_capacity > capacity:
        print(f"Insufficient capacity!")
    else:
        current_capacity += pour
print(current_capacity)
