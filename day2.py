with open('input/day2.txt') as inf:
    lines = inf.readlines()

import re
pattern = r'(\d+)-(\d+) (.): (.*)'

count_valid_1 = 0
count_valid_2 = 0
for line in lines:
    parts = re.match(pattern, line)
    min_occur = int(parts.group(1))
    max_occur = int(parts.group(2))
    symbol = parts.group(3)
    password = parts.group(4)
    pos = 0
    count = 0
    while pos < len(password) and pos >= 0:
        pos = password.find(symbol, pos)
        if pos >= 0:
            count += 1
            pos += len(symbol)
    if count >= min_occur and count <= max_occur:
        count_valid_1 += 1
    if (password[min_occur - 1] == symbol) != (password[max_occur - 1] == symbol):
        count_valid_2 += 1

print(count_valid_1)
print(count_valid_2)
