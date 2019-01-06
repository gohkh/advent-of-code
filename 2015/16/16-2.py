import re

with open("16.txt", 'r') as f:
    aunts = f.readlines()

aunts = [re.split(': |, ', aunt.strip()) for aunt in aunts]
sues = {}

for aunt in aunts:
    number = int(aunt[0].split()[1])
    sues[number] = {}
    for i in range((len(aunt)-1)//2):
        sues[number][aunt[i*2 + 1]] = int(aunt[i*2 + 2])

the_sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
        "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for sue in sues:
    yes = 1
    
    for thing in sues[sue]:
        if thing == "cats" or thing == "trees":
            if sues[sue][thing] <= the_sue[thing]:
                yes = 0
        elif thing == "pomeranians" or thing == "goldfish":
            if sues[sue][thing] >= the_sue[thing]:
                yes = 0
        elif not sues[sue][thing] == the_sue[thing]:
            yes = 0

    if yes:
        print(sue)
