from cat import Cat
from catMain import CatMain
from catFellow1 import *
from item import Item

def main():
    cat_main = CatMain("")
    rocky = BritishShorthair("Rocky", cat_main)
    stoney = ScottishFold("Stoney", cat_main)
    print(cat_main.get_hp())

main()
 