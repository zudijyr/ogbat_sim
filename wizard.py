from character import Character

class Wizard(Character):
    hp = 86
    strength = 37
    agility = 51
    intelligence = 52
    cost = 400
    luck = 50
    image = "wizard.gif"

    elements = {
        'physical': 20,
        'black': 45,
        'white': 35,
        'fire': 32,
        'cold': 32,
        'lightning': 37
        }

    num_attacks = 2
    attack_type = 'magical'
