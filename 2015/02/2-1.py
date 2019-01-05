with open("2.txt", 'r') as f:
    presents = f.readlines()

presents = [present.strip().split("x") for present in presents]
presents = [sorted(int(x) for x in present) for present in presents]

paper = 0

for present in presents:
    l, w, h = present
    paper += (3*l*w + 2*w*h + 2*h*l)

print(paper)
