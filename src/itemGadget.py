from item import Item

class Gadget(Item):

    def __init__(self, name):
        super().__init__(name)

class Catnip(Gadget):

    def __init__(self, name):
        super().__init__(name)
    
    def effect(self, cat):
        amount = cat.get_maxhp()/4
        cat.increase_hp(amount)
        cat.revive()

