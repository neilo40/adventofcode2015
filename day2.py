from itertools import combinations


with open("inputs/day2.txt", 'r') as fh:
    dimensions = fh.readlines()


total_area = 0
total_ribbon = 0
for dimension in dimensions:
    edge_lengths = sorted([int(x) for x in dimension.split('x')])
    face_edges = combinations(edge_lengths, 2)
    print(edge_lengths)
 
    face_areas = [edges[0] * edges[1] for edges in face_edges]
    min_area = min(face_areas)
    area = sum([area * 2 for area in face_areas]) + min_area

    ribbon = sum([edge * 2 for edge in edge_lengths[0:2]])
    volume = reduce(lambda x, y: x*y, edge_lengths)
    ribbon += volume

    total_ribbon += ribbon
    total_area += area


print("Area of paper needed: {}".format(total_area))
print("Length of ribbon needed: {}".format(total_ribbon))
