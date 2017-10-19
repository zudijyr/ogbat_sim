from classes.character import Character

class Imp(Character):
    base_hp = 68
    base_strength = 45
    base_agility = 45
    base_intelligence = 48
    base_luck = 48
    base_cost = 300
    image = "imp.gif"
    growth_hp = 5
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 3
    growth_cost = 60
    movement = 'low sky'

    resistances = {
        'physical': 44,
        'black': 55,
        'white': 35,
        'fire': 37,
        'cold': 44,
        'lightning': 38
        }

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 1
    back_hit = 'one'

class Demon(Character):
    base_hp = 69
    base_strength = 49
    base_agility = 48
    base_intelligence = 53
    base_luck = 52
    base_cost = 800
    image = "demon.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 140
    movement = 'low sky'

    resistances = {
        'physical': 47,
        'black': 65,
        'white': 25,
        'fire': 40,
        'cold': 49,
        'lightning': 44
        }

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 2
    back_hit = 'one'

class Devil(Character):
    base_hp = 70
    base_strength = 56
    base_agility = 51
    base_intelligence = 58
    base_luck = 55
    base_cost = 1300
    image = "devil.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 220
    movement = 'low sky'

    resistances = {
        'physical': 53,
        'black': 86,
        'white': 4,
        'fire': 42,
        'cold': 52,
        'lightning': 48
        }

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 1
    back_hit = 'all'

