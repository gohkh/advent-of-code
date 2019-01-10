from itertools import combinations
from functools import reduce
from operator import mul

with open("24.txt", 'r') as f:
    packages = f.readlines()

packages = [int(package) for package in packages]

def entanglement(group):
    return reduce(mul, group, 1)

def balance(packages, n, total_n):
    if n == 1:
        if n < total_n:
            return True
        elif n == total_n:
            return entanglement(packages)
        return False

    group_weight = sum(packages) // n
    minimum = len(packages)
    groups = []

    for i in range(1, len(packages)):
        if i <= minimum:
            for group in combinations(packages, i):
                if sum(group) == group_weight:

                    # observe that weights of packages are unique
                    leftovers = list(set(packages) - set(group))

                    if n < total_n:
                        return balance(leftovers, n-1, total_n)

                    elif n == total_n and balance(leftovers, n-1, total_n):
                        groups.append(group)
                        minimum = i

    if n == total_n:
        groups.sort(key=entanglement)
        return entanglement(groups[0])

    return False

for total_n in range(3, 5):
    print(balance(packages, total_n, total_n))
