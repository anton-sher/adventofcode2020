with open('input/day13.txt') as f:
    start_ts = int(f.readline())
    buses = list(map(int, filter(lambda x: x != 'x', f.readline().split(','))))

def mins_wait(ts, bus):
    mins_before = ts % bus
    if mins_before == 0:
        return 0
    else:
        return bus - mins_before

min_bus = 0
min_wait = 10000

for bus in buses:
    w = mins_wait(start_ts, bus)
    if w < min_wait:
        min_wait = w
        min_bus = bus

print(min_bus * min_wait)

with open('input/day13.txt') as f:
    start_ts = int(f.readline())
    buses = list(map(int, map(lambda x: '0' if x == 'x' else x, f.readline().split(','))))

maxbus = max(buses)
n = buses.index(maxbus)

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(buses)

bus_rest = [(val, i) for (i, val) in enumerate(buses) if val != 0]

n = 0
mul = 1

for (bus, rest) in bus_rest:
    while (n + rest) % bus != 0:
        n += mul
    mul = lcm(mul, bus)

print(n)
