users = {}
command = input()

while not command == "Statistics":
    if command.startswith("Add"):
        _, username = command.split("->")
        if username in users:
            print(f"{username} is already registered")
        else:
            users[username] = {"emails": []}
    elif command.startswith("Send"):
        username, email = command.split("->")[1:]
        if username in users:
            users[username]["emails"].append(email)
    elif command.startswith("Delete"):
        _, username = command.split("->")
        if username not in users:
            print(f"{username} not found!")
        else:
            users.pop(username)
    command = input()

length = 0
for user in users:
    length = len(users[user]["emails"])
    users[user]["len"] = length

sorted_users = dict(sorted(users.items(), key=lambda kvp: (-kvp[1]["len"], kvp[0])))

print(f"Users count: {len(users)}")
for user in sorted_users:
    print(user)
    for email in sorted_users[user]["emails"]:
        print(f" - {email}")
