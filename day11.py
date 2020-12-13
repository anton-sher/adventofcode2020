with open('input/day11.txt') as f:
    grid = [list(l.replace('\n', '')) for l in f.readlines()]

def adj(x, y):
    return [
        (x1, y1) for (x1, y1) in [
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ]
        if x1 >=0 and x1 < len(grid[0]) and y1 >= 0 and y1 < len(grid) and not (x1 == x and y1 == y)
    ]

def next(grid):
    updates = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            seat = grid[y][x]
            if seat == 'L':
                if '#' not in [grid[y1][x1] for (x1, y1) in adj(x, y)]:
                    updates.append((x, y, '#'))
            elif seat == '#':
                if [grid[y1][x1] for (x1, y1) in adj(x, y)].count('#') >= 4:
                    updates.append((x, y, 'L'))
    for update in updates:
        grid[update[1]][update[0]] = update[2]
    return len(updates) > 0

while next(grid):
    pass

print(sum([r.count('#') for r in grid]))