with open("inputs/day6.txt", 'r') as fh:
    instructions = fh.readlines()


grid = [[0 for x in range(1000)] for y in range(1000)]


for instruction in instructions:
    parts = instruction.split()

    start = [int(x) for x in parts[-3].split(',')]
    end = [int(y) for y in parts[-1].split(',')]

    if parts[0] == "turn":
        if parts[1] == "on":
            modify = lambda x: x + 1
        else:
            modify = lambda x: x - 1
    else:
        modify = lambda x: x + 2

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            new_val = modify(grid[x][y])
            grid[x][y] = 0 if new_val < 0 else new_val


print(sum([sum(row) for row in grid]))
