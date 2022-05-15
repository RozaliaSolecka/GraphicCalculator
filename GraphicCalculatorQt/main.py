import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox


from PyQt5 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('calculator.png'))
        self.setWindowTitle("Kalkulator graficzny")
        self.setFixedSize(QSize(1200, 1200))

        # Create new action
        info = QAction( '&Informacje', self)
        info.triggered.connect(self.clickMethod)

        menuBar = self.menuBar()
        menu = menuBar.addMenu('&Menu')
        menu.addAction(info)

    def clickMethod(self):
        text = "Kalkulator graficzny to aplikacja służąca do tworzenia wykresów funkcji podanych " \
               "przez użytkownika. Liczba operacji możliwych do wykonania jest ograniczona."
        QMessageBox.about(self, "Informacje", text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()