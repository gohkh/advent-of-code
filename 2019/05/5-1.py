with open("5.txt", 'r') as f:
    program = f.readlines()[0]

program = [int(x) for x in program.split(",")]
i = 0
op = int(str(program[i])[-2:])

while not op == 99:
    if op == 1:
        full_op = str(program[i]).rjust(4, "0")
        x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
        y = program[i+2] if int(full_op[-4]) else program[program[i+2]]
        z = program[i+3]
        program[z] = x + y
        i += 4
    elif op == 2:
        full_op = str(program[i]).rjust(4, "0")
        x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
        y = program[i+2] if int(full_op[-4]) else program[program[i+2]]
        z = program[i+3]
        program[z] = x * y
        i += 4
    elif op == 3:
        x = program[i+1]
        program[x] = int(input("ID: "))
        i += 2
    elif op == 4:
        full_op = str(program[i]).rjust(3, "0")
        x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
        print(x)
        i += 2
    else:
        print("error")

    op = int(str(program[i])[-2:])
