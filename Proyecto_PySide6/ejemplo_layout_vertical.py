from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout vertical")

        # 1 Creamos el layout vertical
        layout_vertical = QVBoxLayout()

        # 2 Creamos el contenedor principal y le asignamos el layout
        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)

        # 3 Lo establecemos como contenido central del QMainWindow
        self.setCentralWidget(componente_principal)

        # 4 Añadimos los widgets al layout (después de asignarlo)
        layout_vertical.addWidget(QPushButton("Uno"))
        layout_vertical.addWidget(QPushButton("Dos"))
        layout_vertical.addWidget(QPushButton("Tres"))
        layout_vertical.addWidget(QPushButton("Cuatro"))


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec() 