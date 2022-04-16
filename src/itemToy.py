from re import M


class Toy():

    """
    Toys are only usedd by catMain, toys are like weapons
    """

    toys_description = {
        "laser": "A fun toy can be deadly too, blind your enemies or distract them with the laser toy!",
        "feather wand": "Nothing beats the classics, wave this in front of your enemies to confuse them!",
        "robotic wand": "",
        "cuddly pillow": "",
        "moving stuffed fish": "",
        "stuffed mouse": "",
        "ball tower": "",
    }

    toys_attackPoint = {
        "laser": "2",
        "feather wand": "3"
    }

    def __init__(self, name):
        self.name = name
        self.set_description(name)
        self.attackPoint = 0

# functions for getting information

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_attackPoint(self):
        return self.attackPoint

# functions for setting information

    def set_description(self, name):
        if name in self.toys_description.keys():
            self.description = self.toys_description[name]
        else:
            raise ValueError("Invalid toy's name")
