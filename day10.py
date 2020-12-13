with open('input/day10.txt') as f:
    ratings = sorted([int(l) for l in f.readlines()])

dist = dict()
for i in range(len(ratings) - 1):
    diff = ratings[i+1] - ratings[i]
    dist[diff] = dist.get(diff, 0) + 1

dist[ratings[0]] = dist.get(ratings[0], 0) + 1
dist[3] = dist.get(3, 0) + 1

print(dist[1] * dist[3])

num_combis = dict()
num_combis[0] = 1

for rating in ratings:
    num_combis[rating] = 0
    for i in [1, 2, 3]:
        num_combis[rating] += num_combis.get(rating - i, 0)

print(num_combis[ratings[-1]])