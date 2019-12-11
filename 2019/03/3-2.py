with open("3.txt", 'r') as f:
    wires = [wire.strip().split(",") for wire in f.readlines()]

for wire in wires:
    start = (0, 0)
    for i in range(len(wire)):
        direction = wire[i][0]
        magnitude = int(wire[i][1:])
        if direction == "U":
            end = (start[0], start[1] + magnitude)
            wire[i] = (start, end, magnitude, 1)
        elif direction == "D":
            end = (start[0], start[1] - magnitude)
            wire[i] = (end, start, magnitude, 0)
        elif direction == "R":
            end = (start[0] + magnitude, start[1])
            wire[i] = (start, end, magnitude, 1)
        elif direction == "L":
            end = (start[0] - magnitude, start[1])
            wire[i] = (end, start, magnitude, 0)
        start = end

distances = []
distX = 0
for x in wires[0]:
    distY = 0
    for y in wires[1]:
        if (x[0] == (0, 0) or x[1] == (0, 0)) and (y[0] == (0, 0) or y[1] == (0, 0)):
            distY += y[2]
            continue
        elif (x[0][0] == x[1][0] == y[0][0] == y[1][0]):
            for i in range(x[0][1], x[1][1] + 1):
                if y[0][1] <= i <= y[1][1]:
                    if x[3]:
                        addX = i - x[0][1]
                    else:
                        addX = x[1][1] - i
                    if y[3]:
                        addY = i - y[0][1]
                    else:
                        addY = y[1][1] - i
                    distances.append(distX + addX + distY + addY)
        elif (x[0][1] == x[1][1] == y[0][1] == y[1][1]):
            for i in range(x[0][0], x[1][0] + 1):
                if y[0][0] <= i <= y[1][0]:
                    if x[3]:
                        addX = i - x[0][0]
                    else:
                        addX = x[1][0] - i
                    if y[3]:
                        addY = i - y[0][0]
                    else:
                        addY = y[1][0] - i
                    distances.append(distX + addX + distY + addY)
        elif (x[0][0] == x[1][0] and y[0][1] == y[1][1]):
            if x[0][1] <= y[0][1] <= x[1][1] and y[0][0] <= x[0][0] <= y[1][0]:
                if x[3]:
                    addX = y[0][1] - x[0][1]
                else:
                    addX = x[1][1] - y[0][1]
                if y[3]:
                    addY = x[0][0] - y[0][0]
                else:
                    addY = y[1][0] - x[0][0]
                distances.append(distX + addX + distY + addY)
        elif (x[0][1] == x[1][1] and y[0][0] == y[1][0]):
            if x[0][0] <= y[0][0] <= x[1][0] and y[0][1] <= x[0][1] <= y[1][1]:
                if x[3]:
                    addX = y[0][0] - x[0][0]
                else:
                    addX = x[1][0] - y[0][0]
                if y[3]:
                    addY = x[0][1] - y[0][1]
                else:
                    addY = y[1][1] - x[0][1]
                distances.append(distX + addX + distY + addY)
        distY += y[2]
    distX += x[2]

print(min(distances))
