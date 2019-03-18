with open("1.txt", 'r') as f:
    changes = f.readlines()

changes = [int(change.strip()) for change in changes]
print(sum(changes))
