import re

with open("12.txt", 'r') as f:
    document = f.readlines()[0]

document = [int(x) for x in re.findall("-*\d+", document)]

print(sum(document))
