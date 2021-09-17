# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/list_code.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 345)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 10, 211, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 310, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)

        self.setSlots(Form)
        Form.update_list()
        
        self.pushButton.clicked.connect(Form.update_list)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lista de Codigos"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        self.pushButton.setText(_translate("Form", "Refrescar"))

    def setDB(self, Form, db):
        Form.db = db

    def setDate(self,Form, date):
        Form.date = date
    
    def setSlots(self,Form):
        def update_list():
            self.tableWidget.setRowCount(0)
            try:
                elems = Form.db.list_all_assets()
                for elem in elems:
                    idx = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(idx)
                    self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(str(elem["code"])))
                    self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(elem["name"]))
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error en la base de datos")
                msg.exec()
            
        Form.update_list = update_list
        
