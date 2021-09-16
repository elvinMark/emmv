# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/recorder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from new_product import Ui_Form as new_product_helper
from new_stock import Ui_Form as new_stock_helper
from edit_product import Ui_Form as edit_product_helper
from edit_order import Ui_Form as edit_order_helper
from edit_seller import Ui_Form as edit_seller_helper
from add_product_stock import Ui_Form as add_product_stock_helper
from list_client import Ui_Form as list_client_helper
from report_order import Ui_Form as report_order_helper
from search_seller import Ui_Form as search_seller_helper
from change_stock_name import Ui_Form as change_stock_name_helper
from list_sellers import Ui_Form as list_sellers_helper
from list_order import Ui_Form as list_order_helper
from search_client import Ui_Form as search_client_helper
from new_client import Ui_Form as new_client_helper
from new_seller import Ui_Form as new_seller_helper
from new_order import Ui_Form as new_order_helper
from search_product import Ui_Form as search_product_helper
from report_product import Ui_Form as report_product_helper
from edit_client import Ui_Form as edit_client_helper
from search_order import Ui_Form as search_order_helper

import pdfkit
import sys
sys.path.append("../")

from db.recorder_db import RecorderDB
from tools.prototypes import FormPrototype

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 458, 212))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdministrador = QtWidgets.QMenu(self.menubar)
        self.menuAdministrador.setObjectName("menuAdministrador")
        self.menuClientes = QtWidgets.QMenu(self.menuAdministrador)
        self.menuClientes.setObjectName("menuClientes")
        self.menuProductos = QtWidgets.QMenu(self.menuAdministrador)
        self.menuProductos.setObjectName("menuProductos")
        self.menuVendedores = QtWidgets.QMenu(self.menuAdministrador)
        self.menuVendedores.setObjectName("menuVendedores")
        self.menuStock = QtWidgets.QMenu(self.menuAdministrador)
        self.menuStock.setObjectName("menuStock")
        self.menuPedido = QtWidgets.QMenu(self.menuAdministrador)
        self.menuPedido.setObjectName("menuPedido")
        self.menuConsulta = QtWidgets.QMenu(self.menubar)
        self.menuConsulta.setObjectName("menuConsulta")
        self.menuCliente = QtWidgets.QMenu(self.menuConsulta)
        self.menuCliente.setObjectName("menuCliente")
        self.menuVendedor = QtWidgets.QMenu(self.menuConsulta)
        self.menuVendedor.setObjectName("menuVendedor")
        self.menuAlmacen = QtWidgets.QMenu(self.menuConsulta)
        self.menuAlmacen.setObjectName("menuAlmacen")
        self.menuPedido_2 = QtWidgets.QMenu(self.menuConsulta)
        self.menuPedido_2.setObjectName("menuPedido_2")
        self.menuReporte = QtWidgets.QMenu(self.menubar)
        self.menuReporte.setObjectName("menuReporte")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.toolBar = QtWidgets.QToolBar(MainWindow)
        # self.toolBar.setObjectName("toolBar")
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # MainWindow.insertToolBarBreak(self.toolBar)
        self.actionCrear_Nuevo = QtWidgets.QAction(MainWindow)
        self.actionCrear_Nuevo.setObjectName("actionCrear_Nuevo")
        self.actionEditar = QtWidgets.QAction(MainWindow)
        self.actionEditar.setObjectName("actionEditar")
        self.actionCrear_Nuevo_2 = QtWidgets.QAction(MainWindow)
        self.actionCrear_Nuevo_2.setObjectName("actionCrear_Nuevo_2")
        self.actionEditar_2 = QtWidgets.QAction(MainWindow)
        self.actionEditar_2.setObjectName("actionEditar_2")
        self.actionCrear_Nuevo_3 = QtWidgets.QAction(MainWindow)
        self.actionCrear_Nuevo_3.setObjectName("actionCrear_Nuevo_3")
        self.actionEditar_3 = QtWidgets.QAction(MainWindow)
        self.actionEditar_3.setObjectName("actionEditar_3")
        self.actionA_adir = QtWidgets.QAction(MainWindow)
        self.actionA_adir.setObjectName("actionA_adir")
        self.actionNuevo_Pedido = QtWidgets.QAction(MainWindow)
        self.actionNuevo_Pedido.setObjectName("actionNuevo_Pedido")
        self.actionEditar_4 = QtWidgets.QAction(MainWindow)
        self.actionEditar_4.setObjectName("actionEditar_4")
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionEditar_5 = QtWidgets.QAction(MainWindow)
        self.actionEditar_5.setObjectName("actionEditar_5")
        self.actionCrear_Almacen = QtWidgets.QAction(MainWindow)
        self.actionCrear_Almacen.setObjectName("actionCrear_Almacen")
        self.actionCambiar_Nombre = QtWidgets.QAction(MainWindow)
        self.actionCambiar_Nombre.setObjectName("actionCambiar_Nombre")
        self.actionBsucar = QtWidgets.QAction(MainWindow)
        self.actionBsucar.setObjectName("actionBsucar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionBsucar_2 = QtWidgets.QAction(MainWindow)
        self.actionBsucar_2.setObjectName("actionBsucar_2")
        self.actionLista_de_Productos = QtWidgets.QAction(MainWindow)
        self.actionLista_de_Productos.setObjectName("actionLista_de_Productos")
        self.actionBuscar_2 = QtWidgets.QAction(MainWindow)
        self.actionBuscar_2.setObjectName("actionBuscar_2")
        self.actionReporte_de_Pedidos = QtWidgets.QAction(MainWindow)
        self.actionReporte_de_Pedidos.setObjectName("actionReporte_de_Pedidos")
        self.actionReporte_de_Productos = QtWidgets.QAction(MainWindow)
        self.actionReporte_de_Productos.setObjectName("actionReporte_de_Productos")
        self.menuClientes.addAction(self.actionCrear_Nuevo)
        self.menuClientes.addAction(self.actionEditar)
        self.menuProductos.addAction(self.actionCrear_Nuevo_2)
        self.menuProductos.addAction(self.actionEditar_2)
        self.menuVendedores.addAction(self.actionCrear_Nuevo_3)
        self.menuVendedores.addAction(self.actionEditar_3)
        self.menuStock.addAction(self.actionCrear_Almacen)
        self.menuStock.addAction(self.actionCambiar_Nombre)
        self.menuStock.addSeparator()
        self.menuStock.addAction(self.actionA_adir)
        self.menuPedido.addAction(self.actionNuevo)
        self.menuPedido.addAction(self.actionEditar_5)
        self.menuAdministrador.addAction(self.menuClientes.menuAction())
        self.menuAdministrador.addAction(self.menuProductos.menuAction())
        self.menuAdministrador.addAction(self.menuVendedores.menuAction())
        self.menuAdministrador.addAction(self.menuStock.menuAction())
        self.menuAdministrador.addAction(self.menuPedido.menuAction())
        self.menuCliente.addAction(self.actionBuscar)
        self.menuVendedor.addAction(self.actionBsucar_2)
        self.menuAlmacen.addAction(self.actionLista_de_Productos)
        self.menuPedido_2.addAction(self.actionBuscar_2)
        self.menuConsulta.addAction(self.menuCliente.menuAction())
        self.menuConsulta.addAction(self.menuVendedor.menuAction())
        self.menuConsulta.addAction(self.menuAlmacen.menuAction())
        self.menuConsulta.addAction(self.menuPedido_2.menuAction())
        self.menuReporte.addAction(self.actionReporte_de_Pedidos)
        self.menuReporte.addAction(self.actionReporte_de_Productos)
        self.menubar.addAction(self.menuAdministrador.menuAction())
        self.menubar.addAction(self.menuConsulta.menuAction())
        self.menubar.addAction(self.menuReporte.menuAction())

        self.retranslateUi(MainWindow)

        ##############################################################
        
        MainWindow.new_product_window = FormPrototype()
        helper = new_product_helper().setupUi(MainWindow.new_product_window)
        MainWindow.new_stock_window = FormPrototype()
        helper = new_stock_helper().setupUi(MainWindow.new_stock_window)
        MainWindow.edit_product_window = FormPrototype()
        helper = edit_product_helper().setupUi(MainWindow.edit_product_window)
        MainWindow.edit_order_window = FormPrototype()
        helper = edit_order_helper().setupUi(MainWindow.edit_order_window)
        MainWindow.edit_seller_window = FormPrototype()
        helper = edit_seller_helper().setupUi(MainWindow.edit_seller_window)
        MainWindow.add_product_stock_window = FormPrototype()
        helper = add_product_stock_helper().setupUi(MainWindow.add_product_stock_window)
        MainWindow.list_client_window = FormPrototype()
        helper = list_client_helper().setupUi(MainWindow.list_client_window)
        MainWindow.report_order_window = FormPrototype()
        helper = report_order_helper().setupUi(MainWindow.report_order_window)
        MainWindow.search_seller_window = FormPrototype()
        helper = search_seller_helper().setupUi(MainWindow.search_seller_window)
        MainWindow.change_stock_name_window = FormPrototype()
        helper = change_stock_name_helper().setupUi(MainWindow.change_stock_name_window)
        MainWindow.list_sellers_window = FormPrototype()
        helper = list_sellers_helper().setupUi(MainWindow.list_sellers_window)
        MainWindow.list_order_window = FormPrototype()
        helper = list_order_helper().setupUi(MainWindow.list_order_window)
        MainWindow.search_client_window = FormPrototype()
        helper = search_client_helper().setupUi(MainWindow.search_client_window)
        MainWindow.new_client_window = FormPrototype()
        helper = new_client_helper().setupUi(MainWindow.new_client_window)
        MainWindow.new_seller_window = FormPrototype()
        helper = new_seller_helper().setupUi(MainWindow.new_seller_window)
        MainWindow.new_order_window = FormPrototype()
        helper = new_order_helper().setupUi(MainWindow.new_order_window)
        MainWindow.search_product_window = FormPrototype()
        helper = search_product_helper().setupUi(MainWindow.search_product_window)
        MainWindow.report_product_window = FormPrototype()
        helper = report_product_helper().setupUi(MainWindow.report_product_window)
        MainWindow.edit_client_window = FormPrototype()
        helper = edit_client_helper().setupUi(MainWindow.edit_client_window)
        MainWindow.search_order_window = FormPrototype()
        helper = search_order_helper().setupUi(MainWindow.search_order_window)
        
        def createNewClient():
            MainWindow.new_client_window.show()
        def editClient():
            MainWindow.edit_client_window.show()
        def createNewProduct():
            MainWindow.new_product_window.show()
        def editProduct():
            MainWindow.edit_product_window.show()
        def createNewSeller():
            MainWindow.new_seller_window.show()
        def editSeller():
            MainWindow.edit_seller_window.show()
        def createNewOrder():
            MainWindow.new_order_window.show()
        def editOrder():
            MainWindow.edit_order_window.show()
        def addProductStock():
            MainWindow.add_product_stock_window.show()
        def createStock():
            MainWindow.new_stock_window.show()
        def changeStockName():
            MainWindow.change_stock_name_window.show()
        def changeCurrentDate():
            pass
        def searchClient():
            MainWindow.search_client_window.show()
        def searchSeller():
            MainWindow.search_seller_window.show()
        def listProducts():
            pass
        def searchOrder():
            MainWindow.search_order_window.show()
        def generateReportOrder():
            MainWindow.report_order_window.show()
        def generateReportProduct():
            MainWindow.report_product_window.show()

        MainWindow.createNewClient = createNewClient
        MainWindow.editClient = editClient
        MainWindow.createNewProduct = createNewProduct
        MainWindow.editProduct = editProduct
        MainWindow.createNewSeller = createNewSeller
        MainWindow.editSeller = editSeller
        MainWindow.createNewOrder = createNewOrder
        MainWindow.editOrder = editOrder
        MainWindow.addProductStock = addProductStock
        MainWindow.createStock = createStock
        MainWindow.changeStockName = changeStockName
        MainWindow.changeCurrentDate = changeCurrentDate
        MainWindow.searchClient = searchClient
        MainWindow.searchSeller = searchSeller
        MainWindow.listProducts = listProducts
        MainWindow.searchOrder = searchOrder
        MainWindow.generateReportOrder = generateReportOrder
        MainWindow.generateReportProduct = generateReportProduct
        ##############################################################
        
        self.actionCrear_Nuevo.triggered.connect(MainWindow.createNewClient)
        self.actionEditar.triggered.connect(MainWindow.editClient)
        self.actionCrear_Nuevo_2.triggered.connect(MainWindow.createNewProduct)
        self.actionEditar_2.triggered.connect(MainWindow.editProduct)
        self.actionCrear_Nuevo_3.triggered.connect(MainWindow.createNewSeller)
        self.actionEditar_3.triggered.connect(MainWindow.editSeller)
        self.actionNuevo.triggered.connect(MainWindow.createNewOrder)
        self.actionEditar_5.triggered.connect(MainWindow.editOrder)
        self.actionA_adir.triggered.connect(MainWindow.addProductStock)
        self.actionCrear_Almacen.triggered.connect(MainWindow.createStock)
        self.actionCambiar_Nombre.triggered.connect(MainWindow.changeStockName)
        self.pushButton.clicked.connect(MainWindow.changeCurrentDate)
        self.actionBuscar.triggered.connect(MainWindow.searchClient)
        self.actionBsucar_2.triggered.connect(MainWindow.searchSeller)
        self.actionLista_de_Productos.triggered.connect(MainWindow.listProducts)
        self.actionBuscar_2.triggered.connect(MainWindow.searchOrder)
        self.actionReporte_de_Pedidos.triggered.connect(MainWindow.generateReportOrder)
        self.actionReporte_de_Productos.triggered.connect(MainWindow.generateReportProduct)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recorder - EMMV"))
        self.pushButton.setText(_translate("MainWindow", "Cambiar Fecha"))
        self.menuAdministrador.setTitle(_translate("MainWindow", "Administrador"))
        self.menuClientes.setTitle(_translate("MainWindow", "Clientes"))
        self.menuProductos.setTitle(_translate("MainWindow", "Productos"))
        self.menuVendedores.setTitle(_translate("MainWindow", "Vendedores"))
        self.menuStock.setTitle(_translate("MainWindow", "Almacen"))
        self.menuPedido.setTitle(_translate("MainWindow", "Pedido"))
        self.menuConsulta.setTitle(_translate("MainWindow", "Consulta"))
        self.menuCliente.setTitle(_translate("MainWindow", "Cliente"))
        self.menuVendedor.setTitle(_translate("MainWindow", "Vendedor"))
        self.menuAlmacen.setTitle(_translate("MainWindow", "Almacen"))
        self.menuPedido_2.setTitle(_translate("MainWindow", "Pedido"))
        self.menuReporte.setTitle(_translate("MainWindow", "Reporte"))
        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCrear_Nuevo.setText(_translate("MainWindow", "Crear Nuevo"))
        self.actionEditar.setText(_translate("MainWindow", "Editar"))
        self.actionCrear_Nuevo_2.setText(_translate("MainWindow", "Crear Nuevo"))
        self.actionEditar_2.setText(_translate("MainWindow", "Editar"))
        self.actionCrear_Nuevo_3.setText(_translate("MainWindow", "Crear Nuevo"))
        self.actionEditar_3.setText(_translate("MainWindow", "Editar"))
        self.actionA_adir.setText(_translate("MainWindow", "Añadir Producto"))
        self.actionNuevo_Pedido.setText(_translate("MainWindow", "Nuevo"))
        self.actionEditar_4.setText(_translate("MainWindow", "Editar"))
        self.actionNuevo.setText(_translate("MainWindow", "Crear Nuevo"))
        self.actionEditar_5.setText(_translate("MainWindow", "Editar"))
        self.actionCrear_Almacen.setText(_translate("MainWindow", "Crear Almacen"))
        self.actionCambiar_Nombre.setText(_translate("MainWindow", "Cambiar Nombre"))
        self.actionBsucar.setText(_translate("MainWindow", "Buscar"))
        self.actionBuscar.setText(_translate("MainWindow", "Buscar"))
        self.actionBsucar_2.setText(_translate("MainWindow", "Buscar"))
        self.actionLista_de_Productos.setText(_translate("MainWindow", "Lista de Productos"))
        self.actionBuscar_2.setText(_translate("MainWindow", "Buscar"))
        self.actionReporte_de_Pedidos.setText(_translate("MainWindow", "Reporte de Pedidos"))
        self.actionReporte_de_Productos.setText(_translate("MainWindow", "Reporte de Productos"))

    def setDB(self,MainWindow):
        db = RecorderDB(MainWindow.db_dir)
        MainWindow.new_product_window.db = db
        MainWindow.new_stock_window.db = db
        MainWindow.edit_product_window.db = db
        MainWindow.edit_order_window.db = db
        MainWindow.edit_seller_window.db = db
        MainWindow.add_product_stock_window.db = db
        MainWindow.list_client_window.db = db
        MainWindow.report_order_window.db = db
        MainWindow.search_seller_window.db = db
        MainWindow.change_stock_name_window.db = db
        MainWindow.list_sellers_window.db = db
        MainWindow.list_order_window.db = db
        MainWindow.search_client_window.db = db
        MainWindow.new_client_window.db = db
        MainWindow.new_seller_window.db = db
        MainWindow.new_order_window.db = db
        MainWindow.search_product_window.db = db
        MainWindow.report_product_window.db = db
        MainWindow.edit_client_window.db = db
        MainWindow.search_order_window.db = db

    def setCurrDate(self,MainWindow):
        MainWindow.new_product_window.curr_date = MainWindow.curr_date
        MainWindow.new_stock_window.curr_date = MainWindow.curr_date
        MainWindow.edit_product_window.curr_date = MainWindow.curr_date
        MainWindow.edit_order_window.curr_date = MainWindow.curr_date
        MainWindow.edit_seller_window.curr_date = MainWindow.curr_date
        MainWindow.add_product_stock_window.curr_date = MainWindow.curr_date
        MainWindow.list_client_window.curr_date = MainWindow.curr_date
        MainWindow.report_order_window.curr_date = MainWindow.curr_date
        MainWindow.search_seller_window.curr_date = MainWindow.curr_date
        MainWindow.change_stock_name_window.curr_date = MainWindow.curr_date
        MainWindow.list_sellers_window.curr_date = MainWindow.curr_date
        MainWindow.list_order_window.curr_date = MainWindow.curr_date
        MainWindow.search_client_window.curr_date = MainWindow.curr_date
        MainWindow.new_client_window.curr_date = MainWindow.curr_date
        MainWindow.new_seller_window.curr_date = MainWindow.curr_date
        MainWindow.new_order_window.curr_date = MainWindow.curr_date
        MainWindow.search_product_window.curr_date = MainWindow.curr_date
        MainWindow.report_product_window.curr_date = MainWindow.curr_date
        MainWindow.edit_client_window.curr_date = MainWindow.curr_date
        MainWindow.search_order_window.curr_date = MainWindow.curr_date

    def setWkhtmltopdf(self,MainWindow):
        config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
        
