from item import Item

class Drink(Item):

    """
    Drink is used to regenerate mp
    """

    item_description = {
        "water": "Don't forget to leave your cats clean water everyday",
        "milk": "Should be lactofree",
        "holy water": "As much as a sinner themselves, cats can use some holy water as well!",
        "holy milk": "Deluxe edition of holy water! Cats wash away their sins. Enjoyably!"
    }

    item_value = {
        "water": 1,
        "milk": 2,
        "holy water": 3,
        "holy milk": 4
    }

    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[name]
        # self.value = self.item_value[name]

