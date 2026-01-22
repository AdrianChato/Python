#Adrián Solís León 2ºDAM

import os
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicacion")
        ruta = ("imagen.jpg")

        widget = QLabel("Buenos dias")
        widget.setPixmap(QPixmap(os.path.join(basedir, "imagen.jpg")))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()