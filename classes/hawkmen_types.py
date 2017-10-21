from classes.character import Character

class Hawkman(Character):
    base_hp = 87
    base_strength = 45
    base_agility = 55
    base_intelligence = 52
    base_cost = 400
    base_luck = 42
    image = "hawkman.gif"
    growth_hp = 5
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 1
    growth_cost = 90
    movement = 'low sky'
    alignment = 50

    resistances = {
        'physical': 39,
        'black': 40,
        'white': 40,
        'fire': 36,
        'cold': 40,
        'lightning': 44
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 1
    back_hit = 'one'

class Eagleman(Character):
    base_hp = 86
    base_strength = 49
    base_agility = 60
    base_intelligence = 58
    base_cost = 700
    base_luck = 58
    image = "eagleman.gif"
    growth_hp = 6
    growth_strength = 2
    growth_agility = 4
    growth_intelligence = 2
    growth_cost = 140
    movement = 'low sky'
    alignment = 66

    resistances = {
        'physical': 42,
        'black': 34,
        'white': 56,
        'fire': 39,
        'cold': 43,
        'lightning': 80
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_attack_targetable = True
    back_elements = ['lightning']
    back_num_attacks = 1
    back_hit = 'one'

class Ravenman(Character):
    base_hp = 95
    base_strength = 52
    base_agility = 62
    base_intelligence = 55
    base_cost = 800
    base_luck = 48
    image = "ravenman.gif"
    growth_hp = 6
    growth_strength = 2
    growth_agility = 4
    growth_intelligence = 2
    growth_cost = 120
    movement = 'low sky'
    alignment = 31

    resistances = {
        'physical': 40,
        'black': 69,
        'white': 21,
        'fire': 70,
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
    back_num_attacks = 1
    back_hit = 'one'

