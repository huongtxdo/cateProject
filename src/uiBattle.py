from uiSquare import Square


class Battle():
    """
    The class RobotWorld describes a two dimensional world made up
    of squares that different kinds of robots can inhabit. The squares are
    identified by unique coordinates which range from 0...width-1 and
    0...height-1. Each square is represented by a Square object.

    Robots can be added to the robot world, and the robot world
    maintains a robot listing which allows robots to take their turns in
    a round-robin fashion, in the order in which they were added.
    Each robot is represented by a Robot object.

    See the documentation Robot, Square, Coordinates
    """

    def __init__ (self):
        """
        Creates a new robot world with the specified dimensions.
        Initially all the squares of the new world are empty.

        Parameter width is the width of the world in squares: int

        Parameter height is the height of the world in squares: int
        """
        self.squares = [None] * 9
        for x in range(self.get_width()):      # stepper
            self.squares[x] = [None] * 9
            for y in range(self.get_height()):    # stepper
                self.squares[x][y] = Square()    # fixed value
        self.animals = []                        # container
        self.turn = 0                         # kinda like stepper (but not quite) index to animals list
        self.subject = None
        self.object = None

    def get_width(self):
        """
        Returns width of the world in squares: int
        """
        return len(self.squares)


    def get_height(self):
        """
        Returns the height of the world in squares: int
        """
        return len(self.squares[0])


    def add_animal(self, animal, location):
        if animal.set_world(self, location):
            self.animals.append(animal)
            self.get_square(location).set_animal(animal)
            return True
        else:
            return False


    def add_wall(self, location):
        """
        Adds a wall at the given location in the animal world, if
        possible. If the square is not empty, the method fails to
        do anything.

        Parameter location is the location of the wall: Coordinates

        Returns a boolean value indicating if the operation succeeded: boolean
        """
        return self.get_square(location).set_wall()


    def get_square(self, coordinates):
        """
        Parameter coordinates is a location in the world: Coordinates

        Returns the square that is located at the given location. If the given coordinates point outside of the world,
        this method returns a square that contains a wall and is not located in any animal world: Square
        """
        if self.contains(coordinates):
            return self.squares[coordinates.get_x()][coordinates.get_y()]
        else:
            return Square(True)
 

    def get_number_of_animals(self):
        """
        Returns the number of animals added to this world: int
        """
        return len(self.animals)


    def get_animal(self, turn_number):
        """
        Returns the animal which has the given "turn number".
        The turn numbers of the animals in a world are determined by
        the order in which they were added. I.e., the first animal has
        a turn number of 0, the second one's number is 1, etc.

        Parameter turn_number is the turn number of a animal. Must be on the interval [0, (number of animals minus 1)].: int

        Returns the animal with the given turn number: animal object
        """
        if 0 <= turn_number < self.get_number_of_animals():
            return self.animals[turn_number]
        else:
            return None


    def get_next_animal(self):
        """
        Returns the animal to act next in this world's round-robin turn system, or None if there aren't any animals in the world: animal

        See next_animal_turn()
        """
        if self.get_number_of_animals() < 1:
            return None
        else:
            return self.animals[self.turn]


    def next_animal_turn(self):
        """
        Lets the next animal take its turn. That is, calls the
        take_turn method of the animal whose turn it is,
        and passes the turn to the next animal. The turn is passed
        to the animal with the next highest turn number (i.e. the one
        that was added to the world after the current animal), or wraps
        back to the first animal (turn number 0) if the last turn number
        was reached. That is to say: the animal which was added first,
        moves first, followed by the one that was added second, etc.,
        until all animals have moved and the cycle starts over.
        If there are no animals in the world, the method does nothing.

        See get_next_animal()
        """
        current = self.get_next_animal()
        if current is not None:
            self.turn = (self.turn + 1) % self.get_number_of_animals()
            current.take_turn()


    def next_full_turn(self):
        """
        Lets each animal take its next turn. That is, calls the next_animal_turn
        a number of times equal to the number of animals in the world.
        """
        for count in range(self.get_number_of_animals()):      # stepper
            self.next_animal_turn()


    def contains(self, coordinates):
        """
        Determines if this world contains the given coordinates.

        Parameter coordinates is a coordinate pair: Coordinates

        Returns a boolean value indicating if this world contains the given coordinates: boolean
        """
        x_coordinate = coordinates.get_x()
        y_coordinate = coordinates.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()


    def get_animals(self):
        """
        Returns an array containing all the animals currently located in this world: list
        """
        return self.animals[:]
