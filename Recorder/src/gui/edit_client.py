# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit_client.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 229)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 61))
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
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 411, 89))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 186, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 190, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)

        ##########################################
        def searchClient():
            try:
                info = Form.db.search_client_by_code(self.lineEdit.text())
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("Hubo un problema con la base de datos")
                msg.exec()
            
            if len(info) < 1:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("Codigo de cliente no existe")
                msg.exec()
            else:
                self.lineEdit.setEnabled(False)
                details = info[0]
                self.lineEdit_2.setText(details["name"])
                self.lineEdit_3.setText(details["address"])
                self.comboBox.setCurrentIndex(self.comboBox.findText(details["route"]))
                
        def saveClient():
            code = self.lineEdit.text()
            name = self.lineEdit_2.text()
            address = self.lineEdit_3.text()
            route = self.comboBox.currentText()
            new_info = {"name":name,"address":address,"route":route}
            try:
                Form.db.update_client(code,new_info)
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Mensaje")
                msg.setText("Datos del cliente han sido actualizados")
                msg.exec()
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("No se pudo actualizar los datos del cliente en la base de datos")
                msg.exec()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.comboBox.setCurrentIndex(0)
            self.lineEdit.setEnabled(True)

        def resetFields():
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.comboBox.setCurrentIndex(0)
            self.lineEdit.setEnabled(True)
        
        Form.searchClient = searchClient
        Form.saveClient = saveClient
        Form.resetFields = resetFields
        
        ##########################################
        
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.pushButton.clicked.connect(Form.searchClient)
        self.pushButton_2.clicked.connect(Form.saveClient)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton_4.clicked.connect(Form.resetFields)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Cliente"))
        self.label.setText(_translate("Form", "Codigo del Cliente:"))
        self.pushButton.setText(_translate("Form", "Buscar"))
        self.label_2.setText(_translate("Form", "Nombre del Cliente:"))
        self.label_3.setText(_translate("Form", "Dirección del Cliente:"))
        self.label_4.setText(_translate("Form", "Ruta:"))
        self.comboBox.setItemText(0, _translate("Form", "Zona 1"))
        self.comboBox.setItemText(1, _translate("Form", "Zona 2"))
        self.comboBox.setItemText(2, _translate("Form", "Zona 3"))
        self.comboBox.setItemText(3, _translate("Form", "Zona 4"))
        self.comboBox.setItemText(4, _translate("Form", "Zona 5"))
        self.pushButton_2.setText(_translate("Form", "Guardar"))
        self.pushButton_3.setText(_translate("Form", "Cancelar"))
        self.pushButton_4.setText(_translate("Form", "Limpiar"))
