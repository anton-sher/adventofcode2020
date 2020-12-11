with open('input/day4.txt') as f:
    lines = f.read().splitlines()

passports = []
curr = dict()
for line in lines:
    if len(line) == 0:
        if len(curr) > 0:
            passports.append(curr)
            curr = dict()
    else:
        curr.update(dict([l.split(':', 2) for l in line.split(' ')]))
if (len(curr) > 0):
    passports.append(curr)

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
]

passports_with_all_required_fields = [
    passport for passport in passports
    if len(set(required_fields) - {'cid'} - set(passport.keys())) == 0
    ]
print(len(passports_with_all_required_fields))

import re
rules = {
    'byr': lambda s: re.match(r'^\d{4}$', s) and int(s) >= 1920 and int(s) <= 2002,
    'iyr': lambda s: re.match(r'^\d{4}$', s) and int(s) >= 2010 and int(s) <= 2020,
    'eyr': lambda s: re.match(r'^\d{4}$', s) and int(s) >= 2020 and int(s) <= 2030,
    'hgt': lambda s: (re.match(r'^\d{3}cm$', s) and int(s[0:3]) >= 150 and int(s[0:3]) <= 193) or (re.match(r'^\d{2}in$', s) and int(s[0:2]) >= 59 and int(s[0:2]) <= 76),
    'hcl': lambda s: re.match(r'^#[0-9a-f]{6}$', s),
    'ecl': lambda s: s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda s: re.match(r'^\d{9}$', s),
}

valid_passports = [
    p for p in passports_with_all_required_fields 
    if len([f for f in rules if not rules[f](p[f])]) == 0
]

print(len(valid_passports))
