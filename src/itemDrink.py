from item import Item

class Drink(Item):

    """
    Drink is used to regenerate mp
    """
    item_description = {
        "water": "Don't forget to leave your cats clean water everyday",
        "milk": "Should be lactofree"
    }

    item_value = {
        "water": 1,
        "milk": 2
    }

    def __init__(self, name):
        self.name = name
        self.set_mp()

# functions for getting

    def get_mp(self):
        return self.mp

    def get_description():
        return self.description

# functions for setting
    def set_mp(self, name):
        if name in self.item_value.keys():
            self.mp = self.item_value[name]
        else:
            raise ValueError("Invalid drink's name")

    def set_description(self, name):
        if name in self.item_description.keys():
            self.descrpiption = self.item_description[name]
        else:
            raise ValueError("Invalid drink's name")