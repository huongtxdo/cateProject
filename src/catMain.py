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
        self.cateCoin = 0
        self.weapon = None
        self.attack = 1

#functions for setting
    def set_maxhp(self):
        if not self.maxhp:
            self.maxhp = 18
        else:
            self.maxhp += 10
        self.hp = self.maxhp

    def level_up(self):
        self.level += 1
        self.maxhp += 10
        self.hp = self.maxhp
        self.attack += 2

    def set_atk_value(self, level):
        self.attack = level * 1.6

    def set_defense(self):
        self.defense = self.level * 1.3

    def increase_level(self):
        if self.xp >= 100:
            self.level += math.floor(self.xp/100)

# other functions
    def equip(self, toy):
        """
        only for catMain, equipped toys increase attack
        """
        self.attack += toy.get_attackPoint()
        self.wearpon = toy
