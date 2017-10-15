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
    attack_type = 'melee'

class Knight(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "knight.gif"
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
    attack_type = 'melee'

class Paladin(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "paladin.gif"
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
    attack_type = 'melee'

class BeastTamer(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "beast_tamer.gif"
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
    attack_type = 'melee'

class BeastMaster(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "beast_master.gif"
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
    attack_type = 'melee'

class Samurai(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "samurai.gif"
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
    attack_type = 'melee'

class SamuraiMaster(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "samurai_master.gif"
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
    attack_type = 'melee'

class Ninja(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "ninja.gif"
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
    attack_type = 'melee'

class NinjaMaster(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "ninja_master.gif"
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
    attack_type = 'melee'

class WildMan(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "wild_man.gif"
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
    attack_type = 'melee'

class EvilOne(Character):
    base_hp = 77
    base_strength = 45
    base_agility = 47
    base_intelligence = 40
    base_luck = 45
    base_cost = 100
    image = "evil_one.gif"
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
    attack_type = 'magical'

class Mage(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "mage.gif"
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
    attack_type = 'magical'

class Sorcerer(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "sorcerer.gif"
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
    attack_type = 'magical'

class DollMage(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "doll_mage.gif"
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
    attack_type = 'magical'
    
class DollMaster(Character):
    base_hp = 86
    base_strength = 37
    base_agility = 51
    base_intelligence = 45
    base_cost = 400
    base_luck = 50
    image = "doll_master.gif"
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
    attack_type = 'magical'
