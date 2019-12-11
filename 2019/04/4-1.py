start = 145852
end = 616942
count = 0

def double(x):
    x = str(x)
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            return True
    return False

def increasing(x):
    x = str(x)
    for i in range(1, len(x)):
        if int(x[i]) < int(x[i-1]):
            return False
    return True

for i in range(start, end + 1):
    if double(i) and increasing(i):
        count += 1

print(count)
