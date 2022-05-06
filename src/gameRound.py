import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QObject
import sys

class Round():

    def __init__(self, cat_list, dog_list):
        self.round_end = True
        self.turn = 0
        self.cat_list = cat_list
        self.dog_list = dog_list

    def end(self):
        return self.round_end

    def to_battle(self):
        # should activate when "To battle!" is clicked
        self.round_end = False

    def new_turn(self):
        self.turn += 1

    def change_round_status(self, cat_list, dog_list):
        cat_alive = [ cat.is_alive() for cat in cat_list ]
        dog_alive = [ dog.is_alive() for dog in dog_list ]
        if cat_alive.count(True) == 0 and dog_alive.count(True) != 0:
            self.round_end = True
            print("Fear not! This was just one of your nine lives.")
        elif cat_alive.count(True) != 0 and dog_alive.count(True) == 0:
            self.round_end = True
            print("Meow! Cate kingdom! Here I come!")
        elif cat_alive.count(True) == 0 and dog_alive.count(True) == 0:
            self.round_end = True
            print("A draw is a preparation step for a victory.")
    
    def set_first_player(self, player_choice):
        result = random.choice(["head", "tail"])
        if player_choice == result:
            self.cat_first = True

    def determine_turn_list(self, cat_list, dog_list):
        cat_alive = []
        dog_alive = []
        for cat in cat_list:
            if cat.is_alive():
                cat_alive.append(cat)
        for dog in dog_list:
            if dog.is_alive():
                dog_alive.append(dog)
        num = min(len(cat_alive), len(dog_alive))
        turn_list = [None]*(num*2) 
        turn_list[::2] = cat_alive[:num]
        turn_list[1::2] = dog_alive[:num]
        turn_list.extend(cat_alive[num:])
        turn_list.extend(dog_alive[num:])

        for animal in turn_list:
            if "main" in animal.get_ability_type():
                for dog in dog_alive:
                    app = QApplication(sys.argv)
                    button = QPushButton(dog.get_name())
                    button.pressed.connect(animal.attack(dog))                                                                                         
                    sys.exit(app.exec_())
                    break
            elif "heal" in cat.get_ability_type():
                cat.use_ability(cat_list)