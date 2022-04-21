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
        self.attack = 0
        self.cateCoin = 0
        self.weapon = None
        self.set_level
        self.xp = 0
        self.set_maxhp()
        self.set_defense

#functions for getting
    def get_level(self):
        return self.level

#functions for setting
    def set_maxhp(self):
        if not self.maxhp:
            self.maxhp = 18
        else:
            self.maxhp += 10
        if not self.hp:
            self.hp = self.maxhp

    def set_atk_value(self, level):
        self.attack = level * 1.6

    def set_defense(self):
        self.defense = self.level * 1.3

    def set_level(self):
        self.level = 1 + math.floor(self.xp/100)

# other functions
    def equip(self, toy):
        """
        only for catMain, equipped toys increase attack
        """
        self.attack += toy.get_attackPoint()
        self.wearpon = toy
