from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence

# Nuestra ventana principal hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menús")

        # Obtenemos la referencia a la barra de menús incluida en QMainWindow
        barra_menu = self.menuBar()

        # Añadimos un menú principal
        menu = barra_menu.addMenu("&Menú")

        # Creamos una acción
        accion = QAction("Imprimir por consola", self)
        accion.setShortcut(QKeySequence("Ctrl+P"))  # Atajo de teclado
        accion.triggered.connect(self.imprimir_por_consola)  # Vinculamos acción con método

        # Añadimos la acción al menú
        menu.addAction(accion)

    def imprimir_por_consola(self):
        print("Acción lanzada desde el menú o mediante el atajo de teclado.")


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()