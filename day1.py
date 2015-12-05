with open("inputs/day1.txt", 'r') as fh:
    instructions = fh.read()


floor = 0
position = 0
for instruction in instructions:
    position += 1
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1
    if floor == -1:
      print("In basement at position {}".format(position))


print("ended up on floor {}".format(floor))
