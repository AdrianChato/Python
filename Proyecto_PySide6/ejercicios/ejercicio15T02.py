#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QMessageBox, QMainWindow, QPushButton
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de tareas")
        boton = QPushButton("Gestionar tarea")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        respuesta = QMessageBox.question(
            self,
            "Acción sobre la tarea",
            "¿Qué quieres hacer con la tarea seleccionada?",
            buttons=QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,
            defaultButton=QMessageBox.Ignore
        )

        if respuesta == QMessageBox.Yes:
            QMessageBox.information(
                self,
                "Resultado",
                "La tarea se ha marcado como completada."
            )
        elif respuesta == QMessageBox.No:
            QMessageBox.information(
                self,
                "Resultado",
                "La tarea se ha pospuesto para más tarde."
            )
        else:
            QMessageBox.information(
                self,
                "Resultado",
                "La tarea se mantiene sin cambios."
            )

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()