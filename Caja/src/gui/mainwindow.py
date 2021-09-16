from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

sys.path.append("../")

from gui.caja import Ui_MainWindow as caja_helper

app = QApplication(sys.argv)

mainwindow = QMainWindow()
mainwindow_helper = caja_helper()
mainwindow_helper.setupUi(mainwindow)
mainwindow.show()

sys.exit(app.exec_())
