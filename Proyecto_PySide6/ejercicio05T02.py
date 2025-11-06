#Adrián Solís León 2ºDAM

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")

        widget = QCheckBox("Esto es un checkbox")
        #widget.setCheckState(Qt.Checked)
        widget.setCheckState(Qt.PartiallyChecked)
        #widget.setCheckState(Qt.Unchecked)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, a):
        state = Qt.CheckState(a)
        if state == Qt.Checked:
            print("Marcado completamente")
        elif state == Qt.Unchecked:
            print("Desmarcado")
        else:
            print("Marcado parcialmente")
        print (a)
app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()