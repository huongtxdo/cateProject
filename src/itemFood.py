from item import Item

class Food(Item):
    """
    Food is used to regenerate hp
    """
    def __init__(self, name):
        super().__init__(name)