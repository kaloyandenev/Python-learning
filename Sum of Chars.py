lines = int(input())
sum = 0
for letters in range(lines):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")
