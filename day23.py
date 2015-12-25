with open("inputs/day23.txt", 'r') as fh:
    lines = fh.readlines()

instructions = []
for line in lines:
    parts = line.rstrip().split()
    opcode = parts[0]
    if opcode in ["jmp", "jio", "jie"]:
        offset = int(parts[-1])
        if opcode == "jmp":
            reg = None
        else:
            reg = parts[1].rstrip(',')
    else:
        reg = parts[-1]
        offset = None
    instructions.append((opcode, reg, offset))

registers = {"pc": 0, 'a': 1, 'b': 0}
try:
    while True:
        pc_inc = 1
        opcode, reg, offset = instructions[registers["pc"]]
        if opcode == "jmp":
            pc_inc = offset
        elif opcode == "jio":
            if registers[reg] == 1:
                pc_inc = offset
        elif opcode == "jie":
            if registers[reg] % 2 == 0:
                pc_inc = offset
        elif opcode == "hlf":
            registers[reg] /= 2
        elif opcode == "tpl":
            registers[reg] *= 3
        elif opcode == "inc":
            registers[reg] += 1
        registers["pc"] += pc_inc
except IndexError:
    print(registers['b'])

