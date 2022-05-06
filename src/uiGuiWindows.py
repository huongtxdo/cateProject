"""
only used for testing functions, syntax
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from uiGraphicsItem import *

class Color(QtWidgets.QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        self.setPalette(palette)
        
class Image(QtWidgets.QWidget):
    def __init__(self, image):
        super(Image, self).__init__()
        self.setAutoFillBackground(True)
        label = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap(image)
        label.setPixmap(self.pixmap)
        label.resize(self.pixmap.width(), self.pixmap.height())

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.z = None
        self.setCentralWidget(QtWidgets.QWidget())
        self.setWindowTitle("Make a merry Cate great again!")
        self.setGeometry(0, 0, 702, 550)
        self.cat_container = []
        self.item_container = []
        self.initUI()

    def add_cat(self, cat):
        self.cat_container.append(cat)
    
    def initUI(self):        
    # Overall        
        pagelayout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()
        self.stacklayout = QtWidgets.QStackedLayout()
        button_layout2 = QtWidgets.QHBoxLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(button_layout2)

    # Button Troops
        button = QtWidgets.QPushButton("Troops")
        button.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Troop())

    # Button Inventory
        button = QtWidgets.QPushButton("Inventory")
        button.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Color("white"))

    # Button Shop
        button = QtWidgets.QPushButton("Shop")
        button.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Shop())

    # Button preparation
        button = QtWidgets.QPushButton("Prepare for battle")
        button.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Color("white"))

    #Button to battle
        button = QtWidgets.QPushButton("To battle!")
        button.clicked.connect(self.show_battle_window)
        button_layout2.addWidget(button)
        self.setCentralWidget(button)

        # Add widget with the previous defined page layout~
        # to the central widget
        widget = QtWidgets.QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)

    def show_troop_window(self):
        if not self.z:
            self.z = Troop()
            self.z.show()
        else:
            self.z.close()
            self.z = None
    
    def show_battle_window(self, checked):
        if not self.w:
            self.w = BattleWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None

class BattleWindow(QtWidgets.QWidget):
     def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Fight!")
        self.setGeometry(0, 0, 702, 550)
        self.label = QtWidgets.QLabel("Battle window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class Troop(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        
        self.button1 = QtWidgets.QPushButton('Cate coin: 0', self)
        self.button1.setIcon(QtGui.QIcon("0catMain.png"))
        self.button1.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button1, 0,0)

        self.button2 = QtWidgets.QPushButton('Cate coin: 50', self)
        self.button2.setIcon(QtGui.QIcon("0brittie.png"))
        self.button2.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button2, 0,1)

        self.button3 = QtWidgets.QPushButton('Cate coin: 70', self)
        self.button3.setIcon(QtGui.QIcon("0scottie.png"))
        self.button3.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button3, 0,2)

        self.button4 = QtWidgets.QPushButton('Cate coin: 80', self)
        self.button4.setIcon(QtGui.QIcon("0bennie.png"))
        self.button4.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button4, 1,0)

        self.button5 = QtWidgets.QPushButton('Cate coin: 100', self)
        self.button5.setIcon(QtGui.QIcon("0sphinie.png"))
        self.button5.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button5, 1,1)

        self.button6 = QtWidgets.QPushButton('Cate coin: 110', self)
        self.button6.setIcon(QtGui.QIcon("0mannie.png"))
        self.button6.setIconSize(QtCore.QSize(200,200))
        self.layout.addWidget(self.button6, 1,2)

        self.setLayout(self.layout)
    
class Shop(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
    #add food to shop
        with open('1food.txt') as f:
            lines = f.readlines()
            temp=0
            for line in lines:
                name, value, description, price = line.split("/")
                self.button = QtWidgets.QPushButton("{} - {} hp: Cate coin {}".format(name, value, price), self)
                self.layout.addWidget(self.button, 0 ,temp)
                temp+=1
    #add drink to shop
        with open('1drink.txt') as f:
            lines = f.readlines()
            temp=0
            for line in lines:
                name, value, description, price = line.split("/")
                self.button = QtWidgets.QPushButton("{} - {} mp: Cate coin {}".format(name, value, price), self)
                self.layout.addWidget(self.button, 1,temp)
                temp+=1
    #add toy to shop
        with open('1toy.txt') as f:
            lines = f.readlines()
            temp=0
            for line in lines:
                name, value, description, price = line.split("/")
                self.button = QtWidgets.QPushButton("{} - {} mp: Cate coin {}".format(name, value, price), self)
                self.layout.addWidget(self.button, 2,temp)
                temp+=1     
                   
        self.setLayout(self.layout)

appMain = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
appMain.exec()