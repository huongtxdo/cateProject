class Square():
    """
    The class Square represents a single square in a animal world.
    A square can contain either a wall or a animal or it can be empty.
    """

    def __init__(self, is_wall=False):
        """
        Creates a new square. Initially there is no robot in the square.

        Parameter is_wall_square is a boolean value stating whether there is a wall in the square or not: boolean
        """
        self.animal = None     # most-recent holder (None if no animal in square)
        self.is_wall = is_wall  # flag (one-way currently, since walls can not be removed)


    def get_animal(self):
        """
        Returns the animal in the square or None if there is no animal in the square: animal
        """
        return self.animal


    def is_wall_square(self):
        """
        Returns a boolean value stating whether there is a wall in the square or not: boolean
        """
        return self.is_wall


    def is_empty(self):
        """
        Returns a boolean value stating whether the square is empty (A square is empty if it does not contain a wall or a animal) or not: boolean
        """
        return not self.is_wall_square() and self.animal is None


    def set_animal(self, animal):
        """
        Marks the square as containing a animal, if possible.
        If the square was not empty, the method fails to do anything.

        Parameter animal is the animal to be placed in this square: animal

        Returns a boolean value indicating if the operation succeeded: boolean
        """
        if self.is_empty():
            self.animal = animal
            return True
        else:
            return False


    def remove_animal(self):
        """
        Removes the animal in this square.

        Returns the animal removed from the square or None, if there was no animal: animal
        """
        removed_animal = self.get_animal()
        self.animal = None
        return removed_animal


    def set_wall(self):
        """
        Sets a wall in this square, if possible.
        If the square was not empty, the method fails to do anything.

        Returns a boolean value indicating if the operation succeeded: boolean
        """
        if self.is_empty():
            self.is_wall = True
            return True
        else:
            return False
