import random
from cat import Cat 

"""
catFellow is the cat characters that player can recruit
1: British Shorthair
2: Scottish Fold
"""

class CatFellow(Cat):

# catFellow's HP is randomed
    def __init__(self, name, catMain):
        super().__init__(name)
        self.maxhp = random.randint(15,18)
        self.level = catMain.get_level()
        self.defense = 1.1 * catMain.get_defense()/1.3
        self.hp = self.maxhp
        self.maxmp = 10
        self.mp = self.maxmp
        catMain.recruit(self)

# functions for setting
    def level_up(self):
        self.level += 1
        lowerHP = self.maxhp + 9
        upperHP = self.maxhp + 11
        self.maxhp = random.randint(lowerHP, upperHP) 
        self.hp = self.maxhp
        self.maxmp += 5
        self.mp = self.maxmp

    def get_ability_type(self):
        return self.ability_type

# functions for losing MP by effect:
    def lose_MP(self, value):
        temp = self.mp - value
        self.mp = max(temp, 0)

#functions for using abilities:
    def use_ability(self, target):
        pass