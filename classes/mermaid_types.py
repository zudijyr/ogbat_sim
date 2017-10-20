from classes.character import Character

class Mermaid(Character):
    base_hp = 93
    base_strength = 49
    base_agility = 52
    base_intelligence = 51
    base_luck = 44
    base_cost = 900
    image = "mermaid.gif"
    growth_hp = 5
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 3
    growth_cost = 130
    movement = 'shallows'
    alignment = 57

    resistances = {
        'physical': 29,
        'black': 43,
        'white': 48,
        'fire': 26,
        'cold': 52,
        'lightning': 21
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_targetable = True
    back_elements = ['cold']
    back_num_attacks = 1
    back_hit = 'one'

class Nixie(Character):
    base_hp = 85
    base_strength = 51
    base_agility = 55
    base_intelligence = 57
    base_luck = 41
    base_cost = 1150
    image = "nixie.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 210
    movement = 'shallows'
    alignment = 74

    resistances = {
        'physical': 34,
        'black': 47,
        'white': 62,
        'fire': 31,
        'cold': 60,
        'lightning': 23
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['cold']
    back_num_attacks = 1
    back_hit = 'all'

