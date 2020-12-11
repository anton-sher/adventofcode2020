with open('input/day5.txt') as f:
    lines = f.readlines()

def seat_id(line):
    row = 0
    b = 64
    for i in range(0,7):
        if line[i] == 'B':
            row += b
        b //= 2
    b = 4
    col = 0
    for i in range(7, 10):
        if line[i] == 'R':
            col += b
        b //= 2
    return row * 8 + col

seat_ids = [seat_id(line) for line in lines]
print(max(seat_ids))

for i in sorted(seat_ids):
    if (i + 1) not in seat_ids:
        print(i + 1)
        break