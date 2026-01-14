#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QTimer


class PanelSemaforo(QWidget):
    def __init__(self):
        super().__init__()

        self.__estado_actual = "rojo"

        # Mapa de nombres en español a nombres válidos para Qt
        self._mapa_colores = {
            "rojo": "red",
            "amarillo": "yellow",
            "verde": "green"
        }

        # Layout vacío para estructura
        layout = QVBoxLayout(self)
        layout.addStretch()

        self.setMinimumSize(300, 400)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # cambiar cada 1 segundo
        self.timer.timeout.connect(self.cambiar_estado)
        self.timer.start()

    # Métodos
    def estado(self):
        return self.__estado_actual

    def reiniciar(self):
        self.__estado_actual = "rojo"
        self.update()

    # Ciclo del semáforo
    def cambiar_estado(self):
        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
        else:
            self.__estado_actual = "rojo"

        self.update()

    # Pintado del componente
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        ancho = self.width()
        alto = self.height()

        # Dimensiones del cuerpo del semáforo
        w = min(140, ancho // 2)
        h = min(320, int(alto * 0.7))
        x = (ancho - w) // 2
        y = 20

        # Caja negra
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QColor("black"))
        painter.drawRect(x, y, w, h)

        # Posiciones de las luces
        posiciones = [
            (x + w // 2, int(y + h * 0.20)),  # rojo
            (x + w // 2, int(y + h * 0.50)),  # amarillo
            (x + w // 2, int(y + h * 0.80))   # verde
        ]

        radio = min(40, w // 3)
        colores = ["rojo", "amarillo", "verde"]

        for i, color_esp in enumerate(colores):
            cx, cy = posiciones[i]
            color_qt = self._mapa_colores[color_esp]

            if self.__estado_actual == color_esp:
                painter.setBrush(QColor(color_qt))
            else:
                painter.setBrush(QColor("gray"))

            painter.setPen(QPen(Qt.black, 2))
            painter.drawEllipse(cx - radio, cy - radio, 2 * radio, 2 * radio)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semáforo Automático")
        self.resize(350, 500)
        self.setCentralWidget(PanelSemaforo())


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
