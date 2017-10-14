from graphics import *
class Character:
    name = "name"
    side = "neutral"
    location = Point(0,0)
    row = "front"
    position = 1 #blue left side
    hp = 1
    strength = 1
    agility = 1
    luck = 1
    intelligence = 1

    resistances = {
        'physical': 50,
        'black': 50,
        'white': 50,
        'fire': 50,
        'cold': 50,
        'lightning': 50
        }

    attacking_elements = ['physical']
    num_attacks = 0
    order_value = 0
    attack_type = 'melee'
    #same attack type regardless of row
    is_alive = True
    def __init__(self, name, side, location, row, position):
        self.num_attacks_remaining = self.num_attacks
        self.name = name
        self.side = side
        self.row = row
        self.position = position
        clone_loc = location.clone()
        if (row == "front" and side == "red") or (row == "back" and side == "blue"):
            clone_loc.move(60+70*position,70-30*position)
        else:
            clone_loc.move(70*position,-30*position)
        self.location = clone_loc

