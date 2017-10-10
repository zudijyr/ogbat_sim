from graphics import *
class Character:
    name = "name"
    side = "neutral"
    location = Point(0,0)
    hp = 1
    strength = 1
    agility = 1
    luck = 1
    intelligence = 1
    num_attacks = 0
    order_value = 0
    attack_type = 'physical'
    #same attack type regardless of row
    is_alive = True
    def __init__(self, name, side, location):
        self.num_attacks_remaining = self.num_attacks
        self.location = location
        self.name = name
        self.side = side
