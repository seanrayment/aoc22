grid = []
viewing_scores = []

file = open('input.txt')
for row in file:
    trees = row.strip()
    row_heights = [int(h) for h in trees]
    visible_row = [0 for _ in trees]
    grid.append(row_heights)
    viewing_scores.append(visible_row)


def on_perimeter(row, col):
    if (
        row == 0 or
        col == 0 or
        row == len(grid) - 1 or
        col == len(grid[row]) - 1
    ):
        return True
    else:
        return False


for y in range(len(grid)):  # which row are we in
    for x in range(len(grid[0])):  # which col are we in
        # find the viewing score of this tree
        score = 0
        if (on_perimeter(y, x)):
            viewing_scores[y][x] = 0
            continue
        score = 1

        # along the row
        dir_view = 0
        for i in range(x+1, len(grid[0])):
            if (grid[y][i] < grid[y][x]):
                dir_view += 1
            else:
                dir_view += 1
                break
        score *= dir_view
        # backwards along the row
        dir_view = 0
        for i in range(x-1, -1, -1):
            if (grid[y][i] < grid[y][x]):
                dir_view += 1
            else:
                dir_view += 1
                break
        score *= dir_view
        # down the column
        dir_view = 0
        for j in range(y+1, len(grid)):
            if (grid[j][x] < grid[y][x]):
                dir_view += 1
            else:
                dir_view += 1
                break
        score *= dir_view
        # up the column
        dir_view = 0
        for j in range(y-1, -1, -1):
            if (grid[j][x] < grid[y][x]):
                dir_view += 1
            else:
                dir_view += 1
                break
        score *= dir_view

        viewing_scores[y][x] = score

print(max([max(scores) for scores in viewing_scores]))
