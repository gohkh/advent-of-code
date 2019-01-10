with open("23.txt", 'r') as f:
    instructions = f.readlines()

instructions = [inst.split() for inst in instructions]

def run(pc):
    inst = instructions[pc]
    name = inst[0]
    reg = inst[1]

    if name == "hlf":
        regs[reg] //= 2

    elif name == "tpl":
        regs[reg] *= 3

    elif name == "inc":
        regs[reg] += 1

    elif name == "jie" or name == "jio":
        reg = reg[:-1]
        value = regs[reg]

        if (name == "jie" and not value % 2) or (name == "jio" and value == 1):
            name = "jmp"
            reg = inst[2]

    if name == "jmp":
        pc += (int(reg) - 1)

    pc += 1
    return pc

for i in range(2):
    pc = 0
    regs = {"a": i, "b": 0}

    while pc < len(instructions):
        pc = run(pc)

    print(regs["b"])
