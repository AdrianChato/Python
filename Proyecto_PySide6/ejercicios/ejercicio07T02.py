#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QLineEdit")
        texto = QLineEdit()
        texto.setMaxLength(20)
        texto.setPlaceholderText("Escribe tu ciudad")

        texto.returnPressed.connect(self.mostrar_mensaje)
        texto.textChanged.connect(self.texto_modificado)
        texto.textEdited.connect(self.texto_editado)

        self.setCentralWidget(texto)
        self.texto = texto

    def mostrar_mensaje(self):
        print("Se pulso Enter")

    def texto_modificado(self, s):
        print("Texto modificado: ", s)
        self.setWindowTitle(s)

    def texto_editado(self, a):
        print("Texto editado por el usuario: ", a)

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()