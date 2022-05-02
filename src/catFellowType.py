from catFellow import CatFellow
from catAbility import CatAbility
from catMain import *

"""
catFellow1: British Shorthair
"""

class BritishShorthair(CatFellow):
    """
    British Shorthair deals a certain damage to 1 dog
    """
    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, dog):
        print("British Shorthair uses ability")
        dog.lose_hp(5)
        return super().use_ability(dog)

class ScottishFold(CatFellow):
    """
    Scottish Fold heals every cat
    """
    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, cat_list):
        print("Scottish Fold uses ability")
        for cat in cat_list:
            cat.increase_hp(5)
        return super().use_ability(cat_list)