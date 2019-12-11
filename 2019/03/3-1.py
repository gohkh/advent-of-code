with open("3.txt", 'r') as f:
    wires = [wire.strip().split(",") for wire in f.readlines()]

for wire in wires:
    start = (0, 0)
    for i in range(len(wire)):
        direction = wire[i][0]
        magnitude = int(wire[i][1:])
        if direction == "U":
            end = (start[0], start[1] + magnitude)
            wire[i] = (start, end)
        elif direction == "D":
            end = (start[0], start[1] - magnitude)
            wire[i] = (end, start)
        elif direction == "R":
            end = (start[0] + magnitude, start[1])
            wire[i] = (start, end)
        elif direction == "L":
            end = (start[0] - magnitude, start[1])
            wire[i] = (end, start)
        start = end

distances = []
for x in wires[0]:
    for y in wires[1]:
        if (x[0] == (0, 0) or x[1] == (0, 0)) and (y[0] == (0, 0) or y[1] == (0, 0)):
            continue
        elif (x[0][0] == x[1][0] == y[0][0] == y[1][0]):
            for i in range(x[0][1], x[1][1] + 1):
                if y[0][1] <= i <= y[1][1]:
                    distances.append(abs(x[0][0]) + abs(i))
        elif (x[0][1] == x[1][1] == y[0][1] == y[1][1]):
            for i in range(x[0][0], x[1][0] + 1):
                if y[0][0] <= i <= y[1][0]:
                    distances.append(abs(x[0][1]) + abs(i))
        elif (x[0][0] == x[1][0] and y[0][1] == y[1][1]):
            if x[0][1] <= y[0][1] <= x[1][1] and y[0][0] <= x[0][0] <= y[1][0]:
                distances.append(abs(x[0][0]) + abs(y[0][1]))
        elif (x[0][1] == x[1][1] and y[0][0] == y[1][0]):
            if x[0][0] <= y[0][0] <= x[1][0] and y[0][1] <= x[0][1] <= y[1][1]:
                distances.append(abs(x[0][1]) + abs(y[0][0]))

print(min(distances))
