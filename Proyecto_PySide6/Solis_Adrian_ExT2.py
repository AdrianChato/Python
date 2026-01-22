#Adrián Solís León 2ºDAM

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,QLineEdit, QTextEdit, QComboBox,
    QFormLayout, QVBoxLayout, QPushButton,
    QToolBar, QStatusBar, QMessageBox, QDockWidget, QDialog)   
# Importar lo necesario


# ===================================================================
#                            LOGIN
# ===================================================================
class DialogoLogin(QDialog):
    def __init__(self, parent=None):

        #Creamos lo necesario para hacer el login
        super().__init__()
        self.setWindowTitle("Inicio de sesión")

        layout = QVBoxLayout()

        self.campo_usuario = QLineEdit()
        self.campo_usuario.setPlaceholderText("Usuario")
        layout.addWidget(self.campo_usuario)

        self.campo_password = QLineEdit()
        self.campo_password.setPlaceholderText("Contraseña")
        self.campo_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.campo_password)

        boton_validar = QPushButton("Iniciar sesión")
        boton_validar.clicked.connect(self.validar)
        layout.addWidget(boton_validar)

        self.setLayout(layout)
    #creamos y hacemos la función para validar el login
    def validar(self):
        password = self.campo_password.text()

        if password == "interfaces":
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "La contraseña es incorrecta")


        # TODO: Crear el diseño y los widgets del diálogo de login


