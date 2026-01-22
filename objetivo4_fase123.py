#Adrián Solís León 2ºDAM

#Validar número de alumnos
num_alumnos = 0
while num_alumnos <= 0:
    num_alumnos = int(input("Introduce el número de alumnos: "))
    if num_alumnos <= 0:
        print("Debe ser mayor que 0.")

#Inicializar contadores
total_media = 0
aprobados = 0
necesitan_mejorar = 0
suspensos = 0

#Procesar cada alumno
for i in range(num_alumnos):
    print("\nAlumno", i + 1)
    nombre = input("Nombre: ")

    #Validar número de notas
    num_notas = 0
    while num_notas <= 0:
        num_notas = int(input("¿Cuántas notas tiene " + nombre + "? "))
        if num_notas <= 0:
            print("Debe tener al menos una nota.")

    #Recoger las notas
    suma_notas = 0
    for j in range(num_notas):
        nota = float(input("Introduce la nota " + str(j + 1) + ": "))
        suma_notas += nota

    #Calcular media
    media = suma_notas / num_notas
    total_media += media

    #Mostrar resultado
    resultado = ""
    if media >= 5:
        resultado = "Aprobado"
        aprobados += 1
    elif media >= 4:
        resultado = "Necesita mejorar"
        necesitan_mejorar += 1
    else:
        resultado = "Suspenso"
        suspensos += 1

    print("Media de", nombre, ":", round(media, 2), "->", resultado)

#Mostrar resumen final
media_grupo = total_media / num_alumnos
print("\n--- RESUMEN FINAL ---")
print("Media del grupo:", round(media_grupo, 2))
print("Aprobados:", aprobados)
print("Necesita mejorar:", necesitan_mejorar)
print("Suspensos:", suspensos)