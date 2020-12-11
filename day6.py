from functools import reduce

with open('input/day6.txt') as f:
    text = f.read()

print(sum([len(set([c for c in s]) - {'\n'}) for s in text.split('\n\n')]))

print(sum([
    len(reduce(lambda s1, s2: s1 & s2, [set([c for c in s1]) - {'\n'} for s1 in s.split('\n')])) 
    for s in text.split('\n\n')]))