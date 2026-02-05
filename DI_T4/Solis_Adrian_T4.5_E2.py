#Adrián Solís León 2ºDAM

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualización de informes HTML")

        layout = QVBoxLayout()

    
        self.combo = QComboBox()
        self.combo.addItems([
            "DI_U05_A02_03.html",
            "DI_U05_A02_08.html",
            "DI_U05_A03_11.html"
        ])


        self.web = QWebEngineView()

        self.combo.currentTextChanged.connect(self.cargar_html)

        layout.addWidget(self.combo)
        layout.addWidget(self.web)
        self.setLayout(layout)

    
        self.cargar_html(self.combo.currentText())

    def cargar_html(self, archivo):
        ruta = os.path.abspath(archivo)
        self.web.load(QUrl.fromLocalFile(ruta))


app = QApplication()
ventana = Ventana()
ventana.show()
app.exec()
