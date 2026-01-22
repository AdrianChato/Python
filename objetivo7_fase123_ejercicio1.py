#Adrián Solís León 2ºDAM

#Clase Vehículo y métodos
class Vehiculo:
    def __init__(self, marca, velocidad=0):
        self.__marca = marca
        self.__velocidad = velocidad

    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, nueva_velocidad):
        self.__velocidad = nueva_velocidad

    def acelerar(self, v):
        self.set_velocidad(self.__velocidad + v)

    def desacelerar(self, v):
        self.set_velocidad(self.__velocidad - v)

    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es: {self.__velocidad} km/h")

#Subclase coche que hereda de vehículo
class Coche(Vehiculo):
    def __init__(self, marca, velocidad=0):
        super().__init__(marca, velocidad)
        self.__bocina = "¡tuuut!"

    def get_bocina(self):
        return self.__bocina

    def set_bocina(self, nuevo_sonido):
        self.__bocina = nuevo_sonido

    def klaxonner(self):
        print(self.__bocina)

#Prueba
coche_1 = Coche("Peugeot 208", 10.5)
print(f"La velocidad inicial del coche es: {coche_1.get_velocidad()}")
coche_1.acelerar(50)
coche_1.desacelerar(15)
coche_1.mostrar_velocidad()
coche_1.klaxonner()