#Adrián Solís León 2ºDAM

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progreso: 0%")

        self.progreso_actual = 0

        self.barra = QProgressBar()
        self.barra.setRange(0, 100)
        self.barra.setValue(self.progreso_actual)
        self.setCentralWidget(self.barra)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.preguntar_usuario)
        self.timer.start(2000)

    def preguntar_usuario(self):
        print("\n=== Control de progreso ===")
        print("1 : Aumentar progreso")
        print("2 : Retroceder progreso")
        print("0 : Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self.cambiar_progreso("aumentar")
        elif opcion == "2":
            self.cambiar_progreso("disminuir")
        elif opcion == "0":
            print("Saliendo del programa...")
            self.timer.stop()
            self.close()

    def cambiar_progreso(self, modo):
        if modo == "aumentar":
            self.progreso_actual = min(100, self.progreso_actual + 20)
        elif modo == "disminuir":
            self.progreso_actual = max(0, self.progreso_actual - 20)

        self.barra.setValue(self.progreso_actual)

        if self.progreso_actual == 100:
            self.setWindowTitle("¡Tarea completada!")
        else:
            self.setWindowTitle(f"Progreso: {self.progreso_actual}%")

        print(f"Progreso actual: {self.progreso_actual}%")

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec()