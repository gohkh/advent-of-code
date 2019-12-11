with open("2.txt", 'r') as f:
    original_program = f.readlines()[0]
    original_program = [int(x) for x in original_program.split(",")]

for noun in range(100):
    for verb in range(100):
        program = original_program.copy()
        program[1] = noun
        program[2] = verb
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

        if program[0] == 19690720:
            print(100 * noun + verb)
            break
