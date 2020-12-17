with open('input/day16.txt') as f:
    rules_s, yours_s, others_s = f.read().split('\n\n')

rules = dict()
for rule_line in rules_s.splitlines():
    name, range_strs = rule_line.split(': ')
    range_strs = range_strs.split(' or ')
    ranges = [(int(s), int(e)) for rs in range_strs for (s, e) in [rs.split('-')]]
    rules[name] = ranges

yours = [int(v) for v in yours_s.split('\n')[1].split(',')]

theirs = [[int(v) for v in others_line.split(',')] for others_line in others_s.split('\n')[1:]]

bad_vals = []
good_tickets = []
for ticket in theirs:
    for v in ticket:
        for name in rules:
            for rule in rules[name]:
                if v >= rule[0] and v <= rule[1]:
                    break
            else:
                continue
            break
        else:
            bad_vals.append(v)

print(sum(bad_vals))

good_tickets = []
for ticket in theirs:
    for v in ticket:
        for name in rules:
            for rule in rules[name]:
                if v >= rule[0] and v <= rule[1]:
                    break
            else:
                continue
            break
        else:
            break
    else:
        good_tickets.append(ticket)

possible_field_names = []
for ticket in good_tickets + [yours]:
    field_names = dict()
    for pos, v in enumerate(ticket):
        field_names[pos] = set()
        for name in rules:
            for rule in rules[name]:
                if v >= rule[0] and v <= rule[1]:
                    field_names[pos].add(name)
                    break
    possible_field_names.append(field_names)

name_to_pos = dict()
fields_count = len(good_tickets[0])
while(len(name_to_pos) < fields_count):
    for pos in range(fields_count):
        names_for_pos = possible_field_names[0][pos]
        for field_names in possible_field_names:
            names_for_pos = names_for_pos.intersection(field_names[pos]).difference(name_to_pos.keys())
        if (len(names_for_pos) == 1):
            name_to_pos[list(names_for_pos)[0]] = pos
            break
    else:
        raise Exception("oops")

p = 1
for name in name_to_pos:
    if name.startswith('departure'):
        p *= yours[name_to_pos[name]]

print(p)