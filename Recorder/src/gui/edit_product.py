# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/edit_product.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 289)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 369, 78))
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
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 361, 120))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 201, 41))
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
        self.pushButton_4.setGeometry(QtCore.QRect(380, 250, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.retranslateUi(Form)

        ############################################
        def searchProduct():
            code = self.lineEdit.text()
            try:
                info = Form.db.search_product_by_code(code)
                if len(info) < 1:
                    msg = QtWidgets.QMessageBox(Form)
                    msg.setWindowTitle("Error")
                    msg.setText("No se encontro algun producto con ese codigo")
                    msg.exec()
                else:
                    details = info[0]
                    self.lineEdit.setEnabled(False)
                    self.lineEdit_2.setText(details["name"])
                    self.lineEdit_3.setText(str(details["price_per_unit"]))
                    self.lineEdit_4.setText(str(details["units_per_box"]))
                    self.comboBox.setCurrentIndex(self.comboBox.findText(details["type_of_unit"]))
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("Hubo un problema con la base de datos")
                msg.exec()
        
        def saveProduct():
            code = self.lineEdit.text()
            name = self.lineEdit_2.text()
            price_per_unit = float(self.lineEdit_3.text())
            units_per_box = int(self.lineEdit_4.text())
            type_of_unit = self.comboBox.currentText()
            new_info = {"name" : name,"price_per_unit":price_per_unit,"units_per_box":units_per_box,"type_of_unit":type_of_unit}
            try:
                Form.db.update_product(code,new_info)
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Mensaje")
                msg.setText("Se actualizo el producto correctamente")
                msg.exec()
            except:
                msg = QtWidgets.QMessageBox(Form)
                msg.setWindowTitle("Error")
                msg.setText("Hubo un problema con la base de datos")
                msg.exec()
            self.lineEdit.setEnabled(True)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.comboBox.setCurrentIndex(0)

        def resetFields():
            self.lineEdit.setEnabled(True)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.comboBox.setCurrentIndex(0)
        
        Form.searchProduct = searchProduct
        Form.saveProduct = saveProduct
        Form.resetFields = resetFields
        ############################################
        
        self.pushButton.clicked.connect(Form.searchProduct)
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.pushButton_2.clicked.connect(Form.saveProduct)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton_4.clicked.connect(Form.resetFields)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Producto"))
        self.label.setText(_translate("Form", "Codigo del Producto: "))
        self.pushButton.setText(_translate("Form", "Buscar"))
        self.label_2.setText(_translate("Form", "Nombre del Producto:"))
        self.label_3.setText(_translate("Form", "Precio del Producto:"))
        self.label_4.setText(_translate("Form", "Unidades por Caja:"))
        self.label_5.setText(_translate("Form", "Tipo de Unidad:"))
        self.comboBox.setItemText(0, _translate("Form", "Pack"))
        self.comboBox.setItemText(1, _translate("Form", "Bolsa"))
        self.comboBox.setItemText(2, _translate("Form", "Caja"))
        self.comboBox.setItemText(3, _translate("Form", "Unidad"))
        self.pushButton_2.setText(_translate("Form", "Guardar"))
        self.pushButton_3.setText(_translate("Form", "Cancelar"))
        self.pushButton_4.setText(_translate("Form", "Limpiar"))
