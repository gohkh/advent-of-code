import numpy as np

with open("18.txt", 'r') as f:
    configuration = f.readlines()

grid = np.zeros((102, 102), dtype=int)

for i, row in enumerate(configuration):
    for j, light in enumerate(row):
        if light == "#":
            grid[i+1][j+1] = 1

new_grid = np.copy(grid)

for t in range(100):
    for i in range(1, 101):
        for j in range(1, 101):
            light = grid[i][j]
            subgrid = grid[i-1:i+2, j-1:j+2]
            if light and np.count_nonzero(subgrid) not in (3, 4):
                new_grid[i][j] = 0
            if not light and np.count_nonzero(subgrid) == 3:
                new_grid[i][j] = 1
    grid = np.copy(new_grid)

print(np.count_nonzero(new_grid))
