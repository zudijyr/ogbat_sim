from classes.character import Character

class Amazon(Character):
    base_hp = 83
    base_strength = 42
    base_agility = 50
    base_intelligence = 52
    base_luck = 48
    base_cost = 100
    image = "amazon.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 2
    growth_cost = 30

    resistances = {
        'physical': 38,
        'black': 38,
        'white': 42,
        'fire': 32,
        'cold': 36,
        'lightning': 43
        }

    num_attacks = 2
    attack_type = 'melee'
