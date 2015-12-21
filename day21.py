from itertools import combinations
import sys

stats = {"boss": {"hit_points": 104, "damage": 8, "armor": 1}}
stats["player"] = {"hit_points": 100, "damage": 0, "armor": 0, "player": True}
items = {"weapons": {"dagger": {"cost": 8, "damage": 4, "armor": 0},
                     "shortsword": {"cost": 10, "damage": 5, "armor": 0},
                     "warhammer": {"cost": 25, "damage": 6, "armor": 0},
                     "longsword": {"cost": 40, "damage": 7, "armor": 0},
                     "greataxe": {"cost": 74, "damage": 8, "armor": 0}},
         "armor": {"birthday_suit": {"cost": 0, "damage": 0, "armor": 0},
                   "leather": {"cost": 13, "damage": 0, "armor": 1},
                   "chainmail": {"cost": 31, "damage": 0, "armor": 2},
                   "splintmail": {"cost": 53, "damage": 0, "armor": 3},
                   "bandedmail": {"cost": 75, "damage": 0, "armor": 4},
                   "platemail": {"cost": 102, "damage": 0, "armor": 5}},
         "rings": {"no_ring": {"cost": 0, "damage": 0, "armor": 0},
                   "dmg1": {"cost": 25, "damage": 1, "armor": 0},
                   "dmg2": {"cost": 50, "damage": 2, "armor": 0},
                   "dmg3": {"cost": 100, "damage": 3, "armor": 0},
                   "def1": {"cost": 20, "damage": 0, "armor": 1},
                   "def2": {"cost": 40, "damage": 0, "armor": 2},
                   "def3": {"cost": 80, "damage": 0, "armor": 3}}}
ring_combinations = [("no_ring", "no_ring"), ] + list(combinations(items["rings"], 2))


def fight(player):
    attacker = player
    defender = dict(stats["boss"])
    while attacker["hit_points"] > 0 and defender["hit_points"] > 0:
        dmg = attacker["damage"] - defender["armor"]
        dmg = dmg if dmg > 0 else 1
        defender["hit_points"] -= dmg
        last_attacker = attacker
        attacker = defender
        defender = last_attacker
    return last_attacker 


def equip_items(item_stats):
    new_player_stats = dict(stats["player"])
    for stat in item_stats:
        new_player_stats["damage"] += stat["damage"]
        new_player_stats["armor"] += stat["armor"]
    return new_player_stats


def try_items():
    min_cost = 100000
    max_cost = 0
    for weapon in items["weapons"]:
        weapon_stats = items["weapons"][weapon]
        for armor in items["armor"]:
            armor_stats = items["armor"][armor]
            for rings in ring_combinations:
                item_stats = [items["rings"][ring] for ring in rings]
                item_stats.append(weapon_stats)
                item_stats.append(armor_stats)
                player_stats = equip_items(item_stats)
                print("Simulating fight with player stats: {}".format(player_stats))
                winner = fight(player_stats)
                cost = sum([x["cost"] for x in item_stats])
                if "player" in winner:
                    print("Player won!  Cost: {}".format(cost))
                    min_cost = cost if cost < min_cost else min_cost
                else:
                    print("Player lost!  Cost: {}".format(cost))
                    max_cost = cost if cost > max_cost else max_cost
    return min_cost, max_cost


if __name__ == "__main__":
    costs = try_items()
    print("Min cost: {}, Max cost: {}".format(*costs))
