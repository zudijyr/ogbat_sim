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
    movement = 'forest'

    resistances = {
        'physical': 38,
        'black': 38,
        'white': 42,
        'fire': 32,
        'cold': 36,
        'lightning': 43
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 1
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Valkyrie(Character):
    base_hp = 81
    base_strength = 45
    base_agility = 52
    base_intelligence = 54
    base_luck = 52
    base_cost = 620
    image = "valkyrie.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 80
    movement = 'forest'

    resistances = {
        'physical': 42,
        'black': 32,
        'white': 48,
        'fire': 34,
        'cold': 44,
        'lightning': 52
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['lightning']
    back_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class Muse(Character):
    base_hp = 76
    base_strength = 48
    base_agility = 55
    base_intelligence = 56
    base_luck = 64
    base_cost = 1350
    image = "muse.gif"
    growth_hp = 4
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 210
    movement = 'snow'

    resistances = {
        'physical': 46,
        'black': 15,
        'white': 65,
        'fire': 38,
        'cold': 52,
        'lightning': 60
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['lightning']
    back_num_attacks = 2
    back_hit = 'all'

class Cleric(Character):
    base_hp = 87
    base_strength = 41
    base_agility = 54
    base_intelligence = 52
    base_luck = 49
    base_cost = 200
    image = "cleric.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 1
    growth_intelligence = 3
    growth_cost = 60
    movement = 'plains'

    resistances = {
        'physical': 24,
        'black': 25,
        'white': 55,
        'fire': 23,
        'cold': 21,
        'lightning': 25
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'healing'
    back_elements = ['white']
    back_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class Shaman(Character):
    base_hp = 83
    base_strength = 43
    base_agility = 57
    base_intelligence = 58
    base_luck = 53
    base_cost = 450
    image = "shaman.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 100
    movement = 'plains'

    resistances = {
        'physical': 28,
        'black': 18,
        'white': 62,
        'fire': 27,
        'cold': 25,
        'lightning': 27
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'healing'
    back_targetable = True
    back_elements = ['white']
    back_num_attacks = 3
    back_hit = 'one'

class Monk(Character):
    base_hp = 74
    base_strength = 45
    base_agility = 61
    base_intelligence = 61
    base_luck = 56
    base_cost = 700
    image = "monk.gif"
    growth_hp = 4
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 110
    movement = 'plains'

    resistances = {
        'physical': 32,
        'black': 10,
        'white': 70,
        'fire': 31,
        'cold': 29,
        'lightning': 29
        }

    front_attack_type = 'strength'
    front_elements = ['white']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'healing'
    back_elements = ['white']
    back_num_attacks = 2
    back_hit = 'all'

class Amazon(Character):
    base_hp = 80
    base_strength = 38
    base_agility = 49
    base_intelligence = 58
    base_luck = 67
    base_cost = 510
    image = "witch.gif"
    growth_hp = 3
    growth_strength = 1
    growth_agility = 2
    growth_intelligence = 4
    growth_cost = 70
    movement = 'plains'

    resistances = {
        'physical': 25,
        'black': 48,
        'white': 50,
        'fire': 30,
        'cold': 28,
        'lightning': 31
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'stun'
    back_elements = ['black']
    back_num_attacks = 2
    back_hit = 'all'

class Princess(Character):
    #TODO leader bonus
    base_hp = 70
    base_strength = 37
    base_agility = 48
    base_intelligence = 57
    base_luck = 63
    base_cost = 2000
    image = "princess.gif"
    growth_hp = 2
    growth_strength = 1
    growth_agility = 2
    growth_intelligence = 4
    growth_cost = 250
    movement = 'plains'

    resistances = {
        'physical': 27,
        'black': 20,
        'white': 65,
        'fire': 21,
        'cold': 22,
        'lightning': 25
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['white']
    back_num_attacks = 1
    back_hit = 'all'
