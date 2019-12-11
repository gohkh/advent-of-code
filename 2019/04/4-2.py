start = 145852
end = 616942
count = 0

def double(x):
    x = str(x)
    doubles = set()
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            doubles.add(x[i])
    return doubles

def increasing(x):
    x = str(x)
    for i in range(1, len(x)):
        if int(x[i]) < int(x[i-1]):
            return False
    return True

def triple(x):
    x = str(x)
    triples = set()
    for i in range(2, len(x)):
        if x[i] == x[i-1] == x[i-2]:
            triples.add(x[i])
    return triples

for i in range(start, end + 1):
    if increasing(i) and double(i) > triple(i):
        count += 1

print(count)
