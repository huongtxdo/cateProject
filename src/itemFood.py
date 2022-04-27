from item import Item

class Food(Item):

    """
    Food is used to regenerate hp
    """

    item_description = {
        "royal k9": "Despite its name, it serves its purpose"
    }

    item_value = {
        "royal k9": 5
    }

    def __init__(self, name):
        super().__init__(name)
        # self.description = self.item_description[name]
        # self.value = self.item_value[name]