class Cat():

    def __init__(self, name):
        self.set_name(name)
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

    def get_mp(self):
        return self.mp

    def get_defense(self):
        return self.defense

    def get_level(self):
        return self.level

    def is_alive(self):
        return self.alive

# methods to set name, maxhp and maxmp  
    def set_name(self, name):
        if not name:
            self.name = "MeowLead"   
        else:
            self.name = name

# methods to use items
    def eat(self, food):
        """
        heal the cat
        """
        temp = self.hp + food.get()
        self.hp = min(temp, self.maxhp)

    def drink(self, drink):
        """
        regenerate cat's mana
        """
        temp = self.mp + drink.get()
        self.mp = min(temp, self.maxmp)

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.hp = self.maxhp
        self.mp = self.maxmp
        self.revive()

    def revive(self):
        self.alive = True

    def die(self):
        self.alive = False
        self.hp = 0
        self.mp = 0

# methods for losing hp, mp,...
    def lose_hp(self, value):
        if self.hp > value:
            self.hp = self.hp - value
        else:
            self.hp = 0
            self.alive = False
    
    def increase_hp(self, value):
        temp = self.hp + value
        self.hp = min(temp, self.maxhp)

    def get_hit(self, value):
        amount = max(value - self.defense, 0) 
        