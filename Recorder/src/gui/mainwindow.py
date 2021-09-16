import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from recorder import Ui_MainWindow as main_window_helper
import datetime

sys.path.append("../")

from tools.prototypes import MainWindowPrototype
from tools.recorder_date import RecorderDate

db_dir = "../db/data"
wkhtmltopdf_dir = "/usr/bin/wkhtmltopdf"
curr_date = datetime.datetime.today().date()

app = QApplication(sys.argv)

main_window = MainWindowPrototype(db_dir,wkhtmltopdf_dir,RecorderDate(curr_date.year,curr_date.month,curr_date.day))

helper = main_window_helper()
helper.setupUi(main_window)
helper.setDB(main_window)
helper.setCurrDate(main_window)

main_window.show()

sys.exit(app.exec_())

