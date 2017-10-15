from graphics import *
class Character:
    name = "name"
    side = "neutral"
    location = Point(0,0)
    row = "front"
    position = 1 #blue left side
    level = 1

    base_hp = 1
    base_strength = 1
    base_agility = 1
    base_intelligence = 1
    base_luck = 1
    base_cost = 50
    growth_hp = 1
    growth_strength = 1
    growth_agility = 1
    growth_intelligence = 1
    growth_cost = 10

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
    target = 'one'
    order_value = 0
    hptext = Text(Point(0,0),"")
    attack_type = 'melee'
    #same attack type regardless of row
    is_alive = True
    def __init__(self, name, level, side, location, row, position):
        self.num_attacks_remaining = self.num_attacks
        self.name = name
        self.level = level
        self.hp = self.base_hp + (level-1)*self.growth_hp
        self.strength = self.base_strength + (level-1)*self.growth_strength
        self.agility = self.base_agility + (level-1)*self.growth_agility
        self.intelligence = self.base_intelligence + (level-1)*self.growth_intelligence
        self.cost = self.base_cost + (level-1)*self.growth_cost
        self.luck = self.base_luck
        self.side = side
        self.row = row
        self.position = position
        clone_loc = location.clone()
        if (row == "front" and side == "red") or (row == "back" and side == "blue"):
            clone_loc.move(60+70*position,70-30*position)
        else:
            clone_loc.move(70*position,-30*position)
        self.location = clone_loc
        self.hptext = Text(Point(self.location.getX(),self.location.getY()+40),self.hp)
        self.hptext.setSize(20)
        self.hptext.setTextColor(side)

