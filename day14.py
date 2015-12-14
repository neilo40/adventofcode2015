with open("inputs/day14.txt", 'r') as fh:
    lines = fh.readlines()


schedules = {}
for line in lines:
    parts = line.split()
    name = parts[0]
    speed = int(parts[3])
    duration = int(parts[6])
    rest = int(parts[13])
    schedule = []
    while len(schedule) < 2503:
        schedule += [speed,] * duration
        schedule += [0,] * rest
    schedules[name] = schedule


for reindeer in schedules:
    print("{} flew {} in 2503 seconds".format(reindeer, sum(schedules[reindeer][:2503])))
