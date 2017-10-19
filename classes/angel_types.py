from classes.character import Character

class Angel(Character):
    base_hp = 70
    base_strength = 40
    base_agility = 43
    base_intelligence = 50
    base_luck = 50
    base_cost = 300
    image = "angel.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 3
    growth_cost = 50
    movement = 'low sky'

    resistances = {
        'physical': 27,
        'black': 35,
        'white': 55,
        'fire': 39,
        'cold': 40,
        'lightning': 37
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 1
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['white']
    back_num_attacks = 1
    back_hit = 'one'

class Cherubim(Character):
    base_hp = 71
    base_strength = 45
    base_agility = 46
    base_intelligence = 55
    base_luck = 54
    base_cost = 800
    image = "cherubim.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 4
    growth_cost = 130
    movement = 'low sky'

    resistances = {
        'physical': 31,
        'black': 24,
        'white': 66,
        'fire': 42,
        'cold': 44,
        'lightning': 41
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['white']
    back_num_attacks = 2
    back_hit = 'one'

class Seraphim(Character):
    base_hp = 76
    base_strength = 49
    base_agility = 49
    base_intelligence = 60
    base_luck = 57
    base_cost = 1300
    image = "seraphim.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 210
    movement = 'low sky'

    resistances = {
        'physical': 35,
        'black': 17,
        'white': 77,
        'fire': 45,
        'cold': 48,
        'lightning': 45
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 1
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['white']
    back_num_attacks = 1
    back_hit = 'all'

