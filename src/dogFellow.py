from dog import Dog
import random
import datetime

class DogFellow1(Dog):

    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        alive_cat_list = []
        for cat in cat_list:
            if cat.is_alive():
                alive_cat_list.append(cat)
        seedling = int(datetime.datetime.utcnow().timestamp())
        random.seed(seedling)
        target_index = random.randint(0, len(alive_cat_list)-1)
        alive_cat_list[target_index].lose_hp(self.attackPoint)

class DogFellow2(Dog):
    
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
        target.lose_hp(self.attackPoint)
        
class DogFellow3(Dog):

    def __init__(self, name, attackPoint):
        super().__init__(name)
        self.attackPoint = attackPoint

    def attack(self, cat_list):
        pass