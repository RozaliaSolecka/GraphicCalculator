import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np



class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Informacje", transient_for=parent, flags=0)
        self.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        self.set_default_size(200, 50)

        label = Gtk.Label(label="Kalkulator graficzny to aplikacja służąca do tworzenia wykresów funkcji podanych \n " \
                                "przez użytkownika. Liczba operacji możliwych do wykonania jest ograniczona.")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Kalkulator graficzny")
        self.set_size_request(800, 800)

        self.set_icon_from_file("calculator.png")

        self.x0 = -20
        self.x1 = 21

        # menu
        mb = Gtk.MenuBar()
        menu1 = Gtk.Menu()
        menu = Gtk.MenuItem("Menu")
        menu.set_submenu(menu1)
        acgroup = Gtk.AccelGroup()
        self.add_accel_group(acgroup)
        info = Gtk.MenuItem("Informacje")
        menu1.append(info)
        mb.append(menu)
        info.connect_object('button-press-event', self.on_pop_menu, menu)

        # layout
        self.vbox = Gtk.VBox(spacing=6)
        self.vbox.pack_start(mb, False, False, 0)
        self.add(self.vbox)

        # graph

        self.graph_box = Gtk.Box(spacing=6)
        self.initial_plot()



        # buttons
        self.button_box = Gtk.VBox(spacing=6)
        self.UiComponenets()
        self.vbox.pack_start(self.button_box, True, True, 0)

        self.connect("destroy", Gtk.main_quit)

    def initial_plot(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)  # a Gtk.DrawingArea
        self.graph_box.pack_start(self.canvas, True, True, 0)
        self.vbox.pack_start(self.graph_box, True, True, 0)
        self.ax = self.fig.add_subplot()
        self.draw_plot()




    def UiPlot(self, equation, range_start, range_end):

        self.ax.clear()

        self.x = list(range(range_start, range_end))
        self.y = []


        for i in self.x:
            result = eval(equation, {"x": i})
            self.y.append(result)
        print(self.x)
        print(self.y)

        self.ax.plot(self.x, self.y)



    def UiComponenets(self):

        # label
        self.row_0 = Gtk.Box(spacing=6)

        self.labelFx = Gtk.Label(label="f(x) = ")
        self.row_0.pack_start(self.labelFx, False, False, 0)

        self.label = Gtk.Label(label="")
        self.label.set_justify(Gtk.Justification.LEFT)
        self.row_0.pack_start(self.label, True, True, 0)

        self.push_draw = Gtk.Button(label="Rysuj")

        self.row_0.pack_start(self.push_draw, False, False, 0)

        # buttons
        self.row_1 = Gtk.Box(spacing=6)
        self.row_2 = Gtk.Box(spacing=6)
        self.row_3 = Gtk.Box(spacing=6)
        self.row_4 = Gtk.Box(spacing=6)
        self.row_5 = Gtk.Box(spacing=6)
        self.row_6 = Gtk.Box(spacing=6)

        self.push_1 = Gtk.Button(label="1")
        self.push_2 = Gtk.Button(label="2")
        self.push_3 = Gtk.Button(label="3")
        self.push_4 = Gtk.Button(label="4")
        self.push_5 = Gtk.Button(label="5")
        self.push_6 = Gtk.Button(label="6")
        self.push_7 = Gtk.Button(label="7")
        self.push_8 = Gtk.Button(label="8")
        self.push_9 = Gtk.Button(label="9")
        self.push_0 = Gtk.Button(label="0")
        self.push_x = Gtk.Button(label="x")
        self.push_plus = Gtk.Button(label="+")
        self.push_minus = Gtk.Button(label="-")
        self.push_mul = Gtk.Button(label="*")
        self.push_div = Gtk.Button(label="/")
        self.push_point = Gtk.Button(label=".")
        self.push_clear = Gtk.Button(label="Wyczyść")
        self.push_del = Gtk.Button(label="Usuń")
        self.push_open_bracket = Gtk.Button(label="(")
        self.push_close_bracket = Gtk.Button(label=")")
        self.push_pow = Gtk.Button(label="pow")
        self.push_comma = Gtk.Button(label=",")

        self.push_1.connect("clicked", self.push_1_action)
        self.push_2.connect("clicked", self.push_2_action)
        self.push_3.connect("clicked", self.push_3_action)
        self.push_4.connect("clicked", self.push_4_action)
        self.push_5.connect("clicked", self.push_5_action)
        self.push_6.connect("clicked", self.push_6_action)
        self.push_7.connect("clicked", self.push_7_action)
        self.push_8.connect("clicked", self.push_8_action)
        self.push_9.connect("clicked", self.push_9_action)
        self.push_0.connect("clicked", self.push_0_action)
        self.push_x.connect("clicked", self.push_x_action)
        self.push_plus.connect("clicked", self.push_plus_action)
        self.push_minus.connect("clicked", self.push_minus_action)
        self.push_mul.connect("clicked", self.push_mul_action)
        self.push_div.connect("clicked", self.push_div_action)
        self.push_point.connect("clicked", self.push_point_action)
        self.push_clear.connect("clicked", self.push_clear_action)
        self.push_del.connect("clicked", self.push_del_action)
        self.push_open_bracket.connect("clicked", self.push_open_bracket_action)
        self.push_close_bracket.connect("clicked", self.push_close_bracket_action)
        self.push_pow.connect("clicked", self.push_pow_action)
        self.push_comma.connect("clicked", self.push_comma_action)
        self.push_draw.connect("clicked", self.push_draw_action)

        self.row_1.pack_start(self.push_clear, True, True, 0)
        self.row_1.pack_start(self.push_del, True, True, 0)
        self.row_2.pack_start(self.push_1, True, True, 0)
        self.row_2.pack_start(self.push_2, True, True, 0)
        self.row_2.pack_start(self.push_3, True, True, 0)
        self.row_2.pack_start(self.push_mul, True, True, 0)
        self.row_3.pack_start(self.push_4, True, True, 0)
        self.row_3.pack_start(self.push_5, True, True, 0)
        self.row_3.pack_start(self.push_6, True, True, 0)
        self.row_3.pack_start(self.push_minus, True, True, 0)
        self.row_4.pack_start(self.push_7, True, True, 0)
        self.row_4.pack_start(self.push_8, True, True, 0)
        self.row_4.pack_start(self.push_9, True, True, 0)
        self.row_4.pack_start(self.push_plus, True, True, 0)
        self.row_5.pack_start(self.push_0, True, True, 0)
        self.row_5.pack_start(self.push_point, True, True, 0)
        self.row_5.pack_start(self.push_div, True, True, 0)
        self.row_5.pack_start(self.push_x, True, True, 0)
        self.row_6.pack_start(self.push_open_bracket, True, True, 0)
        self.row_6.pack_start(self.push_close_bracket, True, True, 0)
        self.row_6.pack_start(self.push_pow, True, True, 0)
        self.row_6.pack_start(self.push_comma, True, True, 0)

        self.button_box.pack_start(self.row_0, True, True, 0)
        self.button_box.pack_start(self.row_1, True, True, 0)
        self.button_box.pack_start(self.row_2, True, True, 0)
        self.button_box.pack_start(self.row_3, True, True, 0)
        self.button_box.pack_start(self.row_4, True, True, 0)
        self.button_box.pack_start(self.row_5, True, True, 0)
        self.button_box.pack_start(self.row_6, True, True, 0)

    def push_draw_action(self, widget):
        # get the label text
        equation = self.label.get_text()

        try:
            print(equation)
            self.UiPlot(equation, self.x0, self.x1)
            self.draw_plot()
        except:
            self.label.set_text("Błąd")



    def draw_plot(self) -> None:
        """ Draw or update the current plot """
        self.fig.canvas.draw()

    def push_1_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "1")

    def push_2_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "2")

    def push_3_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "3")

    def push_4_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "4")

    def push_5_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "5")

    def push_6_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "6")

    def push_7_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "7")

    def push_8_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "8")

    def push_9_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "9")

    def push_x_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "x")

    def push_plus_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "+")

    def push_minus_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "-")

    def push_mul_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "*")

    def push_div_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "/")

    def push_point_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + ".")

    def push_clear_action(self, widget):
        self.label.set_text("")

    def push_del_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text[:len(text) - 1])

    def push_0_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "0")

    def push_open_bracket_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "(")

    def push_close_bracket_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + ")")

    def push_pow_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + "pow(")

    def push_comma_action(self, widget):
        text = self.label.get_text()
        self.label.set_text(text + ",")



    def on_pop_menu(self, widget, event):
        dialog = DialogExample(self)
        dialog.run()

        dialog.destroy()

if __name__ == "__main__":
    window = Window()
    window.show_all()
    Gtk.main()