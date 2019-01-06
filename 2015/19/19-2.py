class ReplacementError(Exception):
    pass

with open("19.txt", 'r') as f:
    info = f.readlines()

info = [x.strip() for x in info if not x == "\n"]

molecule = info[-1]
info = info[:-1]

replacements = {}
for x in info:
    original, replacement = x.split(" => ")
    if replacement in replacements:
        raise ReplacementError
    else:
        replacements[replacement] = original

t = 0
while not "e" == molecule:
    for replacement in replacements:
        t += molecule.count(replacement)
        molecule = molecule.replace(replacement, replacements[replacement])

print(t)
