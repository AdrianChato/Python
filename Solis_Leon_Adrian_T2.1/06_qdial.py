# Adrián Solís León 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QDial

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.dial.setRange(0, 10)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.cambiar_volumen)

        self.setCentralWidget(self.dial)
        self.setWindowTitle("Volumen: 0 / 10")

    def cambiar_volumen(self, valor):
        self.setWindowTitle(f"Volumen: {valor} / 10")
        if valor == 10:
            print("¡Volumen máximo alcanzado!")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
