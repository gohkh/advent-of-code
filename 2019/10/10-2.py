import math

with open("10.txt", 'r') as f:
    asteroid_map = [list(x.strip()) for x in f.readlines()]

def asteroid_count(x0, y0):
    detection_map = [row.copy() for row in asteroid_map]
    for y in range(len(asteroid_map)):
        for x in range(len(asteroid_map[0])):
            if detection_map[y][x] == '#' and not (x == x0 and y == y0):
                x_diff = x - x0
                y_diff = y - y0
                for i in range(max(abs(x_diff), abs(y_diff)), 0, -1):
                    if not x_diff % i and not y_diff % i:
                        x_diff = x_diff // i
                        y_diff = y_diff // i
                        break
                new_x = x + x_diff
                new_y = y + y_diff
                while 0 <= new_x < len(detection_map[0]) and 0 <= new_y < len(detection_map):
                    detection_map[new_y][new_x] = '.'
                    new_x += x_diff
                    new_y += y_diff
    return sum([sum([1 if x == '#' else 0 for x in row]) for row in detection_map]) - 1



detection = list()
for y in range(len(asteroid_map)):
    for x in range(len(asteroid_map[0])):
        if asteroid_map[y][x] == '#':
            detection.append((x, y, asteroid_count(x, y)))
x0, y0, count = max(detection, key=lambda x: x[2])

asteroids = list()
for y in range(len(asteroid_map)):
    for x in range(len(asteroid_map[0])):
        if asteroid_map[y][x] == '#' and not (x == x0 and y == y0):
            angle = math.atan2(y - y0, x - x0)
            angle = angle + math.pi / 2
            if angle < 0:
                angle += 2 * math.pi
            asteroids.append([x, y, angle, abs(x-x0) + abs(y-y0)])
asteroids.sort(key=lambda x: x[3])
asteroids.sort(key=lambda x: x[2])

i = 1
while i < len(asteroids):
    if asteroids[i][2] == asteroids[i-1][2]:
        repeat = 1
        while i+repeat <= len(asteroids) and asteroids[i+repeat-1][2] == asteroids[i-1][2]:
            asteroids[i+repeat-1][2] += repeat * 2 * math.pi
            repeat += 1
        i += repeat - 1
    else:
        i += 1

asteroids.sort(key=lambda x: x[2])
print(100 * asteroids[199][0] + asteroids[199][1])
