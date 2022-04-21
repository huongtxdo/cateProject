from cat import Cat 

"""
catFellow is the cat characters that player can recruit
"""

class catFellow(Cat):

    abilities = {
        
    }

    cat_abilities_cooldown = {
        "Rocky": ()
    }

    cat_HpMpMpcost = {

    }

    def __init__(self, name):
        super().__init__(name)
