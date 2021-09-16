# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/new_seller.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 149)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 371, 71))
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
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 186, 31))
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

        ####################################################
        def createSeller():
            name = self.lineEdit.text()
            route = self.comboBox.currentText()
            
            try:
                info = Form.db.search_seller_by_route(route)
                if len(info) > 0:
                    msg = QtWidgets.QMessageBox(Form)
                    msg.setWindowTitle("Error")
                    msg.setText("Existe un vendedor en esa ruta")
                    msg.exec()
                else:
                    Form.db.insert_new_seller(name,route)
                    msg = QtWidgets.QMessageBox(Form)
                    msg.setWindowTitle("Mensaje")
                    msg.setText("Vendedor creado exitosamente")
                    msg.exec()
                    self.lineEdit.setText("")
                    self.comboBox.setCurrentIndex(0)
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("No se pudo crear nuevo vendedor")
                msg.exec()

        Form.createSeller = createSeller
        ####################################################
        
        self.lineEdit.returnPressed.connect(self.comboBox.setFocus)
        self.pushButton.clicked.connect(Form.createSeller)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crear Nuevo Vendedor"))
        self.label.setText(_translate("Form", "Nombre del Vendedor:"))
        self.label_2.setText(_translate("Form", "Ruta:"))
        self.comboBox.setItemText(0, _translate("Form", "Zona 1"))
        self.comboBox.setItemText(1, _translate("Form", "Zona 2"))
        self.comboBox.setItemText(2, _translate("Form", "Zona 3"))
        self.comboBox.setItemText(3, _translate("Form", "Zona 4"))
        self.comboBox.setItemText(4, _translate("Form", "Zona 5"))
        self.pushButton.setText(_translate("Form", "Crear"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
