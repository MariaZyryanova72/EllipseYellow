import sys, random
from PyQt5.Qt import QWidget, QPainter, QApplication, QMainWindow, QColor
from Ui import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.flag = False
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.flag:
            self.flag = False
        else:
            self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 237, 0))
            a = random.randrange(1, 351)
            qp.drawEllipse(100, 100, a, a)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())