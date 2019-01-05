import re

with open("6.txt", 'r') as f:
    insts = f.readlines()

grid = [[0]*1000 for i in range(1000)]

for inst in insts:
    boundaries = re.findall("\d+", inst)
    x, y, X, Y = [int(boundary) for boundary in boundaries]
    for j in range(y, Y+1):
        for i in range(x, X+1):
            if "on" in inst:
                grid[j][i] += 1
            elif "off" in inst:
                if grid[j][i] > 0:
                    grid[j][i] -= 1
            else:
                grid[j][i] += 2

print(sum(sum(row) for row in grid))
