from itertools import permutations


with open("inputs/day13.txt", 'r') as fh:
    lines = fh.readlines()


happiness = {"Neil": {}}
for line in lines:
    parts = line.split()
    person = parts[0]
    neighbour = parts[-1].rstrip('.')
    amount = -int(parts[3]) if parts[2] == "lose" else int(parts[3])
    if parts[0] not in happiness:
        happiness[parts[0]] = {}
    happiness[person].update({neighbour: amount, "Neil": 0})
    happiness["Neil"].update({person: 0})


max_happiness = 0
for seq in permutations(happiness.keys()):
    #print(seq)
    happiness_total = 0
    for i in range(-1, len(seq) - 1):
        this_happiness = happiness[seq[i]][seq[i + 1]]
        neighbour_happiness = happiness[seq[i + 1]][seq[i]]
        #print("{} {} {} {}".format(seq[i], this_happiness, neighbour_happiness, seq[i + 1]))
        happiness_total += (this_happiness + neighbour_happiness)
    max_happiness = happiness_total if happiness_total > max_happiness else max_happiness


print max_happiness

