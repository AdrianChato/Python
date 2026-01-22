#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        self.accion_mensaje = QAction(QIcon.fromTheme("dialog-information"), "Mostrar mensaje", self)
        self.accion_mensaje.setShortcut("Ctrl+M")
        self.accion_mensaje.setWhatsThis("Muestra un mensaje en la consola")
        self.accion_mensaje.triggered.connect(self.mostrar_mensaje)

        self.accion_titulo = QAction(QIcon.fromTheme("document-edit"), "Cambiar título", self)
        self.accion_titulo.setShortcut("Ctrl+L")
        self.accion_titulo.setWhatsThis("Cambia el título de la ventana")
        self.accion_titulo.triggered.connect(self.cambiar_titulo)

        self.accion_desactivar = QAction(QIcon.fromTheme("edit-clear"), "Desactivar acciones", self)
        self.accion_desactivar.setShortcut("Ctrl+D")
        self.accion_desactivar.setWhatsThis("Desactiva las acciones de mensaje y título")
        self.accion_desactivar.triggered.connect(self.desactivar_acciones)

        self.accion_activar = QAction(QIcon.fromTheme("edit-undo"), "Activar acciones", self)
        self.accion_activar.setShortcut("Ctrl+A")
        self.accion_activar.setWhatsThis("Activa las acciones de mensaje y título")
        self.accion_activar.triggered.connect(self.activar_acciones)

        menu_archivo = self.menuBar().addMenu("Archivo")
        menu_archivo.addAction(self.accion_mensaje)
        menu_archivo.addAction(self.accion_titulo)
        menu_archivo.addAction(self.accion_desactivar)

        barra_principal = QToolBar("Barra principal")
        barra_principal.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_principal.addAction(self.accion_mensaje)
        barra_principal.addAction(self.accion_titulo)
        barra_principal.addAction(self.accion_desactivar)
        self.addToolBar(barra_principal)

        barra_secundaria = QToolBar("Barra secundaria")
        barra_secundaria.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_secundaria.addAction(self.accion_activar)
        self.addToolBar(Qt.LeftToolBarArea, barra_secundaria)

    def mostrar_mensaje(self):
        print("Hola, viva españa")

    def cambiar_titulo(self):
        self.setWindowTitle("Título cambiado")

    def desactivar_acciones(self):
        self.accion_mensaje.setEnabled(False)
        self.accion_titulo.setEnabled(False)

    def activar_acciones(self):
        self.accion_mensaje.setEnabled(True)
        self.accion_titulo.setEnabled(True)

app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()