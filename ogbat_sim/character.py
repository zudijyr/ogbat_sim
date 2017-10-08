class Character:
    hp = 1
    strength = 1
    agility = 1
    luck = 1
    intelligence = 1
    num_attacks = 0
    attack_type = 'physical'
    #same attack type regardless of row
    is_alive = True
    def __init__(self):
        self.num_attacks_remaining = self.num_attacks
