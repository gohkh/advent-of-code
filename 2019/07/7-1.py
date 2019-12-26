from itertools import permutations

with open("7.txt", 'r') as f:
    original_program = f.readlines()[0]

def run(phase, input_value):
    inputs = (phase, input_value)
    input_index = 0
    program = [int(x) for x in original_program.split(",")]
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
            program[x] = inputs[input_index]
            input_index += 1
            i += 2
        elif op == 4:
            full_op = str(program[i]).rjust(3, "0")
            x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            return x
            i += 2
        elif op == 5:
            full_op = str(program[i]).rjust(4, "0")
            jump = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            if not jump == 0:
                i = program[i+2] if int(full_op[-4]) else program[program[i+2]]
            else:
                i += 3
        elif op == 6:
            full_op = str(program[i]).rjust(4, "0")
            jump = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            if jump == 0:
                i = program[i+2] if int(full_op[-4]) else program[program[i+2]]
            else:
                i += 3
        elif op == 7:
            full_op = str(program[i]).rjust(4, "0")
            x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            y = program[i+2] if int(full_op[-4]) else program[program[i+2]]
            z = program[i+3]
            program[z] = int(x < y)
            i += 4
        elif op == 8:
            full_op = str(program[i]).rjust(4, "0")
            x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            y = program[i+2] if int(full_op[-4]) else program[program[i+2]]
            z = program[i+3]
            program[z] = int(x == y)
            i += 4
        else:
            print("error")
        op = int(str(program[i])[-2:])

values = list()
for p in permutations(range(5)):
    value = 0
    for i in range(5):
        value = run(p[i], value)
    values.append(value)

print(max(values))
