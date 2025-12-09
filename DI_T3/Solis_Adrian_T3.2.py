# Adrian Solis Leon 2ºDAM

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QPalette, QColor


class AreaTextoLimitada(QTextEdit):
    # Señales personalizadas
    longitud_cambiada = Signal(int)
    limite_superado = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__max_caracteres = 200

        # Conectamos la señal estándar textChanged
        self.textChanged.connect(self.__controlar_texto)

    def __controlar_texto(self):
        texto = self.toPlainText()
        longitud = len(texto)

        # Emitimos la señal con la longitud actual
        self.longitud_cambiada.emit(longitud)

        # Emitimos si se supera el límite
        self.limite_superado.emit(longitud > self.__max_caracteres)

        # Cambiamos el color de fondo según el estado
        paleta = self.palette()
        if longitud <= self.__max_caracteres * 0.8:
            paleta.setColor(QPalette.Base, QColor("white"))
        elif longitud <= self.__max_caracteres:
            paleta.setColor(QPalette.Base, QColor(255, 255, 200))  # amarillo suave
        else:
            paleta.setColor(QPalette.Base, QColor(255, 200, 200))  # rojo suave
        self.setPalette(paleta)

    def max_caracteres(self):
        return self.__max_caracteres


class EtiquetaContadorCaracteres(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Caracteres: 0 / 200")

    def actualizar_conteo(self, longitud, maximo):
        self.setText(f"Caracteres: {longitud} / {maximo}")

        # Cambiamos el color del texto según el estado
        paleta = self.palette()
        if longitud <= maximo * 0.8:
            paleta.setColor(QPalette.WindowText, QColor("black"))
        elif longitud <= maximo:
            paleta.setColor(QPalette.WindowText, QColor("orange"))
        else:
            paleta.setColor(QPalette.WindowText, QColor("red"))
        self.setPalette(paleta)


class BotonLimpiarAviso(QPushButton):
    # Señal personalizada
    texto_limpiado = Signal()

    def __init__(self, area_texto: AreaTextoLimitada, parent=None):
        super().__init__("Limpiar texto", parent)
        self.__area_texto = area_texto

        # Estado inicial: gris claro
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(220, 220, 220))
        self.setPalette(paleta)

        # Conectamos la acción estándar clicked
        self.clicked.connect(self.__limpiar)

    def __limpiar(self):
        # Limpiamos el área de texto
        self.__area_texto.clear()

        # Emitimos la señal personalizada
        self.texto_limpiado.emit()

        # Cambiamos el color del botón a verde suave
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(200, 255, 200))
        self.setPalette(paleta)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de notas con avisos")

        # Contenedor y layout
        contenedor = QWidget()
        layout = QVBoxLayout()

        # Instanciamos los widgets derivados
        self.area_texto = AreaTextoLimitada()
        self.etiqueta_contador = EtiquetaContadorCaracteres()
        self.boton_limpiar = BotonLimpiarAviso(self.area_texto)
        self.etiqueta_info = QLabel("Escribe tu nota y observa los avisos visuales.")

        # Conexiones de señales
        self.area_texto.longitud_cambiada.connect(
            lambda longitud: self.etiqueta_contador.actualizar_conteo(
                longitud, self.area_texto.max_caracteres()
            )
        )
        self.boton_limpiar.texto_limpiado.connect(
            lambda: self.etiqueta_info.setText("Texto limpiado correctamente.")
        )

        # Añadimos al layout
        layout.addWidget(self.etiqueta_contador)
        layout.addWidget(self.area_texto)
        layout.addWidget(self.boton_limpiar)
        layout.addWidget(self.etiqueta_info)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()