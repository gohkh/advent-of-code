with open("7.txt", 'r') as f:
    insts = f.readlines()

insts = [inst.split() for inst in insts]
wires = {}

def get_value(src):
    try:
        return int(src)
    except ValueError:
        if src in wires:
            return wires[src]
        else:
            return src

while insts:
    inst = insts.pop(0)
    dest = inst[-1]

    if len(inst) == 3:
        src1 = inst[0]
        src2, op = src1, ""
    elif len(inst) == 4:
        op, src1 = inst[:2]
        src2 = src1
    elif len(inst) == 5:
        src1, op, src2 = inst[:3]

    src1, src2 = get_value(src1), get_value(src2)
    if not (type(src1) == int and type(src2) == int):
        insts.append(inst)
        continue

    if op == "":
        wires[dest] = src1
    elif op == "NOT":
        wires[dest] = 2**16 - src1 - 1
    elif op == "AND":
        wires[dest] = src1 & src2
    elif op == "OR":
        wires[dest] = src1 | src2
    elif op == "LSHIFT":
        wires[dest] = src1 << src2
    elif op == "RSHIFT":
        wires[dest] = src1 >> src2

print(wires['a'])
