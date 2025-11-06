import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QTextEdit")

        campo = QTextEdit()
        campo.setPlaceholderText("Escribe aquí tu comentario...")

        # Conectamos señales
        campo.textChanged.connect(self.texto_modificado)

        self.setCentralWidget(campo)
        self.campo = campo

    def texto_modificado(self):
        print("El texto ha cambiado")
        print(self.campo.toPlainText())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()