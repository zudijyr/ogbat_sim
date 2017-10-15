from classes.character import Character

class BeastTamer(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "beast_tamer.gif"
    growth_hp = 5
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 20

    resistances = {
        'physical': 44,
        'black': 40,
        'white': 40,
        'fire': 36,
        'cold': 30,
        'lightning': 44
        }

    num_attacks = 2
    attack_type = 'melee'
