from item import Item

class Food(Item):

    """
    Food is used to regenerate hp
    """

    item_description = {
        "Brat": "Despite its name, it serves its purpose",
        "Perfect Fat": "",
        "Coshiba": ""
    }

    item_value = {
        "Brat": 5,
        "Perfect Fat": 6,
        "Coshiba": 7
    }

    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[name]
        # self.value = self.item_value[name]