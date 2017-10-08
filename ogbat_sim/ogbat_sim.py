import sys
import random
from graphics import *
from fighter import Fighter
from amazon import Amazon
from unit import Unit

blue_damage = 0
red_damage = 0
win = GraphWin('Draw units', 700, 500)
message = Text(Point(win.getWidth()/2, 30), 'Ogre Battle Fight Sim')
hp1 = Text(Point(600,390), '0')
hp2 = Text(Point(650,370), '0')
hp3 = Text(Point(590,470), '0')
hp4 = Text(Point(640,440), '0')
hp5 = Text(Point(200,220), '0')
hp6 = Text(Point(250,200), '0')
hp7 = Text(Point(210,170), '0')
hp8 = Text(Point(260,160), '0')

def does_it_hit(attacker, defender):
    #TODO actual to-hit rules
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
    #TODO element types, actual damage rules
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
    #TODO include rows, position
    lowest = 9999
    for character in defending_unit.characters:
        if character.is_alive == False:
            pass
        elif character.hp < lowest:
            lowest = character.hp
            target = character
    return target

def attack(attacker, defender):
    global blue_damage,red_damage
    attacker.num_attacks_remaining -= 1
    hit = does_it_hit(attacker, defender)
    if (hit):
        dam = damage(attacker,defender)
        dam_output = "{0} hits {1} for {2}".format(attacker.name,defender.name,dam)
        print(dam_output)
        message.setText(dam_output)
        defender.hp -= dam
        if attacker.side == "blue":
            blue_damage += dam
        if attacker.side == "red":
            red_damage += dam
        if defender.hp <= 0:
            defender.hp = 0
            defender.is_alive = False

def set_hp_text(unit1,unit2):
    hp1.setText(unit1.characters[0].hp)
    hp2.setText(unit1.characters[1].hp)
    hp3.setText(unit1.characters[2].hp)
    hp4.setText(unit1.characters[3].hp)
    hp5.setText(unit2.characters[0].hp)
    hp6.setText(unit2.characters[1].hp)
    hp7.setText(unit2.characters[2].hp)
    hp8.setText(unit2.characters[3].hp)

def combat_round(all_chars,unit1,unit2):
    for x in all_chars:
        if x.is_alive == False or x.num_attacks_remaining == 0:
            pass
        else:
            win.getMouse()
            if x.side == "blue":
                target = choose_target(x,unit2)
            else:
                target = choose_target(x,unit1)
            attack(x, target)
            set_hp_text(unit1,unit2)

def battle():
    char1_1 = Fighter("fighter 1_1","blue")
    char1_2 = Fighter("fighter 1_2","blue")
    char1_3 = Amazon("amazon 1_3","blue")
    char1_4 = Amazon("amazon 1_4","blue")
    char2_1 = Fighter("fighter 2_1","red")
    char2_2 = Fighter("fighter 2_2","red")
    char2_3 = Amazon("amazon 2_3","red")
    char2_4 = Amazon("amazon 2_4","red")
    unit1 = Unit("blue",[char1_1,char1_2,char1_3,char1_4])
    unit2 = Unit("red",[char2_1,char2_2,char2_3,char2_4])
    set_hp_text(unit1,unit2)
    all_chars = unit1.characters + unit2.characters
    all_chars.sort(key=lambda x: x.agility, reverse=True)
    #TODO include some luck into sorting
    for round_num in range(2):
        combat_round(all_chars,unit1,unit2)
    print("blue damage: {0}".format(blue_damage))
    print("red damage: {0}".format(red_damage))
    if blue_damage > red_damage:
        print("blue side wins!")
    elif blue_damage < red_damage:
        print("red side wins!")
    else:
        print("draw")

def draw_stuff():
    win.setBackground('gray')

    p2 = Point(350,250)
    background = Image(p2,'tiles.gif')
    background.draw(win)

    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    image1 = Image(Point(600,370),'blue_fighter.gif')
    image1.draw(win)
    image2 = Image(Point(650,350),'blue_fighter.gif')
    image2.draw(win)
    image3 = Image(Point(590,450),'blue_amazon.gif')
    image3.draw(win)
    image4 = Image(Point(640,420),'blue_amazon.gif')
    image4.draw(win)

    image5 = Image(Point(200,200),'red_fighter.gif')
    image5.draw(win)
    image6 = Image(Point(250,180),'red_fighter.gif')
    image6.draw(win)
    image7 = Image(Point(210,150),'red_amazon.gif')
    image7.draw(win)
    image8 = Image(Point(260,140),'red_amazon.gif')
    image8.draw(win)

    hp1.setTextColor('red')
    hp1.setSize(15)
    hp1.draw(win)
    hp2.setTextColor('red')
    hp2.setSize(15)
    hp2.draw(win)
    hp3.setTextColor('red')
    hp3.setSize(15)
    hp3.draw(win)
    hp4.setTextColor('red')
    hp4.setSize(15)
    hp4.draw(win)

    hp5.setTextColor('red')
    hp5.setSize(15)
    hp5.draw(win)
    hp6.setTextColor('red')
    hp6.setSize(15)
    hp6.draw(win)
    hp7.setTextColor('red')
    hp7.setSize(15)
    hp7.draw(win)
    hp8.setTextColor('red')
    hp8.setSize(15)
    hp8.draw(win)

    message.setText('Click anywhere to begin')
    win.getMouse()

def main(argv):
    draw_stuff()
    battle()

if __name__ == "__main__":
    main(sys.argv)
