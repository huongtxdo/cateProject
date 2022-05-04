class Game():
    
    def __init__(self):
        self.game_over = False
        self.round = 0

    def game_end(self):
        
    
    def new_round(self):
        self.round += 1

    def check_game_over(self, cat_list, dog_list):
        cat_alive = [ cat.is_alive() for cat in cat_list ]
        dog_alive = [ dog.is_alive() for dog in dog_list ]
        if cat_alive.count(True) == 0 and dog_alive.count(True) != 0:
            self.game_over = True
            print("The Doge kingdom wins")
        elif cat_alive.count(True) != 0 and dog_alive.count(True) == 0:
            self.game_over = True
            print("Victory to the Cate kingdom!")
        elif cat_alive.count(True) == 0 and dog_alive.count(True) == 0:
            self.game_over = True
            print("Hmmm, it's a draw!")