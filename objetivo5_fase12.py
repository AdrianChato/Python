#Adrián Solís León 2ºDAM

#Funciones básicas
def sumar():
    a, b = pedir_dos_numeros()
    print(f"Resultado de la suma: {round(a + b, 2)}")

def restar():
    a, b = pedir_dos_numeros()
    print(f"Resultado de la resta: {round(a - b, 2)}")

def multiplicar():
    a, b = pedir_dos_numeros()
    print(f"Resultado de la multiplicación: {round(a * b, 2)}")

def dividir():
    a, b = pedir_dos_numeros()
    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"Resultado de la división: {round(a / b, 2)}")

#Funciones avanzadas
def potencia():
    base = pedir_numero("Base: ")
    exponente = pedir_numero("Exponente: ")
    print(f"Resultado: {round(base ** exponente, 2)}")

def raiz_cuadrada():
    num = pedir_numero("Número: ")
    if num < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        print(f"Resultado: {round(num ** 0.5, 2)}")

def modulo():
    a, b = pedir_dos_numeros()
    if b == 0:
        print("Error: No se puede calcular el módulo con divisor cero.")
    else:
        print(f"Resultado: {round(a % b, 2)}")

#Funciones de ayuda
def es_numero(valor):
    valor = valor.replace('.', '', 1).replace('-', '', 1)
    return valor.isdigit()

def pedir_numero(mensaje):
    valido = False
    while not valido:
        entrada = input(mensaje)
        if es_numero(entrada):
            numero = float(entrada)
            valido = True
        else:
            print("Entrada inválida. Introduce un número.")
    return numero

def pedir_dos_numeros():
    a = pedir_numero("Introduce el primer número: ")
    b = pedir_numero("Introduce el segundo número: ")
    return a, b

def operaciones_avanzadas():
    volver = False
    while not volver:
        print("\nOperaciones avanzadas:")
        print("a) Potencia")
        print("b) Raíz cuadrada")
        print("c) Módulo")
        print("d) Volver al menú principal")
        opcion = input("Selecciona una opción: ").lower()

        if opcion == 'a':
            potencia()
        elif opcion == 'b':
            raiz_cuadrada()
        elif opcion == 'c':
            modulo()
        elif opcion == 'd':
            volver = True
        else:
            print("Opción inválida. Intenta de nuevo.")

#Menú principal
def menu():
    seguir = True
    while seguir:
        print("\n=========================")
        print("  CALCULADORA AVANZADA")
        print("=========================")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Operaciones avanzadas")
        print("6) Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            sumar()
        elif opcion == '2':
            restar()
        elif opcion == '3':
            multiplicar()
        elif opcion == '4':
            dividir()
        elif opcion == '5':
            operaciones_avanzadas()
        elif opcion == '6':
            print("Fin del programa. ¡Hasta pronto!")
            seguir = False
        else:
            print("Opción inválida. Intenta de nuevo.")

#Ejecutar el programa
menu()