with open("8.txt", 'r') as f:
    codes = f.readlines()

codes = [code.strip() for code in codes]

total_diff = 0

for code in codes:
    diff = code.count("\"") + code.count("\\\\")
    code = code.replace("\\\\", "")
    diff += 3 * code.count("\\x")
    total_diff += diff

print(total_diff)
