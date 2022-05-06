from PyQt5 import QtWidgets, QtCore
from uiGraphicsItem import *
from uiCoordinates import *
from uiBattle import *


class GuiBattle(QtWidgets.QMainWindow):
    
    def __init__(self, battle, square_size):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.battle = battle
        self.square_size = square_size
        self.init_window()
        self.init_buttons()
        self.coor = []
        self.container = []
        self.added_animals = []

        self.add_battle_grid_items()
        self.add_animal_graphics_items()
        self.updaet_animals()

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updaet_animals)
        self.timer.start(10) # Milliseconds


    def add_battle_grid_items(self):
        animal_height = self.battle.get_height()
        animal_width = self.battle.get_width()
        l_grey = QtGui.QColor(211, 211, 211)
        d_grey = QtGui.QColor(20, 20, 20)
        for i in range(animal_width):
            for j in range(animal_height):
                coor = Coordinates(i,j)
                if coor not in self.coor and self.battle.contains(coor):
                    size = QtWidgets.QGraphicsRectItem(i*self.square_size, j*self.square_size, self.square_size, self.square_size)
                    is_wall = self.battle.get_square(coor).is_wall_square()
                    if is_wall: 
                        size.setBrush(d_grey)
                    else: 
                        size.setBrush(l_grey)
                    self.scene.addItem(size)
                    self.coor.append(coor)


    def get_animal_graphics_items(self):
        """
        Returns all the GraphicsItem in the scene.

        NOTE: This is a silly implementation, it would be much more efficient to store
        all animalGraphicsItems in a list and simply return that list.
        """
        items = []
        for item in self.scene.items():
            if type(item) is GraphicsItem:
                items.append(item)
        return items


    def add_animal_graphics_items(self):
        temp = self.battle.get_animals()
        for animal in temp:
            if animal not in self.added_animals:
                item = GraphicsItem(animal, self.square_size)
                self.scene.addItem(item)
                self.added_animals.append(animal)


    def init_buttons(self):
        """
        Adds buttons to the window and connects them to their respective functions
        See: QPushButton at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html
        """
        self.next_turn_btn = QtWidgets.QPushButton("attack")
        self.next_turn_btn.clicked.connect(self.battle.next_full_turn)
        self.horizontal.addWidget(self.next_turn_btn)


    def updaet_animals(self):
        """
        Iterates over all animal items and updates their position to match
        their physical representations in the animal world.
        """
        for animal_item in self.get_animal_graphics_items():
            animal_item.updateAll()


    def init_window(self):
        """
        Sets up the window.
        """
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Title')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
