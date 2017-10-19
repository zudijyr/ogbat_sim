from classes.character import Character

class Gryphon(Character):
    base_hp = 80
    base_strength = 50
    base_agility = 58
    base_intelligence = 37
    base_luck = 53
    base_cost = 200
    image = "gryphon.gif"
    growth_hp = 7
    growth_strength = 2
    growth_agility = 4
    growth_intelligence = 1
    growth_cost = 50

    resistances = {
        'physical': 43,
        'black': 55,
        'white': 35,
        'fire': 33,
        'cold': 48,
        'lightning': 53
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'melee'
    back_elements = ['physical']
    back_num_attacks = 1
    back_hit = 'all'

class Cockatris(Character):
    base_hp = 74
    base_strength = 54
    base_agility = 63
    base_intelligence = 42
    base_luck = 55
    base_cost = 890
    image = "cockatris.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 4
    growth_intelligence = 1
    growth_cost = 80

    resistances = {
        'physical': 46,
        'black': 64,
        'white': 26,
        'fire': 37,
        'cold': 53,
        'lightning': 57
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'petrify'
    back_attack_targetable = True
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Wyrm(Character):
    base_hp = 92
    base_strength = 58
    base_agility = 47
    base_intelligence = 31
    base_luck = 47
    base_cost = 850
    image = "wyrm.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 1
    growth_cost = 170

    resistances = {
        'physical': 45,
        'black': 48,
        'white': 32,
        'fire': 47,
        'cold': 38,
        'lightning': 38
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'melee'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Wyvern(Character):
    base_hp = 89
    base_strength = 63
    base_agility = 51
    base_intelligence = 36
    base_luck = 49
    base_cost = 1700
    image = "wyvern.gif"
    growth_hp = 9
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 1
    growth_cost = 210

    resistances = {
        'physical': 49,
        'black': 50,
        'white': 20,
        'fire': 53,
        'cold': 35,
        'lightning': 42
        }

    front_attack_type = 'melee'
    front_elements = ['physical']
    front_num_attacks = 2
    front_hit = 'one'
    back_attack_type = 'strength'
    back_attack_targetable = True
    back_elements = ['fire']
    back_num_attacks = 2
    back_hit = 'one'

class Giant(Character):
    base_hp = 89
    base_strength = 54
    base_agility = 40
    base_intelligence = 30
    base_luck = 44
    base_cost = 200
    image = "giant.gif"
    growth_hp = 7
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 60

    resistances = {
        'physical': 48,
        'black': 40,
        'white': 40,
        'fire': 42,
        'cold': 37,
        'lightning': 41
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Titan(Character):
    base_hp = 85
    base_strength = 62
    base_agility = 45
    base_intelligence = 40
    base_luck = 41
    base_cost = 920
    image = "titan.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 190

    resistances = {
        'physical': 54,
        'black': 15,
        'white': 80,
        'fire': 47,
        'cold': 39,
        'lightning': 52
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'all'

class IceGiant(Character):
    base_hp = 84
    base_strength = 57
    base_agility = 37
    base_intelligence = 37
    base_luck = 48
    base_cost = 750
    image = "ice_giant.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 2
    growth_cost = 130

    resistances = {
        'physical': 52,
        'black': 35,
        'white': 60,
        'fire': 15,
        'cold': 80,
        'lightning': 54
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['cold']
    back_attack_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class FireGiant(Character):
    base_hp = 75
    base_strength = 59
    base_agility = 49
    base_intelligence = 36
    base_luck = 47
    base_cost = 630
    image = "fire_giant.gif"
    growth_hp = 8
    growth_strength = 4
    growth_agility = 3
    growth_intelligence = 2
    growth_cost = 110

    resistances = {
        'physical': 57,
        'black': 54,
        'white': 32,
        'fire': 80,
        'cold': 15,
        'lightning': 37
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['fire']
    back_attack_targetable = True
    back_num_attacks = 2
    back_hit = 'one'

class Hellhound(Character):
    base_hp = 87
    base_strength = 51
    base_agility = 59
    base_intelligence = 32
    base_luck = 51
    base_cost = 100
    image = "samurai.gif" #TODO
    growth_hp = 6
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 30

    resistances = {
        'physical': 46,
        'black': 58,
        'white': 22,
        'fire': 49,
        'cold': 40,
        'lightning': 37
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['fire']
    back_num_attacks = 2
    back_attack_targetable = True
    back_hit = 'one'

class Cerberus(Character):
    base_hp = 83
    base_strength = 56
    base_agility = 62
    base_intelligence = 48
    base_luck = 53
    base_cost = 570
    image = "samurai_master.gif" #TODO
    growth_hp = 7
    growth_strength = 4
    growth_agility = 4
    growth_intelligence = 4
    growth_cost = 100

    resistances = {
        'physical': 51,
        'black': 65,
        'white': 15,
        'fire': 52,
        'cold': 40,
        'lightning': 36
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength' #TODO charm
    back_elements = ['fire']
    back_num_attacks = 2
    back_attack_targetable = True
    back_hit = 'one'

class Octopus(Character):
    base_hp = 78
    base_strength = 51
    base_agility = 38
    base_intelligence = 47
    base_luck = 50
    base_cost = 300
    image = "octopus.gif"
    growth_hp = 9
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 50

    resistances = {
        'physical': 64,
        'black': 50,
        'white': 50,
        'fire': 54,
        'cold': 53,
        'lightning': 20
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 4
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class Kraken(Character):
    base_hp = 86
    base_strength = 57
    base_agility = 47
    base_intelligence = 50
    base_luck = 50
    base_cost = 700
    image = "kraken.gif"
    growth_hp = 10
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 110

    resistances = {
        'physical': 67,
        'black': 43,
        'white': 57,
        'fire': 59,
        'cold': 58,
        'lightning': 17
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 4
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'all' #TODO non-water attack

class Golem(Character):
    base_hp = 45
    base_strength = 56
    base_agility = 31
    base_intelligence = 30
    base_luck = 39
    base_cost = 100
    image = "ravenman.gif" #TODO golem gif
    growth_hp = 2
    growth_strength = 4
    growth_agility = 1
    growth_intelligence = 2
    growth_cost = 20

    resistances = {
        'physical': 69,
        'black': 55,
        'white': 43,
        'fire': 38,
        'cold': 63,
        'lightning': 61
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class RockGolem(Character):
    base_hp = 53
    base_strength = 60
    base_agility = 32
    base_intelligence = 30
    base_luck = 40
    base_cost = 600
    image = "ravenman.gif" #TODO golem gif
    growth_hp = 2
    growth_strength = 4
    growth_agility = 1
    growth_intelligence = 2
    growth_cost = 70

    resistances = {
        'physical': 73,
        'black': 53,
        'white': 47,
        'fire': 74,
        'cold': 67,
        'lightning': 63
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'

class IronGolem(Character):
    base_hp = 67
    base_strength = 63
    base_agility = 33
    base_intelligence = 30
    base_luck = 45
    base_cost = 1700
    image = "ravenman.gif" #TODO golem gif
    growth_hp = 2
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 180

    resistances = {
        'physical': 82,
        'black': 63,
        'white': 90,
        'fire': 41,
        'cold': 81,
        'lightning': 72
        }

    front_attack_type = 'strength'
    front_elements = ['physical']
    front_num_attacks = 3
    front_hit = 'one'
    back_attack_type = 'strength'
    back_elements = ['physical']
    back_num_attacks = 2
    back_hit = 'one'
