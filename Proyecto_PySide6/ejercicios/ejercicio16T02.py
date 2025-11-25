#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QColorDialog, QFontDialog
)
from PySide6.QtGui import QFont


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de archivo y preferencias")

        contenedor = QWidget()
        layout = QVBoxLayout()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        self.label_texto = QLabel("")
        layout.addWidget(self.label_texto)

        boton_abrir = QPushButton("Abrir archivo de texto")
        boton_abrir.clicked.connect(self.abrir_archivo)
        layout.addWidget(boton_abrir)

        boton_guardar = QPushButton("Guardar archivo como...")
        boton_guardar.clicked.connect(self.guardar_archivo)
        layout.addWidget(boton_guardar)

        boton_color = QPushButton("Elegir color de fondo")
        boton_color.clicked.connect(self.cambiar_color)
        layout.addWidget(boton_color)

        boton_fuente = QPushButton("Cambiar fuente del texto")
        boton_fuente.clicked.connect(self.cambiar_fuente)
        layout.addWidget(boton_fuente)

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
            self.label_texto.setText(contenido)

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(self.label_texto.text())

    def cambiar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.label_texto.setStyleSheet(f"background-color: {color.name()};")

    def cambiar_fuente(self):
        ok, fuente = QFontDialog.getFont()
        if ok:
            self.label_texto.setFont(fuente)

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()