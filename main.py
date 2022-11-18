from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QMetaObject, QRect
import sys
import random


class MainWindow(QMainWindow):
    button_1: QPushButton
    do_paint: bool = False

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(646, 495)
        self.button_1 = QPushButton(self)
        self.button_1.setGeometry(QRect(280, 200, 75, 23))
        self.button_1.setText("Кнопка")
        self.button_1.pressed.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, _) -> None:
        if not self.do_paint:
            return
        qp = QPainter()
        qp.begin(self)
        for _ in range(3):
            qp.setBrush(QColor(*(random.randint(0, 255) for _ in range(3))))
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            s = random.randint(0, 50)
            qp.drawEllipse(x, y, s, s)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
