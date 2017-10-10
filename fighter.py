from character import Character

class Fighter(Character):
    hp = 77
    strength = 45
    agility = 47
    luck = 45
    intelligence = 40

    elements = {
        'physical': 44,
        'black': 40,
        'white': 40,
        'fire': 36,
        'cold': 30,
        'lightning': 44
        }

    num_attacks = 2
    attack_type = 'melee'
