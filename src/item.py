class Item():

    def __init__(self, name):
        self.name = name
        self.stock = 0

# functions for getting

    def get_name(self):
        return self.name 

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get(self):
        return self.value

    def get_stock(self):
        return self.get_stock

# functions for setting

    def increase_stock(self):
        self.stock += 1

    def decrease_stock(self):
        self.stock = max(0, self.stock - 1)

                

