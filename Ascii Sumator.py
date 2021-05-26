start_char = ord(input())
end_char = ord(input())
string = input()
total_sum = 0
for char in string:
    if start_char < ord(char) < end_char:
        total_sum += ord(char)


print(total_sum)
