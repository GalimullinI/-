import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint
from PyQt5.QtGui import QPainter, QColor


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.coords = [0, 0]
        self.click = 0
        self.setWindowTitle('Жёлтые окружности')

    def run(self):
        self.click = 1
        self.update()

    def paintEvent(self, event):
        if self.click == 1:
            qp = QPainter()
            qp.begin(self)
            for i in range(3):
                self.drawCircle(qp)
            qp.end()
        else:
            pass

    def drawCircle(self, qp):
        self.coords = [randint(100, 500), randint(100, 500)]
        x = randint(50, 300)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.coords[0] - x // 2, self.coords[1] - x // 2, x, x)
        self.click = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())