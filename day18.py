import re

with open("inputs/day18.txt", 'r') as fh:
    lines = fh.readlines()

# The grid should be 100 x 100 with a border of "off" cells
grid1 = [['.' for x in range(102)]]
grid1 += [['.', ] + [x for x in line.rstrip()] + ['.', ] for line in lines]
grid1 += [['.' for x in range(102)]]

grid2 = [['.' for x in range(102)] for y in range(102)]


def get_neighbours(row, cell):
    return [(row - 1, cell - 1), (row - 1, cell), (row - 1, cell + 1),
            (row, cell - 1), (row, cell + 1),
            (row + 1, cell - 1), (row + 1, cell), (row + 1, cell + 1)]


def new_cell_state(grid, row, cell):
    on_neighbours = sum([1 for z in get_neighbours(row, cell) if grid[z[0]][z[1]] == '#'])
    if grid[row][cell] == '.':
        return '#' if on_neighbours == 3 else '.'
    else:
        return '#' if on_neighbours in [2, 3] else '.'


def do_cycle():
    # don't evaluate the borders
    for row in range(1, 101):
        for cell in range(1, 101):
            if (row, cell) in [(1, 1), (1, 100), (100, 1), (100, 100)]:
                grid2[row][cell] = '#'
            else:
                grid2[row][cell] = new_cell_state(grid1, row, cell)


def print_grid(grid):
    for r in grid:
        print(re.sub('\.', ' ', ''.join(r)))
    print("---")


for step in range(1000):
    do_cycle()
    print_grid(grid2)
    grid3 = grid2
    grid2 = grid1
    grid1 = grid3

print(sum([row.count('#') for row in grid1]))
