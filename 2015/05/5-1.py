with open("5.txt", 'r') as f:
    strings = f.readlines()

strings = [string.strip() for string in strings]

nice = 0

for string in strings:
    vowels = 0
    double = 0
    disallowed = 0
    disallowed_strs = {'a': 'b', 'c': 'd', 'p': 'q', 'x': 'y'}
    prev = ""
    for letter in string:
        if letter in "aeiou":
            vowels += 1
        if letter == prev:
            double = 1
        if prev in disallowed_strs and disallowed_strs[prev] == letter:
            disallowed = 1
            break
        prev = letter
    if not disallowed and double and vowels >= 3:
        nice += 1

print(nice)
