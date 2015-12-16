import re


with open("inputs/day16.txt", 'r') as fh:
    lines = fh.readlines()


sues = {}
for line in lines:
    parts = line.rstrip().split(',')
    sue_num = parts[0].split()[1].rstrip(':')
    parts[0] = re.sub("Sue \d*: ", "", parts[0]) 
    traits = {x.split(':')[0].lstrip(): int(x.split(':')[1]) for x in parts}
    sues.update({int(sue_num): traits})


evidence = {"children": lambda x: x == 3, "cats": lambda x: x > 7, "samoyeds": lambda x: x == 2, 
    "pomeranians": lambda x: x < 3, "akitas": lambda x: x == 0, "vizslas": lambda x: x == 0, 
    "goldfish": lambda x: x < 5, "trees": lambda x: x > 3, "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1}


for sue in sues:
    candidate = True
    for trait in sues[sue]:
        if not evidence[trait](sues[sue][trait]):
            #print("Sue {} is eliminated, {} != {}".format(sue, sues[sue][trait], evidence[trait]))
            candidate = False
            break
    if candidate:
        print("Sue {} is a candidate".format(sue))
