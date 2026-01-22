#Adrián Solís León 2ºDAM

#Solicitamos los datos al usuario
primer_nombre = input("Introduce tu nombre: ")
nombre_apellidos = input("Introduce tu nombre completo: ")
curso = input("Introduce tu curso: ")
grupo = input("Introduce tu grupo: ")
carpeta = input("Introduce el nombre de la carpeta del proyecto: ")

#Mostramos la ficha con solo un print como dice el ejercicio
print(
    f"--------------------------------\n"
    f"\tFicha del alumno/a\n"
    f"--------------------------------\n"
    f"Nombre: \"{nombre_apellidos}\"\n"
    f"Curso: {curso}\tGrupo: {grupo}\n"
    f"Ruta del proyecto: C:\\Users\\{primer_nombre}\\DAM\\{carpeta}\n"
    f"--------------------------------"
)
