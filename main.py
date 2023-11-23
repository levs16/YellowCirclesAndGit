import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        width = self.graphicsView.width()
        height = self.graphicsView.height()
        scene = QtWidgets.QGraphicsScene()
        n = random.randint(1, 10)
        for i in range(n):
            d = random.randint(10, 100)
            x = random.randint(0, width - d)
            y = random.randint(0, height - d)
            circle = QtWidgets.QGraphicsEllipseItem(x, y, d, d)
            circle.setBrush(QColor("yellow"))
            scene.addItem(circle)
        self.graphicsView.setScene(scene)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())


#############COPYRIGHT-AND-USAGE#############
#  Written by Lev, Sokolov on 23Nov 2023    #
#          Owned by Aboba Inc.              #
#          Free to use and edit             #
#############################################