#Adrián Solís León 2ºDAM

# Solicitar frase al usuario
frase = input("Introduce una frase o palabra: ")

print("\n--- FORMATO DEL TEXTO ---")
print("Capitalizada:", frase.capitalize())
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Invertida:", frase.swapcase())

print("\n--- ANÁLISIS DEL CONTENIDO ---")
print("¿Solo letras?:", frase.isalpha())
print("¿Solo números?:", frase.isdigit())
print("¿Letras y números?:", frase.isalnum())
print("¿Está en minúsculas?:", frase.islower())
print("¿Está en mayúsculas?:", frase.isupper())

print("\n--- LONGITUD ---")
print("Número total de caracteres:", len(frase))
print("Caracteres reales (sin espacios):", len(frase.replace(" ", "")))

print("\n--- LIMPIEZA ---")
print("Sin espacios al principio:", frase.lstrip())
print("Sin espacios al final:", frase.rstrip())
print("Sin espacios en ambos lados:", frase.strip())

# Reemplazo de palabra
buscar = "Python"
nueva = "Java"
frase_modificada = frase.replace(buscar, nueva)
print("\nPalabra a buscar:", buscar)
print("Palabra nueva:", nueva)
print("Frase modificada:", frase_modificada)

print("\n--- CARACTERES ---")
print("Carácter mayor:", max(frase))
print("Carácter menor:", min(frase))

print("\n--- LISTA DE PALABRAS ---")
lista_palabras = frase.split()
print("Lista:", lista_palabras)
print("Número de palabras:", len(lista_palabras))

print("\n--- DIVISIÓN POR '/' ---")
print("Resultado del split('/'): ", frase.split("/"))

print("\n--- ANÁLISIS COMPLETO FINALIZADO ---")