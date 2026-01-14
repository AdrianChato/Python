from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QMainWindow, QPushButton
)
from PySide6.QtGui import QPalette, QColor, QPainter, QPen
from PySide6.QtCore import Signal, Qt
import sys



class BotonContador(QPushButton):

    # Señal personalizada que enviará un entero
    contador_actualizado = Signal(int)

    def __init__(self, parent=None):
        super().__init__("Añadir Incidencia", parent)
        self.__contador = 0

        self.clicked.connect(self.__incrementar)

    def __incrementar(self):
        # Actualizamos el contador interno
        self.__contador = self.__contador + 1

        # Actualizamos el texto del botón
        nuevo_texto = "Incidencias Añadidas: " + str(self.__contador)
        self.setText(nuevo_texto)

        # Emitimos la señal con el nuevo valor
        self.contador_actualizado.emit(self.__contador)

    def contador(self):
        return self.__contador
    
    def reiniciar(self):
        self.__contador = 0
        return self.contador_actualizado.emit(self.__contador)


class IndicadorCircular(QWidget):

    def __init__(self):
        super().__init__()
        self._valor = 0  
        self._texto = "OK"
        self.setObjectName("IndicadorCircular") 

    def setValor(self, valor: int):
        self._valor = valor
        self.update() 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Determinar color según el contador
        if self._valor >= 8:
            color = QColor("red")
        elif self._valor >= 4:
            color = QColor("yellow")
        elif self._valor >=1:
            color = QColor("green")
        else:
            color = QColor("white")

        # Relleno
        painter.setBrush(color)

        # Borde negro
        painter.setPen(QPen(Qt.black, 3))

        # Dibujo del círculo
        lado = min(self.width(), self.height()) - 10
        x = (self.width() - lado) // 2
        y = (self.height() - lado) // 2

        painter.drawEllipse(x, y, lado, lado)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel de Inicio - Adrián")

        contenedor = QWidget()
        layout = QVBoxLayout()

        self.indicador = IndicadorCircular()

        self.boton = BotonContador()
        self.boton.contador_actualizado.connect(self.actualizarIndicador)
        self.boton2 = QPushButton("Reset")
        self.boton2.clicked.connect(self.actualizaReset)


        # Layout

        layout.addWidget(self.indicador, alignment=Qt.AlignCenter)

        layout.addWidget(self.boton)
        layout.addWidget(self.boton2)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def actualizarIndicador(self):
        n = self.boton.contador()
        self.indicador.setValor(n)

    def actualizaReset(self):

        self.boton.reiniciar()


app = QApplication(sys.argv)

# Leer el archivo QSS
with open("Simulacion.qss", "r") as f:
    app.setStyleSheet(f.read())

ventana = VentanaPrincipal()
ventana.resize(400, 500)

ventana.indicador.setMinimumSize(120, 120)

ventana.show()

app.exec()
