from catFellow import CatFellow
from catAbility import CatAbility

"""
catFellow1: British Shorthair
"""

class BritishShorthair(CatFellow):

    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, target):
        print("British Shorthair usability")
        return super().use_ability(target)

class ScottishFold(CatFellow):

    def __init__(self, name, catMain):
        super().__init__(name, catMain)

    def use_ability(self, target):
        print("Scottish Fold uses ability")
        return super().use_ability(target)