from item import Item

class Toy(Item):

    """
    Toys are only used by catMain, toys are like weapons
    """

    item_description = {
        "laser": "A fun toy can be deadly too, blind your enemies or distract them with the laser toy!",
        "feather wand": "Nothing beats the classics, wave this in front of your enemies to confuse them!",
        "robotic wand": "",
        "cuddly pillow": "",
        "moving stuffed fish": "",
        "stuffed mouse": "",
        "ball tower": "",
    }

    item_value = {
        "laser": 2,
        "feather wand": 3,
        "robotic wand": 3.5,
        "cuddly pillow": 4,
        "moving stuffed fish": 5,
        "stuffed mouse": 6,
        "ball tower": 10,
    }

    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[self.name]
        # self.value = self.item_value[self.name]


