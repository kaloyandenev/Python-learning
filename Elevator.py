people = int(input())
capacity = int(input())
travels = (people // capacity)
if not people % capacity == 0:
    travels += 1
print(travels)
