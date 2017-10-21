from classes.character import Character

class Pumpkin(Character):
    base_hp = 98
    base_strength = 45
    base_agility = 45
    base_intelligence = 31
    base_luck = 72
    base_cost = 100
    image = "pumpkin.gif"
    growth_hp = 3
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 20
    movement = 'forest'
    alignment = 45

    resistances = {
        'physical': 33,
        'black': 45,
        'white': 38,
        'fire': 11,
        'cold': 37,
        'lightning': 34
        }

    front_attack_type = 'pumpkin'
    front_elements = ['physical']
    front_num_attacks = 1
    front_attack_targetable = True
    front_hit = 'one'
    back_attack_type = 'pumpkin'
    back_elements = ['physical']
    back_num_attacks = 1
    back_attack_targetable = True
    back_hit = 'one'

class Halloween(Character):
    base_hp = 88
    base_strength = 50
    base_agility = 58
    base_intelligence = 37
    base_luck = 82
    base_cost = 100
    image = "halloween.gif"
    growth_hp = 4
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 2
    growth_cost = 50
    movement = 'forest'
    alignment = 18

    resistances = {
        'physical': 60,
        'black': 69,
        'white': 22,
        'fire': 37,
        'cold': 56,
        'lightning': 64
        }

    front_attack_type = 'pumpkin'
    front_elements = ['physical']
    front_num_attacks = 2
    front_attack_targetable = True
    front_hit = 'one'
    back_attack_type = 'pumpkin'
    back_elements = ['physical']
    back_num_attacks = 2
    back_attack_targetable = True
    back_hit = 'one'
