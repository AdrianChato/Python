#Adrián Solís León 2ºDAM

import os
import platform
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio - Componentes flotantes")

        self.setCentralWidget(QLabel("Área principal de la aplicación"))

        dock1 = QDockWidget("Panel 1", self)
        dock1.setWidget(QTextEdit("Panel de notas"))
        dock1.setFeatures(QDockWidget.NoDockWidgetFeatures)  
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget("Panel 2", self)
        dock2.setWidget(QLabel("Panel de estado"))
        dock2.setFeatures(QDockWidget.DockWidgetFloatable)  
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        dock3 = QDockWidget("Panel 3", self)
        dock3.setWidget(QLabel("Panel de ayuda"))
        dock3.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

        # --- BARRA DE ESTADO ---
        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel(platform.system()))
        barra_estado.showMessage("Listo. Paneles creados correctamente.")

        # --- MENÚ Y ACCIÓN ---
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menú")

        ruta_icono = os.path.join(os.path.dirname(__file__), "imprimir.png")
        accion = QAction(QIcon(ruta_icono), "Imprimir por consola", self)
        accion.setStatusTip("Imprimir por consola")
        accion.setShortcut(QKeySequence("Ctrl+P"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

        # --- BARRA DE HERRAMIENTAS ---
        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

    def imprimir_por_consola(self):
        print("Acción lanzada desde el menú, el atajo o la barra de herramientas.")

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()