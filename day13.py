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

while True:
    found = True
    for i in range(len(buses)):
        if buses[i] != 0 and n % buses[i] != i:
            found = False
            break
    if found:
        break
    n += maxbus

print(n)
