with open("24.txt", 'r') as f:
    grid = f.readlines()

grid = [list(x.strip()) for x in grid]
for x in grid:
    x.insert(0, '.')
    x.append('.')

padding = ['.'] * len(grid[0])
grid.insert(0, padding)
grid.append(padding)

history = set()
rating = 0
for y in range(1, len(grid) - 1): # current rating
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == '#':
            rating += 2**((y-1)*(len(grid[0])-2) + x - 1)

def adjacent_bug_count(x, y):
    count = 0
    if grid[y-1][x] == '#':
        count += 1
    if grid[y][x-1] == '#':
        count += 1
    if grid[y][x+1] == '#':
        count += 1
    if grid[y+1][x] == '#':
        count += 1
    return count

while not rating in history:
    new_grid = [['.']*len(grid[0]) for i in range(len(grid))]
    history.add(rating)
    rating = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == '#':
                if adjacent_bug_count(x, y) == 1:
                    new_grid[y][x] = '#'
                    rating += 2**((y-1)*(len(grid[0])-2) + x - 1)
            elif grid[y][x] == '.':
                if 1 <= adjacent_bug_count(x, y) <= 2:
                    new_grid[y][x] = '#'
                    rating += 2**((y-1)*(len(grid[0])-2) + x - 1)
    grid = new_grid

print(rating)
