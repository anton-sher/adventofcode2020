with open('input/day14.txt') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

mask = ''
mem = dict()

for l in lines:
    if l.startswith('mask = '):
        mask = l[7:]
    elif l.startswith('mem'):
        addr, val = l[4:].split('] = ')
        addr, val = int(addr), int(val)
        valb = "{0:036b}".format(val)
        mem[addr] = int(''.join([mask[i] if mask[i] != 'X' else valb[i] for i in range(36)]), 2)

print(sum(mem.values()))

mask = ''
mem = dict()

for l in lines:
    if l.startswith('mask = '):
        mask = l[7:]
    elif l.startswith('mem'):
        addr, val = l[4:].split('] = ')
        addr, val = int(addr), int(val)
        addrb = "{0:036b}".format(addr)
        xses = mask.count('X')
        for flt in range(2 ** xses):
            fltb = ("{0:0" + str(xses) + "b}").format(flt)
            j = 0
            d = []
            for i in range(36):
                if mask[i] == 'X':
                    d.append(fltb[j])
                    j += 1
                elif mask[i] == '0':
                    d.append(addrb[i])
                else:
                    d.append('1')
            mem[int(''.join(d), 2)] = val

print(sum(mem.values()))