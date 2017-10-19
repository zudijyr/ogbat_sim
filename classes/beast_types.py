from classes.character import Character

class Gryphon(Character):
    base_hp = 80
    base_strength = 50
    base_agility = 58
    base_intelligence = 37
    base_luck = 53
    base_cost = 200
    image = "gryphon.gif"
    growth_hp = 7
    growth_strength = 2
    growth_agility = 4
    growth_intelligence = 1
    growth_cost = 50

    resistances = {
        'physical': 43,
        'black': 55,
        'white': 35,
        'fire': 33,
        'cold': 48,
        'lightning': 53
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'melee'
    back_elements = ['physical']
    back_num_attacks = 1
    back_hit = 'all'

class Cockatris(Character):
    base_hp = 74
    base_strength = 54
    base_agility = 63
    base_intelligence = 42
    base_luck = 55
    base_cost = 890
    image = "cockatris.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 4
    growth_intelligence = 1
    growth_cost = 80

    resistances = {
        'physical': 46,
        'black': 64,
        'white': 26,
        'fire': 37,
        'cold': 53,
        'lightning': 57
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'petrify'
    back_elements = ['physical']
    back_num_attacks = 1
    back_hit = 'all'

class Wyrm(Character):
    base_hp = 92
    base_strength = 58
    base_agility = 47
    base_intelligence = 31
    base_luck = 47
    base_cost = 850
    image = "wyrm.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 1
    growth_cost = 170

    resistances = {
        'physical': 45,
        'black': 48,
        'white': 32,
        'fire': 47,
        'cold': 38,
        'lightning': 38
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'melee'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Wyvern(Character):
    base_hp = 89
    base_strength = 63
    base_agility = 51
    base_intelligence = 36
    base_luck = 49
    base_cost = 1700
    image = "wyvern.gif"
    growth_hp = 9
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 1
    growth_cost = 210

    resistances = {
        'physical': 49,
        'black': 50,
        'white': 20,
        'fire': 53,
        'cold': 35,
        'lightning': 42
        }

    front_attack_type = 'melee'
