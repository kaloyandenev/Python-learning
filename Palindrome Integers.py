def check_if_palindrome(input_str):
    if_palindrome = True
    for index in range(len(input_str)):
        if not input_str[index] == input_str[index][::-1]:
            if_palindrome = False
            print(if_palindrome)
        else:
            if_palindrome = True
            print(if_palindrome)


palindrome_input = input().split(", ")
check_if_palindrome(palindrome_input)
