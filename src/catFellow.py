import random
import datetime
import math
from cat import Cat 
from catMain import CatMain
from catAbility import CatAbility

"""
catFellow is the cat characters that player can recruit
1: British Shorthair
2: Scottish Fold
"""

class CatFellow(Cat):

# catFellow's HP is randomed
    def __init__(self, name, catMain):
        super().__init__(name)
        self.set_maxhp()
        self.level = catMain.get_level()
        self.defense = 1.1 * catMain.get_defense()/1.3
        #self.set_ability()
        self.hp = self.maxhp

# functions for setting
    def set_maxhp(self):
        if not self.maxhp:
            lowerHP = 15
            upperHP = 18
        else:
            lowerHP = self.maxhp + 9
            upperHP = self.maxhp + 11
        seedling = int(datetime.datetime.utcnow().timestamp())
        random.seed(seedling)
        self.maxhp = random.randint(lowerHP, upperHP)
        # if not self.hp:
        #     self.hp = self.maxhp  

    # def set_ability(self):
    #     if self.name in self.cat_abilities.keys():
    #         abilityName = CatAbility.cat_abilities[self.name]
    #         self.ability = CatAbility(abilityName)
    #     else: 
    #         raise ValueError("Cannot find ability of this cat's name")

# functions for losing MP by effect:
    def lose_MP(self, value):
        temp = self.mp - value
        self.mp = max(temp, 0)

#functions for using abilities:
    def use_ability(self, target):
        # abilityMP = CatAbility.abilitiesMP[self.ability]
        # if self.mp < abilityMP:
        #     raise ValueError("{} doesn't have enough mana to use their ability.".format(self.name))
        # else:
        #     pass
        pass