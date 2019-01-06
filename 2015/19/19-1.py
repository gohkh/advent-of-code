import re

with open("19.txt", 'r') as f:
    info = f.readlines()

info = [x.strip() for x in info if not x == "\n"]

molecule = info[-1]
replacements = info[:-1]
molecules = set()

for replacement in replacements:
    original, replacement = replacement.split(" => ")
    for i in [m.start() for m in re.finditer(original, molecule)]:
        new_molecule = molecule[:i] + molecule[i:].replace(original, replacement, 1)
        molecules.add(new_molecule)

print(len(molecules))
