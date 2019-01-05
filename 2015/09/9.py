from itertools import permutations

with open("9.txt", 'r') as f:
    distances = f.readlines()

locations = {}

for distance in distances:
    distance = distance.split()
    loc1, loc2, dist = distance[0], distance[2], int(distance[4])
    if loc1 not in locations:
        locations[loc1] = {}
    if loc2 not in locations:
        locations[loc2] = {}
    locations[loc1][loc2] = dist
    locations[loc2][loc1] = dist

route_lengths = set()

for route in permutations(locations):
    distance = 0
    for i in range(1, len(route)):
        distance += locations[route[i-1]][route[i]]
    route_lengths.add(distance)

print(min(route_lengths))
print(max(route_lengths))
