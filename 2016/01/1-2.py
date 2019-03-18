with open("1.txt", 'r') as f:
    instructions = f.readlines()[0]

instructions = instructions.split(", ")
axes = ["NS", "EW"]
index = 0
location = {"NS": 0, "EW": 0}
locations = set()
twice = False

for instruction in instructions:
    if instruction[0] == "R":
        index += 1
    elif instruction[0] == "L":
        index -= 1
    index %= 4
    axis = axes[index%2]
    unit_displacement = (-1)**(index//2)
    distance = int(instruction[1:])

    for i in range(distance):
        location[axis] += unit_displacement
        if (location["NS"], location["EW"]) in locations:
            shortest_distance = abs(location["NS"]) + abs(location["EW"])
            print(shortest_distance)
            twice = True
            break
        else:
            locations.add((location["NS"], location["EW"]))

    if twice:
        break
