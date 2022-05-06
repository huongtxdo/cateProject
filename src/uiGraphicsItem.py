from PyQt5 import QtWidgets, QtGui, QtCore

class GraphicsItem(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, animal, square_size):
        # Call init of the parent object
        super(GraphicsItem, self).__init__()

        # Do other stuff
        self.animal = animal
        self.world = self.animal.get_world()
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
        self.updatePosition()
        self.updateColor()


    def updatePosition(self):
        animal_location = self.animal.get_location()
        x_coor = animal_location.get_x()
        y_coor = animal_location.get_y()
        self.setPos(x_coor*self.square_size, y_coor*self.square_size)

    def updateColor(self):
        dodger_blue = QtGui.QColor(30,144,255)
        deep_sky_blue = QtGui.QColor(0,191,255)
        crimson_red = QtGui.QColor(220,20,60)
        tomato_red = QtGui.QColor(255,99,71)
        if "main" in self.animal.get_ability_type():
            self.setBrush(dodger_blue)
        elif "boss" in self.animal.get_ability_type():
            self.setBrush(crimson_red)
        elif "dog" in self.animal.get_ability_type():
            self.setBrush(tomato_red)
        else:
            self.setBrush(deep_sky_blue)


    def mousePressEvent(self, *args, **kwargs):
        if not self.world.subject:
            self.world.subject = self.animal
        else:
            self.world.subject.attack(self.animal)
        self.world.subject = None

        # if "main" in self.animal.get_ability_type():
        #     target = mousePressEvent()
        #     self.animal.attack(target)
        # # elif "boss" in self.animal.get_ability_type():
        # #     self.setBrush(crimson_red)
        # # elif "dog" in self.animal.get_ability_type():
        # #     self.setBrush(tomato_red)
        # # else:
        # #     self.setBrush(deep_sky_blue)
