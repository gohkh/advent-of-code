with open("3.txt", 'r') as f:
    directions = f.readlines()[0]

santa = (0, 0)
robo = (0, 0)
houses = {santa, robo}

for i, direction in enumerate(directions):
    x, y = (robo if i % 2 else santa)
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    if i % 2:
        house = robo = (x, y)
    else:
        house = santa = (x, y)
    houses.add(house)

print(len(houses))
