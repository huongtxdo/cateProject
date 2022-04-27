import random

class CatAbility():

    abilitiesMP = {
        "Act cute": 1, #all dogs lose the will to fight, 
        "Act coy": 1, #this cat will always 
        "Blind": 1, #all dogs become blind, have 50% chance to miss the attack
        "Bite": 2, #inflict damage to dog
        "Ignore": 2, #
        "Purr": 1,
        "Scheme": 2,
    }

    cat_abilities = {
        "Britt the British Shorthair": "Act coy",
        "Scotty the Scottish Fold": "Act cute",
        "Sia the Siamese": "Skeme",
        "Manny the Maine Coon": "",
        "Benny the Bengal": "",
    }

    def __init__(self, name):
        self.name = name
        self.set_manaCost()

    def set_manaCost(self):
        if self.name in self.abilitiesMP.keys():
            self.manaCost = self.abilitiesMP[self.name]
        else:
            raise ValueError("Invalid ability's name")

        


