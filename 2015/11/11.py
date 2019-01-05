puzzle_input = "vzbxkghb"

pw = [ord(letter) for letter in puzzle_input]

def next_pw(pw):
    pw[-1] += 1
    for i in range(len(pw)):
        if pw[-i-1] > 122:
            pw[-i-1] = 97
            pw[-i-2] += 1
    return pw

def valid(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return 0

    pair = set()
    prev = ""
    for letter in pw:
        if letter == prev:
            pair.add(letter)
        prev = letter
    if len(pair) < 2:
        return 0

    for i in range(6):
        three = pw[i:i+3]
        three = [x - three[0] for x in three]
        if three == [0, 1, 2]:
            return 1

    return 0

for i in range(2):
    while not valid(pw):
        pw = next_pw(pw)

    print(''.join(chr(letter) for letter in pw))

    pw = next_pw(pw)
