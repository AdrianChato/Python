#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QDial

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        dial = QDial()
        dial.setRange(0, 10)
        dial.setNotchesVisible(True)
        dial.valueChanged.connect(self.cambiar_volumen)

        self.setCentralWidget(dial)
        self.setWindowTitle("Volumen: 0 / 10")

    def cambiar_volumen(self, valor):
        self.setWindowTitle(f"Volumen: {valor} / 10")
        if valor == 10:
            print("¡Volumen máximo alcanzado!")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
