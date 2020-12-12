with open('input/day8.txt') as f:
    input_lines = [l.replace('\n', '') for l in f.readlines()]

instructions = [
    (i[0], int(i[1]))
    for instruction in input_lines
    for i in [instruction.split(' ')]
]

executed = set()
ptr = 0
acc = 0
while True:
    if ptr in executed:
        break
    executed.add(ptr)
    ins, cnt = instructions[ptr]
    if ins == 'nop':
        ptr += 1
    elif ins == 'jmp':
        ptr += cnt
    elif ins == 'acc':
        acc += cnt
        ptr += 1
    else:
        raise Exception("WTH")

print(acc)

def execute(change_at_ptr):
    executed = set()
    ptr = 0
    acc = 0
    while True:
        if ptr >= len(instructions):
            good = True
            break
        if ptr in executed:
            good = False
            break
        executed.add(ptr)
        ins, cnt = instructions[ptr]
        if ptr == change_at_ptr:
            if ins == 'acc':
                good = False
                break
            elif ins == 'nop':
                ins = 'jmp'
            elif ins == 'jmp':
                ins = 'nop'
            else:
                raise Exception("WTH")
        if ins == 'nop':
            ptr += 1
        elif ins == 'jmp':
            ptr += cnt
        elif ins == 'acc':
            acc += cnt
            ptr += 1
        else:
            raise Exception("WTH")
    return good, acc

for c in range(len(instructions)):
    good, acc = execute(c)
    if good:
        print(acc)
        break
