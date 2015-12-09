from itertools import permutations
from collections import deque


with open("inputs/day9.txt", 'r') as fh:
    lines = fh.readlines()


distances = {}
for line in lines:
    source, _, dest, _, dist = line.split()
    if source not in distances:
        distances[source] = {}
    distances[source][dest] = int(dist)
    if dest not in distances:
        distances[dest] = {}
    distances[dest][source] = int(dist)


route_distances = []
for permutation in permutations(distances.keys(), len(distances.keys())):
    distance = 0
    source_idx = 0
    dest_idx = 1
    for i in range(7):
        distance += distances[permutation[source_idx + i]][permutation[dest_idx + i]]
    route_distances.append(distance)


print("Shortest route: {}".format(min(route_distances)))
print("Longest route: {}".format(max(route_distances)))

