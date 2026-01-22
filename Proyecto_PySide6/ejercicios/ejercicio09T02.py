#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout
)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 9")
        layout_principal = QHBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_principal)
        self.setCentralWidget(componente_principal)
      
        # Creamos un QStackedLayout y añadimos cuatro "capas" al layout apilado
        botones_horizontal = QHBoxLayout()
        boton1h = QPushButton("H1")
        boton2h = QPushButton("H2")
        boton3h = QPushButton("H3")
        boton4h = QPushButton("H4")
        botones_horizontal.addWidget(boton1h)
        botones_horizontal.addWidget(boton2h)
        botones_horizontal.addWidget(boton3h)
        botones_horizontal.addWidget(boton4h)
      
        # Creamos un layout vertical con tres botones
        # Cada botón hará visible una capa a través de la ranura
        layout_botones = QVBoxLayout()
        boton1 = QPushButton("V1")
        boton2 = QPushButton("V2")
        boton3 = QPushButton("V3")
        boton4 = QPushButton("V4")
        layout_botones.addWidget(boton1)
        layout_botones.addWidget(boton2)
        layout_botones.addWidget(boton3)
        layout_botones.addWidget(boton4)
      
        # Añadimos los layouts al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(botones_horizontal)

    

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec() 