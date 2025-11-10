# Adrián Solís León 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QVBoxLayout

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pestaña 1")

        self.tabs = QTabWidget()

        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Bienvenido"))
        tab1.setLayout(tab1_layout)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Segunda pestaña"))
        tab2.setLayout(tab2_layout)

        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("Tercera pestaña"))
        tab3.setLayout(tab3_layout)

        self.tabs.addTab(tab1, "Inicio")
        self.tabs.addTab(tab2, "Página 2")
        self.tabs.addTab(tab3, "Página 3")

        self.tabs.currentChanged.connect(self.cambiar_pestania)

        self.setCentralWidget(self.tabs)

    def cambiar_pestania(self, indice):
        self.setWindowTitle(f"Pestaña {indice + 1}")
        print(f"Pestaña actual: {indice}")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
