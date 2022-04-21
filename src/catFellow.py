import random
import datetime
from cat import Cat 

"""
catFellow is the cat characters that player can recruit
"""

class CatFellow(Cat):

    abilitiesMP = {
        "Act cute": 1,
        "Act coy": 1,
        "Blind": 1,
        "Bite": 2,
        "Ignore": 2,
        "Purr": 1,
        "Skeme": 2,
    }

    cat_abilities = {
        "Britt the British Shorthair": "Act coy",
        "Scotty the Scottish Fold": "Act cute",
        "Sia the Siamese": "Skeme",
        "Manny the Maine Coon": "",
        "Benny the Bengal": "",
    }

# seed for randomizer

# catFellow's HP is randomed

    def __init__(self, name, level):
        super().__init__(name)
        self.set_maxhp(level)
        self.set_ability

# functions for setting

    def set_maxhp(self):
        lowerHP = self.level * 10 - 3
        upperHP = self.level * 10 + 3
        seedling = int(datetime.datetime.utcnow().timestamp())
        random.seed(seedling)
        self.maxhp = random.randint(lowerHP, upperHP)
        if not self.hp:
            self.hp = self.maxhp

    def set_ability(self):
        if self.name in self.cat_abilities.keys():
            self.ability = self.cat_abilities[self.name]
        else: 
            raise ValueError("Invalid cat's name")

# functions for losing MP by effect:
    def lose_MP(self, value):
        temp = self.mp - value
        self.mp = max(temp, 0)

#functions for using abilities:
    def use_ability(self):
        abilityMP = self.abilitiesMP[self.ability]
        if self.mp < abilityMP:
            raise ValueError("{} doesn't have enough mana to use their ability.".format(self.name))
        else:
            


    
        