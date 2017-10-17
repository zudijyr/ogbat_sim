from classes.character import Character

class Faerie(Character):
    base_hp = 48
    base_strength = 38
    base_agility = 52
    base_intelligence = 49
    base_luck = 62
    base_cost = 100
    image = "faerie.gif"
    growth_hp = 3
    growth_strength = 2
    growth_agility = 4
    growth_intelligence = 4
    growth_cost = 70

    resistances = {
        'physical': 30,
        'black': 40,
        'white': 50,
        'fire': 20,
        'cold': 23,
        'lightning': 28
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'kiss'
    back_elements = ['physical']
    back_num_attacks = 1
    back_hit = 'one'

class Pixie(Character):
    base_hp = 56
    base_strength = 43
    base_agility = 57
    base_intelligence = 53
    base_luck = 65
    base_cost = 400
    image = "pixie.gif"
    growth_hp = 3
    growth_strength = 2
    growth_agility = 5
    growth_intelligence = 4
    growth_cost = 170

    resistances = {
        'physical': 32,
        'black': 40,
        'white': 55,
        'fire': 28,
        'cold': 25,
        'lightning': 26
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'kiss'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Sylph(Character):
    base_hp = 64
    base_strength = 40
    base_agility = 63
    base_intelligence = 47
    base_luck = 68
    base_cost = 700
    image = "sylph.gif"
    growth_hp = 4
    growth_strength = 3
    growth_agility = 5
    growth_intelligence = 4
    growth_cost = 250

    resistances = {
        'physical': 35,
        'black': 30,
        'white': 60,
        'fire': 36,
        'cold': 27,
        'lightning': 22
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'magical'
    back_elements = ['white']
    back_num_attacks = 1
    back_hit = 'all'
