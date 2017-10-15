from classes.character import Character

class Fighter(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "fighter.gif"
    growth_hp = 5
    growth_strength = 2
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 20

    resistances = {
        'physical': 44,
        'black': 40,
        'white': 40,
        'fire': 36,
        'cold': 30,
        'lightning': 44
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class Knight(Character):
    base_hp = 76
    base_strength = 49
    base_agility = 52
    base_intelligence = 44
    base_cost = 600
    base_luck = 50
    image = "knight.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 90

    resistances = {
        'physical': 47,
        'black': 34,
        'white': 46,
        'fire': 39,
        'cold': 43,
        'lightning': 37
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class Paladin(Character):
    base_hp = 67
    base_strength = 56
    base_agility = 56
    base_intelligence = 45
    base_cost = 1100
    base_luck = 60
    image = "paladin.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 170

    resistances = {
        'physical': 53,
        'black': 26,
        'white': 54,
        'fire': 41,
        'cold': 46,
        'lightning': 40
        }

    num_attacks = 3
    hit = 'one'
    attack_type = 'melee'

class BeastTamer(Character):
    base_hp = 85
    base_strength = 51
    base_agility = 47
    base_intelligence = 38
    base_luck = 43
    base_cost = 350
    image = "beast_tamer.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 50

    resistances = {
        'physical': 44,
        'black': 46,
        'white': 34,
        'fire': 28,
        'cold': 31,
        'lightning': 35
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class BeastMaster(Character):
    base_hp = 79
    base_strength = 53
    base_agility = 49
    base_intelligence = 36
    base_luck = 46
    base_cost = 850
    image = "beast_master.gif"
    growth_hp = 5
    growth_strength = 4
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 130

    resistances = {
        'physical': 48,
        'black': 55,
        'white': 25,
        'fire': 27,
        'cold': 35,
        'lightning': 39
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class Samurai(Character):
    base_hp = 85
    base_strength = 50
    base_agility = 54
    base_intelligence = 21
    base_cost = 700
    base_luck = 47
    image = "samurai.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 100

    resistances = {
        'physical': 46,
        'black': 39,
        'white': 51,
        'fire': 32,
        'cold': 37,
        'lightning': 34
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class SamuraiMaster(Character):
    base_hp = 96
    base_strength = 55
    base_agility = 59
    base_intelligence = 54
    base_cost = 1200
    base_luck = 54
    image = "samurai_master.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 180

    resistances = {
        'physical': 52,
        'black': 21,
        'white': 69,
        'fire': 34,
        'cold': 35,
        'lightning': 37
        }

    num_attacks = 3
    hit = 'one'
    attack_type = 'melee'

class Ninja(Character):
    base_hp = 76
    base_strength = 46
    base_agility = 50
    base_intelligence = 50
    base_cost = 500
    base_luck = 48
    image = "ninja.gif"
    growth_hp = 4
    growth_strength = 3
    growth_agility = 3
    growth_intelligence = 2
    growth_cost = 110

    resistances = {
        'physical': 45,
        'black': 43,
        'white': 37,
        'fire': 50,
        'cold': 44,
        'lightning': 43
        }

    num_attacks = 3
    hit = 'one'
    attack_type = 'melee'

class NinjaMaster(Character):
    base_hp = 77
    base_strength = 51
    base_agility = 52
    base_intelligence = 55
    base_cost = 1300
    base_luck = 56
    image = "ninja_master.gif"
    growth_hp = 5
    growth_strength = 3
    growth_agility = 4
    growth_intelligence = 3
    growth_cost = 190

    resistances = {
        'physical': 47,
        'black': 68,
        'white': 2,
        'fire': 52,
        'cold': 46,
        'lightning': 45
        }

    num_attacks = 3
    hit = 'one'
    attack_type = 'melee'

class WildMan(Character):
    base_hp = 71
    base_strength = 52
    base_agility = 53
    base_intelligence = 41
    base_luck = 54
    base_cost = 400
    image = "wild_man.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 1
    growth_cost = 50

    resistances = {
        'physical': 48,
        'black': 46,
        'white': 34,
        'fire': 43,
        'cold': 38,
        'lightning': 36
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class EvilOne(Character):
    base_hp = 74
    base_strength = 58
    base_agility = 57
    base_intelligence = 42
    base_luck = 62
    base_cost = 900
    image = "evil_one.gif"
    growth_hp = 6
    growth_strength = 3
    growth_agility = 2
    growth_intelligence = 2
    growth_cost = 130

    resistances = {
        'physical': 54,
        'black': 55,
        'white': 25,
        'fire': 46,
        'cold': 40,
        'lightning': 39
        }

    num_attacks = 2
    hit = 'one'
    attack_type = 'melee'

class Wizard(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "wizard.gif"
    growth_hp = 2
    growth_strength = 1
    growth_agility = 1
    growth_intelligence = 4
    growth_cost = 70

    resistances = {
        'physical': 20,
        'black': 45,
        'white': 35,
        'fire': 32,
        'cold': 32,
        'lightning': 37
        }

    attacking_elements = ['physical', 'black', 'fire', 'cold', 'lightning']
    num_attacks = 2
    hit = 'one'
    attack_type = 'magical'

class Mage(Character):
    base_hp = 81
    base_strength = 38
    base_agility = 49
    base_intelligence = 45
    base_cost = 800
    base_luck = 48
    image = "mage.gif"
    growth_hp = 2
    growth_strength = 1
    growth_agility = 1
    growth_intelligence = 4
    growth_cost = 150

    resistances = {
        'physical': 24,
        'black': 51,
        'white': 29,
        'fire': 34,
        'cold': 35,
        'lightning': 38
        }

    attacking_elements = ['physical', 'black', 'fire', 'cold', 'lightning']
    num_attacks = 1
    hit = 'all'
    attack_type = 'magical'

class Sorcerer(Character):
    base_hp = 37
    base_strength = 39
    base_agility = 47
    base_intelligence = 55
    base_cost = 1200
    base_luck = 45
    image = "sorcerer.gif"
    growth_hp = 3
    growth_strength = 1
    growth_agility = 1
    growth_intelligence = 4
    growth_cost = 180

    resistances = {
        'physical': 28,
        'black': 59,
        'white': 21,
        'fire': 36,
        'cold': 38,
        'lightning': 39
        }

    attacking_elements = ['physical', 'black', 'fire', 'cold', 'lightning']
    num_attacks = 2
    hit = 'all'
    attack_type = 'magical'

class DollMage(Character):
    base_hp = 78
    base_strength = 40
    base_agility = 54
    base_intelligence = 53
    base_cost = 1280
    base_luck = 47
    image = "doll_mage.gif"
    growth_hp = 3
    growth_strength = 1
    growth_agility = 2
    growth_intelligence = 3
    growth_cost = 160

    resistances = {
        'physical': 28,
        'black': 37,
        'white': 43,
        'fire': 44,
        'cold': 39,
        'lightning': 27
        }

    attacking_elements = ['physical']
    num_attacks = 1
    hit = 'all'
    attack_type = 'magical'

class DollMaster(Character):
    base_hp = 78
    base_strength = 38
    base_agility = 57
    base_intelligence = 57
    base_cost = 1280
    base_luck = 42
    image = "doll_master.gif"
    growth_hp = 3
    growth_strength = 1
    growth_agility = 3
    growth_intelligence = 3
    growth_cost = 190

    resistances = {
        'physical': 21,
        'black': 21,
        'white': 59,
        'fire': 47,
        'cold': 41,
        'lightning': 29
        }

    attacking_elements = ['physical']
    num_attacks = 2
    hit = 'all'
    attack_type = 'magical'
