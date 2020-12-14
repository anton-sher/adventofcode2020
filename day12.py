with open('input/day12.txt') as f:
    commands = [(lc[0], int(lc[1:])) for l in f.readlines() for lc in [l.replace('\n', '')]]

dirx = 1
diry = 0

x = 0
y = 0

def rot(dx, dy, turns, sign):
    dx2, dy2 = dx, dy
    for _ in range(turns):
        dx2, dy2 = - dy2 * sign, dx2 * sign
    return dx2, dy2

for (cmd, val) in commands:
    ox, oy, odirx, odiry = x, y, dirx, diry
    if cmd == 'N':
        y += val
    elif cmd == 'S':
        y -= val
    elif cmd == 'W':
        x -= val
    elif cmd == 'E':
        x += val
    elif cmd == 'L':
        dirx, diry = rot(dirx, diry, val // 90, 1)
    elif cmd == 'R':
        dirx, diry = rot(dirx, diry, val // 90, -1)
    elif cmd == 'F':
        x, y = x + dirx * val, y + diry * val
    else:
        raise Exception("what is " + cmd)
    # print(ox, oy, odirx, odiry, '(', cmd, val, ')->', x, y, dirx, diry)

print(x, y, abs(x) + abs(y))

# part 2

x, y = 0, 0
dirx, diry = 10, 1

for (cmd, val) in commands:
    ox, oy, odirx, odiry = x, y, dirx, diry
    if cmd == 'N':
        diry += val
    elif cmd == 'S':
        diry -= val
    elif cmd == 'W':
        dirx -= val
    elif cmd == 'E':
        dirx += val
    elif cmd == 'L':
        dirx, diry = rot(dirx, diry, val // 90, 1)
    elif cmd == 'R':
        dirx, diry = rot(dirx, diry, val // 90, -1)
    elif cmd == 'F':
        x, y = x + dirx * val, y + diry * val
    else:
        raise Exception("what is " + cmd)
    # print(ox, oy, odirx, odiry, '(', cmd, val, ')->', x, y, dirx, diry)

print(x, y, abs(x) + abs(y))
