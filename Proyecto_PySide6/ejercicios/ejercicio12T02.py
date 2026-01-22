#Adrián Solís León 2ºDAM

import os
import platform
import getpass
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menú, barra de herramientas y barra de estado")

        # --- MENÚ ---
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Archivo")

        
        ruta_icono_mensaje = os.path.join(os.path.dirname(__file__), "imprimir.png")
        accion_mensaje = QAction(QIcon(ruta_icono_mensaje), "Mostrar mensaje temporal", self)
        accion_mensaje.setShortcut(QKeySequence("Ctrl+T"))
        accion_mensaje.setStatusTip("Mostrar mensaje temporal en la barra de estado")
        accion_mensaje.triggered.connect(self.mostrar_mensaje_temporal)

        
        ruta_icono_limpiar = os.path.join(os.path.dirname(__file__), "imprimir.png")
        accion_limpiar = QAction(QIcon(ruta_icono_limpiar), "Limpiar mensaje", self)
        accion_limpiar.setShortcut(QKeySequence("Ctrl+L"))
        accion_limpiar.setStatusTip("Limpiar mensaje de la barra de estado")
        accion_limpiar.triggered.connect(self.limpiar_mensaje)

        
        ruta_icono_sistema = os.path.join(os.path.dirname(__file__), "imprimir.png")
        accion_sistema = QAction(QIcon(ruta_icono_sistema), "Mostrar información del sistema", self)
        accion_sistema.setShortcut(QKeySequence("Ctrl+I"))
        accion_sistema.setStatusTip("Mostrar información del sistema operativo")
        accion_sistema.triggered.connect(self.mostrar_informacion_sistema)

        menu.addAction(accion_mensaje)
        menu.addAction(accion_limpiar)
        menu.addAction(accion_sistema)

        # --- BARRA DE HERRAMIENTAS ---
        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(accion_mensaje)
        barra_herramientas.addAction(accion_limpiar)
        barra_herramientas.addAction(accion_sistema)
        self.addToolBar(barra_herramientas)

        # --- BARRA DE ESTADO ---
        self.barra_estado = self.statusBar()

        # Componente permanente con el nombre del usuario
        usuario = getpass.getuser()
        self.barra_estado.addPermanentWidget(QLabel(f"Usuario: {usuario}"))

        # Mensaje inicial (2 segundos)
        self.barra_estado.showMessage("Aplicación iniciada correctamente", 2000)

        # --- QTimer para alternar mensajes ---
        self.mensajes = ["Esperando acción...", "Listo para trabajar"]
        self.indice_mensaje = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.alternar_mensaje)
        self.timer.start(6000)

    def mostrar_mensaje_temporal(self):
        self.barra_estado.showMessage("Mensaje temporal: desaparece en 3 segundos", 3000)

    def limpiar_mensaje(self):
        self.barra_estado.clearMessage()

    def mostrar_informacion_sistema(self):
        sistema = platform.system()
        self.barra_estado.addWidget(QLabel(f"Sistema: {sistema}"))

    def alternar_mensaje(self):
        self.barra_estado.showMessage(self.mensajes[self.indice_mensaje], 3000)
        self.indice_mensaje = (self.indice_mensaje + 1) % len(self.mensajes)


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()