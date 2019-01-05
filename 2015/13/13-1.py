from itertools import permutations

with open("13.txt", 'r') as f:
    preferences = f.readlines()

happiness = {}

for preference in preferences:
    preference = preference.split()
    person = preference[0]
    neighbour = preference[-1][:-1]
    if person not in happiness:
        happiness[person] = {}

    if preference[2] == "gain":
        happiness[person][neighbour] = int(preference[3])
    elif preference[2] == "lose":
        happiness[person][neighbour] = 0 - int(preference[3])

all_totals = set()

for seating in permutations(happiness):
    total = 0
    for i in range(len(seating)):
        person = seating[i-1]
        total += happiness[person][seating[i-2]] + happiness[person][seating[i]]
    all_totals.add(total)

print(max(all_totals))
