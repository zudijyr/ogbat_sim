class Unit:
    def __init__(self, side, characters, tactic = 'weak'):
        self.side = side
        self.characters = characters
        self.tactic = tactic
        for char in characters:
            char.tactic = tactic
