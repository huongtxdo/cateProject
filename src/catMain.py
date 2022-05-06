from cat import Cat

"""
catMain is the player's avatar
"""

class CatMain(Cat):

    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.xp = 0
        self.maxhp = 18
        self.hp = self.maxhp
        self.coin = 0
        self.weapon = None
        self.damage = 1
        self.defense = 1
        self.allies = []
        self.ability_type = ["main"]

# fucntions for getting

    def get_damage(self):
        return self.damage
    
    def get_weapon(self):
        return self.weapon

    def get_coin(self):
        return self.coin

    def get_xp(self):
        return self.xp

    def get_allies(self):
        return self.allies

# other functions

    def level_up(self):
        self.level += 1
        self.maxhp += 10
        self.hp = self.maxhp
        self.damage += 1.6
        self.defense += 1.3
        self.xp -= 100
        for ally in self.allies:
            ally.level_up()
    
    def add_coin(self, value):
        self.coin += value

    def add_xp(self, value):
        self.xp += value 

    def equip(self, toy):
        """
        only for catMain, equipped toys increase damage
        """
        self.damage += toy.get()
        self.weapon = toy

    def attack(self, target):
        amount = max(self.damage - target.get_defense(), 0)
        target.lose_hp(amount)

    def use(self, gadget, cat):
        """
        only for catMain, use gadgets with various effects
        """
        gadget.effect(cat)

# function to recruit allies
    def recruit(self, ally):
        self.allies.append(ally)
