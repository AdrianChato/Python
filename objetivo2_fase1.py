#Adrián Solís León 2ºDAM

#1 Solicita dos enteros y muestra operaciones básicas
print("- 1 -")
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)


#2 Solicita tres reales y muestra el promedio redondeado a 2 decimales
print("- 2 -")
x = float(input("Introduce el primer número: "))
y = float(input("Introduce el segundo número: "))
z = float(input("Introduce el tercer número: "))
promedio = round((x + y + z) / 3, 2)
print("El promedio es:", promedio)

#3 Compara dos enteros y muestra tres condiciones
print("- 3 -")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print("¿El primero es mayor?", num1 > num2)
print("¿Son iguales?", num1 == num2)
print("¿El segundo es distinto de cero?", num2 != 0)

#4 Solicita dos valores lógicos y muestra operaciones booleanas
print("- 4 -")
bool1 = eval(input("Introduce el primer valor lógico (True/False): "))
bool2 = eval(input("Introduce el segundo valor lógico (True/False): "))
print("Resultado de and:", bool1 and bool2)
print("Resultado de or:", bool1 or bool2)
print("Resultado de not primer valor:", not bool1)
print("Resultado de not segundo valor:", not bool2)

#5 Solicita dos edades como texto, convierte a entero y muestra suma y promedio
print("- 5 -")
edad1 = int(input("Edad de la primera persona: "))
edad2 = int(input("Edad de la segunda persona: "))
suma = edad1 + edad2
promedio = round(suma / 2, 1)
print("Suma total:", suma)
print("Promedio:", promedio)

#6 Evalúa expresiones lógicas con dos números reales
print("- 6 -")
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
print("(a > 10) and (b < 5):", (a > 10) and (b < 5))
print("(a == b) or (b > 0):", (a == b) or (b > 0))
print("not (a < b):", not (a < b))

#7 Divide dos reales y muestra el resultado redondeado a 1 decimal
print("- 7 -")
dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))
resultado = round(dividendo / divisor, 1)
print("Resultado redondeado:", resultado)
