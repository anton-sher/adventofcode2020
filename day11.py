with open('input/day11.txt') as f:
    grid = [list(l.replace('\n', '')) for l in f.readlines()]

def ingrid(x1, y1):
    return x1 >=0 and x1 < len(grid[0]) and y1 >= 0 and y1 < len(grid)

def adj(x, y):
    return [
        (x1, y1) for (x1, y1) in [
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ]
        if ingrid(x1, y1) and not (x1 == x and y1 == y)
    ]

adj2_data = dict()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        adj2_data[(x, y)] = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    dist = 1
                    while ingrid(x + dx * dist, y + dy * dist):
                        if grid[y+dy*dist][x + dx * dist] != '.':
                            adj2_data[(x, y)].append((x + dx * dist, y+dy*dist))
                            break
                        dist += 1

def adj2(x, y):
    return adj2_data[(x, y)]

def next(grid, adjfn, thresh):
    updates = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            seat = grid[y][x]
            if seat == 'L':
                if '#' not in [grid[y1][x1] for (x1, y1) in adjfn(x, y)]:
                    updates.append((x, y, '#'))
            elif seat == '#':
                if [grid[y1][x1] for (x1, y1) in adjfn(x, y)].count('#') >= thresh:
                    updates.append((x, y, 'L'))
    for update in updates:
        grid[update[1]][update[0]] = update[2]
    return updates

while True:
    updates = next(grid, adj, 4)
    if (len(updates) == 0):
        break

print(sum([r.count('#') for r in grid]))

with open('input/day11.txt') as f:
    grid = [list(l.replace('\n', '')) for l in f.readlines()]

while True:
    updates = next(grid, adj2, 5)
    if (len(updates) == 0):
        break

print(sum([r.count('#') for r in grid]))