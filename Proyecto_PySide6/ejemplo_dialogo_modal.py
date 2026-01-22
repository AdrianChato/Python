from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con diálogos")

        boton = QPushButton("Haz clic para mostrar el diálogo")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic recibido, se mostrará el diálogo.")
        dialogo = QDialog(self)
        dialogo.setWindowTitle("Ventana de diálogo")
        dialogo.exec()

app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec() 