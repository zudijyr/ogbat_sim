from character import Character

class Amazon(Character):
    hp = 83
    strength = 42
    agility = 50
    intelligence = 52
    luck = 48
    image = "amazon.gif"

    elements = {
        'physical': 38,
        'black': 38,
        'white': 42,
        'fire': 32,
        'cold': 36,
        'lightning': 43
        }

    num_attacks = 2
    attack_type = 'melee'
