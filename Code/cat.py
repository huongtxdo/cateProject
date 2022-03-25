from itemDrink import Drink
from itemFood import Food


class Cat():

    def __init__(self, name):
        self.set_name(name)
        self.description = ""
        self.maxhp = 0
        self.hp = 0
        self.maxmp = 0
        self.mp = 0
        self.defense = 0

# all the methods that return information
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_def(self):
        return self.defense

# methods to set name, maxhp and maxmp  
    def set_name(self, name):
        if not name:
            self.name = "MeowLead"   
        else:
            self.name = name

    def set_maxhp(self, value):
        self.maxhp = value

    def set_maxmp(self, value):
        self.maxmp = value

# methods to use items
    def eat(self, food):
        """
        heal the cat
        """
        temp = self.hp + food.get_hp()
        if temp < self.maxhp:
            self.hp = temp
        else:
            self.hp = self.maxhp

    def drink(self, drink):
        """
        regenerate cat's mana
        """
        temp = self.mp + drink.get_mp()
        if temp < self.maxmp:
            self.mp = temp
        else:
            self.mp = self.maxmp

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.hp = self.maxmp
        self.mp = self.maxmp

    

