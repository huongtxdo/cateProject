from cat import Cat
from catMain import CatMain
from catFellowType import *
from item import *
from itemDrink import *
from itemFood import *
from itemToy import *

def main():
    cat_main = CatMain("")
    rocky = BritishShorthair("Rocky", cat_main)
    cat_main.recruit(rocky)
    scottie = ScottishFold("Scottie", cat_main)
    cat_main.recruit(scottie)
    cat_main.add_coin(100)
    cat_main.add_xp(101)
    cat_main.level_up()

    print(rocky.get_level())


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
 