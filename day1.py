with open('input/day1.txt') as f:
    numbers = [int(l) for l in  f.readlines()]

print([
    (a, b, a * b)
    for a in numbers
    for b in numbers
    if a + b == 2020
])

print([
    (a, b, c, a * b * c)
    for a in numbers
    for b in numbers
    for c in numbers
    if a + b + c == 2020
])