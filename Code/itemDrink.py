class Drink():

    """
    Drink is used to regenerate mp
    """

    def __init__(self, name, mp):
        self.name = name
        self.mp = mp

    def get_mp(self):
        return self.mp