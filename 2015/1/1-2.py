with open("1.txt", 'r') as f:
    instructions = f.readlines()[0]

floor = 0

for i, inst in enumerate(instructions):
    if inst == "(":
        floor += 1
    elif inst == ")":
        floor -= 1

    if floor == -1:
        print(i + 1)
        break
