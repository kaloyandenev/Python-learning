dictionary = {}
count_of_words = int(input())
for _ in range(count_of_words):
    word = input()
    synonym = input()
    if word in dictionary:
        dictionary[word] += [synonym]
    else:
        dictionary[word] = [synonym]
for key in dictionary:
    print(f'{key} - {", ".join(dictionary[key])}')
