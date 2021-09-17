from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import datetime

sys.path.append("../")

from gui.caja import Ui_MainWindow as caja_helper
from db.caja_db import CajaDB
from tools.caja_date import CajaDate

today = datetime.datetime.today()

app = QApplication(sys.argv)

mainwindow = QMainWindow()
mainwindow.db = CajaDB("../db/data/")
mainwindow.date = CajaDate(today.year,today.month,today.day)
mainwindow_helper = caja_helper()
mainwindow_helper.setupUi(mainwindow)
mainwindow.show()

sys.exit(app.exec_())