# ===================================================================
#                        VENTANA PRINCIPAL
# ===================================================================
class VentanaPrincipal(QMainWindow):

    #Creamos la ventana principal con todo
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encuesta de satisfacción")
        self.setMinimumSize(800, 600)

        # TODO: declarar variables necesarias

        self.crear_central()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
        self.crear_dock_notas()
        self.conectar_senales()

    # ---------------------------------------------------------------
    #Widget Central
    def crear_central(self):
        widget_central = QWidget()
        

        # Crear widgets
        self.line_edit_nombre = QLineEdit()
        self.line_edit_nombre.setPlaceholderText("Inicia Sesion para rellenar el nombre")
        self.line_edit_nombre.setMaxLength(60)
        
        self.line_edit_telefono = QLineEdit()
        self.line_edit_telefono.setPlaceholderText("Número de teléfono")
        self.line_edit_telefono.setMaxLength(60)  # longitud máxima

        self.combo_compañia = QComboBox()
        self.combo_compañia.addItems(["Orange", "Jazztel", "Movistar"])

        self.combo_satisfaccion = QComboBox()
        self.combo_satisfaccion.addItems(["Baja", "Media", "Alta"])



        # Layouts
        layout_form = QFormLayout()
        # Añadimos los datos con QFormLayout
        layout_form.addRow("Nombre:", self.line_edit_nombre)
        layout_form.addRow("Teléfono:", self.line_edit_telefono)
        layout_form.addRow("Compañia:", self.combo_compañia)
        layout_form.addRow("Satisfacción Global:", self.combo_satisfaccion)

        # Para la prioridad creamos un layout horizontal

        # Layout principal vertical que incluye el formulario y el QTextEdit
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_form)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)
        pass

    # ---------------------------------------------------------------
    def crear_dock_notas(self):
        #Creamos el Dock abajo
        dock1 = QDockWidget("Notas Internas", self)
        dock1.setWidget(QTextEdit("Notas internas sobre esta encuesta..."))
        dock1.setMinimumWidth(50)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock1)
        pass

    # ---------------------------------------------------------------
    def crear_acciones(self):
        #Creamos todas las acctiones
        self.accion_iniciar_sesion = QAction("Iniciar Sesión", self)
        self.accion_iniciar_sesion.triggered.connect(self.slot_login)

        self.accion_limpiar_encuesta = QAction("Nueva Encuesta", self)
        self.accion_limpiar_encuesta.setShortcut("Ctrl+N")
        self.accion_limpiar_encuesta.triggered.connect(self.slot_nueva_encuesta)

        self.accion_ver_resumen = QAction("Ver Resumen", self)
        self.accion_ver_resumen.triggered.connect(self.slot_ver_resumen)

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.slot_salir)

        self.accion_acerca_de = QAction("Acerca de...", self)
        self.accion_acerca_de.triggered.connect(self.slot_acerca_de)
        pass

    # ---------------------------------------------------------------
    def crear_menus(self):
        #Creamos el menú y le añadimos sus acciones
        barra_menus = self.menuBar()

        menu_archivo = barra_menus.addMenu("&Encuesta")
        menu_archivo.addAction(self.accion_iniciar_sesion)
        menu_archivo.addAction(self.accion_limpiar_encuesta)
        menu_archivo.addAction(self.accion_ver_resumen)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)

        menu_ayuda = barra_menus.addMenu("&Ayuda")
        menu_ayuda.addAction(self.accion_acerca_de)
        pass

    # ---------------------------------------------------------------
    def crear_toolbar(self):
        #Creamos la barra de herramientas
        toolbar = QToolBar("Barra herramientas")
        toolbar.setMovable(True)
        toolbar.addAction(self.accion_limpiar_encuesta)
        toolbar.addAction(self.accion_ver_resumen)
        self.addToolBar(toolbar)
        pass

    # ---------------------------------------------------------------
    def crear_statusbar(self):
        #Creamos la barra de estado
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)
        self.statusBar().showMessage("Listo")
        pass

    # ---------------------------------------------------------------
    def conectar_senales(self):
        # Cuando cambia el texto del título -> slot_titulo_cambiado
        #self.line_edit_titulo.textChanged.connect(self.slot_titulo_cambiado)

        # Cuando cambia la categoría -> slot_categoria_cambiada
        self.combo_compañia.currentTextChanged.connect(self.slot_compania_cambiada)
        self.combo_satisfaccion.currentTextChanged.connect(self.slot_satisfaccion_cambiada)
        self.combo_compañia.currentTextChanged.connect(self.slot_compania_cambiada)

        # Prioridades: conectamos toggled para ambos radio buttons
        #self.radio_prioridad_normal.toggled.connect(self.slot_prioridad_cambiada)
        #self.radio_prioridad_alta.toggled.connect(self.slot_prioridad_cambiada)
        pass

    # ---------------------------------------------------------------
    def slot_login(self):

        login = DialogoLogin()
        resultado = login.exec()

        if resultado == QDialog.Accepted:
            ventana = VentanaPrincipal()
            ventana.showMaximized()
            app.exec()
        else:
            app.exit()

    # ---------------------------------------------------------------
    def slot_nueva_encuesta(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar limpieza",
            "¿Estás seguro de que quieres limpiar la encuesta?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:

            self.statusBar().showMessage("Encuesta limpiada", 3000)
        pass

    # ---------------------------------------------------------------
    def slot_ver_resumen(self):
        QMessageBox.information(
            self,
            "Encuesta de compañias móviles",
            "Nombre: Adrián Solís \n\nCompañia: Orange\nSatisfacción global: Mala"
        )
        pass

    # ---------------------------------------------------------------
    def slot_salir(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar salida",
            "¿Quieres salir de la aplicación?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            QApplication.quit()
        pass

    # ---------------------------------------------------------------
    def slot_acerca_de(self):
        QMessageBox.information(
            self,
            "Encuesta de compañias móviles",
            "Acerca de la encuesta de compañias móviles \n\nExamen de PySide6\n2ºDAM"
        )
        pass

    # ---------------------------------------------------------------
    def slot_compania_cambiada(self, nueva):
        # Mostrar compañia en la barra de estado
        self.statusBar().showMessage(f"Compañia: {nueva}", 2000)
        pass

    # ---------------------------------------------------------------
    def slot_satisfaccion_cambiada(self, nueva):
        # Mostrar Satisfacción en la barra de estado
        self.statusBar().showMessage(f"Satisfacción: {nueva}", 2000)
        pass

    # ---------------------------------------------------------------
    def slot_recomienda_cambiado(self, checked):
        # TODO: Mensaje en la barra de estado
        pass

    # ---------------------------------------------------------------
    def slot_nombre_cambiado(self, nuevo_nombre):
        ventana_titulo = "Compañia de teléfono móvil"
        if nuevo_nombre.strip():
            ventana_titulo = f"{nuevo_nombre} - Compañia de teléfono móvil"
        self.setWindowTitle(ventana_titulo)
        pass


# ===================================================================
#                       EJECUCIÓN DE LA APP
# ===================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

