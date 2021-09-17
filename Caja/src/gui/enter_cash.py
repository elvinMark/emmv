# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/enter_cash.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(428, 346)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 114))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 411, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Form)

        self.setSlots(Form)
        
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.returnPressed.connect(self.lineEdit_3.setFocus)
        self.lineEdit_2.returnPressed.connect(Form.set_details)
        self.lineEdit_3.returnPressed.connect(self.pushButton.setFocus)
        self.pushButton.clicked.connect(Form.enter_new_input)
        self.lineEdit.returnPressed.connect(Form.enter_code)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ingresos por Efectivo"))
        self.label_2.setText(_translate("Form", "Detalles:"))
        self.label_3.setText(_translate("Form", "Importe:"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.label_5.setText(_translate("Form", "Nombre:"))
        self.pushButton.setText(_translate("Form", "Ingresar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Detalles"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Monto"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Fecha"))


    def setDB(self,Form,db):
        Form.db = db

    def setDate(self,Form,date):
        Form.date = date

    def setSlots(self,Form):
        def clear_fields():
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.label_4.setText("")
        
        def set_details():
            if self.lineEdit_2.text() == "":
                self.lineEdit_2.setText("Cobranza del dia")
        
        def enter_code():
            try:
                info = Form.db.search_asset_by_code(int(self.lineEdit.text()))
                if len(info) < 1:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("No se encontro el codigo en la base de datos")
                else:
                    self.label_4.setText(info[0]["name"])
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Hubo un problema con la base de datos")

        def enter_new_input():
            name = self.label_4.text()
            details = self.lineEdit_2.text()
            amount = self.lineEdit_3.text()
            try:
                Form.db.insert_new_input_cash(name,details,float(amount),Form.date.timestamp())
                idx = self.tableWidget.rowCount()
                self.tableWidget.insertRow(idx)
                self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(details))
                self.tableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem(amount))
                self.tableWidget.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(Form.date)))
                clear_fields()
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("No se pudo guardar la informacion")
                
        Form.enter_new_input = enter_new_input
        Form.set_details = set_details
        Form.enter_code = enter_code
