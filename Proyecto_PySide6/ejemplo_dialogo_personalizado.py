from PySide6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QVBoxLayout,
    QLabel, QPushButton
)
from PySide6.QtCore import QLibraryInfo, QTranslator

class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo personalizado")

        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        caja = QDialogButtonBox(botones)

        caja.accepted.connect(self.accept)
        caja.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("¿Quieres realizar esta acción?"))
        layout.addWidget(caja)

        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con diálogo personalizado")

        boton = QPushButton("Mostrar diálogo personalizado")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic recibido, se mostrará el diálogo.")
        dialogo = DialogoPersonalizado(self)
        dialogo.setWindowTitle("Ventana de diálogo personalizado")

        resultado = dialogo.exec()
        if resultado:
            print("Aceptado")
        else:
            print("Cancelado")

def cargar_traductor(app):
    traductor = QTranslator(app)
    ruta = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qt_es", ruta)
    app.installTranslator(traductor)

app = QApplication([])
cargar_traductor(app)
ventana = VentanaPrincipal()
ventana.show()
app.exec() 