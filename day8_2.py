with open("inputs/day8.txt", 'r') as fh:
    lines = fh.readlines()


total_code = 0
total_memory = 0
for line in lines:
    line = line.strip()    
    total_code += len(line)
    string_total = 0
    for letter in repr(line):
        string_total += 2 if letter in ['"', r'\\'] else 1
    print("{} : {} : {}".format(line, len(line), string_total))
    total_memory += string_total


print(total_memory - total_code)
