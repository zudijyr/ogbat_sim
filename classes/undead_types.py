from classes.character import Character

class Skeleton(Character):
    base_hp = 0
    base_strength = 43
    base_agility = 42
    base_intelligence = 32
    base_luck = 55
    base_cost = 100
    image = "skeleton.gif"
    growth_hp = 0
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 20
    movement = 'plains'
    is_undead = True

    resistances = {
        'physical': 50,
        'black': 50,
        'white': 50,
        'fire': 50,
        'cold': 50,
        'lightning': 50
        } #these are just listed as 'n/a' but i need some number

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['black']
    back_num_attacks = 1
    back_hit = 'one'

class Wraith(Character):
    base_hp = 0
    base_strength = 51
    base_agility = 49
    base_intelligence = 44
    base_luck = 55
    base_cost = 350
    image = "wraith.gif"
    growth_hp = 0
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 0
    movement = 'plains'
    is_undead = True

    resistances = {
        'physical': 50,
        'black': 50,
        'white': 50,
        'fire': 50,
        'cold': 50,
        'lightning': 50
        } #these are just listed as 'n/a' but i need some number

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['black']
    back_num_attacks = 1
    back_hit = 'one'

class Ghost(Character):
    base_hp = 0
    base_strength = 35
    base_agility = 57
    base_intelligence = 50
    base_luck = 48
    base_cost = 100
    image = "ghost.gif"
    growth_hp = 0
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 20
    movement = 'low sky'
    is_undead = True

    resistances = {
        'physical': 50,
        'black': 50,
        'white': 50,
        'fire': 50,
        'cold': 50,
        'lightning': 50
        } #these are just listed as 'n/a' but i need some number

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 1
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 2
    back_hit = 'one'

class Phantom(Character):
    base_hp = 0
    base_strength = 45
    base_agility = 62
    base_intelligence = 53
    base_luck = 50
    base_cost = 200
    image = "phantom.gif"
    growth_hp = 0
    growth_strength = 2
    growth_agility = 3
    growth_intelligence = 4
    growth_cost = 40
    movement = 'low sky'
    is_undead = True

    resistances = {
        'physical': 50,
        'black': 50,
        'white': 50,
        'fire': 50,
        'cold': 50,
        'lightning': 50
        } #these are just listed as 'n/a' but i need some number

    front_attack_type = 'strength'
    front_elements = ['black']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'intelligence'
    back_elements = ['black']
    back_num_attacks = 3
    back_hit = 'one'
