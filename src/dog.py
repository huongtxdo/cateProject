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

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.hp = self.maxmp
        self.mp = self.maxmp