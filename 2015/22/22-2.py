class Character():
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
        self.armor = 0

    def attack(self, opponent):
        damage = self.damage - opponent.armor
        opponent.HP -= max(1, damage)

    def alive(self):
        return self.HP > 0

class Player(Character):
    def __init__(self, HP, mana):
        super().__init__(HP, 0)
        self.mana = mana
        self.effects = []

    def attack(self, spell_damage, opponent):
        damage = spell_damage - opponent.armor
        opponent.HP -= max(1, damage)

    def cast(self, spell, opponent):

        # cannot cast spell to start an effect which is already active
        if spell.name in [effect.name for effect in self.effects]:
            return False

        self.mana -= spell.cost
        if self.mana < 0: # must have enough mana to cast spells
            return False

        if spell.turns: # start effect
            spell.timer = spell.turns
            self.effects.append(spell)
        else:
            self.attack(spell.damage, opponent)
            self.HP += spell.heal
        return True

    def apply_effects(self, opponent):
        for effect in self.effects.copy():
            if effect.damage:
                self.attack(effect.damage, opponent)
            if effect.timer == effect.turns:
                self.armor += effect.armor
            self.HP += effect.heal
            self.mana += effect.mana
            effect.timer -= 1

            if effect.timer == 0: # end effect
                self.armor -= effect.armor
                self.effects.remove(effect)

class Spell():
    def __init__(self, name, cost, damage, armor, heal, mana, turns):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.heal = heal
        self.mana = mana
        self.turns = turns
        self.timer = turns

magic_missile = Spell("Magic Missile", 53, 4, 0, 0, 0, 0)
drain = Spell("Drain", 73, 2, 0, 2, 0, 0)
shield = Spell("Shield", 113, 0, 7, 0, 0, 6)
poison = Spell("Poison", 173, 3, 0, 0, 0, 6)
recharge = Spell("Recharge", 229, 0, 0, 0, 101, 5)
spells = [magic_missile, drain, shield, poison, recharge]

def total_cost(seq):
    return sum(spell.cost for spell in seq)

def main():
    seqs = [[spell] for spell in spells]
    new_seqs = seqs.copy()
    success_seq = None
    max_cost = 10**1000

    while new_seqs:
        seqs = new_seqs.copy()
        new_seqs = []

        for seq in seqs:
            result = simulate(seq.copy())

            if result == 1: # player wins
                cost = total_cost(seq)
                if cost < max_cost:
                    success_seq = seq.copy()
                    max_cost = cost

            elif result is None: # inconclusive
                for spell in spells:
                    new_seq = seq + [spell]
                    cost = total_cost(new_seq)
                    if cost < max_cost:
                        new_seqs.append(new_seq)
            # ignore cases where boss wins

    if success_seq:
        print(max_cost)

def simulate(seq):
    player = Player(50, 500)
    boss = Character(58, 9) # puzzle input

    while player.alive():

        player.HP -= 1 # lose 1 HP at start of player's turn before effects apply
        if not player.alive():
            return 0

        player.apply_effects(boss) # apply effects at start of player's turn
        if not boss.alive():
            return 1

        # player's turn
        if not seq: # check if there are any more spells to cast
            return None
        casted = player.cast(seq.pop(0), boss) # cast spell and check if valid
        if not casted:
            return 0
        elif not boss.alive():
            return 1

        player.apply_effects(boss) # apply effects at start of boss's turn
        if not boss.alive():
            return 1

        # boss's turn
        boss.attack(player)

    return 0

main()
