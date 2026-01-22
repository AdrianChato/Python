from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Aplicacion")

        widget = QLabel("Buenos dias")
        widget.setPixmap(QPixmap("imagen.jpg"))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()