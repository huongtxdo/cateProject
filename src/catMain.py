from cat import Cat

"""
catMain is the player's avatar
"""

class mainCat(Cat):

    def __init__(self, name):
        super().__init__(name)
        self.attack = 0
        self.cateCoin = 0
        self.weapon = ""
        

    def set_atk_value(self, value):
        self.attack = value