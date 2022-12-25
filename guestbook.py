from __future__ import print_function

# from PyQt5.Qt import QApplication, QUrl, QDesktopServices
from functools import partial
from gb_ui import *
from gb_ui_dlgcreator import *

import webbrowser

hostname = 'localhost'
username = 'room'
password = 'therif'
database = 'api_lumen'


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def showCreator(self):
    self.dialogCreator = MyDialog()
    self.dialogCreator.show()

def openBrowser(self):
    print("Masuk B")
    webbrowser.open("https://github.com/therif/pbe_guestbook_python")
    # url = QUrl("https://github.com/therif/pbe_guestbook_python")
    # QDesktopServices.openUrl(url)


def signals(self):    
    self.actionCreator.triggered.connect(self.showCreator)
    self.actionGit.triggered.connect(partial(self.openBrowser))

    self.btnClear.clicked.connect(self.hapussemua)

def hapussemua(self):
    self._ops = ""
    self._angka = ""
    self._angka2 = ""
    self._hasil = ""
    self.ed_ops.clear()
    self.ed_hasil.clear()
    

Ui_MainWindow.signals = signals
Ui_MainWindow.hapussemua = hapussemua
Ui_MainWindow.showCreator = showCreator
Ui_MainWindow.openBrowser = openBrowser

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    # ui.varcustom()

    MainWindow.show()
    sys.exit(app.exec_())

