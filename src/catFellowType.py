import random
from catFellow import CatFellow
from catMain import *

"""
catFellow1: British Shorthair
"""

class BritishShorthair(CatFellow):
    """"
    Regenerate a certain amount of HP to all allies
    """
    def __init__(self, name, catMain):
        super().__init__(name, catMain)
        self.hp_regen = self.level * 3 + random.randint(self.level, 2*self.level)

    def use_ability(self, cat_list):
        print("British Shorthair uses ability")
        for cat in cat_list:
            if cat.is_alive():
                cat.increase_hp(self.hp_regen)
        return super().use_ability(cat_list)

class ScottishFold(CatFellow):
    """'
    deal a certain amount of damage to an enemy    
    """
    def __init__(self, name, catMain):
        super().__init__(name, catMain)
        self.damage = self.get_level() * 5 + random.randint(self.level, 3*self.level)

    def use_ability(self, enemy):
        print("Scottish Fold uses ability")
        enemy.lose_hp(self.damage)
        return super().use_ability(enemy)
