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

    #for x in unit1.characters:
    #    print(x.name)
    #    print(x.hp)
    #for x in unit2.characters:
    #    print(x.name)
    #    print(x.hp)

def battle():
    global blue_damage,red_damage,win,message
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
    global win,message
    win.setBackground('gray')

    p2 = Point(350,250)
    background = Image(p2,'tiles.gif')
    background.draw(win)

    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    image1 = Image(Point(600,400),'blue_fighter.gif')
    image1.draw(win)
    image2 = Image(Point(650,380),'blue_fighter.gif')
    image2.draw(win)
    image3 = Image(Point(600,440),'blue_amazon.gif')
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

    message.setText('Click anywhere to begin') # change text message
    win.getMouse()

def main(argv):
    draw_stuff()
    battle()

if __name__ == "__main__":
    main(sys.argv)
