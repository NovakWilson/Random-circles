import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
from math import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Случайная окружность')
        
        self.btn = QPushButton('Нарисовать', self)
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.update_paint)
        
    def update_paint(self):
        self.update()

    def draw_crl(self, qp):
        self.x = randint(0, self.size().width())
        self.y = randint(0, self.size().height())
        
        color = "%06x" % randint(0, 0xFFFFFF)
        size = randint(5, 200)
        pen = QPen(QColor('#' + color), 1)
        qp.begin(self)
        qp.setPen(pen)
        qp.setBrush(QColor('#' + color))
        qp.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)
        qp.end()        

    def paintEvent(self, event):
        qp = QPainter()
        self.draw_crl(qp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
