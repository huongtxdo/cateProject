from item import Item

class Toy(Item):
    """
    Toys are only used by catMain, toys are like weapons
    """
    toy_list = []
    with open('1toy.txt') as f:
        lines = f.readlines()
        for line in lines:
            attribute_list = line.split("/")
            toy_list.append(attribute_list)
    toy_list_name = [toy[0] for toy in toy_list]

    def __init__(self, name):
        super().__init__(name)
        self.value = int(self.toy_list[self.toy_list_name.index(name)][1])
        self.description = self.toy_list[self.toy_list_name.index(name)][2]
        self.price = int(self.toy_list[self.toy_list_name.index(name)][3])
