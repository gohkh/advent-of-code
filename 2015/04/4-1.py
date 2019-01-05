puzzle_input = "yzbqklnj"

import hashlib

number = 0
md5_hash = ""

while not md5_hash[:5] == "00000":
    number += 1
    key = puzzle_input + str(number)
    md5_hash = hashlib.md5(key.encode()).hexdigest()

print(number)
