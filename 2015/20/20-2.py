puzzle_input = 33100000

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if not n % i
        for factor in (i, n//i)
    )

house = 0
presents = 0
elves = {}

while presents < puzzle_input:
    house += 1
    presents = 0

    for factor in factors(house):
        if factor in elves:
            if elves[factor]:
                presents += 11 * factor
                elves[factor] -= 1
        else:
            elves[factor] = 49
            presents += 11 * factor

print(house)
