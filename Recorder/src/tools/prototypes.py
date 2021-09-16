import pdfkit
from PyQt5.QtWidgets import QWidget, QMainWindow

class FormPrototype(QWidget):
    def __init__(self):
        super().__init__()
        self.resetFields = lambda : None

    def closeEvent(self,event):
        self.resetFields()


class MainWindowPrototype(QMainWindow):
    def __init__(self,db_dir,wkhtmltopdf_dir,curr_date):
        super().__init__()
        self.db_dir = db_dir
        self.wkhtmltopdf_dir = wkhtmltopdf_dir
        self.curr_date = curr_date
