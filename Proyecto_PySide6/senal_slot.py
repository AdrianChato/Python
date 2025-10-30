from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        boton = QPushButton("Pulsa")
        boton.clicked.connect(self.el_boton_fue_pulsado)

        self.setCentralWidget(boton)
    def el_boton_fue_pulsado(self):
        print("Lo has pulsado")

app = QApplication()
window= VentanaPrincipal()
window.show()
app.exec()