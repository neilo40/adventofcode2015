from itertools import combinations_with_replacement as comb


with open("inputs/day15.txt", 'r') as fh:
    lines = fh.readlines()


ingredients = {}
for line in lines:
    parts = line.split()
    parts = [x.rstrip(',') for x in parts]
    ingredients[parts[0].rstrip(':')] = {"capacity": int(parts[2]),
                                         "durability": int(parts[4]),
                                         "flavor": int(parts[6]),
                                         "texture": int(parts[8]),
                                         "calories": int(parts[10])}


best_score = 0
recipes = comb(ingredients.keys(), 100)
for recipe in recipes:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingredient in recipe:
        capacity += ingredients[ingredient]["capacity"]
        durability += ingredients[ingredient]["durability"]
        flavor += ingredients[ingredient]["flavor"]
        texture += ingredients[ingredient]["texture"]
        calories += ingredients[ingredient]["calories"]
    if calories != 500 or capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        continue
    score = capacity * durability * flavor * texture
    best_score = score if score > best_score else best_score


print best_score