import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLineEdit, QTextEdit, QComboBox,
    QRadioButton, QFormLayout, QVBoxLayout,
    QHBoxLayout, QToolBar, QStatusBar, QMessageBox
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título y tamaño mínimo
        self.setWindowTitle("Mini Bloc de Notas")
        self.setMinimumSize(700, 500)

        # Widgets del formulario (declarados como atributos)
        self.line_edit_titulo = None
        self.combo_categoria = None
        self.radio_prioridad_normal = None
        self.radio_prioridad_alta = None
        self.texto_nota = None

        # Acciones
        self.accion_limpiar_nota = None
        self.accion_imprimir_nota = None
        self.accion_salir = None
        self.accion_acerca_de = None

        # Construcción de la ventana
        self.crear_central()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
        self.conectar_senales()

    # =========================
    # ZONA CENTRAL
    # =========================
    def crear_central(self):
        widget_central = QWidget()

        # Crear widgets
        self.line_edit_titulo = QLineEdit()
        self.line_edit_titulo.setPlaceholderText("Título de la nota...")
        self.line_edit_titulo.setMaxLength(60)  # longitud máxima

        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Trabajo", "Ideas", "Otros"])

        self.radio_prioridad_normal = QRadioButton("Normal")
        self.radio_prioridad_alta = QRadioButton("Alta")
        self.radio_prioridad_normal.setChecked(True)  # Normal por defecto

        self.texto_nota = QTextEdit()
        self.texto_nota.setPlaceholderText("Escribe aquí el contenido de la nota...")

        # Layouts
        layout_form = QFormLayout()
        # Añadimos título y categoría con QFormLayout
        layout_form.addRow("Título:", self.line_edit_titulo)
        layout_form.addRow("Categoría:", self.combo_categoria)

        # Para la prioridad creamos un layout horizontal
        layout_prioridad = QHBoxLayout()
        layout_prioridad.addWidget(self.radio_prioridad_normal)
        layout_prioridad.addWidget(self.radio_prioridad_alta)
        layout_form.addRow("Prioridad:", layout_prioridad)

        # Layout principal vertical que incluye el formulario y el QTextEdit
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_form)
        layout_principal.addWidget(self.texto_nota)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    # =========================
    # ACCIONES
    # =========================
    def crear_acciones(self):
        # Crear acciones con texto, icono opcional y atajo
        self.accion_limpiar_nota = QAction("Limpiar nota", self)
        self.accion_limpiar_nota.setShortcut("Ctrl+L")
        self.accion_limpiar_nota.triggered.connect(self.slot_limpiar_nota)

        self.accion_imprimir_nota = QAction("Imprimir nota", self)
        self.accion_imprimir_nota.setShortcut("Ctrl+P")
        self.accion_imprimir_nota.triggered.connect(self.slot_imprimir_nota)

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.slot_salir)

        self.accion_acerca_de = QAction("Acerca de...", self)
        self.accion_acerca_de.triggered.connect(self.slot_acerca_de)

    # =========================
    # MENÚS
    # =========================
    def crear_menus(self):
        barra_menus = self.menuBar()

        menu_archivo = barra_menus.addMenu("&Archivo")
        menu_archivo.addAction(self.accion_limpiar_nota)
        menu_archivo.addAction(self.accion_imprimir_nota)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)

        menu_ayuda = barra_menus.addMenu("&Ayuda")
        menu_ayuda.addAction(self.accion_acerca_de)

    # =========================
    # TOOLBAR
    # =========================
    def crear_toolbar(self):
        toolbar = QToolBar("Barra herramientas")
        toolbar.setMovable(False)
        # Opcional: iconos si se tuvieran (aquí utilizamos los textos)
        toolbar.addAction(self.accion_limpiar_nota)
        toolbar.addAction(self.accion_imprimir_nota)
        self.addToolBar(toolbar)

    # =========================
    # STATUSBAR
    # =========================
    def crear_statusbar(self):
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)
        self.statusBar().showMessage("Listo")  # mensaje inicial

    # =========================
    # SEÑALES
    # =========================
    def conectar_senales(self):
        # Cuando cambia el texto del título -> slot_titulo_cambiado
        self.line_edit_titulo.textChanged.connect(self.slot_titulo_cambiado)

        # Cuando cambia la categoría -> slot_categoria_cambiada
        self.combo_categoria.currentTextChanged.connect(self.slot_categoria_cambiada)

        # Prioridades: conectamos toggled para ambos radio buttons
        self.radio_prioridad_normal.toggled.connect(self.slot_prioridad_cambiada)
        self.radio_prioridad_alta.toggled.connect(self.slot_prioridad_cambiada)

    # =========================
    # UTILIDADES
    # =========================
    def obtener_prioridad_actual(self):
        # Único return: devolvemos "Normal" o "Alta" según el radio seleccionado
        if self.radio_prioridad_alta.isChecked():
            prioridad = "Alta"
        else:
            prioridad = "Normal"
        return prioridad

    def limpiar_contenido_nota(self):
        # Restablece todos los campos a su estado por defecto
        self.line_edit_titulo.clear()
        self.combo_categoria.setCurrentIndex(0)
        self.radio_prioridad_normal.setChecked(True)
        self.texto_nota.clear()

    def imprimir_en_consola(self):
        titulo = self.line_edit_titulo.text()
        categoria = self.combo_categoria.currentText()
        prioridad = self.obtener_prioridad_actual()
        contenido = self.texto_nota.toPlainText()

        print("=" * 40)
        print("NOTA ACTUAL")
        print("=" * 40)
        print(f"Título   : {titulo}")
        print(f"Categoría: {categoria}")
        print(f"Prioridad: {prioridad}")
        print("-" * 40)
        print("Contenido:")
        print(contenido)
        print("=" * 40)

    # =========================
    # SLOTS (LÓGICA)
    # =========================
    def slot_limpiar_nota(self):
        respuesta = QMessageBox.question(
            self,
            "Confirmar limpieza",
            "¿Estás seguro de que quieres limpiar la nota?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.limpiar_contenido_nota()
            self.statusBar().showMessage("Nota limpiada", 3000)

    def slot_imprimir_nota(self):
        self.imprimir_en_consola()
        self.statusBar().showMessage("Nota impresa en la consola", 3000)

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

    def slot_acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de Mini Bloc de Notas",
            "Mini Bloc de Notas\n\nEjemplo práctico con PySide6.\nHecho para simulación de examen."
        )

    def slot_titulo_cambiado(self, nuevo_titulo):
        # Actualizar título de la ventana dinámicamente (si hay texto)
        ventana_titulo = "Mini Bloc de Notas"
        if nuevo_titulo.strip():
            ventana_titulo = f"{nuevo_titulo} - Mini Bloc de Notas"
        self.setWindowTitle(ventana_titulo)

        # Mostrar mensaje en la barra de estado con el título actual (breve)
        self.statusBar().showMessage(f"Título: {nuevo_titulo}", 2000)

    def slot_categoria_cambiada(self, nueva_categoria):
        # Mostrar categoría en la barra de estado
        self.statusBar().showMessage(f"Categoría: {nueva_categoria}", 2000)

    def slot_prioridad_cambiada(self, checked):
        # Solo actuamos cuando checked == True (evita doble mensajes)
        if not checked:
            return
        prioridad = self.obtener_prioridad_actual()
        self.statusBar().showMessage(f"Prioridad: {prioridad}", 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
