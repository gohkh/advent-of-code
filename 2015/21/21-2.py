from itertools import product

class Character():
    def __init__(self, HP, damage, armor):
        self.HP = HP
        self.damage = damage
        self.armor = armor

    def attack(self, opponent):
        damage = self.damage - opponent.armor
        if damage < 1:
            damage = 1
        opponent.HP -= damage

weapons = {"Dagger": {"cost": 8, "damage": 4, "armor": 0},
            "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
            "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
            "Longsword": {"cost": 40, "damage": 7, "armor": 0},
            "Greataxe": {"cost": 74, "damage": 8, "armor": 0}
            }

armor = {"Leather": {"cost": 13, "damage": 0, "armor": 1},
        "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "Platemail": {"cost": 102, "damage": 0, "armor": 5}
        }

rings = {"Damage +1": {"cost": 25, "damage": 1, "armor": 0},
        "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
        "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
        "Defence +1": {"cost": 20, "damage": 0, "armor": 1},
        "Defence +2": {"cost": 40, "damage": 0, "armor": 2},
        "Defence +3": {"cost": 80, "damage": 0, "armor": 3}
        }

weapon_combs = list(weapons.keys())
armor_combs = [None] + list(armor.keys())
ring_combs = [[None, None]]
for ring1 in rings:
    ring_combs.append([ring1, None])
    for ring2 in rings:
        if ring2 > ring1:
            ring_combs.append([ring1, ring2])

def cost_(comb):
    weapon_, armor_, rings_ = comb
    cost = weapons[weapon_]["cost"]
    if armor_:
        cost += armor[armor_]["cost"]
    for ring in rings_:
        if ring:
            cost += rings[ring]["cost"]
    return cost

equipment_combs = list(product(weapon_combs, armor_combs, ring_combs))
equipment_combs.sort(key=cost_, reverse=True)

def equip(player, comb):
    weapon_, armor_, rings_ = comb
    player.damage = weapons[weapon_]["damage"]
    player.armor = 0
    if armor_:
        player.armor += armor[armor_]["armor"]
    for ring in rings_:
        if ring:
            player.damage += rings[ring]["damage"]
            player.armor += rings[ring]["armor"]

def match(player, boss):
    while True:
        player.attack(boss)
        if boss.HP <= 0:
            return 1
        boss.attack(player)
        if player.HP <= 0:
            return 0

result = 1
while result:
    player = Character(100, 0, 0)
    comb = equipment_combs.pop(0)
    equip(player, comb)
    boss = Character(103, 9, 2) # puzzle input
    result = match(player, boss)

print(cost_(comb))
