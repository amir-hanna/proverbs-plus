#!/usr/bin/python3

from proverbs_plus_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum, unique
import random_quote
from screen_scrap import scrap_page
from PyQt5.QtCore import QThread, pyqtSignal, QObject

@unique
class Direction(Enum):
    RANDOM = 0
    NEXT = 1
    PREVIOUS = 2

# worker class with a multi-purpose dynamically linked function
class Worker(QObject):
    done = pyqtSignal(tuple)
    
    def __init__(self, func, *args, **kwargs):
        QObject.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs

    # code in this method will run asynchronously on a separate thread
    def dowork(self):
        result = self.func(*self.args, **self.kwargs)
        self.done.emit(result)


class Main_Window(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        
        self.plainTextEdit_page_0.setPlainText(self.get_verse(Direction.RANDOM))
        self.btn_previous.clicked.connect(lambda: self.plainTextEdit_page_0.setPlainText(self.get_verse(Direction.PREVIOUS)))
        self.btn_next.clicked.connect(lambda: self.plainTextEdit_page_0.setPlainText(self.get_verse(Direction.NEXT)))

        self.btn_screen_0.clicked.connect(lambda: self.switch_screen(1, 'Scrap Screen'))
        self.btn_screen_1.clicked.connect(lambda: self.switch_screen(0, 'Proverbs'))

        # enter url, regex txt, and delay for scrapping here
        url = ''
        txt = ''
        wait_secs = 3 * 60 * 60 -20
 
        # pass the the wrapper_func and its arguments (arguments for function inside the wrapper)
        self.worker = Worker(self.wrapper_func, url, txt, wait_secs)

        self.thread = QThread()
        
        # recommended way of running code on a separate thread
        self.worker.moveToThread(self.thread)

        # connect signals to slots
        self.worker.done.connect(self.set_page)
        self.thread.started.connect(self.worker.dowork)
        
        self.thread.start()

        self.center()
        MainWindow.show()
        
    # this method will be passed to the worker object to run asynchronously on a separate thread
    def wrapper_func(self, *args, **kwargs):
        scrap_result, bool_interesting = scrap_page(*args)

        # must always return tuple of any dimentions to match the worker 'done' signal
        return (scrap_result, bool_interesting)


    def set_page(self, result):
        # unpack result from wrapper_func
        scrap_result, bool_interesting = result
        self.plainTextEdit_page_1.setPlainText(scrap_result)
        self.btn_screen_0.setText("Scrap Screen")

        if bool_interesting:
            self.btn_screen_0.setStyleSheet("background-color: #ff7f7f")


    def switch_screen(self, p_index, str_title):
        self.stackedWidget.setCurrentIndex(p_index)
        MainWindow.setWindowTitle(str_title)
        self.btn_screen_0.setStyleSheet("")

    def center(self):
        qr = MainWindow.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def get_verse(self, direction):
        if direction == Direction.RANDOM:
            self.quote_list, self.cur_pos = random_quote.quote_list('/home/amir/Documents/proverbs.json', 'fef08fec8be3919359bb0780c0e3320d37f49997f6dcd3e2cbf54ecc45a8c912eec80abcec9f394a295b0b16889bfbe2a90a2ca6530ab3a79a45c222168a46d9')
            return self.quote_list[self.cur_pos]
        elif direction == Direction.PREVIOUS and self.cur_pos > 0:
            self.cur_pos -= 1
            return self.quote_list[self.cur_pos]
        elif direction == Direction.NEXT and self.cur_pos < len(self.quote_list) - 1:
            self.cur_pos += 1
            return self.quote_list[self.cur_pos]
        else:
            return self.label.text()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Main_Window(MainWindow)
    sys.exit(app.exec_())

