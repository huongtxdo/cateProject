class Food():

    """
    Food is used to regenerate hp
    """

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp