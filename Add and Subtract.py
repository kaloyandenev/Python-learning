def add_and_subtract(n1, n2, n3):
    def add_numbers(n1, n2):
        return n1 + n2

    def substract(result, n3):
        return result - n3
    return substract(add_numbers(n1, n2), n3)

num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))
