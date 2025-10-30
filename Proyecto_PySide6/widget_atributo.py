from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize

class VentanaPrinciapl (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setMinimumSize(QSize(480,320))

        texto = QLineEdit()
        texto.textChanged.connect(self.texto_modificado)
        self.texto = texto

    def texto_modificado(self):
        texto_recuperado = self.texto.text()
        self.setWindowTitle(texto_recuperado)

app = QApplication()
window = VentanaPrinciapl()
window.show()
app.exec()