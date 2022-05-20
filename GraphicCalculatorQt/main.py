import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

import pyqtgraph as pg
from frange import drange


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_x = True
        self.x0 = 1
        self.x1 = 20

        self.setWindowIcon(QtGui.QIcon('calculator.png'))
        self.setWindowTitle("Kalkulator graficzny")
        self.setFixedSize(QSize(800, 800))

        # Create new action
        info = QAction('&Informacje', self)
        info.triggered.connect(self.clickMethod)

        menuBar = self.menuBar()
        menu = menuBar.addMenu('&Menu')
        menu.addAction(info)

        self.pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.panel_layout = QHBoxLayout()
        self.graph_layout = QHBoxLayout()
        self.row_1 = QHBoxLayout()
        #self.row_1_2 = QHBoxLayout()
        self.row_2 = QHBoxLayout()
        self.row_3 = QHBoxLayout()
        self.row_4 = QHBoxLayout()
        self.row_5 = QHBoxLayout()

        self.pagelayout.addLayout(self.graph_layout)
        self.pagelayout.addLayout(self.panel_layout)
        self.pagelayout.addLayout(self.button_layout)
        self.pagelayout.addLayout(self.row_1)
        #self.pagelayout.addLayout(self.row_1_2)
        self.pagelayout.addLayout(self.row_2)
        self.pagelayout.addLayout(self.row_3)
        self.pagelayout.addLayout(self.row_4)
        self.pagelayout.addLayout(self.row_5)

        widget = QWidget()
        widget.setLayout(self.pagelayout)
        self.setCentralWidget(widget)


        self.plt = pg.PlotWidget()
        self.x = []
        self.y = []
        self.plt.sigRangeChanged.connect(self.viewboxChanged)

        self.plt.setBackground('w')
        self.plt.showGrid(x=True, y=True)
        self.graph_layout.addWidget(self.plt)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def viewboxChanged(self, view, range_v):
        ## range_v[0] will return the list: [x_0, x_1]
        self.x0 = range_v[0][0]
        self.x1 = range_v[0][1]

        if self.init_x:
            self.init_x = False
            pass
        else:
            print(self.x0, self.x1)

            equation = self.label.text()

            if equation != '':
                self.UiPlot(equation, self.x0, self.x1)
            self.init_x = True


    def UiPlot(self, equation, range_start, range_end):

        self.plt.clear()

        self.x = list(drange(range_start, range_end, 0.1))
        self.y = []
        for i in self.x:
            result = eval(equation, {"x": i})
            self.y.append(result)

        self.plt.showGrid(x=True, y=True)
        pen = pg.mkPen(color=(255, 0, 0))

        try:
            self.plt.plot(self.x, self.y, pen = pen)
            self.init_x = False
        except:
            self.init_x = False
            self.plt.clear()
            self.plt.showGrid(x=True, y=True)
            self.plt.setBackground('w')

            self.label.setText("Błąd")

    # method for widgets

    def UiComponents(self):

        # f(x) label
        labelFx = QLabel('f(x) = ', self)

        self.panel_layout.addWidget(labelFx, 1)

        # creating a label
        self.label = QLabel(self)

        # creating label multi line
        self.label.setWordWrap(True)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 1px solid black;"
                                 "background : white;"
                                 "}")
        self.panel_layout.addWidget(self.label, 15)

        # adding number button to the screen
        # creating a push button
        pushDraw = QPushButton("Rysuj", self)

        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.red)
        pushDraw.setGraphicsEffect(c_effect)

        self.panel_layout.addWidget(pushDraw, 2)

        # creating a push button
        push1 = QPushButton("1", self)
        # creating a push button
        push2 = QPushButton("2", self)
        # creating a push button
        push3 = QPushButton("3", self)
        # creating a push button
        push4 = QPushButton("4", self)
        # creating a push button
        push5 = QPushButton("5", self)
        # creating a push button
        push6 = QPushButton("6", self)
        # creating a push button
        push7 = QPushButton("7", self)
        push8 = QPushButton("8", self)
        # creating a push button
        push9 = QPushButton("9", self)
        # creating a push button
        push0 = QPushButton("0", self)
        # creating push button
        push_x = QPushButton("x", self)
        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_x.setGraphicsEffect(c_effect)
        # creating push button
        push_plus = QPushButton("+", self)
        # creating push button
        push_minus = QPushButton("-", self)
        # creating push button
        push_mul = QPushButton("*", self)
        # creating push button
        push_div = QPushButton("/", self)
        # creating push button
        push_point = QPushButton(".", self)
        # clear button
        push_clear = QPushButton("Wyczyść", self)
        # clear button
        #push_clear_ranges = QPushButton("Wyczyść zakresy", self)
        # del one character button
        push_del = QPushButton("Usuń", self)

        # # start range label
        # labelStart = QLabel('Zakres x od = ', self)
        # self.row_1_2.addWidget(labelStart, 1)
        #
        # # creating a label
        # self.labelStartVal = QLabel(self)
        # # setting style sheet to the label
        # self.labelStartVal.setStyleSheet("QLabel"
        #                          "{"
        #                          "border : 1px solid black;"
        #                          "background : white;"
        #                          "}")
        # self.labelStartVal.setText("0")
        # self.row_1_2.addWidget(self.labelStartVal, 1)
        #
        # # end range label
        # labelEnd = QLabel('Zakres x do = ', self)
        # self.row_1_2.addWidget(labelEnd, 1)
        #
        # # creating a label
        # self.labelEndVal = QLabel(self)
        # # setting style sheet to the label
        # self.labelEndVal.setStyleSheet("QLabel"
        #                                  "{"
        #                                  "border : 1px solid black;"
        #                                  "background : white;"
        #                                  "}")
        # self.labelEndVal.setText("100")
        # self.row_1_2.addWidget(self.labelEndVal, 1)
        # self.row_1_2.addWidget(push_clear_ranges)

        self.row_1.addWidget(push_clear)
        self.row_1.addWidget(push_del)
        self.row_2.addWidget(push1)
        self.row_2.addWidget(push2)
        self.row_2.addWidget(push3)
        self.row_2.addWidget(push_mul)
        self.row_3.addWidget(push4)
        self.row_3.addWidget(push5)
        self.row_3.addWidget(push6)
        self.row_3.addWidget(push_minus)
        self.row_4.addWidget(push7)
        self.row_4.addWidget(push8)
        self.row_4.addWidget(push9)
        self.row_4.addWidget(push_plus)
        self.row_5.addWidget(push0)
        self.row_5.addWidget(push_point)
        self.row_5.addWidget(push_div)
        self.row_5.addWidget(push_x)

        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_x.clicked.connect(self.action_x)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        #push_clear_ranges.clicked.connect(self.action_clear_ranges)
        push_del.clicked.connect(self.action_del)
        pushDraw.clicked.connect(self.action_draw)

    def action_draw(self):
        # get the label text
        equation = self.label.text()
        # startRange = self.labelStartVal.text()
        # endRange = self.labelEndVal.text()

        try:
            self.UiPlot(equation, self.x0, self.x1)

        except:
            # setting text to the label
            self.plt.clear()
            self.plt.showGrid(x=True, y=True)
            self.plt.setBackground('w')

            self.label.setText("Błąd")

    def action_x(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "x")

    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "+")

    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "-")

    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "/")

    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "*")

    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        # clearing the label text
        self.label.setText("")

    # def action_clear_ranges(self):
    #     # clearing the label text
    #     self.labelStartVal.setText("")
    #     self.labelEndVal.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])

    def clickMethod(self):
        text = "Kalkulator graficzny to aplikacja służąca do tworzenia wykresów funkcji podanych " \
               "przez użytkownika. Liczba operacji możliwych do wykonania jest ograniczona."
        QMessageBox.about(self, "Informacje", text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()


    window.show()

    app.exec()