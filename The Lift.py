tourists = int(input())
lift = [int(el) for el in input().split()]
empty_seats_left = False

for index in range(len(lift)):
    empty_space = 4 - lift[index]
    if empty_space > 0:
        for _ in range(empty_space):
            tourists -= 1
            lift[index] += 1
            if tourists == 0:
                break
    if tourists == 0:
        break

for seats in lift:
    if seats != 4:
        empty_seats_left = True

lift = [str(el) for el in lift]
if empty_seats_left and tourists <= 0:
    print(f"The lift has empty spots!\n{' '.join(lift)}")
elif empty_seats_left == False and tourists > 0:
    print(f"There isn't enough space! {tourists} people in a queue!\n{' '.join(lift)}"
)
elif not empty_seats_left and tourists <= 0:
    print(f"{' '.join(lift)}")
