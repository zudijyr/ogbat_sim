from classes.character import Character

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

