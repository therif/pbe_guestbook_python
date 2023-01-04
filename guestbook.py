from __future__ import print_function

# from PyQt5.Qt import QApplication, QUrl, QDesktopServices
from functools import partial
from ui_main import *
from ui_abCreator import *
from ui_rpt import *

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
    # conn.query("SELECT * FROM gb")
    # result = conn.store_result()
    # for i in range(result.num_rows()):
    #     print(result.fetch_row())

def tampilkanDariDB(self):
    cur = conn.cursor()
    cur.execute("SELECT * FROM gb")
    allSQLRows = cur.fetchall()
    self.tableWidget.setRowCount(len(allSQLRows)) ##set number of rows
    self.tableWidget.setColumnCount(5) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns

    row = 0
    while True:
        sqlRow = cur.fetchone()
        if sqlRow == None:
            break ##stops while loop if there is no more lines in sql table
        for col in range(0, 5): ##otherwise add row into tableWidget
            self.tableWidget.setItem(row, col, QtGui.QTableWidgetItem(sqlRow[col]))
        row += 1


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MyReport(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyReport, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        # decfale signal disini jika
        # self.ui.exit.clicked.connect(self.handle)

    def tampilhasil(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM gb")
        allSQLRows = cur.fetchall()
        # print(allSQLRows)
        # self.ui.tableWidget.setRowCount(len(allSQLRows)) ##set number of rows
        # self.ui.tableWidget.setColumnCount(5) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns
        
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'TGL', 'NAMA', 'EMAIL', 'HP', 'STATUS'])
        self.ui.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(allSQLRows):
            self.ui.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                if (column_number == 5):
                    # pilihane dropdown kudu kok toto nang kene
                    # pilihane hadir = 1, nggak = 0
                    #  di uine totonen, karo set en
                    sstatus = ''
                    if (data == 0):
                        sstatus = 'Skip'
                    else:
                        sstatus = 'Hadir'
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(sstatus)))

                else :
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

def showReportView(self):
    self.rptForm = MyReport()
    # self.rptForm.show()
    # tampilkanDariDB(self)

    self.rptForm.tampilhasil()

    # cur = conn.cursor()
    # cur.execute("SELECT * FROM gb")
    # allSQLRows = cur.fetchall()
    # Ui_Form.tableWidget.setRowCount(len(allSQLRows)) ##set number of rows
    # Ui_Form.tableWidget.setColumnCount(5) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns

    # row = 0
    # while True:
    #     sqlRow = cur.fetchone()
    #     if sqlRow == None:
    #         break ##stops while loop if there is no more lines in sql table
    #     for col in range(0, 5): ##otherwise add row into tableWidget
    #         self.rptForm.tableWidget.setItem(row, col, QtGui.QTableWidgetItem(sqlRow[col]))
    #     row += 1

def showCreator(self):
    self.dialogCreator = MyDialog()
    self.dialogCreator.show()

def openBrowser(self):
    webbrowser.open("https://github.com/therif/pbe_guestbook_python")
    # url = QUrl("https://github.com/therif/pbe_guestbook_python")
    # QDesktopServices.openUrl(url)


def signals(self):    
    self.actionCreator.triggered.connect(self.showCreator)
    self.actionView.triggered.connect(self.showReportView)
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
Ui_MainWindow.tampilkanDariDB = tampilkanDariDB
Ui_MainWindow.showReportView = showReportView


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

