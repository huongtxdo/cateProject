class Cat():

    def __init__(self, name):
        self.set_name(name)
        self.maxhp = 0
        self.maxmp = 0
        self.set_defense
        self.attack = 0
        self.dead = False

# all the methods that return information
    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_defense(self):
        return self.defense

# methods to set name, maxhp and maxmp  
    def set_name(self, name):
        if not name:
            self.name = "MeowLead"   
        else:
            self.name = name

    def set_maxhp(self):
        pass

    def set_maxmp(self, value):
        self.maxmp = value
        if not self.mp:
            self.mp = self.maxmp

    def set_defense(self):
        pass
   

# methods to use items
    def eat(self, food):
        """
        heal the cat
        """
        temp = self.hp + food.get_hp()
        self.hp = min(temp, self.maxhp)

    def drink(self, drink):
        """
        regenerate cat's mana
        """
        temp = self.mp + drink.get_mp()
        self.mp = min(temp, self.maxmp)

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.hp = self.maxmp
        self.mp = self.maxmp

# methods for losing hp, mp,...
    def lose_HP(self, value):
        if self.hp > value:
            self.hp = self.hp - value
        else:
            self.hp = 0
            self.dead = True
    

