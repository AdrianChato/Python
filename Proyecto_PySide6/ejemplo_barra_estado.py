import os
import platform
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menú, barra de herramientas y barra de estado")

        # --- MENÚ ---
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menú")

        ruta_icono = os.path.join(os.path.dirname(__file__), "imprimir.png")
        accion = QAction(QIcon(ruta_icono), "Imprimir por consola", self)
        accion.setWhatsThis("Imprime un texto por consola al pulsar el botón o el atajo.")
        accion.setStatusTip("Imprimir por consola")
        accion.setShortcut(QKeySequence("Ctrl+P"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

        # --- BARRA DE HERRAMIENTAS ---
        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

        # --- BARRA DE ESTADO ---
        barra_estado = self.statusBar()

        # Añadimos un componente permanente con el nombre del sistema operativo
        barra_estado.addPermanentWidget(QLabel(platform.system()))

        # Mostramos un mensaje temporal (3 segundos)
        barra_estado.showMessage("Listo. Esperando acción...", 3000)

    def imprimir_por_consola(self):
        print("Acción lanzada desde el menú, el atajo o la barra de herramientas.")

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()