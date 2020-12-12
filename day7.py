with open('input/day7.txt') as f:
    raw_rules = [s.replace('\n', '') for s in f.readlines()]

rules = dict()
for raw_rule in raw_rules:
    container_color, content = raw_rule.split(' bags contain ', 1)
    content_parts = content.replace('.', '').replace('no other bags', '').split(', ')
    if content_parts == ['']:
        content_parts = []
    rules[container_color] = dict([
        (color.replace(' bags', '').replace(' bag', ''), int(count))
        for content_part in content_parts
        for (count, color) in [content_part.split(' ', 1)]
        ])

contained_bags = {'shiny gold'}

container_bags = []

while True:
    next_level = [color for color in rules 
        if len(set(rules[color].keys()).intersection(contained_bags)) > 0
        ]
    container_bags.extend(next_level)
    contained_bags = next_level
    if len(next_level) == 0:
        break

print(len(set(container_bags)))

root_container = ['shiny gold']
contents = []

while True:
    next_level = []
    for bag in root_container:
        for inbag in rules[bag]:
            next_level.extend([inbag] * rules[bag][inbag])
    contents.extend(next_level)
    root_container = next_level
    if len(next_level) == 0:
        break

print(len(contents))
