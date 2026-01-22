#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.button = QPushButton("Pulsar")

        self.button.pressed.connect(self.the_button_was_clicked)
        self.button.released.connect(self.the_button_was_toggled)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Boton presionado")
        self.button.setText("Soltar")


    def the_button_was_toggled(self):
        print("Boton liberado")
        self.button.setText("Pulsar")

app = QApplication()
window= MainWindow()
window.show()
app.exec()

