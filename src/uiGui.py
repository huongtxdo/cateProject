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
        self.setCentralWidget(QtWidgets.QWidget())
        self.setWindowTitle("Make a merry Cate great again!")
        self.setGeometry(0, 0, 702, 550)
        #self.acceptDrops()
        
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
        self.stacklayout.addWidget(Image("cats.jpg"))

        # Button Inventory
        button = QtWidgets.QPushButton("Inventory")
        button.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Color("white"))

        # Button Shop
        button = QtWidgets.QPushButton("Shop")
        button.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(button)
        self.stacklayout.addWidget(Color("yellow"))

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
    
    def show_battle_window(self, checked):
        self.w = BattleWindow()
        self.w.show()

class BattleWindow(QtWidgets.QWidget):

    def __ini__init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Fight!")
        self.setGeometry(0, 0, 702, 550)
        self.label = QtWidgets.QLabel("Battle window")
        layout.addWidget(self.label)
        self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()