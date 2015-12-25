boss_stats = {"hit_points": 71, "damage": 10, "armor": 0}
player_stats = {"hit_points": 50, "mana": 500, "armor": 0}
spells = {"missile": {"cost": 53, "damage": 4},
          "drain": {"cost": 73, "damage": 2, "heal": 2},
          "shield": {"cost": 113, "armor": [7, ] * 6},
          "poison": {"cost": 173, "damage": [3, ] * 6},
          "recharge": {"cost": 229, "mana": [101, ] * 5}}
queues = {"mana": [], "heal": [], "damage": [], "armor": []}


def boss_move():
    dmg = boss_stats["damage"] - player_stats["armor"]
    dmg = dmg if dmg > 0 else 1
    player_stats["hit_points"] -= dmg


def player_move():
    pass


