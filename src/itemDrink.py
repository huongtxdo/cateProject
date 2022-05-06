from item import Item

class Drink(Item):
    """
    Drink is used to regenerate mp
    """
    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[name]
        # self.value = self.item_value[name]

