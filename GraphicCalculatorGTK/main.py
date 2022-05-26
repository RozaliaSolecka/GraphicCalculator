import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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

        vbox = Gtk.VBox(False, 1)
        vbox.pack_start(mb, False, False, 0)
        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)

    def on_pop_menu(self, widget, event):
        dialog = DialogExample(self)
        response = dialog.run()

        dialog.destroy()

if __name__ == "__main__":
    window = Window()
    window.show_all()
    Gtk.main()