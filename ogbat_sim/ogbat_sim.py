import sys
import random
from fighter import Fighter
from amazon import Amazon
from unit import Unit

def does_it_hit(attacker, defender, attack_type):
    if attack_type == "physical":
        attack_speed = attacker.agility
        defend_speed = defender.agility
    elif attack_type == "magical":
        attack_speed = attacker.intelligence
        defend_speed = defender.intelligence
    attack_luck = attacker.luck
    defend_luck = defender.luck
    speed_diff = attack_speed - defend_speed
    luck_diff = attack_luck - defend_luck
    HIT_BONUS = 5
    rand = random.randint(1,10)
    if (rand <= speed_diff + luck_diff/2 + HIT_BONUS):
        return True
    else:
        return False

def damage(attacker, defender, attack_type):
    if attack_type == "physical":
        attack_power = attacker.strength
        defend_power = defender.strength
    elif attack_type == "magical":
        attack_power = attacker.intelligence
        defend_power = defender.intelligence
    attack_luck = attacker.luck
    defend_luck = defender.luck
    power_diff = attack_power - defend_power
    luck_diff = attack_luck - defend_luck
    rand = random.randint(1,10)
    return max(int(rand + power_diff + luck_diff/2),1)

def attack(attacker, defender):
    hit = does_it_hit(attacker, defender, "physical")
    if (hit):
        defender.hp -= (damage(attacker,defender, "physical"))
        if defender.hp <= 0:
            defender.hp = 0
            defender.is_alive = False

def battle():
    char1_1 = Fighter()
    char1_2 = Amazon()
    char2_1 = Fighter()
    char2_2 = Amazon()
    unit1 = Unit([char1_1,char1_2])
    unit2 = Unit([char2_1,char2_2])
    for x in unit1.characters:
        attack(x, char2_1)
    for x in unit2.characters:
        attack(x, char1_1)
    print(char1_1.hp)
    print(char2_1.hp)

def main(argv):
    battle()

if __name__ == "__main__":
    main(sys.argv)
