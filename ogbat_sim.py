import sys
import random
from graphics import *
from classes.fighter import Fighter
from classes.amazon import Amazon
from classes.wizard import Wizard
from classes.unit import Unit

blue_damage = 0
red_damage = 0
win = GraphWin('Ogre Battle Fight Sim', 700, 500)
message = Text(Point(win.getWidth()/2, 30), '')
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

def choose_element(attacker, defender):
    low_score = 101
    lowest = 'element'
    for element in attacker.attacking_elements:
        if defender.resistances[element] < low_score:
            lowest = element
            low_score = defender.resistances[element]
    return lowest

def calc_tac_bonuses(attacker_tactic, defender_tactic):
    att_tac_bonus = 0
    def_tac_bonus = 0
    if (attacker_tactic == 'weak'):
        att_tac_bonus += 4
    if (attacker_tactic == 'strong'):
        att_tac_bonus -= 4
    if (defender_tactic == 'weak'):
        def_tac_bonus -= 4
    if (defender_tactic == 'strong'):
        def_tac_bonus += 4
    return att_tac_bonus,def_tac_bonus

def damage(attacker, defender, attack_element, attacker_tactic, defender_tactic):
    attack_type = attacker.attack_type
    if attack_type == "melee":
        attack_power = attacker.strength
        defend_power = defender.strength
    elif attack_type == "magical":
        attack_power = attacker.intelligence
        defend_power = defender.intelligence

    att_tac_bonus,def_tac_bonus = calc_tac_bonuses(attacker_tactic, defender_tactic)
    movement = 0
    time = 0
    kiss = 0
    #TODO movement,time,kiss
    #damage formula from Deathlike2's unit analysis gamefaq
    raw_damage = attack_power/2 + movement*2 - time/5 + att_tac_bonus + kiss + random.randint(1,8)
    attack_multiplier = 1 #TODO special attacks like ianuki
    raw_damage = raw_damage*attack_multiplier
    resistance = defender.resistances[attack_element]
    absorption = ((defend_power/2 + movement*2 - time/5 + kiss + random.randint(3,10)) * resistance/100) + def_tac_bonus
    damage = max(raw_damage - absorption,1) #TODO quake
    damage = min(damage,defender.hp)
    return int(damage)

def choose_target(attacker, defending_unit):
    #TODO include tactic
    lowest = 9999
    possible_targets = []
    if attacker.attack_type == 'magical': #TODO ianuki
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

def draw_attack_recs(attacker,defender):
    global current_rec,target_rec
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

def attack(attacker, defender):
    global blue_damage,red_damage
    draw_attack_recs(attacker,defender)
    attacker.num_attacks_remaining -= 1
    hit = does_it_hit(attacker, defender)
    if (hit):
        attack_element = choose_element(attacker, defender)
        dam = damage(attacker,defender,attack_element,'weak','weak')
        dam_output = "{0} hits {1} with {2} for {3}".format(attacker.name,defender.name,attack_element,dam)
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
    for char in unit1.characters:
        char.hptext.draw(win)
    for char in unit2.characters:
        char.hptext.draw(win)

def set_hp_text(all_chars):
    for char in all_chars:
        char.hptext.setText(char.hp)

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
            set_hp_text(all_chars)

def turn_order(unit1,unit2):
    all_chars = unit1.characters + unit2.characters
    movement_factor = 0 #TODO
    for char in all_chars:
        char.order_value = char.agility + char.luck/2 + movement_factor + random.randint(3,10)
    all_chars.sort(key=lambda x: x.order_value, reverse=True)
    return all_chars

def battle():
    top_left = Point(int(win.width/7), int(win.height/3))
    bottom_right = Point(int(3*win.width/7), int(2*win.height/3))
    char1_1 = Fighter("fighter 1_1",2,"blue",bottom_right,"front",0)
    char1_2 = Fighter("fighter 1_2",5,"blue",bottom_right,"front",1.5)
    char1_3 = Amazon("amazon 1_3",3,"blue",bottom_right,"back",0)
    char1_4 = Amazon("amazon 1_4",5,"blue",bottom_right,"back",1)
    char1_5 = Wizard("wizard 1_5",5,"blue",bottom_right,"back",2)
    char2_1 = Fighter("fighter 2_1",1,"red",top_left,"front",0)
    char2_2 = Fighter("fighter 2_2",3,"red",top_left,"front",2)
    char2_3 = Amazon("amazon 2_3",5,"red",top_left,"back",0)
    char2_4 = Amazon("amazon 2_4",4,"red",top_left,"back",1)
    char2_5 = Wizard("wizard 2_5",5,"red",top_left,"back",2)

    unit1 = Unit("blue",[char1_1,char1_2,char1_3,char1_4,char1_5])
    unit2 = Unit("red",[char2_1,char2_2,char2_3,char2_4,char2_5])
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
    p2 = Point(win.width/2,win.height/2)
    background = Image(p2,'images/tiles.gif')
    background.draw(win)

    message.setTextColor('gray')
    message.setStyle('italic')
    message.setSize(30)
    message.draw(win)

    for i in range(5):
        image = Image(unit1.characters[i].location,"images/blue_" + unit1.characters[i].image)
        image.draw(win)
    for i in range(5):
        image = Image(unit2.characters[i].location,"images/red_" + unit2.characters[i].image)
        image.draw(win)

    message.setText('Click anywhere to begin')
    win.getMouse()

def main(argv):
    battle()

if __name__ == "__main__":
    main(sys.argv)
