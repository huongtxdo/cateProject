from cat import Cat
from item import Item

"""
catMain is the player's avatar
"""

class mainCat(Cat):

    def __init__(self, name):
        super().__init__(name)
        self.attack = 0
        self.cateCoin = 0
        self.weapon = None
        

    def set_atk_value(self, value):
        self.attack = value
 
    def equip(self, toy):
        """
        only for catMain, equipped toys increase attack
        """
        self.attack = toy.get_attackPoint()