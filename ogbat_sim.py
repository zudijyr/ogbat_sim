import sys
import random
from graphics import *
from fighter import Fighter
from amazon import Amazon
from unit import Unit

blue_damage = 0
red_damage = 0
win = GraphWin('Draw units', 700, 500)
hp1 = Text(Point(0,0),"")
hp2 = Text(Point(0,0),"")
hp3 = Text(Point(0,0),"")
hp4 = Text(Point(0,0),"")
hp5 = Text(Point(0,0),"")
hp6 = Text(Point(0,0),"")
hp7 = Text(Point(0,0),"")
hp8 = Text(Point(0,0),"")
message = Text(Point(win.getWidth()/2, 30), 'Ogre Battle Fight Sim')
current_rec = Rectangle(Point(0,0),Point(1,1))
target_rec = Rectangle(Point(0,0),Point(1,1))

def does_it_hit(attacker, defender):
    #TODO movement factor
    movement_factor = 0
    attack_type = attacker.attack_type
    if attack_type == "melee":
        attack_speed = attacker.agility
        defend_speed = defender.agility
    elif attack_type == "magical":
        attack_speed = attacker.intelligence
        defend_speed = defender.intelligence
    attack_luck = attacker.luck
    defend_luck = defender.luck
    HIT_BONUS = 5
    friend_factor = 0 #TODO charm status, special attacks

    #hit formula from Deathlike2's unit mechanics gamefaq
    hit_success = attack_speed + attack_luck/2 + movement_factor + random.randint(0,7)
    evasion_success = defend_speed + defend_luck/2 + movement_factor + friend_factor + random.randint(0,7)
    target_difference = hit_success - evasion_success
    rand_hit_num = random.randint(0,9)
    if (target_difference <= -49 ):
        return (rand_hit_num < 4)
    elif (target_difference >= -48 and target_difference <= -33):
        return (rand_hit_num < 5)
    elif (target_difference >= -32 and target_difference <= -17):
        return (rand_hit_num < 6)
    elif (target_difference >= -16 and target_difference <= -1):
        return (rand_hit_num < 7)
    elif (target_difference >= 0 and target_difference <= 15):
        return (rand_hit_num < 8)
    elif (target_difference >= 16 and target_difference <= 31):
        return (rand_hit_num < 9)
    elif (target_difference > 32):
        return True

def damage(attacker, defender):
    attack_type = attacker.attack_type
    if attack_type == "melee":
        attack_power = attacker.strength
        defend_power = defender.strength
    elif attack_type == "magical":
        attack_power = attacker.intelligence
        defend_power = defender.intelligence
    attack_luck = attacker.luck
    defend_luck = defender.luck

    #formula from Deathlike2's unit analysis gamefaq
    movement = 0
    time = 0
    tactics = 0
    kiss = 0
    #TODO movement,time,tactics,kiss
    raw_damage = attack_power/2 + movement*2 - time/5 + tactics + kiss + random.randint(1,8)
    attack_multiplier = 1 #TODO special attacks like ianuki
    raw_damage = raw_damage*attack_multiplier
    resistance = defender.elements['physical'] #TODO choose resistance element
    absorption = ((defend_power/2 + movement*2 - time/5 + kiss + random.randint(3,10)) * resistance/100) + tactics
    damage = max(raw_damage - absorption,1) #TODO quake
    return int(damage)

def choose_target(attacker, defending_unit):
    #TODO include tactic
    lowest = 9999
    possible_targets = []
    if attacker.attack_type == 'magic': #todo ianuki
        possible_targets = defending_unit.characters
    else:
        for char in defending_unit.characters:
            if char.is_alive and char.row == 'front':
                possible_targets.append(char) #can target anything alive in front row
        if len(possible_targets) == 0:
            possible_targets = defending_unit.characters #if no front row alive, target anything left
        elif len(possible_targets) == 1:
            alive_char = possible_targets[0]
            for char in defending_unit.characters:
                target_diff = abs(char.position - attacker.position)
                front_row_diff = abs(alive_char.position - attacker.position)
                if char.is_alive and target_diff < 1 and front_row_diff > 1:
                    possible_targets.append(char)
                #this lets melee targets back row if the only alive front row char is on the opposite side

    for character in possible_targets:
        if character.is_alive == False:
            pass
        elif character.hp < lowest:
            lowest = character.hp
            target = character
    return target

def attack(attacker, defender):
    global blue_damage,red_damage,current_rec,target_rec
    current_rec.undraw()
    target_rec.undraw()

    up_left = Point(attacker.location.getX()-20,attacker.location.getY()-20)
    corner = Point(attacker.location.getX()+20,attacker.location.getY()+20)
    current_rec = Rectangle(up_left,corner)
    current_rec.setOutline("white")
    current_rec.setWidth(5)
    current_rec.draw(win)

    target_up_left = Point(defender.location.getX()-20,defender.location.getY()-20)
    target_corner = Point(defender.location.getX()+20,defender.location.getY()+20)
    target_rec = Rectangle(target_up_left,target_corner)
    target_rec.setOutline("black")
    target_rec.setWidth(5)
    target_rec.draw(win)
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
    else:
        output = "{0} misses {1}".format(attacker.name,defender.name)
        print(output)
        message.setText(output)

