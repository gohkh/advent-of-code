from itertools import combinations

with open("17.txt", 'r') as f:
    containers = [int(container.strip()) for container in f.readlines()]

count = 0

for i in range(len(containers)):
    for combination in combinations(containers, i+1):
        if sum(combination) == 150:
            count += 1

print(count)
