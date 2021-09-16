# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/new_product.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 185)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 419, 134))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 211, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)

        ############################################
        def createProduct():
            name = self.lineEdit.text()
            price_per_unit = self.lineEdit_2.text()
            units_per_box = self.lineEdit_3.text()
            type_of_unit = self.comboBox.currentText()
            try:
                Form.db.insert_new_product(name,price_per_unit,units_per_box,type_of_unit)
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Mensaje")
                msg.setText("El producto se creo correctamente")
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("No se pudo crear el nuevo producto")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.comboBox.setCurrentIndex(0)
        
        Form.createProduct = createProduct
        ############################################
        
        self.pushButton_2.clicked.connect(Form.createProduct)
        self.pushButton.clicked.connect(Form.close)
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.returnPressed.connect(self.lineEdit_3.setFocus)
        self.lineEdit_3.returnPressed.connect(self.comboBox.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crear Nuevo Producto"))
        self.label.setText(_translate("Form", "Nombre del Producto: "))
        self.label_2.setText(_translate("Form", "Precio por Unidad"))
        self.label_3.setText(_translate("Form", "Unidades por Caja:"))
        self.label_4.setText(_translate("Form", "Tipo de Unidad:"))
        self.comboBox.setItemText(0, _translate("Form", "Pack"))
        self.comboBox.setItemText(1, _translate("Form", "Bolsa"))
        self.comboBox.setItemText(2, _translate("Form", "Caja"))
        self.comboBox.setItemText(3, _translate("Form", "Unidad"))
        self.pushButton_2.setText(_translate("Form", "Crear"))
        self.pushButton.setText(_translate("Form", "Cancelar"))
