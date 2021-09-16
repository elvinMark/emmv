import tinydb
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Windows apperance
        self.setWindowTitle("Recorder - EMMV")
        self.resize(500,500)

        # Help Windows
        self.create_product = CreateProduct()
        self.edit_product = EditProduct()
        self.create_client = CreateClient()
        self.edit_client = EditClient()
        self.create_seller = CreateSeller()
        self.edit_seller = EditSeller()
        
        # Menu Bar
        menuBar = QMenuBar(self)

        # Admin Menu
        adminMenu = QMenu("Administrador",self)

        # Product Sub Menu
        productSubMenu = QMenu("Productos",self)
        createNewProductAction = QAction("Crear",self)
        createNewProductAction.triggered.connect(self.create_product.show)
        editProductAction = QAction("Editar",self)
        editProductAction.triggered.connect(self.edit_product.show)
        productSubMenu.addAction(createNewProductAction)
        productSubMenu.addAction(editProductAction)

        # Stock Sub Menu
        stockSubMenu = QMenu("Almacen",self)
        
        # Client Sub Menu
        clientSubMenu = QMenu("Clientes",self)
        createNewClientAction = QAction("Crear",self)
        createNewClientAction.triggered.connect(self.create_client.show)
        editClientAction = QAction("Editar",self)
        editClientAction.triggered.connect(self.edit_client.show)
        clientSubMenu.addAction(createNewClientAction)
        clientSubMenu.addAction(editClientAction)

        # Seller Sub Menu
        sellersSubMenu = QMenu("Vendedores",self)
        createNewSellerAction = QAction("Crear",self)
        createNewSellerAction.triggered.connect(self.create_seller.show)
        editSellerAction = QAction("Editar",self)
        editSellerAction.triggered.connect(self.edit_seller.show)
        sellersSubMenu.addAction(createNewSellerAction)
        sellersSubMenu.addAction(editSellerAction)

        # Adding the sub menus to Admin menu
        adminMenu.addMenu(productSubMenu)
        adminMenu.addMenu(stockSubMenu)
        adminMenu.addMenu(clientSubMenu)
        adminMenu.addMenu(sellersSubMenu)

        # Adding the Admin menu to the Menu Bar
        menuBar.addMenu(adminMenu)

        # Adding the consult menu to the Menu Bar
        consultMenu = QMenu("Consulta",self)
        menuBar.addMenu(consultMenu)

        # Adding the Help menu to the Menu Bar
        helpMenu = QMenu("Ayuda",self)
        menuBar.addMenu(helpMenu)

        # Adding the Menu Bar to the Window
        self.setMenuBar(menuBar)

    def closeEvent(self,event):
        self.create_product.close()
        self.edit_product.close()
        self.create_client.close()
        self.edit_client.close()
        self.create_seller.close()
        self.edit_seller.close()

class CreateProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Nuevo Producto")
        self.resize(500,300)

        layout = QVBoxLayout()
        
        nameLayout = QHBoxLayout()
        nameProductLabel = QLabel("Nombre del Producto:",self)
        nameProductText = QTextEdit(parent=self)
        nameLayout.addWidget(nameProductLabel)
        nameLayout.addWidget(nameProductText)

        priceLayout = QHBoxLayout()
        priceProductLabel = QLabel("Precio del Producto:",self)
        priceProductText = QTextEdit(parent=self)
        priceLayout.addWidget(priceProductLabel)
        priceLayout.addWidget(priceProductText)

        layout.addLayout(nameLayout)
        layout.addLayout(priceLayout)
        
        self.setLayout(layout)
        
class EditProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editar Producto")
        self.resize(500,300)

class CreateClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Nuevo Cliente")
        self.resize(500,300)

class EditClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editar Cliente")
        self.resize(500,300)

class CreateSeller(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Nuevo Vendedor")
        self.resize(500,300)

class EditSeller(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editar Vendedor")
        self.resize(500,300)
