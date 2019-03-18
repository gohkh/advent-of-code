with open("1.txt",'r') as f:
    changes = f.readlines()

changes = [int(change.strip()) for change in changes]
freq = 0
freqs = {freq}
duplicate = False

while not duplicate:
    for change in changes:
        freq += change
        if freq in freqs:
            duplicate = True
            break
        else:
            freqs.add(freq)

print(freq)
