import random

class Dog():
 
    def __init__(self, name):
        self.name = name
        self.defense = 0
        self.attackPoint = 0
        self.alive = True
        self.world = None 
        self.location = None
        self.ability_type = ["dog"]

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

    def get_location(self):
        return self.location
    
    def get_ability_type(self):
        return self.ability_type

    def is_alive(self):
        return self.alive

# attack type

    def attackRandom(self, cat_list):
        alive_cat_list = []
        for cat in cat_list:
            if cat.is_alive():
                alive_cat_list.append(cat)
        target_index = random.randint(0, len(alive_cat_list)-1)
        target = alive_cat_list[target_index]
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)

    def attackLowerHP(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if target == None:
                    target = cat
                elif cat.get_hp() < target.get_hp():
                    target = cat
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)

    def attackHighestHP(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if target == None:
                    target = cat
                elif cat.get_hp() > target.get_hp():
                    target = cat
        amount = max(self.attackPoint - target.get_defense(), 0)
        target.lose_hp(amount)
    
    def attackHealer(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if "heal" in cat.get_ability_type():
                    target = cat
                    break
        if target:
            amount = max(self.attackPoint - target.get_defense(), 0)
            target.lose_hp(amount)
            return True
    
    def attackShield(self, cat_list):
        target = None
        for cat in cat_list:
            if cat.is_alive():
                if "shield" in cat.get_ability_type():
                    target = cat
                    break
        if target:
            amount = max(self.attackPoint - target.get_defense(), 0)
            target.lose_hp(amount)
            return True

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

# GUI related

    def get_world(self):
        return self.world
    
    def set_world(self, world, location):
        target_square = world.get_square(location)
        if not target_square.is_empty() or self.get_world() is not None:
            return False
        else:
            self.world = world
            self.location = location
            return True