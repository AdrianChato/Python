#Adrián Solís León 2ºDAM

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QRadioButton, QMainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        widget = QRadioButton("Activar función")
        widget.isChecked()

        widget.toggled.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, a):
        if (a == True):
            self.setWindowTitle("Función ACTIVA")
        else:
            self.setWindowTitle("Función DESACTIVADA")

        

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()