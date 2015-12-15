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
        schedule += [speed, ] * duration
        schedule += [0, ] * rest
    schedules[name] = schedule


for reindeer in schedules:
    print("{} flew {} in 2503 seconds".format(reindeer, sum(schedules[reindeer][:2503])))


scores = {}
for reindeer in schedules:
    scores.update({reindeer: {"dist": 0, "score": 0}})


for sec in range(2503):
    for reindeer in scores:
        scores[reindeer]["dist"] += schedules[reindeer][sec]
    furthest = 0
    winning = []
    for reindeer in scores:
        if scores[reindeer]["dist"] == furthest:
            winning.append(reindeer)
        elif scores[reindeer]["dist"] > furthest:
            furthest = scores[reindeer]["dist"]
            winning = [reindeer, ]
    for reindeer in winning:
        scores[reindeer]["score"] += 1


from pprint import pprint as pp
pp(scores)

