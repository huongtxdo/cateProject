from dog import Dog

"""
Dog Bosses' attacks are not random
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
    #Bubu
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []
        
class Pomeranian(Dog):
    #Pompom
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []

class Chihuahua(Dog):
    #Qiqi
    def __init__(self, name):
        super().__init__(name)
        self.xp = 0
        self.maxhp = 0
        self.droppedItems = []
    
    def attack(self, cat_list):
        for cat in cat_list:
            if cat.is_alive():
                amount = cat.get_maxhp()/10
                cat.lose_hp(amount)
        