#Adrián Solís León 2ºDAM

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apertura de informes HTML")

        layout = QVBoxLayout()

        # Botones para cada informe
        btn1 = QPushButton("DI_U05_A02_03.html")
        btn2 = QPushButton("DI_U05_A02_08.html")
        btn3 = QPushButton("DI_U05_A03_11.html")

        # Conexión de botones
        btn1.clicked.connect(lambda: self.abrir_html("DI_U05_A02_03.html"))
        btn2.clicked.connect(lambda: self.abrir_html("DI_U05_A02_08.html"))
        btn3.clicked.connect(lambda: self.abrir_html("DI_U05_A03_11.html"))

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)

    def abrir_html(self, archivo):
        ruta = os.path.abspath(archivo)
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta))


app = QApplication()
ventana = Ventana()
ventana.show()
app.exec_()
