shared = []
total_priority = 0

rucksacks_file = open('input.txt', 'r')
rucksacks = rucksacks_file.readlines()
for sack_idx in range(0, len(rucksacks) - 2, 3):
    sack1 = rucksacks[sack_idx].strip()
    sack2 = rucksacks[sack_idx + 1].strip()
    sack3 = rucksacks[sack_idx + 2].strip()
    shared_pair_candidates = set()
    shared_group_candidates = set()
    for item in sack1:
        shared_pair_candidates.add(item)
    for item in sack2:
        if item in shared_pair_candidates:
            shared_group_candidates.add(item)
    for item in sack3:
        if item in shared_group_candidates:
            shared.append(item)
            break

for item in shared:
    if item.isupper():
        total_priority += ord(item) - 38
    else:
        total_priority += ord(item) - 96

print(total_priority)
