class Round():

    def __init__(self, cat_list, dog_list):
        self.round_end = False
        self.turn = 0
        self.cat_list = []
        self.dog_list = []

    def new_turn(self):
        self.turn += 1

    def check_round_end(self, cat_list, dog_list):
        cat_alive = [ cat.is_alive() for cat in cat_list ]
        dog_alive = [ dog.is_alive() for dog in dog_list ]
        if cat_alive.count(True) == 0 and dog_alive.count(True) != 0:
            self.round_end = True
            print("Meow, what a tragedy! Your cats have lost all of their life")
        elif cat_alive.count(True) != 0 and dog_alive.count(True) == 0:
            self.round_end = True
            print("Meow, we actually did it!")
        elif cat_alive.count(True) == 0 and dog_alive.count(True) == 0:
            self.round_end = True
            print("Hmmm, it's a draw!")
    
    def turn(self, me, you):
        