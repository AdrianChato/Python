from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QMainWindow, QPushButton
)
from PySide6.QtGui import QPalette, QColor, QPainter, QPen
from PySide6.QtCore import Signal, Qt
import sys

# ===============================================================
# 1) COMPONENTE DERIVADO DE QLineEdit
# ===============================================================
from PySide6.QtWidgets import QLineEdit


class EntradaLimitada(QLineEdit):
    """
    Componente derivado de QLineEdit con:
    - estado interno: límite de caracteres
    - señales personalizadas
    - colores dinámicos usando palette()
    """

    longitud_cambiada = Signal(int)
    limite_superado = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__max_car = 20

        # Señal estándar → método interno
        self.textChanged.connect(self.__controlar)

    def __controlar(self):
        """
        Controla:
        - longitud
        - colores del fondo
        - emisión de señales personalizadas
        """
        texto = self.text()
        n = len(texto)

        self.longitud_cambiada.emit(n)
        self.limite_superado.emit(n > self.__max_car)

        pal = self.palette()

        if n <= self.__max_car * 0.8:
            pal.setColor(QPalette.Base, QColor("white"))
        elif n <= self.__max_car:
            pal.setColor(QPalette.Base, QColor(255, 255, 180))
        else:
            pal.setColor(QPalette.Base, QColor(255, 180, 180))

        self.setPalette(pal)

    def maximo(self):
        return self.__max_car


# ===============================================================
# 2) COMPONENTE CREADO DESDE CERO (hereda de QWidget)
# ===============================================================
class IndicadorCircular(QWidget):
    """
    Componente completamente personalizado.
    Se dibuja con QPainter y cambia color según valor.
    """

    def __init__(self):
        super().__init__()
        self._valor = 0  # Estado interno
        self.setObjectName("IndicadorCircular")  # Añadido para aplicar el QSS

    def setValor(self, valor: int):
        self._valor = valor
        self.update()  # obliga a redibujar → paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Determinar color según valor
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


# ===============================================================
# 3) VENTANA PRINCIPAL QUE USA TODO
# ===============================================================
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SIMULACRO TEMA 3 — Adrián Solís León")

        contenedor = QWidget()
        layout = QVBoxLayout()

        # Widgets derivados
        self.entrada = EntradaLimitada()
        self.etiqueta_estado = QLabel("Caracteres: 0 / 20")
        self.etiqueta_limite = QLabel()

        # Componente creado a mano
        self.indicador = IndicadorCircular()

        # Botón de ejemplo
        self.boton = QPushButton("Actualizar indicador")
        self.boton.clicked.connect(self.actualizarIndicador)

        # ------------------------------
        # Conexión de señales personalizadas
        # ------------------------------
        self.entrada.longitud_cambiada.connect(
            lambda n: self.etiqueta_estado.setText(
                f"Caracteres: {n} / {self.entrada.maximo()}"
            )
        )

        self.entrada.limite_superado.connect(
            lambda s: self.etiqueta_limite.setText(
                "¡Límite superado!" if s else ""
            )
        )

        # Layout
        layout.addWidget(QLabel("Entrada limitada (derivada):"))
        layout.addWidget(self.entrada)
        layout.addWidget(self.etiqueta_estado)
        layout.addWidget(self.etiqueta_limite)

        layout.addWidget(QLabel("Indicador Circular (creado desde cero):"))
        layout.addWidget(self.indicador, alignment=Qt.AlignCenter)

        layout.addWidget(self.boton)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def actualizarIndicador(self):
        """
        Actualiza el indicador usando el número de caracteres.
        """
        n = len(self.entrada.text())
        self.indicador.setValor(n)


# ===============================================================
# EJECUCIÓN PRINCIPAL (carga de estilos QSS)
# ===============================================================
app = QApplication(sys.argv)

# Leer el archivo QSS
with open("Simulacion.qss", "r") as f:
    app.setStyleSheet(f.read())

ventana = VentanaPrincipal()
ventana.resize(400, 500)

# Asegurarse de que el indicador tiene tamaño suficiente
ventana.indicador.setMinimumSize(100, 100)

ventana.show()

app.exec()
