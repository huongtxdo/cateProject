class Gadget():

    def __init__(self):
        self.stock = 1

# functions for getting
    def get_stock(self):
        return self.stock

    def increase_stock(self):
        self.stock += 1

    def decrease_stock(self):
        self.stock = max(0, self.stock - 1)

class Catnip(Gadget):
    """
    Catnip revives 1 cat and heals 25% of that cat's max hp
    """
    def __init__(self):
        super().__init__()
    
    def effect(self, cat):
        amount = cat.get_maxhp()/4
        cat.revive()
        cat.increase_hp(amount)

class Blanket(Gadget):
    """
    The cat with blanket will always be the target of dogFellows.
    Double the cat's defense
    """
    def __init__(self):
        super().__init__()

    def effect(self, cat):
        cat.add_ability_type("shield")
        cat.defense = 2 * cat.defense
