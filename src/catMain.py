import math
from cat import Cat
from item import Item
from catAbility import CatAbility

"""
catMain is the player's avatar
"""

class CatMain(Cat):

    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.xp = 0
        self.maxhp = 18
        self.hp = self.maxhp
        self.coin = 0
        self.weapon = None
        self.attack = 1
        self.allies = []

# fucntions for getting

    def get_attack(self):
        return self.attack
    
    def get_weapon(self):
        return self.weapon

    def get_coin(self):
        return self.coin

    def get_xp(self):
        return self.xp

# other functions

    def level_up(self):
        self.level += 1
        self.maxhp += 10
        self.hp = self.maxhp
        self.attack += 1.6
        self.defense += 1.3
        self.xp -= 100
        for ally in self.allies:
            ally.level += 1
    
    def add_coin(self, value):
        self.coin +=  value

    def add_xp(self, value):
        self.xp += value 

    def equip(self, toy):
        """
        only for catMain, equipped toys increase attack
        """
        self.attack += toy.get()
        self.weapon = toy

# function to recruit allies
    def recruit(self, ally):
        self.allies.append(ally)
