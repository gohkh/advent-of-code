with open("9.txt", 'r') as f:
    program = f.readlines()[0]

program = [int(x) for x in program.split(",")]
program = {k: v for k, v in enumerate(program)}
i = 0
base = 0
op = int(str(program[i])[-2:])

while not op == 99:
    if op == 1:
        full_op = str(program[i]).rjust(5, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        y = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        z = program[i+3] + base if int(full_op[-5]) else program[i+3]
        program[z] = x + y
        i += 4
    elif op == 2:
        full_op = str(program[i]).rjust(5, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        y = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        z = program[i+3] + base if int(full_op[-5]) else program[i+3]
        program[z] = x * y
        i += 4
    elif op == 3:
        x = program[i+1] + base if int(full_op[-3]) else program[i+1]
        program[x] = int(input("ID: "))
        i += 2
    elif op == 4:
        full_op = str(program[i]).rjust(3, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        print(x)
        i += 2
    elif op == 5:
        full_op = str(program[i]).rjust(4, "0")
        jump = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        if not jump == 0:
            i = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        else:
            i += 3
    elif op == 6:
        full_op = str(program[i]).rjust(4, "0")
        jump = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        if jump == 0:
            i = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        else:
            i += 3
    elif op == 7:
        full_op = str(program[i]).rjust(5, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        y = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        z = program[i+3] + base if int(full_op[-5]) else program[i+3]
        program[z] = int(x < y)
        i += 4
    elif op == 8:
        full_op = str(program[i]).rjust(5, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        y = program[i+2] if int(full_op[-4]) % 2 else program[program[i+2] + base if int(full_op[-4]) else program[i+2]]
        z = program[i+3] + base if int(full_op[-5]) else program[i+3]
        program[z] = int(x == y)
        i += 4
    elif op == 9:
        full_op = str(program[i]).rjust(3, "0")
        x = program[i+1] if int(full_op[-3]) % 2 else program[program[i+1] + base if int(full_op[-3]) else program[i+1]]
        base += x
        i += 2
    else:
        print("error")
    op = int(str(program[i])[-2:])
