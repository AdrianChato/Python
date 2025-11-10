# Adrián Solís León 2ºDAM
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fecha y hora actual")

        self.fecha_hora = QDateTimeEdit()
        self.fecha_hora.setDateTime(QDateTime.currentDateTime())
        self.fecha_hora.setDisplayFormat("dddd d 'de' MMMM 'de' yyyy hh:mm")

        self.fecha_hora.dateTimeChanged.connect(self.mostrar_fecha_hora)

        self.setCentralWidget(self.fecha_hora)

    def mostrar_fecha_hora(self, dt):
        print(f"Fecha elegida: {dt.toString('dddd, d de MMMM de yyyy hh:mm')}")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()
