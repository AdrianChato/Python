#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QCheckBox, QPushButton, QLineEdit, QRadioButton, QComboBox
)

import sys

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarea 3.1 - Personalización con QSS")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Checkbox personalizado:"))
        layout.addWidget(QCheckBox("Opción 1"))

        layout.addWidget(QLabel("Botón personalizado:"))
        layout.addWidget(QPushButton("Aceptar"))

        layout.addWidget(QLabel("Caja de texto personalizada:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("RadioButton personalizado:"))
        layout.addWidget(QRadioButton("Opción A"))
        layout.addWidget(QRadioButton("Opción B"))

        layout.addWidget(QLabel("ComboBox personalizado:"))
        combo = QComboBox()
        combo.addItems(["Elemento 1", "Elemento 2", "Elemento 3"])
        layout.addWidget(combo)

        self.setLayout(layout)

 

app = QApplication(sys.argv)
with open("Solis_Adrian_estilos_T3.1.qss", "r") as f:
    app.setStyleSheet(f.read())
ventana = VentanaPrincipal()
ventana.show()
app.exec()