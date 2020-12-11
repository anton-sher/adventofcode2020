import math

with open('input/day3.txt') as inf:
    terrain = [l[0:-1] for l in inf.readlines()]

def trees_on_slope(slope_x, slope_y):
    x = 0
    y = 0
    count_trees = 0

    width = len(terrain[0])
    height = len(terrain)
    while y + slope_y < height:
        x = (x + slope_x) % width
        y += slope_y
        if terrain[y][x] == '#':
            count_trees += 1
    return count_trees

print(trees_on_slope(3, 1))
print(math.prod([trees_on_slope(sx, sy) for (sx, sy) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))