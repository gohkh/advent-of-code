with open("3.txt", 'r') as f:
    directions = f.readlines()[0]

house = (0, 0)
houses = {house}

for direction in directions:
    x, y = house
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    house = (x, y)
    houses.add(house)

print(len(houses))
