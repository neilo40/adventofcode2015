def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 and i * 50 >= n), [n, ]))

puzzle_input = 29000000

house_count = 0
house_num = 0
while house_count < puzzle_input:
    house_num += 1
    f = list(factors(house_num))
    house_count = sum(f) * 11

print(house_num)
