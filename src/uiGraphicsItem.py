from PyQt5 import QtWidgets, QtGui, QtCore

class GraphicsItem(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, animal, square_size):
        # Call init of the parent object
        super(GraphicsItem, self).__init__()

        # Do other stuff
        self.animal = animal
        self.square_size = square_size
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.constructTriangleVertices()
        self.updateAll()

    
    def constructTriangleVertices(self):
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip
        triangle.append(QtCore.QPointF(0, self.square_size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.square_size, self.square_size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)


    def updateAll(self):
        """
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent animal.
        """
        self.updatePosition()
        self.updateColor()


    def updatePosition(self):
        """
        Implement me!

        Update the coordinates of this item to match the attached animal.
        Remember to take in to account the size of the squares.

        A animal in the first (0, 0) square should be drawn at (0, 0).

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsPolygonItem.html
        and its parent class QGraphicsItem at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsItem.html

        For getting the location of the parent animal, look at the animal-class
        in animal.py.
        """
        animal_location = self.animal.get_location()
        x_coor = animal_location.get_x()
        y_coor = animal_location.get_y()
        self.setPos(x_coor*self.square_size, y_coor*self.square_size)

    def updateColor(self):
        """
        Implement me!

        Draw broken animals in red, stuck animals in yellow and working animals in green.

        The rgb values of the colors must be the following:
        - red: (255, 0, 0)
        - yellow: (255, 255, 0)
        - green: (0, 255, 0)

        See: setBrush() at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QAbstractGraphicsShapeItem.html
        and QBrush at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QBrush.html
        and QColor at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html

        Look at animal.py for checking the status of the animal.
        Friends are blue, enemies are red
        """
        dodger_blue = QtGui.QColor(30,144,255)
        deep_sky_blue = QtGui.QColor(0,191,255)
        crimson_red = QtGui.QColor(220,20,60)
        tomato_red = QtGui.QColor(255,99,71)
        if "main" in self.robot.get_ability_type():
            self.setBrush(dodger_blue)
        elif "boss" in self.robot.get_ability_type():
            self.setBrush(crimson_red)
        elif "dog" in self.robot.get_ability_type():
            self.setBrush(tomato_red)
        else:
            self.setBrush(deep_sky_blue)


    def mousePressEvent(self, *args, **kwargs):
        """
        Implement me!

        If the clicked animal is broken, fix it.
        This function is called everytime this object is clicked on the scene.

        Hint: You don't need to do anything with the *args or **kwargs. One line solution should be sufficient.
        """
        if self.animal.is_broken(): 
            self.animal.fix()
