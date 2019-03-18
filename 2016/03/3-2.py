with open("3.txt", 'r') as f:
    triangles = f.readlines()

triangles = [[int(x) for x in triangle.split()] for triangle in triangles]
possible = 0

for i in range(len(triangles)//3):
    triangle0 = [triangles[3*i][0], triangles[3*i+1][0], triangles[3*i+2][0]]
    triangle1 = [triangles[3*i][1], triangles[3*i+1][1], triangles[3*i+2][1]]
    triangle2 = [triangles[3*i][2], triangles[3*i+1][2], triangles[3*i+2][2]]
    for triangle in [triangle0, triangle1, triangle2]:
        triangle.sort()
        possible += int(triangle[0] + triangle[1] > triangle[2])

print(possible)
