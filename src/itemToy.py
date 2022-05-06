from item import Item

class Toy(Item):
    """
    Toys are only used by catMain, toys are like weapons
    """
    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[self.name]
        # self.value = self.item_value[self.name]


