import unittest

from cat import Cat
from catFellow import CatFellow
from catFellowType import BritishShorthair, ScottishFold
from itemFood import Food


class Test(unittest.TestCase):

    def test_empty_name(self):
        britishShorthair = Cat("")
        self.assertEqual("MeowLead" ,britishShorthair.get_name(),  "Wrong name")

    # def test_eat_food(self):
    #     test_cat = Cat("test")
    #     test_cat.set_maxhp(10)
    #     test_cat.get_hit(2)
    #     test_food = Food("royal k9")
    #     test_cat.eat(test_food)
    #     self.assertEqual(10, test_cat.get_hp(), "HP cannot be more than the maximum")

    # def test_cat_dead(self):
    #     test_cat = Cat("test")
    #     test_cat.set_maxhp(10) 
    #     test_cat.get_hit(11)
    #     self.assertTrue(test_cat.dead, "Cat should be dead")

    def test_cat_ability(self):
        test_cat_main = Cat("test")
        test_cat_british_shorthair = ScottishFold("Rocky", test_cat_main)
        test_cat_british_shorthair.use_ability(test_cat_british_shorthair)
        self.assertEqual(0,0)
        


if __name__ == "__main__":
    unittest.main()