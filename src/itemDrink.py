from operator import indexOf
from item import Item

class Drink(Item):
    """
    Drink is used to regenerate mp
    """    
    drink_list = []
    with open('1drink.txt') as f:
        lines = f.readlines()
        for line in lines:
            attribute_list = line.split("/")
            drink_list.append(attribute_list)
    drink_list_name = [drink[0] for drink in drink_list]

    def __init__(self, name):
        super().__init__(name)
        self.value = int(self.drink_list[self.drink_list_name.index(name)][1])
        self.description = self.drink_list[self.drink_list_name.index(name)][2]
        self.price = int(self.drink_list[self.drink_list_name.index(name)][3])

