import random

class Round():

    def __init__(self, cat_list, dog_list):
        self.round_end = False
        self.turn = 0
        self.cat_list = cat_list
        self.dog_list = dog_list
        self.cat_first = False

    def get_round_end(self):
        return self.round_end

    def new_turn(self):
        self.turn += 1

    def change_round_status(self, cat_list, dog_list):
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
    
    def set_first_player(self, player_choice):
        result = random.choice(["head", "tail"])
        if player_choice == result:
            self.cat_first = True

    def turn(self, cat_list, dog_list):
        cat_alive = [ cat.is_alive() for cat in cat_list ]
        dog_alive = [ dog.is_alive() for dog in dog_list ]
        turn_list = []
        num = min(len(cat_alive), len(dog_alive))
        turn_list = [None]*(num*2) 
        if self.cat_first:
            turn_list[::2] = cat_alive[:num]
            turn_list[1::2] = dog_alive[:num]
            turn_list.extend(cat_alive[num:])
            turn_list.extend(dog_alive[num:])
        else:
            turn_list[::2] = dog_alive[:num]
            turn_list[1::2] = cat_alive[:num]
            turn_list.extend(dog_alive[num:])
            turn_list.extend(cat_alive[num:])