import random

class Dog():
 
    def __init__(self, name):
        self.name = name
        self.defense = 0
        self.attackPoint = 0
        self.alive = True

# all the methods that return information
    def get_name(self): 
        return self.name

    def get_maxhp(self):
        return self.maxhp

    def get_maxmp(self):
        return self.maxmp

    def get_hp(self):
        return self.hp

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

# attack random

    def attackRandom(self, cat_list):
        alive_cat_list = []
        for cat in cat_list:
            if cat.is_alive():
                alive_cat_list.append(cat)
        target_index = random.randint(0, len(alive_cat_list)-1)
        target = alive_cat_list[target_index]
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)

# methods for losing hp, mp,...
    def lose_hp(self, value):
        if self.hp > value:
            self.hp = round(self.hp - value, 1)
        else:
            self.hp = 0
            self.alive = False
    
    def increase_hp(self, value):
        temp = self.hp + value
        self.hp = min(round(temp, 1), self.maxhp)

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.hp = self.maxmp
        self.mp = self.maxmp