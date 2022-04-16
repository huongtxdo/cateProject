class Food():

    """
    Food is used to regenerate hp
    """

    food_description = {
        "royal k9": "Despite its name, it serves its purpose"
    }

    food_hp = {
        "royal k9": 5
    }

    def __init__(self, name):
        self.name = name
        self.set_hp(name)

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp
    
    def get_description(self):
        return self.description

    def set_hp(self, name):
        if name in self.food_hp.keys():
            self.hp = self.food_hp[name]
        else:
            raise ValueError("Invalid food's name")

    def set_description(self, name):
        if name in self.food_description.keys():
            self.description = self.food_description[name]
        else:
            raise ValueError("Invalid food's name")