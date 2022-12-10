grid = []
visible_trees = []

file = open('input.txt')
for row in file:
    trees = row.strip()
    row_heights = [int(h) for h in trees]
    visible_row = [0 for _ in trees]
    grid.append(row_heights)
    visible_trees.append(visible_row)


"""
General approach: Do a pass over each row and each column from both directions. If we are on the perimeter
of the 'forest', assign 1 to visibility. Keep track of the tallest tree we've seen so far, and if the
current tree is shorter than that, assign 0 to visiblity.
"""


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


# left to right
for j in range(len(grid)):  # which row are we on
    high = 0
    for i in range(len(grid[0])):  # which column of that row are we on
        if (i == 0):
            high = grid[j][i]
        if (on_perimeter(j, i)):
            visible_trees[j][i] = 1
        elif (grid[j][i] > high):
            high = grid[j][i]
            visible_trees[j][i] = 1

# # right to left
for j in range(len(grid)):  # which row are we on
    high = 0
    for i in range(len(grid[0])-1, -1, -1):  # which column of that row are we on
        if (i == len(grid[0]) - 1):
            high = grid[j][i]
        if (on_perimeter(j, i)):
            visible_trees[j][i] = 1
        elif (grid[j][i] > high):
            high = grid[j][i]
            visible_trees[j][i] = 1

# top down
for i in range(len(grid[0])):  # which column are we on
    high = 0
    for j in range(len(grid)):  # which row are we on
        if (j == 0):
            high = grid[j][i]
        if (on_perimeter(j, i)):
            visible_trees[j][i] = 1
        elif (grid[j][i] > high):
            high = grid[j][i]
            visible_trees[j][i] = 1

# bottom up
for i in range(len(grid[0])):  # which column are we on
    high = 0
    for j in range(len(grid)-1, -1, -1):  # which row are we on
        if (j == len(grid) - 1):
            high = grid[j][i]
        if (on_perimeter(j, i)):
            visible_trees[j][i] = 1
        elif (grid[j][i] > high):
            high = grid[j][i]
            visible_trees[j][i] = 1

print(sum([sum(arr) for arr in visible_trees]))
