#Adrián Solís León 2ºDAM

#Solicita los tres números
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

#Haces las expresiones
expresion1 = (a < b) and (b < c)
expresion2 = (a == b) or (b == c)
expresion3 = not (a > c)

#Mostramos los resultados
print("(a < b) and (b < c):", expresion1)
print("(a == b) or (b == c):", expresion2)
print("not (a > c):", expresion3)