#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QVBoxLayout,
    QLabel, QPushButton
)
from PySide6.QtCore import QLibraryInfo, QTranslator


class DialogoModo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Diálogo de selección de modo")


        botones = QDialogButtonBox.Yes | QDialogButtonBox.No | QDialogButtonBox.Help
        self.caja = QDialogButtonBox(botones)


        self.caja.button(QDialogButtonBox.Yes).clicked.connect(self._yes_clicked)
        self.caja.button(QDialogButtonBox.No).clicked.connect(self._no_clicked)
        self.caja.button(QDialogButtonBox.Help).clicked.connect(self.reject)


        self.boton_pulsado = None

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Selecciona el modo de operación que quieres activar:"))
        layout.addWidget(self.caja)

        self.setLayout(layout)

    def _yes_clicked(self):
        self.boton_pulsado = QDialogButtonBox.Yes
        self.accept()

    def _no_clicked(self):
        self.boton_pulsado = QDialogButtonBox.No
        self.accept()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de modo de operación")

        boton = QPushButton("Elegir modo")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        dialogo = DialogoModo(self)
        resultado = dialogo.exec()

        if resultado == QDialog.Accepted:
            if dialogo.boton_pulsado == QDialogButtonBox.Yes:
                print("Modo A activado")
            elif dialogo.boton_pulsado == QDialogButtonBox.No:
                print("Modo B activado")
        else:
            print("Se ha solicitado ayuda")


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