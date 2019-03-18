with open("1.txt", 'r') as f:
    instructions = f.readlines()[0]

directions = ["North", "East", "South", "West"]
index = 0
location = {"North": 0, "East": 0, "South": 0, "West": 0}

instructions = instructions.split(", ")
for instruction in instructions:
    if instruction[0] == "R":
        index += 1
    elif instruction[0] == "L":
        index -= 1
    index %= 4
    direction = directions[index]

    distance = int(instruction[1:])
    location[direction] += distance

shortest_distance = abs(location["North"] - location["South"]) + abs(location["East"] - location["West"])
print(shortest_distance)
