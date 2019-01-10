def next_position(position):
    row, column = position
    if row == 1:
        return column + 1, 1
    else:
        return row - 1, column + 1

def next_code(code):
    return (code * 252533) % 33554393

position = (1, 1)
code = 20151125

while not position == (3010,3019): # puzzle input
    position = next_position(position)
    code = next_code(code)

print(code)
