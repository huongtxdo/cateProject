import random

class CatAbility():

    abilitiesMP = {
        "Act cute": 1, #dog loses 
        "Act coy": 1, #
        "Blind": 1, #
        "Bite": 2, #inflict damage to dog
        "Ignore": 2, #
        "Purr": 1,
        "Skeme": 2,
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

        


