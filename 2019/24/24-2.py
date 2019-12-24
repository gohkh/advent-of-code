import copy

with open("24.txt", 'r') as f:
    grid = [list(x.strip()) for x in f.readlines()]

empty_grid = [['.'] * 5 for i in range(5)]
level = dict()
for i in range(-201, 202):
    level[i] = copy.deepcopy(empty_grid)
level[0] = grid

def adjacent_bug_count(x, y, z):
    count = 0

    if y == 0: # top
        if previous_level[z-1][1][2] == '#':
            count += 1
    elif y == 3 and x == 2:
        for a in previous_level[z+1][4]:
            if a == '#':
                count += 1
    else:
        if previous_level[z][y-1][x] == '#':
            count += 1

    if x == 0: # left
        if previous_level[z-1][2][1] == '#':
            count += 1
    elif x == 3 and y == 2:
        for i in range(5):
            if previous_level[z+1][i][4] == '#':
                count += 1
    else:
        if previous_level[z][y][x-1] == '#':
            count += 1

    if x == 4: # right
        if previous_level[z-1][2][3] == '#':
            count += 1
    elif x == 1 and y == 2:
        for i in range(5):
            if previous_level[z+1][i][0] == '#':
                count += 1
    else:
        if previous_level[z][y][x+1] == '#':
            count += 1

    if y == 4: # bottom
        if previous_level[z-1][3][2] == '#':
            count += 1
    elif y == 1 and x == 2:
        for a in previous_level[z+1][0]:
            if a == '#':
                count += 1
    else:
        if previous_level[z][y+1][x] == '#':
            count += 1

    return count

for i in range(1, 201):
    previous_level = dict()
    for j in range(-i - 1, i + 2):
        previous_level[j] = copy.deepcopy(level[j])
    for z in range(-i, i + 1):
        for y in range(len(level[z])):
            for x in range(len(level[z][0])):
                if x == 2 and y == 2:
                    continue
                if level[z][y][x] == '#':
                    if not adjacent_bug_count(x, y, z) == 1:
                        level[z][y][x] = '.'
                elif level[z][y][x] == '.':
                    if 1 <= adjacent_bug_count(x, y, z) <= 2:
                        level[z][y][x] = '#'

count = 0
for z in range(-200, 201):
    for row in level[z]:
        count += sum([1 if x == '#' else 0 for x in row])
print(count)
