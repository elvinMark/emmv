# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/create_code.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 95)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.retranslateUi(Form)

        self.setSlots(Form)
        
        self.lineEdit.returnPressed.connect(self.pushButton.setFocus)
        self.pushButton.clicked.connect(Form.create_new_code)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crear Codigo - EMMV"))
        self.label.setText(_translate("Form", "Nombre: "))
        self.pushButton.setText(_translate("Form", "Crear"))

    def setDB(self,Form,db):
        Form.db = db

    def setDate(self,Form,date):
        Form.date = date
    
    def setSlots(self,Form):
        def create_new_code():
            name = self.lineEdit.text()
            try:
                tmp_ = Form.db.search_asset_by_name(name)
                if len(tmp_) > 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El nombre ya existe en la base de datos")
                    msg.exec()

                else:
                    try:
                        generated_code = Form.db.insert_new_asset(name)
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Mensaje")
                        msg.setText(f"Nuevo codigo creado exitosamente\ncodigo generado: {generated_code}")
                        msg.exec()
                    except:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Error en la base de datos")
                        msg.exec()
            
            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error en la base de datos")
                msg.exec()
                
            self.lineEdit.setText("")
        Form.create_new_code = create_new_code
        
