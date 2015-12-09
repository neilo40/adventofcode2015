with open("inputs/day8.txt", 'r') as fh:
    lines = fh.readlines()


def parse(string):
    s = string.decode('string_escape')
    num_bytes = len(s) - 2
    return num_bytes


total_code = 0
total_memory = 0
for line in lines:
    line = line.strip()    
    total_code += len(line)
    total_memory += parse(line)


print(total_code - total_memory)
