from item import Item

class Food(Item):
    """
    Food is used to regenerate hp
    """
    food_list = []
    with open('1food.txt') as f:
        lines = f.readlines()
        for line in lines:
            attribute_list = line.split("/")
            food_list.append(attribute_list)
    food_list_name = [food[0] for food in food_list]

    def __init__(self, name):
        super().__init__(name)
        self.value = int(self.food_list[self.food_list_name.index(name)][1])
        self.description = self.food_list[self.food_list_name.index(name)][2]
        self.price = int(self.food_list[self.food_list_name.index(name)][3])
