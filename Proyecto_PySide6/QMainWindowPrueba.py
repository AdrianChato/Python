from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow (QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Aplicacion")
            button = QPushButton("Pulsa")
            self.setCentralWidget(button)
            #self.setFixedSize(QSize(400,300))
            self.setMaximumSize(QSize(600,400))
            self.setMinimumSize(QSize(400,200))
app = QApplication([])
window = MainWindow()
window.show()
app.exec()