with open('input/day9.txt') as f:
    numbers = [int(l) for l in f.readlines()]

print(numbers)

idx = 25

while numbers[idx] in [a + b for a in numbers[idx-25:idx] for b in numbers[idx-25:idx]]:
    idx += 1

answer1 = numbers[idx]
print(answer1)

for start in range(len(numbers)):
    for stop in range(start, len(numbers)):
        s = numbers[start:stop]
        if sum(s) == answer1:
            print(min(s) + max(s))
            break
    else:
        continue
    break
