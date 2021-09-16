import sys
from PyQt5.QtWidgets import QApplication
from windows import MainWindow

# Creating the Application
app = QApplication(sys.argv)

# Creating the main window
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
