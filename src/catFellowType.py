from catFellow import CatFellow
from catAbility import CatAbility
from catMain import *

"""
catFellow1: British Shorthair
"""

class BritishShorthair(CatFellow):

    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, ally):
        print("British Shorthair uses ability")
        print(ally.get_hp())
        ally.lose_hp(5)
        print(ally.get_hp())
        return super().use_ability(ally)

class ScottishFold(CatFellow):

    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, target):
        print("Scottish Fold uses ability")
        return super().use_ability(target)