def password_validator(password):
    password = str(password)
    digits_counter = 0
    pass_is_valid = True
    if len(password) < 6 or len(password) > 10:
        pass_is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        pass_is_valid = False
        print("Password must consist only of letters and digits")
    for element in password:
        if element.isnumeric():
            digits_counter += 1
    if digits_counter < 2:
        pass_is_valid = False
        print("Password must have at least 2 digits")
    if pass_is_valid:
        print("Password is valid")

input_pass = input()
password_validator(input_pass)

