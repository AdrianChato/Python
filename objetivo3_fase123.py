#Adrián Solís León 2ºDAM

#Comprobar un número
numero = int(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

#Comparar dos números
num1 = int(input("\nIntroduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    print("El primero es mayor que el segundo.")
elif num2 > num1:
    print("El segundo es mayor que el primero.")
else:
    print("Ambos son iguales.")

#Comprobar texto dentro de una frase
frase = input("\nEscribe una frase: ")
palabra = input("Escribe una palabra: ")
if palabra in frase:
    print("La palabra está en la frase.")
else:
    print("La palabra no se encuentra.")

#Verificar el formato de una cadena
texto = input("\nEscribe un texto: ")
empieza_mayus = texto[0].isupper()
termina_punto = texto.endswith(".")
if empieza_mayus and termina_punto:
    print("Empieza por mayúscula.")
    print("Termina en punto.")
elif empieza_mayus:
    print("Empieza por mayúscula.")
elif termina_punto:
    print("Termina en punto.")
else:
    print("El texto no cumple las condiciones.")

#Clasificar una nota
nota = float(input("\nIntroduce una nota (0-10): "))
if 0 <= nota <= 4:
    print("Insuficiente.")
elif nota == 5:
    print("Suficiente.")
elif nota == 6:
    print("Bien.")
elif 7 <= nota <= 8:
    print("Notable.")
elif 9 <= nota <= 10:
    print("Sobresaliente.")
else:
    print("Nota no válida.")

print("\nFin del programa.")