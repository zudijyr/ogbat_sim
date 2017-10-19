import sys
from os import system
from platform import system as platform
import random
from graphics import *
from classes.unit import Unit
from classes.fighter_types import *
from classes.amazon_types import *
from classes.faerie_types import *
from classes.hawkmen_types import *
from classes.beast_types import *
from classes.dragon_types import *
from classes.angel_types import *
from classes.imp_types import *
from classes.pumpkin_types import *
from classes.undead_types import *

blue_damage = 0
red_damage = 0
win = GraphWin('Ogre Battle Fight Sim', 700, 500)
message = Text(Point(win.getWidth()/2, 30), '')
current_rec = Rectangle(Point(0,0),Point(1,1))
target_rec = Rectangle(Point(0,0),Point(1,1))

def calc_movement_bonus(unit, terrain):
    #not sure these numbers are accurate, they are from the ogrebattlesaga wiki
    high_sky_moves = {'wall':5,'city':5,'snow road':7,'sky':7,'desert':6,'road':7,
            'volcano':5,'cliff':5,'dark mountain':5,'snow mountain':6,'swamp':7,
            'mountain':6,'snow forest':7,'barrens':7,'snow plains':7,'forest':7,
            'reef':6,'plains':7,'shallows':6,'deep sea':6}
    plains_moves = {'wall':0,'city':6,'snow road':5,'sky':0,'desert':3,'road':6,
            'volcano':1,'cliff':1,'dark mountain':2,'snow mountain':1,'swamp':1,
            'mountain':2,'snow forest':3,'barrens':3,'snow plains':4,'forest':4,
            'reef':1,'plains':5,'shallows':1,'deep sea':1}
    forest_moves = {'wall':0,'city':5,'snow road':5,'sky':0,'desert':2,'road':6,
            'volcano':2,'cliff':1,'dark mountain':2,'snow mountain':2,'swamp':3,
            'mountain':3,'snow forest':5,'barrens':5,'snow plains':3,'forest':6,
            'reef':1,'plains':4,'shallows':1,'deep sea':1}
    mountain_moves = {'wall':0,'city':4,'snow road':5,'sky':0,'desert':3,'road':6,
            'volcano':5,'cliff':3,'dark mountain':4,'snow mountain':4,'swamp':1,
            'mountain':5,'snow forest':3,'barrens':5,'snow plains':3,'forest':5,
            'reef':1,'plains':3,'shallows':1,'deep sea':1}
    snow_moves = {'wall':0,'city':4,'snow road':7,'sky':0,'desert':1,'road':6,
            'volcano':1,'cliff':1,'dark mountain':5,'snow mountain':5,'swamp':2,
            'mountain':3,'snow forest':5,'barrens':4,'snow plains':6,'forest':5,
            'reef':1,'plains':4,'shallows':1,'deep sea':1}
    marsh_moves = {'wall':0,'city':3,'snow road':3,'sky':0,'desert':1,'road':4,
            'volcano':1,'cliff':1,'dark mountain':1,'snow mountain':1,'swamp':6,
            'mountain':1,'snow forest':2,'barrens':2,'snow plains':3,'forest':3,
            'reef':6,'plains':4,'shallows':4,'deep sea':3}
    shallows_moves = {'wall':0,'city':3,'snow road':2,'sky':0,'desert':1,'road':3,
            'volcano':1,'cliff':1,'dark mountain':1,'snow mountain':1,'swamp':2,
            'mountain':1,'snow forest':1,'barrens':1,'snow plains':1,'forest':1,
            'reef':4,'plains':3,'shallows':7,'deep sea':5}
    deep_sea_moves = {'wall':0,'city':3,'snow road':1,'sky':0,'desert':1,'road':2,
            'volcano':1,'cliff':1,'dark mountain':1,'snow mountain':1,'swamp':2,
            'mountain':1,'snow forest':1,'barrens':1,'snow plains':1,'forest':1,
            'reef':3,'plains':2,'shallows':5,'deep sea':7}
    slow_moves = {'wall':0,'city':3,'snow road':1,'sky':0,'desert':1,'road':2,
            'volcano':1,'cliff':1,'dark mountain':1,'snow mountain':1,'swamp':1,
            'mountain':1,'snow forest':1,'barrens':1,'snow plains':1,'forest':1,
            'reef':1,'plains':1,'shallows':1,'deep sea':1}
    if unit.movement == 'high sky':
        return high_sky_moves[terrain]
    elif unit.movement == 'low sky':
        if terrain == 'wall':
            return 1
        return (high_sky_moves[terrain] - 1)
    elif unit.movement == 'plains':
        return plains_moves[terrain]
    elif unit.movement == 'forest':
        return forest_moves[terrain]
    elif unit.movement == 'mountain':
        return mountain_moves[terrain]
    elif unit.movement == 'snow':
        return snow_moves[terrain]
    elif unit.movement == 'marsh':
        return marsh_moves[terrain]
    elif unit.movement == 'shallows':
        return shallows_moves[terrain]
    elif unit.movement == 'deep sea':
        return deep_sea_moves[terrain]
    elif unit.movement == 'slow':
        return slow_moves[terrain]
    #error if no matching movement type

