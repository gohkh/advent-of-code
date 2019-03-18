with open("3.txt", 'r') as f:
    triangles = f.readlines()

triangles = [[int(x) for x in triangle.split()] for triangle in triangles]
possible = 0

for triangle in triangles:
    triangle.sort()
    possible += int(triangle[0] + triangle[1] > triangle[2])

print(possible)
