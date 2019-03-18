with open ("2.txt", 'r') as f:
    lines = f.readlines()

code = ""
grid = [[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,"A","B","C",0], [0,0,"D",0,0]]
coords = {"x": 0, "y": 2}

def move(axis, amount):
    coords[axis] += amount
    if grid[coords["y"]][coords["x"]] == 0:
        coords[axis] -= amount

for line in lines:
    for instruction in line:
        if instruction == "U" and coords["y"] > 0:
            move("y", -1)
        if instruction == "D" and coords["y"] < 4:
            move("y", 1)
        if instruction == "L" and coords["x"] > 0:
            move("x", -1)
        if instruction == "R" and coords["x"] < 4:
            move("x", 1)

    code += str(grid[coords["y"]][coords["x"]])

print(code)
