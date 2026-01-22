from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout, QPushButton,QLabel,QLineEdit,QSpinBox,QDoubleSpinBox
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout vertical")

        # 1 Creamos el layout vertical
        layout_formulario = QFormLayout()

        # 2 Creamos el contenedor principal y le asignamos el layout
        componente_principal = QWidget()
        componente_principal.setLayout(layout_formulario)

        # 3 Lo establecemos como contenido central del QMainWindow
        self.setCentralWidget(componente_principal)

        # 4 Añadimos los widgets al layout (después de asignarlo)
        layout_formulario.addRow(QLabel("Texto: "), QLineEdit())
        layout_formulario.addRow(QLabel("Entero: "), QSpinBox())
        layout_formulario.addRow(QLabel("Decimal: "), QDoubleSpinBox())


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec() 