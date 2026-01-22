#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QVBoxLayout

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página 1")

        tabs = QTabWidget()

        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Bienvenido"))
        tab1.setLayout(tab1_layout)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Segunda página"))
        tab2.setLayout(tab2_layout)

        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("Tercera página"))
        tab3.setLayout(tab3_layout)

        tabs.addTab(tab1, "Inicio")
        tabs.addTab(tab2, "Página 2")
        tabs.addTab(tab3, "Página 3")

        tabs.currentChanged.connect(self.cambiar_pagina)

        self.setCentralWidget(tabs)

    def cambiar_pagina(self, indice):
        self.setWindowTitle(f"Página {indice + 1}")
        print(f"Página actual: {indice}")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
