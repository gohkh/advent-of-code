with open("2.txt", 'r') as f:
    program = f.readlines()[0]

program = [int(x) for x in program.split(",")]
program[1] = 12
program[2] = 2
i = 0

while not program[i] == 99:
    x = program[i+1]
    y = program[i+2]
    z = program[i+3]

    if program[i] == 1:
        program[z] = program[x] + program[y]
    elif program[i] == 2:
        program[z] = program[x] * program[y]
    else:
        print("error")

    i += 4

print(program[0])
