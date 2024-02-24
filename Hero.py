from Entity import Entity
import random


class Hero(Entity):
    def __init__(self, name, hp, mana, min_dmg, max_dmg, weapon):
        super().__init__(name, hp, mana, min_dmg, max_dmg)
        self.weapon = weapon
        self.dmg = random.randint(min_dmg, max_dmg)

    def attack_using_weapon(self, objective):
        if self.weapon is not None:
            current_dmg = self.dmg + self.weapon.dmg
            objective.hp = current_dmg
            print(f'{self.name} атаковал {objective.name} \n'
                  f'{objective.name} потерял {current_dmg} здоровья \n'
                  f'Осталось у {objective.name} осталось {objective.hp} \n')
        else:
            self.physic_attack(objective)
