with open("2.txt", 'r') as f:
    presents = f.readlines()

presents = [present.strip().split("x") for present in presents]
presents = [sorted(int(x) for x in present) for present in presents]

ribbon = 0

for present in presents:
    l, w, h = present
    ribbon += (2*(l+w) + l*w*h)

print(ribbon)
