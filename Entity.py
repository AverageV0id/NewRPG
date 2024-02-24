import random


class Entity:

    def __init__(self, name, health, mana, min_dmg, max_dmg):
        self.name = name
        self.hp = health
        self.mana = mana
        self.dmg = random.randint(min_dmg, max_dmg)
        # self.defense = defense
        self.dead = False

    def physic_attack(self, objective):
        current_dmg = self.dmg
        objective.hp = current_dmg
        print(f'{self.name} атаковал {objective.name} \n'
              f'{objective.name} потерял {current_dmg} здоровья \n'
              f'У {objective.name} осталось {self.hp-objective.hp} \n')

    def сheck_for_death(self):
        if self.hp <= 0:
            print(f'{self.name} умер \n')
            self.dead = True

    def use(self, item):
        self.hp += item.hp
        print(f"{self.name}, использовал {item.name}")
