from Hero import Hero


class Enemy(Hero):
    def __init__(self, name, hp, mana, min_dmg, max_dmg, weapon, ability):
        super().__init__(name, hp, mana, min_dmg, max_dmg, weapon)
        self.ability = ability

