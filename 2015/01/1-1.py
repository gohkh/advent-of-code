with open("1.txt", 'r') as f:
    instructions = f.readlines()[0]

floor = instructions.count("(") - instructions.count(")")
print(floor)
