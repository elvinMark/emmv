# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/new_client.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 162)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 431, 89))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 186, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)

        #######################################################
        def createClient():
            try:
                Form.db.insert_new_client(self.lineEdit.text(),self.lineEdit_2.text(),str(self.comboBox.currentText()))
                msg = QMessageBox(Form)
                msg.setWindowTitle("Mensaje")
                msg.setText("Cliente creado satisfactoriamente")
                msg.exec()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.comboBox.setCurrentIndex(0)
                
            except:
                msg = QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("Cliente no pudo ser creado")
                msg.exec()

        Form.createClient = createClient
        #######################################################
        
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.returnPressed.connect(self.pushButton.setFocus)
        self.pushButton.clicked.connect(Form.createClient)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crear Nuevo Cliente"))
        self.label.setText(_translate("Form", "Nombre del Cliente:"))
        self.label_2.setText(_translate("Form", "Dirección del Cliente:"))
        self.label_3.setText(_translate("Form", "Ruta:"))
        self.comboBox.setItemText(0, _translate("Form", "Zona 1"))
        self.comboBox.setItemText(1, _translate("Form", "Zona 2"))
        self.comboBox.setItemText(2, _translate("Form", "Zona 3"))
        self.comboBox.setItemText(3, _translate("Form", "Zona 4"))
        self.comboBox.setItemText(4, _translate("Form", "Zona 5"))
        self.pushButton.setText(_translate("Form", "Crear"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
