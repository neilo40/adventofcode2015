from itertools import combinations, chain


sizes = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
c = [combinations(sizes, x) for x in range(1, len(sizes))]
print(len([y for y in chain(*c) if sum(y) == 150]))


