#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(self.cambiar_brillo)

        self.setCentralWidget(slider)
        self.setWindowTitle("Nivel de brillo: 50%")
        print("Nivel de brillo: 50%")

    def cambiar_brillo(self, valor):
        self.setWindowTitle(f"Nivel de brillo: {valor}%")
        print(f"Nivel de brillo: {valor}%")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
