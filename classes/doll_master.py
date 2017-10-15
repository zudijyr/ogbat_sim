from classes.character import Character

class DollMaster(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "doll_master.gif"
    growth_hp = 2
    growth_strength = 1
    growth_agility = 1
    growth_intelligence = 4
    growth_cost = 70

    resistances = {
        'physical': 20,
        'black': 45,
        'white': 35,
        'fire': 32,
        'cold': 32,
        'lightning': 37
        }

    attacking_elements = ['physical', 'black', 'fire', 'cold', 'lightning']
    num_attacks = 2
    attack_type = 'magical'
