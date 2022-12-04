col_2_mappings = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

result_mappings = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

total = 0

input_txt = open('input.txt', 'r')
games = input_txt.readlines()
for game in games:
    moves = game.strip().split()
    opp_move = moves[0]
    my_move = moves[1]

    total += col_2_mappings[my_move]
    total += result_mappings[opp_move][my_move]

print(total)
