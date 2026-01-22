#Adrián solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo ComboBox")

        combo = QComboBox()
        combo.addItems(["Python", "Java", "C++", "Kotlin"])

        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.InsertAfterCurrent)
        combo.setMaxCount(6)

        combo.currentIndexChanged.connect(self.cambio_indice)
        combo.currentTextChanged.connect(self.cambio_texto)

        self.setCentralWidget(combo)

    def cambio_indice(self, i):
        print("Indice seleccionado: ", i)

    def cambio_texto(self, s):
        print("Texto seleccionado: ", s)
        self.setWindowTitle(s)

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
