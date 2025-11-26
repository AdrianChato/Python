import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QComboBox,
    QRadioButton,
    QTextEdit,
    QMessageBox,
    QVBoxLayout,
    QFormLayout,
    QToolBar,
    QStatusBar
)
from PySide6.QtGui import QAction,QKeySequence
from PySide6.QtCore import Qt


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # TODO: tÃ­tulo y tamaÃ±o mÃ­nimo de la ventana
        self.setWindowTitle("Prueba Examen")


        widget_central = QWidget()
        texto = QLineEdit()
        texto.textChanged.connect(self.conectar_senales)
        

        combo = QComboBox()
        combo.addItems(["Trabajo", "Ideas", "Otros"])
        combo.currentTextChanged.connect(self.conectar_senales)

        boton1 = QRadioButton("Normal")
        boton2 = QRadioButton("Alta")
        boton1.isChecked()
        boton1.toggled.connect(self.conectar_senales)
        boton2.toggled.connect(self.conectar_senales)

        nota = QTextEdit()
        nota.setPlaceholderText("Escribe aquí tu nota...")

        nota.textChanged.connect(self.conectar_senales)

        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("Archivo")
        #menu_archivo.addAction(...)
        accion = QAction("Imprimir nota", self)
        accion.setShortcut(QKeySequence("Ctrl+P"))  # Atajo de teclado
        accion.triggered.connect(self.imprimir_en_consola)
        accion2 = QAction("Limpiar nota", self)
        accion2.setShortcut(QKeySequence("Ctrl+L"))  # Atajo de teclado
        accion2.triggered.connect(self.limpiar_contenido_nota)
        accion3 = QAction("Salir", self)
        accion3.setShortcut(QKeySequence("Ctrl+X"))  # Atajo de teclado
        accion3.triggered.connect(self.slot_salir)
        menu_archivo.addAction(accion)
        menu_archivo.addAction(accion2)
        menu_archivo.addAction(accion3)
        menu_ayuda = barra_menus.addMenu("Ayuda")
        accion4 = QAction("Acerca de...", self)
        accion4.setShortcut(QKeySequence("Ctrl+U"))  # Atajo de teclado
        accion4.triggered.connect(self.slot_acerca_de)
        menu_ayuda.addAction(accion4)
        #menu_ayuda.addAction(...)


        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(accion)
        barra_herramientas.addAction(accion2)
        self.addToolBar(barra_herramientas)

        self.accion_limpiar_nota = QAction("Limpiar nota", self)
        #self.accion_limpiar_nota.triggered.connect(...)

        # TODO: crear layouts (formulario + layout principal)
        layout_form = QFormLayout()
        layout_principal = QVBoxLayout()

        layout_form.addWidget(texto)
        layout_form.addWidget(combo)
        layout_form.addWidget(boton1)
        layout_form.addWidget(boton2)
        layout_form.addWidget(nota)

        # TODO: aÃ±adir widgets al layout del formulario

        # TODO: aÃ±adir layouts al layout principal
        layout_principal.addLayout(layout_form)
        # TODO: setLayout del widget central
        widget_central.setLayout(layout_principal)

        self.setCentralWidget(widget_central)
        #self.setMinimumSize("300")

        # TODO: declarar atributos de widgets (title, categoria, prioridad, area de texto)
        # self.line_edit_titulo = None
        # ...

        # TODO: declarar acciones (limpiar, imprimir, salir, acerca de)
        # self.accion_limpiar_nota = None
        # ...

        # ConstrucciÃ³n general
        #self.crear_central()       # TODO: completar
        #self.crear_acciones()      # TODO: completar
        #self.crear_menus()         # TODO: completar
        #self.crear_toolbar()       # TODO: completar
        #self.crear_statusbar()     # TODO: completar
        #self.conectar_senales()    # TODO: completar

    # =========================
    # CREACIÃ“N DE LA ZONA CENTRAL
    # =========================
    def crear_central(self):
        widget_central = QWidget()

        texto = QLineEdit()
        texto.textChanged.connect(self.conectar_senales)
        

        combo = QComboBox()
        combo.addItems(["Trabajo", "Ideas", "Otros"])
        combo.currentTextChanged.connect(self.conectar_senales)

        boton1 = QRadioButton("Normal")
        boton2 = QRadioButton("Alta")
        boton1.isChecked()
        boton1.toggled.connect(self.conectar_senales)
        boton2.toggled.connect(self.conectar_senales)

        nota = QTextEdit()
        nota.setPlaceholderText("Escribe aquí tu nota...")

        nota.textChanged.connect(self.conectar_senales)

        # TODO: crear layouts (formulario + layout principal)
        layout_form = QFormLayout()
        layout_principal = QVBoxLayout()

        layout_form.addWidget(texto)
        layout_form.addWidget(combo)
        layout_form.addWidget(boton1)
        layout_form.addWidget(boton2)
        layout_form.addWidget(nota)

        # TODO: aÃ±adir widgets al layout del formulario

        # TODO: aÃ±adir layouts al layout principal
        layout_principal.addLayout(layout_form)
        # TODO: setLayout del widget central
        widget_central.setLayout(layout_principal)

        self.setCentralWidget(widget_central)

    # =========================
    # ACCIONES, MENÃš Y TOOLBAR
    # =========================
    def crear_acciones(self):
        # TODO: crear acciones (QAction) con texto y atajos
        self.accion_limpiar_nota = QAction("Limpiar nota", self)
        self.accion_limpiar_nota.triggered.connect(...)
        pass

    def crear_menus(self):
        # TODO: crear la barra de menÃºs y aÃ±adir los menÃºs Archivo y Ayuda
        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("Archivo")
        menu_archivo.addAction(...)
        menu_ayuda = barra_menus.addMenu("Acerca de...")
        menu_ayuda.addAction(...)
        pass

    def crear_toolbar(self):
        # TODO: crear barra de herramientas y aÃ±adir las acciones bÃ¡sicas
        toolbar = QToolBar()
        toolbar.addAction(...)
        pass

    def crear_statusbar(self):
        # TODO: crear barra de estado y mostrar un mensaje inicial
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)
        pass

    # =========================
    # SEÃ‘ALES
    # =========================
    def conectar_senales(self):
        # TODO conectar seÃ±ales como textChanged, currentTextChanged, toggled...
        pass

    # =========================
    # FUNCIONES DE UTILIDAD
    # =========================
    def obtener_prioridad_actual(self):
        # TODO devolver prioridad actual
        prioridad = ""
        return prioridad    # Ãºnico return

    def limpiar_contenido_nota(self):
        # TODO borrar tÃ­tulo, categorÃ­a, prioridad y contenido
        pass

    def imprimir_en_consola(self):
        # TODO imprimir la nota completa usando print con comas
        pass

    # =========================
    # SLOTS (LOGICA)
    # =========================
    def slot_limpiar_nota(self):
        # TODO mostrar cuadro de confirmaciÃ³n y limpiar si aceptan
        pass

    def slot_imprimir_nota(self):
        # TODO llamar a imprimir_en_consola y mostrar mensaje
        pass

    def slot_salir(self):
        # TODO pedir confirmaciÃ³n antes de cerrar
        pass

    def slot_acerca_de(self):
        # TODO mostrar QMessageBox.information
        pass

    def slot_titulo_cambiado(self, nuevo_titulo):
        # TODO actualizar tÃ­tulo de la ventana y barra de estado
        pass

    def slot_categoria_cambiada(self, nueva_categoria):
        # TODO mostrar categorÃ­a en la barra
        pass

    def slot_prioridad_cambiada(self, checked):
        # TODO reaccionar solo si checked es True
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()