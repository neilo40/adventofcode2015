with open("inputs/day6.txt", 'r') as fh:
    instructions = fh.readlines()


grid = [[False for x in range(1000)] for y in range(1000)]


for instruction in instructions:
    parts = instruction.split()

    start = [int(x) for x in parts[-3].split(',')]
    end = [int(y) for y in parts[-1].split(',')]

    if parts[0] == "turn":
        modify = lambda x: True if parts[1] == "on" else False
    else:
        modify = lambda x: not x

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            grid[x][y] = modify(grid[x][y])


print(sum([row.count(True) for row in grid]))
