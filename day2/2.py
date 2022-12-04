result_mappings = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}

total = 0

input_txt = open('input.txt', 'r')
games = input_txt.readlines()
for game in games:
    moves = game.strip().split()
    opp_move = moves[0]
    my_move = moves[1]

    total += result_mappings[opp_move][my_move]

print(total)
