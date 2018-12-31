puzzle_input = "3113322113"

prev_seq = puzzle_input
next_seq = ""
n, count = "", ""

for i in range(50):
    for number in prev_seq:
        if number == n:
            count += 1
        else:
            next_seq += (str(count) + n)
            n = number
            count = 1
    prev_seq = next_seq + str(count) + n
    next_seq = ""
    n, count = "", ""

    if i == 39:
        print(len(prev_seq))

print(len(prev_seq))
