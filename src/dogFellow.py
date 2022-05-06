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

    def use_ability(self, cat_list):
        if not self.attackShield(cat_list):
            self.attackRandom(cat_list)

class DogFellow2(Dog):
    """
    Dog2 attacks cat with the lowest hp
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def use_ability(self, cat_list):
        if not self.attackShield(cat_list):
            self.attackLowerHP(cat_list)
        
class DogFellow3(Dog):
    """
    Dog3 attacks cat with the highest hp
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def use_ability(self, cat_list):
        if not self.attackShield(cat_list):
            self.attackHighestHP(cat_list)

class DogFellow4(Dog):
    """
    Dog4 attacks cat that can heal. 
    If there is none, Dog4 attacks randomly
    """
    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def use_ability(self, cat_list):
        if not self.attackShield(cat_list):
            if not self.attackHealer(cat_list):
                self.attackRandom(cat_list)


