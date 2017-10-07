import sys

class Unit:
    hp = 0
    attack = 0
    defense = 0

class Fighter(Unit):
    hp = 10
    attack = 5
    defense = 2

class Amazon(Unit):
    hp = 20
    attack = 4
    defense = 1

def attack(attacker, defender):
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
