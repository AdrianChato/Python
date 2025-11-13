#Adrián Solís León 2ºDAM

from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fecha y hora actual")

        fecha_hora = QDateTimeEdit()
        fecha_hora.setDateTime(QDateTime.currentDateTime())
        fecha_hora.setDisplayFormat("dddd, d 'de' MMMM 'de' yyyy hh:mm")

        fecha_hora.dateTimeChanged.connect(self.mostrar_fecha_hora)

        self.setCentralWidget(fecha_hora)

    def mostrar_fecha_hora(self, a):
        print(f"Fecha elegida: {a.toString("dddd, d 'de' MMMM 'de' yyyy hh:mm")}")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
