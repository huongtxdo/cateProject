from numpy import append
from catMain import CatMain
from catFellowType import *
from dogBoss import *
from dogFellow import *
from item import *
from itemDrink import *
from itemFood import *
from itemToy import *
from itemGadget import *

from game import *
from gameRound import *

import sys
from PyQt5.QtWidgets import QApplication
from uiGuiBattle import *
from uiGuiWindows import *
from uiBattle import *
from uiCoordinates import *

def main():

    current_game = Game()
    while not current_game.end():
        # Player can check their troops, inventory, and go shopping
        appMain = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        
        current_game.new_round()

        # below is collected from Prepare for battle tab
        cat_main = CatMain("")
        brittie = BritishShorthair("Brittie", cat_main)
        scottie = ScottishFold("Scottie", cat_main)
        cat_main.add_coin(100)
        cat_main.add_xp(100)
        cat_main.level_up()

        qiqi = Chihuahua("Qiqi")
        dog1 = DogFellow1("Dog 1", 10)
        dog2 = DogFellow2("Dog 2", 8)

        cat_list = [cat_main, brittie, scottie]
        dog_list = [qiqi, dog1, dog2]

        current_round = Round(cat_list, dog_list)
        current_round.to_battle()
        while not current_round.end():
            test_battle = Battle()
            test_battle.add_animal(cat_main,Coordinates(2,3))
            test_battle.add_animal(brittie,Coordinates(1,1))
            test_battle.add_animal(scottie,Coordinates(1,5))

            test_battle.add_animal(qiqi,Coordinates(6,3))
            test_battle.add_animal(dog1,Coordinates(7,1))
            test_battle.add_animal(dog2,Coordinates(7,5))

            turn_list = current_round.determine_turn_list(cat_list, dog_list)
            

            global app
            app = QApplication(sys.argv)
            gui = GuiBattle(test_battle, 50)
            sys.exit(app.exec_())
        current_game.check_game_over(cat_list, dog_list)
        appMain.exec()

main()