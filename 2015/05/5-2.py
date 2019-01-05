import re

with open("5.txt", 'r') as f:
    strings = f.readlines()

strings = [string.strip() for string in strings]

nice = 0

for string in strings:
    if re.findall(r'(.)(.)\1', string):
        prev = ""
        for letter in string:
            if prev and string.count(prev + letter) > 1:
                nice += 1
                break
            prev = letter

print(nice)
