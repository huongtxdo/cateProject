from catMain import CatMain
from catFellowType import *
from dogBoss import *
from dogFellow import *
from item import *
from itemDrink import *
from itemFood import *
from itemToy import *
from itemGadget import *

def main():
    cat_main = CatMain("")
    brittie = BritishShorthair("Brittie", cat_main)
    scottie = ScottishFold("Scottie", cat_main)

    qiqi = Chihuahua("Qiqi")
    dog1 = DogFellow1("Dog 1", 10)
    dog2 = DogFellow2("Dog 2", 8)
    
    cat_main.add_coin(100)
    cat_main.add_xp(100)
    cat_main.level_up()
    cat_list = [cat_main, brittie, scottie]
    dog_list = [qiqi, dog1, dog2]
    





    # game_over = False
    # while not game_over:
    #     turn_list = [cat_main, rocky, scottie]
    #     # selected_cat = mouse_click_event(on that cat)
    #     # selected_cat attack
    #     # action = mouse_click_event()
    #     mouse_click_event()
    
    #     turn_over = False
    #     while not turn_over:
    #         #if end_turn_button pressed, turn_over = True


main()
 