def draw_hp_text(unit1,unit2):
    global hp1,hp2,hp3,hp4,hp5,hp6,hp7,hp8
    hp1 = Text(Point(unit1.characters[0].location.getX(), unit1.characters[0].location.getY()+30),unit1.characters[0].hp)
    hp2 = Text(Point(unit1.characters[1].location.getX(), unit1.characters[1].location.getY()+30),unit1.characters[1].hp)
    hp3 = Text(Point(unit1.characters[2].location.getX(), unit1.characters[2].location.getY()+30),unit1.characters[2].hp)
    hp4 = Text(Point(unit1.characters[3].location.getX(), unit1.characters[3].location.getY()+30),unit1.characters[3].hp)
    hp5 = Text(Point(unit2.characters[0].location.getX(), unit2.characters[0].location.getY()+30),unit2.characters[0].hp)
    hp6 = Text(Point(unit2.characters[1].location.getX(), unit2.characters[1].location.getY()+30),unit2.characters[1].hp)
    hp7 = Text(Point(unit2.characters[2].location.getX(), unit2.characters[2].location.getY()+30),unit2.characters[2].hp)
    hp8 = Text(Point(unit2.characters[3].location.getX(), unit2.characters[3].location.getY()+30),unit2.characters[3].hp)
    hp1.setTextColor('blue')
    hp1.setSize(20)
    hp1.draw(win)
    hp2.setTextColor('blue')
    hp2.setSize(20)
    hp2.draw(win)
    hp3.setTextColor('blue')
    hp3.setSize(20)
    hp3.draw(win)
    hp4.setTextColor('blue')
    hp4.setSize(20)
    hp4.draw(win)

    hp5.setTextColor('red')
    hp5.setSize(20)
    hp5.draw(win)
    hp6.setTextColor('red')
    hp6.setSize(20)
    hp6.draw(win)
    hp7.setTextColor('red')
    hp7.setSize(20)
    hp7.draw(win)
    hp8.setTextColor('red')
    hp8.setSize(20)
    hp8.draw(win)

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

def turn_order(unit1,unit2):
    all_chars = unit1.characters + unit2.characters
    movement_factor = 0 #TODO
    for char in all_chars:
        char.order_value = char.agility + char.luck/2 + movement_factor + random.randint(3,10)
    all_chars.sort(key=lambda x: x.order_value, reverse=True)
    return all_chars

def battle():
    char1_1 = Fighter("fighter 1_1","blue",Point(600,370),"front",0)
    char1_2 = Fighter("fighter 1_2","blue",Point(650,350),"front",1.5)
    char1_3 = Amazon("amazon 1_3","blue",Point(590,450),"back",0)
    char1_4 = Amazon("amazon 1_4","blue",Point(640,420),"back",1.5)
    char2_1 = Fighter("fighter 2_1","red",Point(200,200),"front",0)
    char2_2 = Fighter("fighter 2_2","red",Point(250,180),"front",1)
    char2_3 = Amazon("amazon 2_3","red",Point(210,140),"back",0)
    char2_4 = Amazon("amazon 2_4","red",Point(260,120),"back",1.5)
    #some bug... 2_4 should attack 1_4

    unit1 = Unit("blue",[char1_1,char1_2,char1_3,char1_4])
    unit2 = Unit("red",[char2_1,char2_2,char2_3,char2_4])
    draw_stuff(unit1,unit2)
    draw_hp_text(unit1,unit2)
    for round_num in range(4):
        all_chars = turn_order(unit1,unit2)
        combat_round(all_chars,unit1,unit2)
    win.getMouse()
    current_rec.undraw()
    target_rec.undraw()
    print("blue damage: {0}".format(blue_damage))
    print("red damage: {0}".format(red_damage))
    if blue_damage > red_damage:
        print("blue side wins!")
        message.setText("blue side wins!")
    elif blue_damage < red_damage:
        print("red side wins!")
        message.setText("red side wins!")
    else:
        print("draw")
        message.setText("draw!")
    win.getMouse()

def draw_stuff(unit1,unit2):
    win.setBackground('gray')

    p2 = Point(win.width/2,win.height/2)
    background = Image(p2,'tiles.gif')
    background.draw(win)

    message.setTextColor('gray')
    message.setStyle('italic')
    message.setSize(30)
    message.draw(win)

    image1 = Image(unit1.characters[0].location,'blue_fighter_big.gif')
    image1.draw(win)
    image2 = Image(unit1.characters[1].location,'blue_fighter_big.gif')
    image2.draw(win)
    image3 = Image(unit1.characters[2].location,'blue_amazon_big.gif')
    image3.draw(win)
    image4 = Image(unit1.characters[3].location,'blue_amazon_big.gif')
    image4.draw(win)

    image5 = Image(unit2.characters[0].location,'red_fighter_big.gif')
    image6 = Image(unit2.characters[1].location,'red_fighter_big.gif')
    image7 = Image(unit2.characters[2].location,'red_amazon_big.gif')
    image7.draw(win)
    image8 = Image(unit2.characters[3].location,'red_amazon_big.gif')
    image8.draw(win)
    image5.draw(win)
    image6.draw(win)

    message.setText('Click anywhere to begin')
    win.getMouse()

def main(argv):
    battle()

if __name__ == "__main__":
    main(sys.argv)
