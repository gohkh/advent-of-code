from itertools import combinations

with open("17.txt", 'r') as f:
    containers = [int(container.strip()) for container in f.readlines()]

count = 0
minimum = len(containers)

for i in range(len(containers)):
    if i <= minimum:
        for combination in combinations(containers, i+1):
            if sum(combination) == 150:
                count += 1
                minimum = i

print(count)
