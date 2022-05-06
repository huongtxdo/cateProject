from dog import Dog

"""
Dog Bosses' attacks are not random
Dog Bosses' attacks always ignore shield
"""

class GreatDane(Dog):
    #Danny
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []
    
class GoldenRetriver(Dog):
    #Goldie
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []

class Samoyed(Dog):
    #Sammie
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []

class Bulldog(Dog):
    #Bulbul
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []
        
class Pomeranian(Dog):
    #Pompom
    """
    Pomeranian ignores cats' defense
    Pomeranian first attacks cat that can heal
    if there's no healer, Pomeranian attacks cat with lowest HP
    """
    def __init__(self, name):
        super().__init__(name)
        self.xp = 75
        self.maxhp = 350
        self.droppedItems = []
        self.attackPoint = 20
        self.ability_type = ["boss"]

    def attack(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if "heal" in cat.get_ability_type():
                    target = cat
                    break
        if target:
            target.lose_hp(self.attackPoint)
        else:
            for cat in cat_list:
                if cat.is_alive():
                    if target == None:
                        target = cat
                    elif cat.get_hp() < target.get_hp():
                        target = cat
            target.lose_hp(self.attackPoint)

class Chihuahua(Dog):
    #Qiqi
    """
    Chihuahua deals 10% of the max hp of every cat every round
    Then Chihuahua attacks cat that can heal
    If there's no healer, Chihuahua attacks cat with lowest HP 
    """
    def __init__(self, name):
        super().__init__(name)
        self.xp = 95
        self.maxhp = 500
        self.hp = self.maxhp
        self.attackPoint = 20
        self.attack = 10
        self.ability_type = ["boss"]
        self.droppedItems = ["Key to the Cate kindom"]
    
    def attack(self, cat_list):
        for cat in cat_list:
            if cat.is_alive():
                amount = cat.get_maxhp()/20
                cat.lose_hp(amount)
        if not self.attackHealer(cat_list):
            self.attackLowerHP(cat_list)