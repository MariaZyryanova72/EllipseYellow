import sys, random
from PyQt5.Qt import QPainter, QApplication, QColor, QPushButton, QMainWindow


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 529, 498)
        self.setWindowTitle('Рисование КРУГА')

        self.pushButton = QPushButton("Нарисовать круг", self)
        self.pushButton.resize(511, 31)
        self.pushButton.move(10, 20)


class App(Interface):
    def __init__(self):
        self.flag = False
        super().__init__()
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
            qp.setBrush(QColor(random.randrange(255), random.randrange(255), random.randrange(255)))
            a = random.randrange(1, 351)
            qp.drawEllipse(100, 100, a, a)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())