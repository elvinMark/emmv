# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caja.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from create_code import Ui_Form as create_code_helper
from list_code import Ui_Form as list_code_helper
from enter_cash import Ui_Form as enter_cash_helper
from enter_check import Ui_Form as enter_check_helper
from enter_ticket import Ui_Form as enter_ticket_helper
from expenses import Ui_Form as expenses_helper
from consult_inputs import Ui_Form as consult_inputs_helper
from consult_expenses import Ui_Form as consult_expenses_helper
from report_all import Ui_Form as report_all_helper

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 146)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 287, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 22))
        self.menubar.setObjectName("menubar")
        self.menuIngresos = QtWidgets.QMenu(self.menubar)
        self.menuIngresos.setObjectName("menuIngresos")
        self.menuEgresos = QtWidgets.QMenu(self.menubar)
        self.menuEgresos.setObjectName("menuEgresos")
        self.menuConsulta = QtWidgets.QMenu(self.menubar)
        self.menuConsulta.setObjectName("menuConsulta")
        self.menuReporte = QtWidgets.QMenu(self.menubar)
        self.menuReporte.setObjectName("menuReporte")
        self.menuAdministrador = QtWidgets.QMenu(self.menubar)
        self.menuAdministrador.setObjectName("menuAdministrador")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEfectivo = QtWidgets.QAction(MainWindow)
        self.actionEfectivo.setObjectName("actionEfectivo")
        self.actionCheque = QtWidgets.QAction(MainWindow)
        self.actionCheque.setObjectName("actionCheque")
        self.actionVoucher = QtWidgets.QAction(MainWindow)
        self.actionVoucher.setObjectName("actionVoucher")
        self.actionGastos = QtWidgets.QAction(MainWindow)
        self.actionGastos.setObjectName("actionGastos")
        self.actionCrear_Codigo = QtWidgets.QAction(MainWindow)
        self.actionCrear_Codigo.setObjectName("actionCrear_Codigo")
        self.actionLista_de_Codigos = QtWidgets.QAction(MainWindow)
        self.actionLista_de_Codigos.setObjectName("actionLista_de_Codigos")
        self.actionIngresos = QtWidgets.QAction(MainWindow)
        self.actionIngresos.setObjectName("actionIngresos")
        self.actionEgresos = QtWidgets.QAction(MainWindow)
        self.actionEgresos.setObjectName("actionEgresos")
        self.actionReporte_de_Caja = QtWidgets.QAction(MainWindow)
        self.actionReporte_de_Caja.setObjectName("actionReporte_de_Caja")
        self.menuIngresos.addAction(self.actionEfectivo)
        self.menuIngresos.addAction(self.actionCheque)
        self.menuIngresos.addAction(self.actionVoucher)
        self.menuEgresos.addAction(self.actionGastos)
        self.menuConsulta.addAction(self.actionIngresos)
        self.menuConsulta.addAction(self.actionEgresos)
        self.menuReporte.addAction(self.actionReporte_de_Caja)
        self.menuAdministrador.addAction(self.actionCrear_Codigo)
        self.menuAdministrador.addAction(self.actionLista_de_Codigos)
        self.menubar.addAction(self.menuAdministrador.menuAction())
        self.menubar.addAction(self.menuIngresos.menuAction())
        self.menubar.addAction(self.menuEgresos.menuAction())
        self.menubar.addAction(self.menuConsulta.menuAction())
        self.menubar.addAction(self.menuReporte.menuAction())

        self.retranslateUi(MainWindow)

        self.setDate(MainWindow)
        self.setWindows(MainWindow)
        self.setSlots(MainWindow)
        
        self.pushButton.clicked.connect(MainWindow.enable_date_edit)
        # self.dateEdit.userDateChanged['QDate'].connect(MainWindow.change_system_date)
        self.dateEdit.calendarWidget().clicked.connect(MainWindow.change_system_date)
        self.actionCrear_Codigo.triggered.connect(MainWindow.window_create_code)
        self.actionCheque.triggered.connect(MainWindow.window_input_check)
        self.actionEfectivo.triggered.connect(MainWindow.window_input_cash)
        self.actionVoucher.triggered.connect(MainWindow.window_input_ticket)
        self.actionLista_de_Codigos.triggered.connect(MainWindow.window_list_code)
        self.actionGastos.triggered.connect(MainWindow.window_output_expenses)
        self.actionIngresos.triggered.connect(MainWindow.window_consult_inputs)
        self.actionEgresos.triggered.connect(MainWindow.window_consult_outputs)
        self.actionReporte_de_Caja.triggered.connect(MainWindow.window_report_all)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caja - EMMV"))
        self.label.setText(_translate("MainWindow", "Fecha:"))
        self.pushButton.setText(_translate("MainWindow", "Cambiar Fecha"))
        self.menuIngresos.setTitle(_translate("MainWindow", "Ingresos"))
        self.menuEgresos.setTitle(_translate("MainWindow", "Egresos"))
        self.menuConsulta.setTitle(_translate("MainWindow", "Consulta"))
        self.menuReporte.setTitle(_translate("MainWindow", "Reporte"))
        self.menuAdministrador.setTitle(_translate("MainWindow", "Administrador"))
        self.actionEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.actionCheque.setText(_translate("MainWindow", "Cheque"))
        self.actionVoucher.setText(_translate("MainWindow", "Voucher"))
        self.actionGastos.setText(_translate("MainWindow", "Gastos"))
        self.actionCrear_Codigo.setText(_translate("MainWindow", "Crear Codigo"))
        self.actionLista_de_Codigos.setText(_translate("MainWindow", "Lista de Codigos"))
        self.actionIngresos.setText(_translate("MainWindow", "Ingresos"))
        self.actionEgresos.setText(_translate("MainWindow", "Egresos"))
        self.actionReporte_de_Caja.setText(_translate("MainWindow", "Reporte de Caja"))

    def setDate(self,MainWindow):
        self.dateEdit.setDate(MainWindow.date.to_qdate())
        
    def setWindows(self,MainWindow):
        self.create_code = QtWidgets.QWidget()
        helper = create_code_helper()
        helper.setDB(self.create_code,MainWindow.db)
        helper.setDate(self.create_code,MainWindow.date)
        helper.setupUi(self.create_code)
        
        self.list_code = QtWidgets.QWidget()
        helper = list_code_helper()
        helper.setDB(self.list_code,MainWindow.db)
        helper.setDate(self.list_code,MainWindow.date)
        helper.setupUi(self.list_code)
        
        self.enter_cash = QtWidgets.QWidget()
        helper = enter_cash_helper()
        helper.setDB(self.enter_cash,MainWindow.db)
        helper.setDate(self.enter_cash,MainWindow.date)
        helper.setupUi(self.enter_cash)

        self.enter_check = QtWidgets.QWidget()
        helper = enter_check_helper()
        helper.setupUi(self.enter_check)

        self.enter_ticket = QtWidgets.QWidget()
        helper = enter_ticket_helper()
        helper.setupUi(self.enter_ticket)

        self.expenses = QtWidgets.QWidget()
        helper = expenses_helper()
        helper.setupUi(self.expenses)

        self.consult_inputs = QtWidgets.QWidget()
        helper = consult_inputs_helper()
        helper.setupUi(self.consult_inputs)

        self.consult_expenses = QtWidgets.QWidget()
        helper = consult_expenses_helper()
        helper.setupUi(self.consult_expenses)

        self.report_all = QtWidgets.QWidget()
        helper = report_all_helper()
        helper.setupUi(self.report_all)
        
    def setSlots(self,MainWindow):
        def enable_data_edit():
            self.dateEdit.setReadOnly(False)
        def change_system_date():
            print("changing")
            self.dateEdit.setReadOnly(True)
        def window_create_code():
            self.create_code.show()
        def window_input_check():
            self.enter_check.show()
        def window_input_cash():
            self.enter_cash.show()
        def window_input_ticket():
            self.enter_ticket.show()
        def window_list_code():
            self.list_code.show()
        def window_output_expenses():
            self.expenses.show()
        def window_consult_inputs():
            self.consult_inputs.show()
        def window_consult_outputs():
            self.consult_expenses.show()
        def window_report_all():
            self.report_all.show()
        
        MainWindow.enable_date_edit = enable_data_edit
        MainWindow.change_system_date = change_system_date
        MainWindow.window_create_code = window_create_code
        MainWindow.window_input_check = window_input_check
        MainWindow.window_input_cash = window_input_cash
        MainWindow.window_input_ticket = window_input_ticket
        MainWindow.window_list_code = window_list_code
        MainWindow.window_output_expenses = window_output_expenses
        MainWindow.window_consult_inputs = window_consult_inputs
        MainWindow.window_consult_outputs = window_consult_outputs
        MainWindow.window_report_all = window_report_all
