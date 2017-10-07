import sys
import random
from ogbat_sim.unit import Unit
from ogbat_sim.fighter import Fighter
from ogbat_sim.amazon import Amazon

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
    return max(rand + power_diff + luck_diff/2,1)

def attack(attacker, defender):
    hit = does_it_hit(attacker, defender, "physical")
    if (hit):
        defender.hp -= (damage(attacker,defender, "physical"))

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
