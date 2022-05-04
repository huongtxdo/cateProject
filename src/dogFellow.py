from dog import Dog
import random
import datetime

class DogFellow1(Dog):
    """
    Dog1 attacks randomly
    """
    def __init__(self, name, attackPoint): 
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        self.attackRandom(cat_list)

class DogFellow2(Dog):
    """
    Dog2 attacks cat with the lowest hp
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if target == None:
                    target = cat
                elif cat.get_hp() < target.get_hp():
                    target = cat
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)
        
class DogFellow3(Dog):
    """
    Dog3 attacks cat with the highest hp
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if target == None:
                    target = cat
                elif cat.get_hp() > target.get_hp():
                    target = cat
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)

class DogFellow4(Dog):
    """
    Dog4 attacks cat that can heal. 
    If there is none, Dog4 attacks randomly
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if "heal" in cat.get_ability_type():
                    target = cat
        if target == None:
            self.attackRandom(cat_list)
        else:
            amount = max(self.attackPoint - target.get_defense(), 0)
            target.lose_hp(amount)


