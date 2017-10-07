import sys
import random

class Unit:
    hp = 1
    attack = 1
    defense = 1
    agility = 1

class Fighter(Unit):
    hp = 10
    attack = 5
    defense = 2
    agility = 10

class Amazon(Unit):
    hp = 20
    attack = 4
    defense = 1
    agility = 10

def does_it_hit(attack_speed, defend_speed):
    diff = attack_speed - defend_speed
    rand = random.randint(1,10)
    if (rand <= diff + 5):
        return True
    else:
        return False

def attack(attacker, defender):
    hit = does_it_hit(attacker.agility, defender.agility)
    if (hit):
        defender.hp -= (attacker.attack - defender.defense)

def battle():
    unit1 = Fighter()
    unit2 = Amazon()
    for x in range(3):
        attack(unit1, unit2)
        attack(unit2, unit1)
    print(unit1.hp)
    print(unit2.hp)

def main(argv):
    battle()

if __name__ == "__main__":
    main(sys.argv)
