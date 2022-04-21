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
        self.name = name
        self.set_description()
        self.set_hp(name)

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp
    
    def get_description(self):
        return self.description

    def set_hp(self, name):
        if name in self.item_value.keys():
            self.hp = self.item_value[name]
        else:
            raise ValueError("Invalid food's name")

    def set_description(self, name):
        if name in self.item_description.keys():
            self.description = self.item_description[name]
        else:
            raise ValueError("Invalid food's name")