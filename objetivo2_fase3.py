#Adrián Solís León 2ºDAM

#Creamos tres listas con nombres de productos informáticos.
ordenadores = ["Portátil", "Sobremesa", "Servidor"]
perifericos = ["Ratón", "Teclado", "Monitor"]
accesorios = ["Altavoces", "Funda", "Webcam"]

#Creamos una tupla con tres precios distintos.
precios_base = (750, 1200, 2200)

#Creamos un diccionario que agrupa las listas por categoría.
catalogo = {
    "Ordenadores": ordenadores,
    "Periféricos": perifericos,
    "Accesorios": accesorios
}

#Mostramos las tres listas
print(ordenadores)
print(perifericos)
print(accesorios)

#Mostramos la tupla de precios
print(precios_base)

#Mostramos el contenido completo del diccionario
print(catalogo)

#Mostramos el segundo periférico
print("Segundo periférico:", catalogo["Periféricos"][1])
