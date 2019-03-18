with open ("2.txt", 'r') as f:
    lines = f.readlines()

code = ""
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = y = 1

for line in lines:
    for instruction in line:
        if instruction == "U" and y > 0:
            y -= 1
        if instruction == "D" and y < 2:
            y += 1
        if instruction == "L" and x > 0:
            x -= 1
        if instruction == "R" and x < 2:
            x += 1

    code += str(grid[y][x])

print(code)
