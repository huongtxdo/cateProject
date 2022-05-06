import random 

class Cat():

    def __init__(self, name):
        self.set_name(name)
        self.damage = 0
        self.alive = True 
        self.world = None 
        self.location = None
        self.enemies = []
        self.allies = [self]

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

    def get_ability_type(self):
        return self.ability_type
    
    def get_damage(self):
        return self.damage

    def get_location(self):
        return self.location

    def get_enemies(self):
        return self.enemies

    def get_allies(self):
        return self.allies

    def is_alive(self):
        return self.alive

# methods to set name, maxhp and maxmp  
    def set_name(self, name):
        if not name:
            self.name = "MeowLead"   
        else:
            self.name = name

    def add_ally(self, cat):
        self.allies.append(cat)

    def add_enemy(self, dog):
        self.enemies.append(dog)

    def add_ability_type(self, ability):
        if ability not in self.ability_type:
            self.ability_type.append(ability)

    def remove_ability_type(self, ability):
        if ability in self.ability_type:
            self.ability_type.remove(ability)

# methods to use items
    def eat(self, food):
        """
        heal the cat
        """
        if self.is_alive() and food.get_stock() > 0:
            temp = self.hp + food.get()
            self.hp = min(temp, self.maxhp)
            food.decrease_stock()

    def drink(self, drink):
        """
        regenerate cat's mana
        """
        if self.is_alive() and drink.get_stock() > 0:
            temp = self.mp + drink.get()
            self.mp = min(temp, self.maxmp)
            drink.decrease_stock()

    def regenerate(self):
        """
        Return the cat to the original state
        """
        self.revive() 
        self.hp = self.maxhp
        self.mp = self.maxmp

    def revive(self):
        self.alive = True

    def die(self):
        self.alive = False
        self.hp = 0
        self.mp = 0

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