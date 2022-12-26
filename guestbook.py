from __future__ import print_function

# from PyQt5.Qt import QApplication, QUrl, QDesktopServices
from functools import partial
from gb_ui import *
from gb_ui_dlgcreator import *

import webbrowser
import MySQLdb

host = 'localhost'
user = 'room'
password = 'therif'
port = 3306
db = 'pbe_kel4'

conn = MySQLdb.Connection(
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)

# def DBConnection(self):
#     try:
#         db = mdb.connect('localhost', 'root', '', 'pyqt5')
#         QMessageBox.about(self, 'Connection', 'Database Connected Successfully')

#     except mdb.Error as e:
#         QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
#         sys.exit(1)


def insertDataGb(self):
    nama = self.namaLineEdit.text().strip()
    nohp = self.noHPLineEdit.text().strip()
    email = self.emailLineEdit.text().strip()
    hasil = conn.query(f"""INSERT INTO gb 
        (nama, hp, email, status) 
        VALUES ('{nama}', '{nohp}', '{email}', 1);""")
    hasil2 = conn.commit()
    print(hasil)
    print(hasil2)

    # harusnya ger result jika oke, clear.
    # ini langsung anggep ok pasti masuk datanya
    self.namaLineEdit.clear()
    self.noHPLineEdit.clear()
    self.emailLineEdit.clear()

    # Example of how to fetch table data:
    conn.query("""SELECT * FROM gb""")
    result = conn.store_result()
    for i in range(result.num_rows()):
        print(result.fetch_row())


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def showCreator(self):
    self.dialogCreator = MyDialog()
    self.dialogCreator.show()

def openBrowser(self):
    webbrowser.open("https://github.com/therif/pbe_guestbook_python")
    # url = QUrl("https://github.com/therif/pbe_guestbook_python")
    # QDesktopServices.openUrl(url)


def signals(self):    
    self.actionCreator.triggered.connect(self.showCreator)
    self.actionGit.triggered.connect(partial(self.openBrowser))

    self.btnSubmit.clicked.connect(partial(self.insertDataGb))
    self.btnClear.clicked.connect(self.hapussemua)

def hapussemua(self):
    self._ops = ""
    self._angka = ""
    self._angka2 = ""
    self._hasil = ""
    self.ed_ops.clear()
    self.ed_hasil.clear()
    
def setDateSkrg(self):
    # waktunow = QtCore.QDateTime.fromString(date_time, 'yyyy/M/d hh:mm:ss')
    # self.dateTimeEdit.setDateTime(waktunow)
    # dt = QtWidgets.QDateTimeEdit(QtWidgets.QDateTime.currentDateTime())
    # now = QtCore.QDateTime(QDateTime.currentDateTime())
    self.tanggalDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

Ui_MainWindow.signals = signals
Ui_MainWindow.hapussemua = hapussemua
Ui_MainWindow.showCreator = showCreator
Ui_MainWindow.openBrowser = openBrowser
Ui_MainWindow.setDateSkrg = setDateSkrg
Ui_MainWindow.insertDataGb = insertDataGb

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    # ui.varcustom()
    ui.setDateSkrg()

    MainWindow.show()
    sys.exit(app.exec_())

