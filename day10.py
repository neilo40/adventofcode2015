puzzle_input = "1113222113"


def expand(string):
    parts = []
    seq = string[0]
    for char in string[1:]:
        if char != seq[-1]:
            parts.append(seq)
            seq = ""
        seq += char
    parts.append(seq)
    return "".join(["{}{}".format(len(x), x[0]) for x in parts])


puzzle_output = ""
for i in range(1, 51):
    puzzle_output = expand(puzzle_input)
    puzzle_input = puzzle_output
    print("After iteration {}, output is {}, length is {}".format(i, puzzle_output[:100], len(puzzle_output)))
