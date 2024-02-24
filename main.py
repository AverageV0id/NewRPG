import time
#  from art import *
from Hero import Hero
from Enemy import Enemy
from Weapon import Weapon

bow = Weapon('Лук', dmg=15)

main_hero = Hero(name='Guide', hp=100, min_dmg=6, max_dmg=30, weapon=bow, mana=0)

slime = Weapon('Слизь', dmg=20)
enemies = []

for i in range(0, 5, 1):
    mob = Enemy(name=f'Слизнь {i}', hp=50, min_dmg=15, max_dmg=40, mana=0, weapon=slime, ability='jump')
    enemies.append(mob)

enemy_count = 0
# tprint
print('Start')

while not main_hero.dead and enemy_count != len(enemies):
    while not enemies[enemy_count].dead:

        if main_hero.dead:
            break

        main_hero.attack_using_weapon(enemies[enemy_count])
        enemies[enemy_count].сheck_for_death()

        if enemies[enemy_count].dead:
            break

        enemies[enemy_count].attack_using_weapon(main_hero)
        main_hero.сheck_for_death()
        time.sleep(3)

    enemy_count += 1

# tprint()
print('Gameover')