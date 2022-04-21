from cat import Cat
from item import Item

"""
catMain is the player's avatar
"""

class CatMain(Cat):

    def __init__(self, name, level):
        super().__init__(name)
        self.attack = 0
        self.cateCoin = 0
        self.weapon = None
        self.set_maxhp(level)
        
    def set_maxhp(self):
        self.maxhp = self.level * 10 + 8
        if not self.hp:
            self.hp = self.maxhp

    def set_atk_value(self, level):
        self.attack = level * 1.5
 
    def equip(self, toy):
        """
        only for catMain, equipped toys increase attack
        """
        self.attack += toy.get_attackPoint()
        self.wearpon = toy
