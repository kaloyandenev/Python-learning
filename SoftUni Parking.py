users = {}
number_of_users = int(input())
for _ in range(number_of_users):
    command = input().split()
    user = command[1]
    if command[0] == "register":
        plate = command[2]
        if user in users:
            print(f"ERROR: already registered with plate number {users[user]}")
        else:
            users[user] = plate
            print(f"{user} registered {plate} successfully")
    elif command[0] == "unregister":
        if user not in users:
            print(f"ERROR: user {user} not found")
        else:
            users.pop(user)
            print(f"{user} unregistered successfully")

for user in users:
    print(f"{user} => {users[user]}")
