stacks = [
    [],
    ['Q', 'G', 'P', 'R', 'L', 'C', 'T', 'F'],
    ['J', 'S', 'F', 'R', 'W', 'H', 'Q', 'N'],
    ['Q', 'M', 'P', 'W', 'H', 'B', 'F'],
    ['F', 'D', 'T', 'S', 'V'],
    ['Z', 'F', 'V', 'W', 'D', 'L', 'Q'],
    ['S', 'L', 'C', 'Z'],
    ['F', 'D', 'V', 'M', 'B', 'Z'],
    ['B', 'J', 'T'],
    ['H', 'P', 'S', 'L', 'G', 'B', 'N', 'Q']
]

moves = open('input.txt')
for move_str in moves:
    sentence_parts = move_str.strip().split()
    quantity = int(sentence_parts[1])
    from_stack = int(sentence_parts[3])
    to_stack = int(sentence_parts[5])
    crates = stacks[from_stack][:quantity]
    stacks[from_stack] = stacks[from_stack][quantity:]
    stacks[to_stack] = crates + stacks[to_stack]

for stack in stacks:
    print(stack)
