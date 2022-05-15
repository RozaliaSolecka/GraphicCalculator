# import sys
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtGui
#
# import pyqtgraph as pg
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowIcon(QtGui.QIcon('calculator.png'))
#         self.setWindowTitle("Kalkulator graficzny")
#         self.setFixedSize(QSize(1200, 1200))
#
#         # Create new action
#         info = QAction( '&Informacje', self)
#         info.triggered.connect(self.clickMethod)
#
#         menuBar = self.menuBar()
#         menu = menuBar.addMenu('&Menu')
#         menu.addAction(info)
#
#         # calling method
#         self.UiComponents()
#
#         # calling method
#         self.UiPlot()
#
#         # showing all the widgets
#         self.show()
#
#     # method for plot
#
#     def UiPlot(self):
#         # creating a widget object
#         widget = QWidget()
#
#
#         # creating a plot window
#         plot = pg.plot()
#
#         # create list for y-axis
#         y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
#
#         # create horizontal list i.e x-axis
#         x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#         # create pyqt5graph bar graph item
#         # with width = 0.6
#         # with bar colors = green
#         bargraph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='g')
#
#         # add item to plot window
#         # adding bargraph item to the plot window
#         plot.addItem(bargraph)
#
#         # Creating a grid layout
#         layout = QGridLayout()
#
#         # setting this layout to the widget
#         widget.setLayout(layout)
#
#
#
#         # plot window goes on right side, spanning 3 rows
#         layout.addWidget(plot, 0, 1, 3, 1)
#
#         # setting this widget as central widget of the main window
#         self.setCentralWidget(widget)
#
#
#     # method for widgets
#
#     def UiComponents(self):
#
#         # creating a label
#         self.label = QLabel(self)
#
#         # setting geometry to the label
#         self.label.setGeometry(150, 600, 800, 70)
#
#         # creating label multi line
#         self.label.setWordWrap(True)
#
#         # setting style sheet to the label
#         self.label.setStyleSheet("QLabel"
#                                  "{"
#                                  "border : 1px solid black;"
#                                  "background : white;"
#                                  "}")
#
#         # f(x) label
#         labelFx = QLabel('f(x) = ', self)
#
#         # setting geometry
#         labelFx.setGeometry(100, 600, 90, 70)
#
#         # adding number button to the screen
#         # creating a push button
#         pushDraw = QPushButton("Rysuj", self)
#
#         # adding equal button a color effect
#         c_effect = QGraphicsColorizeEffect()
#         c_effect.setColor(Qt.red)
#         pushDraw.setGraphicsEffect(c_effect)
#
#         # setting geometry
#         pushDraw.setGeometry(960, 600, 190, 70)
#         # creating a push button
#         push1 = QPushButton("1", self)
#
#         # setting geometry
#         push1.setGeometry(50, 730, 267.5, 40)
#
#         # creating a push button
#         push2 = QPushButton("2", self)
#
#         # setting geometry
#         push2.setGeometry(327.5, 730, 267.5, 40)
#
#         # creating a push button
#         push3 = QPushButton("3", self)
#
#         # setting geometry
#         push3.setGeometry(605, 730, 267.5, 40)
#
#         # creating a push button
#         push4 = QPushButton("4", self)
#
#         # setting geometry
#         push4.setGeometry(50, 780, 267.5, 40)
#
#         # creating a push button
#         push5 = QPushButton("5", self)
#
#         # setting geometry
#         push5.setGeometry(325.5, 780, 267.5, 40)
#
#         # creating a push button
#         push6 = QPushButton("6", self)
#
#         # setting geometry
#         push6.setGeometry(605, 780, 267.5, 40)
#
#         # creating a push button
#         push7 = QPushButton("7", self)
#
#         # setting geometry
#         push7.setGeometry(50, 830, 267.5, 40)
#
#         # creating a push button
#         push8 = QPushButton("8", self)
#
#         # setting geometry
#         push8.setGeometry(327.5, 830, 267.5, 40)
#
#         # creating a push button
#         push9 = QPushButton("9", self)
#
#         # setting geometry
#         push9.setGeometry(605, 830, 267.5, 40)
#
#         # creating a push button
#         push0 = QPushButton("0", self)
#
#         # setting geometry
#         push0.setGeometry(50, 880, 267.5, 40)
#
#         # adding operator push button
#         # creating push button
#         push_x = QPushButton("x", self)
#
#         # setting geometry
#         push_x.setGeometry(882.5, 880, 267.5, 40)
#
#         # adding equal button a color effect
#         c_effect = QGraphicsColorizeEffect()
#         c_effect.setColor(Qt.blue)
#         push_x.setGraphicsEffect(c_effect)
#
#         # creating push button
#         push_plus = QPushButton("+", self)
#
#         # setting geometry
#         push_plus.setGeometry(882.5, 830, 267.5, 40)
#
#         # creating push button
#         push_minus = QPushButton("-", self)
#
#         # setting geometry
#         push_minus.setGeometry(882.5, 780, 267.5, 40)
#
#         # creating push button
#         push_mul = QPushButton("*", self)
#
#         # setting geometry
#         push_mul.setGeometry(882.5, 730, 267.5, 40)
#
#         # creating push button
#         push_div = QPushButton("/", self)
#
#         # setting geometry
#         push_div.setGeometry(605, 880, 267.5, 40)
#
#         # creating push button
#         push_point = QPushButton(".", self)
#
#         # setting geometry
#         push_point.setGeometry(327.5, 880, 267.5, 40)
#
#         # clear button
#         push_clear = QPushButton("Wyczyść", self)
#         push_clear.setGeometry(50, 680, 545, 40)
#
#         # del one character button
#         push_del = QPushButton("Usuń", self)
#         push_del.setGeometry(605, 680, 545, 40)
#
#         # adding action to each of the button
#         push_minus.clicked.connect(self.action_minus)
#         push_x.clicked.connect(self.action_x)
#         push0.clicked.connect(self.action0)
#         push1.clicked.connect(self.action1)
#         push2.clicked.connect(self.action2)
#         push3.clicked.connect(self.action3)
#         push4.clicked.connect(self.action4)
#         push5.clicked.connect(self.action5)
#         push6.clicked.connect(self.action6)
#         push7.clicked.connect(self.action7)
#         push8.clicked.connect(self.action8)
#         push9.clicked.connect(self.action9)
#         push_div.clicked.connect(self.action_div)
#         push_mul.clicked.connect(self.action_mul)
#         push_plus.clicked.connect(self.action_plus)
#         push_point.clicked.connect(self.action_point)
#         push_clear.clicked.connect(self.action_clear)
#         push_del.clicked.connect(self.action_del)
#         pushDraw.clicked.connect(self.action_draw)
#
#     def action_draw(self):
#         # get the label text
#         equation = self.label.text()
#
#         try:
#             # getting the ans
#             ans = eval(equation)
#
#             # setting text to the label
#             self.label.setText(str(ans))
#
#         except:
#             # setting text to the label
#             self.label.setText("Wrong Input")
#
#     def action_x(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + " x ")
#
#     def action_plus(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + " + ")
#
#     def action_minus(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + " - ")
#
#     def action_div(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + " / ")
#
#     def action_mul(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + " * ")
#
#     def action_point(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + ".")
#
#     def action0(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "0")
#
#     def action1(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "1")
#
#     def action2(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "2")
#
#     def action3(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "3")
#
#     def action4(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "4")
#
#     def action5(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "5")
#
#     def action6(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "6")
#
#     def action7(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "7")
#
#     def action8(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "8")
#
#     def action9(self):
#         # appending label text
#         text = self.label.text()
#         self.label.setText(text + "9")
#
#     def action_clear(self):
#         # clearing the label text
#         self.label.setText("")
#
#     def action_del(self):
#         # clearing a single digit
#         text = self.label.text()
#         print(text[:len(text) - 1])
#         self.label.setText(text[:len(text) - 1])
#
#     def clickMethod(self):
#         text = "Kalkulator graficzny to aplikacja służąca do tworzenia wykresów funkcji podanych " \
#                "przez użytkownika. Liczba operacji możliwych do wykonania jest ograniczona."
#         QMessageBox.about(self, "Informacje", text)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     window = MainWindow()
#     window.show()
#
#     app.exec()