from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class AlbumentationsGui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    app =QApplication([])
    gui = AlbumentationsGui()
    gui.show()
    app.exec_()