def does_it_hit(attacker, defender, terrain):
    attack_type = attacker.attack_type
    if attack_type in ('strength','iainuki','petrify','pumpkin'):
        attack_speed = attacker.agility
        defend_speed = defender.agility
    elif attack_type == 'intelligence':
        attack_speed = attacker.intelligence
        defend_speed = defender.intelligence

    att_move_bonus = calc_movement_bonus(attacker,terrain)
    def_move_bonus = calc_movement_bonus(defender,terrain)
    friend_factor = 0 #TODO charm status, special attacks
    if (defender.is_undead and attack_element != 'white' and attack_type not in ('healing','petrify','pumpkin'):
        return False

    #hit formula from Deathlike2's unit mechanics gamefaq
    hit_success = attack_speed + attacker.luck/2 + att_move_bonus + random.randint(0,7)
    evasion_success = defend_speed + defender.luck/2 + def_move_bonus + friend_factor + random.randint(0,7)
    target_difference = hit_success - evasion_success
    rand_hit_num = random.randint(0,9)
    if attack_type in ('pumpkin','petrify','stun','charm'):
        hit_success = attack_speed + attacker.luck/2 + random.randint(3,10)
        evasion_success = defend_speed + defender.luck/2 + friend_factor + random.randint(3,10)
        target_difference = hit_success - evasion_success
    if attack_type == 'pumpkin':
        rand_hit_num += 1
    if attack_type == 'petrify':
        rand_hit_num += 3
    if attack_type == 'stun':
        rand_hit_num += 4
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

def choose_element(attacker, targets):
    low_score = 101
    lowest = 'element'
    defender = targets[0] #targets should be sorted by tactics priority
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

def damage(attacker, defender, attack_element, attacker_tactic, defender_tactic, terrain):
    attack_type = attacker.attack_type
    if attack_type in ('strength','iainuki','petrify'):
        attack_power = attacker.strength
        defend_power = defender.strength
    elif attack_type == 'intelligence':
        attack_power = attacker.intelligence
        defend_power = defender.intelligence

    att_tac_bonus,def_tac_bonus = calc_tac_bonuses(attacker_tactic, defender_tactic)
    att_move_bonus = calc_movement_bonus(attacker,terrain)
    def_move_bonus = calc_movement_bonus(defender,terrain)
    time = 0
    kiss = 0
    if attack_type == 'petrify':
        defender.is_petrified = True
        print("{0} has been petrified".format(defender.name))
    if attack_type == 'pumpkin':
        return int(defender.hp/2)
    #TODO time,kiss
    #damage formula from Deathlike2's unit analysis gamefaq
    raw_damage = attack_power/2 + att_move_bonus*2 - time/5 + att_tac_bonus + kiss + random.randint(1,8)
    attack_multiplier = 1 #TODO special attacks like ianuki
    if attack_type == 'iainuki':
        attack_multiplier = 1.5
        blowback = int(0.5 * raw_damage)
        blowback = min(blowback,attacker.hp)
        print("{0} suffers {1} from iainuki blowback".format(attacker.name,blowback))
        attacker.hp -= blowback
    raw_damage = raw_damage*attack_multiplier
    resistance = defender.resistances[attack_element]
    absorption = ((defend_power/2 + def_move_bonus*2 - time/5 + kiss + random.randint(3,10)) * resistance/100) + def_tac_bonus
    damage = max(raw_damage - absorption,1) #TODO quake
    damage = min(damage,defender.hp)
    return int(damage)

def choose_target(attacker, defending_unit):
    #TODO include tactic
    lowest = 9999
    possible_targets = []
    target = []
    if attacker.hit == 'all':
        for char in defending_unit.characters:
            if char.is_alive:
                target.append(char)
        return target #hit all TODO sort by tactic

    elif (attacker.attack_type in('intelligence','iainuki')) or attacker.targetable:
        for char in defending_unit.characters:
            if char.is_alive:
                possible_targets.append(char)
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
            current_target = character
    target.append(current_target)
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

def attack(attacker, defender, terrain, attack_element):
    global blue_damage,red_damage
    draw_attack_recs(attacker,defender)
    hit = does_it_hit(attacker, defender, terrain, attack_element)
    if (hit):
        dam = damage(attacker,defender,attack_element,'weak','weak',terrain)
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
            #this will look weird when killing undead but should work
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

def combat_round(all_chars,unit1,unit2,terrain):
    for attacker in all_chars:
        if attacker.is_alive == False or attacker.num_attacks_remaining == 0 or attacker.is_petrified:
            pass
        else:
            win.getMouse()
            attacker.num_attacks_remaining -= 1
            if attacker.side == "blue":
                targets = choose_target(attacker,unit2)
            else:
                targets = choose_target(attacker,unit1)
            attack_element = choose_element(attacker, targets)
            for char in targets:
                attack(attacker, char, terrain, attack_element)
                set_hp_text(all_chars)

def turn_order(all_chars, terrain):
    for char in all_chars:
        move_bonus = calc_movement_bonus(char, terrain)
        char.order_value = char.agility + char.luck/2 + move_bonus + random.randint(3,10)
    all_chars.sort(key=lambda x: x.order_value, reverse=True)
    return all_chars

def battle():
    terrain = 'city' #TODO set this somehow
    top_left = Point(int(win.width/7), int(win.height/3))
    bottom_right = Point(int(3*win.width/7), int(2*win.height/3))
    unit1_charlist = []
    level = 25
    char1_1 = Halloween("halloween 1_1",level,"blue",bottom_right,"front",0)
    unit1_charlist.append(char1_1)
    char1_5 = Halloween("halloween 1_1",level,"blue",bottom_right,"front",2)
    unit1_charlist.append(char1_5)
    char1_2 = Devil("devil 1_1",level,"blue",bottom_right,"back",0)
    unit1_charlist.append(char1_2)
    char1_3 = Devil("devil 1_2",level,"blue",bottom_right,"back",1)
    unit1_charlist.append(char1_3)
    char1_4 = Devil("devil 1_3",level,"blue",bottom_right,"back",2)
    unit1_charlist.append(char1_4)
    #char1_3 = Salamand("salamand 1_1",level,"blue",bottom_right,"back",2)
    #unit1_charlist.append(char1_3)
    #char1_2 = Ravenman("ravenman 1_2",level,"blue",bottom_right,"front",1.5)
    #unit1_charlist.append(char1_2)
    #char1_3 = Lich("lich 1_3",level,"blue",bottom_right,"back",0)
    #unit1_charlist.append(char1_3)
    #char1_3 = DollMaster("dollmaster 1_3",level,"blue",bottom_right,"back",0)
    #unit1_charlist.append(char1_3)
    #char1_3 = Sorcerer("sorcerer 1_3",level,"blue",bottom_right,"back",0)
    #unit1_charlist.append(char1_3)
    #char1_4 = Tigerman("tigerman 1_4",level,"blue",bottom_right,"back",1)
    #unit1_charlist.append(char1_4)
    #char1_5 = BeastTamer("beast tamer 1_5",level,"blue",bottom_right,"back",2)
    #unit1_charlist.append(char1_5)

    unit2_charlist = []
    char2_1 = ZombieDragon("zombie dragon 2_1",level,"red",top_left,"front",0)
    unit2_charlist.append(char2_1)
    #char2_2 = WildMan("wild man 2_2",level,"red",top_left,"front",2)
    #unit2_charlist.append(char2_2)
    #char2_3 = Samurai("samurai 2_3",5,"red",top_left,"back",0)
    #unit2_charlist.append(char2_3)
    #char2_4 = SamuraiMaster("samurai master 2_4",5,"red",top_left,"back",1)
    #unit2_charlist.append(char2_4)
    #char2_3 = Sylph("sylph 2_3",level,"red",top_left,"back",0)
    #unit2_charlist.append(char2_3)
    #char2_4 = Sylph("sylph 2_4",level,"red",top_left,"back",1)
    #unit2_charlist.append(char2_4)
    #char2_5 = Sylph("sylph 2_5",level,"red",top_left,"back",2)
    #unit2_charlist.append(char2_5)

    unit1 = Unit("blue",unit1_charlist)
    unit2 = Unit("red",unit2_charlist)
    all_chars = unit1_charlist + unit2_charlist
    draw_stuff(unit1,unit2,terrain)
    draw_hp_text(unit1,unit2)
    max_rounds = 1
    for char in all_chars:
        if char.num_attacks > max_rounds:
            max_rounds = char.num_attacks
    for round_num in range(max_rounds):
        all_chars = turn_order(all_chars,terrain)
        combat_round(all_chars,unit1,unit2,terrain)
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

def draw_stuff(unit1,unit2,terrain):
    p2 = Point(win.width/2,win.height/2)
    background = Image(p2,'images/city_blank.gif')
    background.draw(win)

    message.setTextColor('gray')
    message.setStyle('italic')
    message.setSize(30)
    message.draw(win)

    for i in range(len(unit1.characters)):
        image = Image(unit1.characters[i].location,"images/blue_" + unit1.characters[i].image)
        image.draw(win)
    for i in range(len(unit2.characters)):
        image = Image(unit2.characters[i].location,"images/red_" + unit2.characters[i].image)
        image.draw(win)

    message.setText('Click anywhere to begin')

def main(argv):
    if platform() == 'Darwin':  # How Mac OS X is identified by Python
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    battle()

if __name__ == "__main__":
    main(sys.argv)

#TODO unit test for positional targeting
#TODO unit test for terrain movement bonus
