import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from Ui import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.coords = [0, 0]
        self.click = 0
        self.setWindowTitle('Случайные окружности')

    def run(self):
        self.click = 1
        self.update()

    def paintEvent(self, event):
        if self.click == 1:
            qp = QPainter()
            qp.begin(self)
            for i in range(5):
                self.drawCircle(qp)
            qp.end()
        else:
            pass

    def drawCircle(self, qp):
        self.coords = [randint(100, 900), randint(100, 600)]
        x = randint(50, 300)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(self.coords[0] - x // 2, self.coords[1] - x // 2, x, x)
        self.click = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())