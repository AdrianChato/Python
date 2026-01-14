#Adrián Solís León 2ºDAM

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt


class PanelSemaforo(QWidget):
    def __init__(self):
        super().__init__()

        # estado privado: "rojo", "amarillo", "verde"
        self.__estado_actual = "rojo"

        layout = QVBoxLayout(self)

        # botón dentro del propio componente
        self.boton_cambiar = QPushButton("Cambiar")
        self.boton_cambiar.clicked.connect(self.cambiar_estado)

        # dejar espacio arriba para el dibujo y poner el botón abajo centrado
        layout.addStretch()
        layout.addWidget(self.boton_cambiar)
        layout.setAlignment(self.boton_cambiar, Qt.AlignHCenter)

        self.setMinimumSize(300, 400)

        # mapeo de nombres en español 
        self._mapa_colores = {
            "rojo": "red",
            "amarillo": "yellow",
            "verde": "green"
        }

    # métodos 
    def estado(self):
        return self.__estado_actual

    def reiniciar(self):
        self.__estado_actual = "rojo"
        self.update()

    # lógica 
    def cambiar_estado(self):
        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
        else:
            self.__estado_actual = "rojo"
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        ancho = self.width()
        alto = self.height()

        # dimensiones del semáforo
        w = min(140, ancho // 2)
        h = min(320, int(alto * 0.7))
        x = (ancho - w) // 2
        y = 20

        # dibujar el rectángulo negro del semáforo
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QColor("black"))
        painter.drawRect(x, y, w, h)

        # calcular posiciones dinámicas de las 3 luces
        posiciones = [
            (x + w // 2, int(y + h * 0.20)),  # rojo (arriba)
            (x + w // 2, int(y + h * 0.50)),  # amarillo (medio)
            (x + w // 2, int(y + h * 0.80))   # verde (abajo)
        ]

        radio = min(40, w // 3)

        colores = ["rojo", "amarillo", "verde"]

        for i, color_esp in enumerate(colores):
            cx, cy = posiciones[i]
            # traducir a color conocido por Qt
            color_qt = self._mapa_colores.get(color_esp, "gray")

            if self.__estado_actual == color_esp:
                painter.setBrush(QColor(color_qt))
            else:
                painter.setBrush(QColor("gray"))

            # contorno negro
            painter.setPen(QPen(Qt.black, 2))
            painter.drawEllipse(cx - radio, cy - radio, 2 * radio, 2 * radio)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TAREA 3.3 - Semáforo")
        self.resize(350, 500)
        self.setCentralWidget(PanelSemaforo())


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()