import sys
import random
from fighter import Fighter
from amazon import Amazon
from unit import Unit

def does_it_hit(attacker, defender):
    attack_type = attacker.attack_type
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

def damage(attacker, defender):
    attack_type = attacker.attack_type
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

def choose_target(attacker, defending_unit):
    lowest = 9999
    for character in defending_unit.characters:
        if character.is_alive == False:
            pass
        elif character.hp < lowest:
            lowest = character.hp
            target = character
    return target

def attack(attacker, defender):
    attacker.num_attacks_remaining -= 1
    hit = does_it_hit(attacker, defender)
    if (hit):
        dam = damage(attacker,defender)
        print("{0} hits {1} for {2}".format(attacker.name,defender.name,dam))
        defender.hp -= dam
        if defender.hp <= 0:
            defender.hp = 0
            defender.is_alive = False

def battle():
    char1_1 = Fighter("fighter 1_1")
    char1_2 = Fighter("fighter 1_2")
    char1_3 = Amazon("amazon 1_3")
    char1_4 = Amazon("amazon 1_4")
    char2_1 = Fighter("fighter 2_1")
    char2_2 = Fighter("fighter 2_2")
    char2_3 = Amazon("amazon 2_3")
    char2_4 = Amazon("amazon 2_4")
    unit1 = Unit([char1_1,char1_2,char1_3,char1_4])
    unit2 = Unit([char2_1,char2_2,char2_3,char2_4])
    for round in range(2):
        for x in unit1.characters:
            if x.is_alive == False or x.num_attacks_remaining == 0:
                pass
            else:
                target = choose_target(x,unit2)
                attack(x, target)
        for x in unit2.characters:
            if x.is_alive == False or x.num_attacks_remaining == 0:
                pass
            else:
                target = choose_target(x,unit1)
                attack(x, target)
        for x in unit1.characters:
            print(x.name)
            print(x.hp)
        for x in unit2.characters:
            print(x.name)
            print(x.hp)

def main(argv):
    battle()

if __name__ == "__main__":
    main(sys.argv)
