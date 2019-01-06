puzzle_input = 33100000

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if not n % i
        for factor in (i, n//i)
    )

house = 0
presents = 0

while presents < puzzle_input:
    house += 1
    presents = 10 * sum(factors(house))

print(house)
