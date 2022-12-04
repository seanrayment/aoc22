shared = []
total_priority = 0

rucksacks = open('input.txt', 'r')
for pair in rucksacks:
    contents = pair.strip()
    sack1 = contents[:(len(contents) // 2)]
    sack2 = contents[(len(contents) // 2):]
    items = set()
    for item in sack1:
        items.add(item)
    for item in sack2:
        if item in items:
            shared.append(item)
            break

for item in shared:
    if item.isupper():
        total_priority += ord(item) - 38
    else:
        total_priority += ord(item) - 96

print(total_priority)
