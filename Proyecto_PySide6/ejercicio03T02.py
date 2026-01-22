#Adrián Solís León 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi App")
        self.label = QLabel("Sistema en espera")
        self.label.setFont(QFont("Arial", 24))
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.setCentralWidget(self.label)
        self.label.setText("Sistema operativo iniciado")

app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()