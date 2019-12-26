from itertools import permutations

with open("7.txt", 'r') as f:
    original_program = f.readlines()[0]

def run(amp, program, i, input_index):
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
            try:
                x = program[i+1]
                program[x] = inputs[amp][input_index]
                input_index += 1
                i += 2
            except IndexError:
                return (program, i, input_index)
        elif op == 4:
            full_op = str(program[i]).rjust(3, "0")
            x = program[i+1] if int(full_op[-3]) else program[program[i+1]]
            inputs[(amp+1)%5].append(x)
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
    return (None, -1, -1)

values = list()
for p in permutations(range(5, 10)):
    programs = [[int(x) for x in original_program.split(",")] for i in range(5)]
    pointers = [0] * 5
    input_indices = [0] * 5
    inputs = [[x] for x in p]
    inputs[0].append(0)
    while not programs[4] is None:
        for i in range(5):
            programs[i], pointers[i], input_indices[i] = run(i, programs[i], pointers[i], input_indices[i])
    values.append(inputs[0][-1])

print(max(values))
