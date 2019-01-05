with open("8.txt", 'r') as f:
    strings = f.readlines()

strings = [string.strip() for string in strings]

diffs = [(2 + string.count("\"") + string.count("\\")) for string in strings]
total_diff = sum(diffs)

print(total_diff)
