#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QSize

class MainWindow (QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Aplicacion")
            self.setFixedSize(QSize(400,300))
            #self.setMaximumSize(QSize(600,400))
            #self.setMinimumSize(QSize(400,200))
            button = QPushButton("Pulsa")
            self.setCentralWidget(button)
            


app = QApplication([])
button = QPushButton("Hola PySide6")
button.show()
window = MainWindow()
window.show()
app.exec()