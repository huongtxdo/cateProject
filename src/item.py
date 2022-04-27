class Item():

    def __init__(self, name):
        self.name = name
        self.description = self.item_description[name]
        self.value = self.item_value[name]

# functions for getting

    def get_name(self):
        return self.name 

    def get_description(self):
        return self.description

    def get(self):
        return self.value
