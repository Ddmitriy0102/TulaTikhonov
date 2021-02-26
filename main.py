import sys
import random

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.btn1.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        q = random.randint(1, 5)
        for i in range(q):
            qp.setBrush(QColor(255, 255, 0))
            w = random.randint(20, 200)
            x, y = random.randint(30, 450), random.randint(30, 450)
            qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())