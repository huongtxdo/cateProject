from catMain import CatMain
from catFellowType import *
from dogBoss import *
from dogFellow import *
from item import *
from itemDrink import *
from itemFood import *
from itemToy import *

def main():
    cat_main = CatMain("")
    brittie = BritishShorthair("Brittie", cat_main)
    scottie = ScottishFold("Scottie", cat_main)
    
    cat_main.add_coin(100)
    cat_main.add_xp(101)
    cat_main.level_up()
    scottie.lose_hp(30)
    cat_list = [cat_main, brittie, scottie]
    boss = DogFellow2("Qiqi", 5)
    print(cat_main.get_hp(), brittie.get_hp(), scottie.get_hp())
    boss.attack(cat_list)
    print(cat_main.get_hp(), brittie.get_hp(), scottie.get_hp())


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
 