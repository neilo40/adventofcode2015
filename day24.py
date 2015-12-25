from itertools import combinations

with open("inputs/day24.txt", 'r') as fh:
    package_sizes = [int(x.rstrip()) for x in fh.readlines()]

# group_size = sum(package_sizes) / 3
group_size = 20


def get_groups(existing_groups, available_package_sizes):
    if len(existing_groups) == 3:
        return existing_groups
    else:
        groups = reduce(list.__add__,
                    [list(combinations(available_package_sizes, l)) for l in range(1, len(available_package_sizes))])
        groups = [g for g in groups if sum(g) == group_size]
        group_combinations = []
        for group in groups:
            group_combinations.append(get_groups(existing_groups + list(group),
                                                 set(available_package_sizes) - set(group)))

        return group_combinations


print(get_groups([], range(1, 6) + range(7, 12)))
