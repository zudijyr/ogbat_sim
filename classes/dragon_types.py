from classes.character import Character

class Dragon(Character):
    base_hp = 93
    base_strength = 60
    base_agility = 37
    base_intelligence = 42
    base_luck = 50
    base_cost = 850
    image = "dragon.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 1
    growth_intelligence = 1
    growth_cost = 100
    movement = 'plains'
    alignment = 50

    resistances = {
        'physical': 52,
        'black': 44,
        'white': 44,
        'fire': 50,
        'cold': 46,
        'lightning': 47
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_attack_targetable = True
    back_elements = ['fire']
    back_num_attacks = 2
    back_hit = 'one'

class SilverDragon(Character):
    base_hp = 95
    base_strength = 64
    base_agility = 38
    base_intelligence = 46
    base_luck = 50
    base_cost = 1400
    image = "silver_dragon.gif"
    growth_hp = 9
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 160
    movement = 'snow'
    alignment = 71

    resistances = {
        'physical': 53,
        'black': 37,
        'white': 66,
        'fire': 58,
        'cold': 60,
        'lightning': 64
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['cold']
    back_attack_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class GoldDragon(Character):
    base_hp = 90
    base_strength = 69
    base_agility = 41
    base_intelligence = 50
    base_luck = 51
    base_cost = 1650
    image = "gold_dragon.gif"
    growth_hp = 10
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 230
    movement = 'snow'
    alignment = 77

    resistances = {
        'physical': 57,
        'black': 27,
        'white': 71,
        'fire': 23,
        'cold': 69,
        'lightning': 66
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_attack_targetable = True
    back_elements = ['cold']
    back_num_attacks = 2
    back_hit = 'one'

class PlatinumDragon(Character):
    base_hp = 83
    base_strength = 63
    base_agility = 45
    base_intelligence = 46
    base_luck = 53
    base_cost = 2000
    image = "platinum_dragon.gif"
    growth_hp = 11
    growth_strength = 5
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 250
    movement = 'snow'
    alignment = 82

    resistances = {
        'physical': 61,
        'black': 17,
        'white': 76,
        'fire': 11,
        'cold': 88,
        'lightning': 69
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    front_attack_targetable = True
    back_attack_type = 'strength'
    back_elements = ['cold']
    back_num_attacks = 2
    back_hit = 'all'

class RedDragon(Character):
    base_hp = 91
    base_strength = 62
    base_agility = 40
    base_intelligence = 44
    base_luck = 50
    base_cost = 1100
    image = "red_dragon.gif"
    growth_hp = 9
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 150
    movement = 'mountain'
    alignment = 50

    resistances = {
        'physical': 54,
        'black': 44,
        'white': 44,
        'fire': 58,
        'cold': 44,
        'lightning': 60
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['fire']
    back_num_attacks = 2
    back_attack_targetable = True
    back_hit = 'one'

class RedDragonII(Character):
    base_hp = 87
    base_strength = 67
    base_agility = 43
    base_intelligence = 48
    base_luck = 53
    base_cost = 1350
    image = "red_dragon_ii.gif"
    growth_hp = 10
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 200
    movement = 'mountain'
    alignment = 50

    resistances = {
        'physical': 59,
        'black': 48,
        'white': 48,
        'fire': 67,
        'cold': 25,
        'lightning': 63
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['fire']
    back_num_attacks = 2
    back_attack_targetable = True
    back_hit = 'one'

class Salamand(Character):
    base_hp = 80
    base_strength = 61
    base_agility = 47
    base_intelligence = 44
    base_luck = 56
    base_cost = 1700
    image = "salamand.gif"
    growth_hp = 11
    growth_strength = 5
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 250
    movement = 'mountain'
    alignment = 50

    resistances = {
        'physical': 62,
        'black': 51,
        'white': 51,
        'fire': 86,
        'cold': 11,
        'lightning': 67
        }

    front_attack_type = 'strength'
    front_elements = ['fire']
    front_num_attacks = 2
    front_hit = 'one'
    front_attack_targetable = True
    back_attack_type = 'intelligence'
    back_elements = ['fire']
    back_num_attacks = 2
    back_hit = 'all'

class BlackDragon(Character):
    base_hp = 97
    base_strength = 65
    base_agility = 36
    base_intelligence = 43
    base_luck = 50
    base_cost = 1300
    image = "black_dragon.gif"
    growth_hp = 9
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 150
    movement = 'plains'
    alignment = 29

    resistances = {
        'physical': 55,
        'black': 64,
        'white': 35,
        'fire': 49,
        'cold': 51,
        'lightning': 69
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_attack_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class Tiamat(Character):
    base_hp = 86
    base_strength = 70
    base_agility = 39
    base_intelligence = 47
    base_luck = 48
    base_cost = 1550
    image = "tiamat.gif"
    growth_hp = 10
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 210
    movement = 'plains'
    alignment = 23

    resistances = {
        'physical': 59,
        'black': 69,
        'white': 30,
        'fire': 53,
        'cold': 54,
        'lightning': 76
        }

    front_attack_type = 'strength'
    front_attack_targetable = True
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 2
    back_hit = 'all'

class ZombieDragon(Character):
    base_hp = 78
    base_strength = 64
    base_agility = 43
    base_intelligence = 53
    base_luck = 63
    base_cost = 1900
    image = "zombie_dragon.gif"
    growth_hp = 11
    growth_strength = 5
    growth_agility = 4
    growth_intelligence = 3
    growth_cost = 250
    movement = 'marsh'
    alignment = 0

    resistances = {
        'physical': 73,
        'black': 83,
        'white': 15,
        'fire': 79,
        'cold': 78,
        'lightning': 86
        }

    front_attack_type = 'strength'
    front_attack_targetable = True
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_attack_targetable = True
    back_elements = ['black']
    back_num_attacks = 2
    back_hit = 'one'
