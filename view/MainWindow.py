import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from view.CentralWidget import CentralWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setObjectName("MainWindow")
        self.setWindowTitle("Cardan Grille")
        # self.setWindowIcon(QIcon("/Images/icon.png"))

        self.setCentralWidget(CentralWidget(self))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    sys.exit(app.exec_())
