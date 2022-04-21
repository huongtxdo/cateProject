class Item():

    def __init__(self, name):
        self.set_name(name)
        self.description

# functions for getting

    def get_name(self):
        return self.name 

    def get_description(self):
        return self.description

    def get(self):
        return self.value

# functions for setting

    def set_name(self, name):
        if name:
            self.name = name
        else:
            raise ValueError("Item's name cannot be empty")

    def set_description(self, name):
        if name in self.item_description:
            self.description = self.item_description[name]
        else: 
            raise ValueError("Invalid name")
