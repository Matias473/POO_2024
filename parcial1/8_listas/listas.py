"""
List (Array)
son colecciones o conjuntos de datos/valor bajo un mismo nombre, para acceder a los valores
se hace con un indice numerico


Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable permite miembros duplicados
"""
"""

#ejemplo 1- crear una lista de numeros e imprimir el contenido
numeros = [23,34]
print(numeros[0])

#recorrer una lista con un for
numeros = [23,34]
for i in numeros:
    print(i)

#recorrer una lista con while
numeros = [23,34]
i=0
while i<= len(numeros) -1:
    print(numeros[i])
    i+=1
"""
"""
#ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra

palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra {palabra_buscar} en la posición {i}")
else:
    print("No encontré la palabra en la lista")
"""
"""
#con ciclo while
palabra = ["hola", "utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

i = 0
encontrada = False

while i < len(palabra): #la funcion .len() se usa para sacar la longitud de la lista
    if palabra[i] == palabra_buscar:
        print(f"Encontré la palabra {palabra_buscar} en la posición {i}")
        encontrada = True
    i += 1

if not encontrada:
    print("No encontré la palabra en la lista")
"""

"""#añadir o eliminar elementos en una lista
numeros = [23,34,23]
print(numeros)

#añadir elementos a una lista
numeros.append(100)
numeros.append(100)
print(numeros)
numeros.insert(3,200) #se coloca posicion y despues lo que se quiere añadir
#la posicion inicia en 0 
# si se coloca un numero negativo jala la posicion de derecha a izquierda
print(numeros)

#eliminar elementos de una lista
numeros.remove(100) #indica el elemento a remover
print(numeros)
numeros.pop(2) #indica la posicion del elemento a borrar
print(numeros)
"""
"""
agenda = [
    ("Carlos", 618123467),
    ("Leo", 6678293),
    ("Sebastian", 727357839),
    ("Pedro", 672883293)
]

for i, (nombre, numero) in enumerate(agenda, start=1):
    print(f"{i}.- {nombre}: {numero}")

"""
"""
#ejemplo 5 crear un programa que permita gestionar (administrar) peliculas,
#colocar un menu de opciones para agregar, remover, consultar pleiculas.
#Notas:
#Utilizar funciones y mandar llamar desde otro archivo
#Utilizar listas para almacenar los nombres de peliculas

#pasos en base a lo aprendido
#1- crear 2 carpetas (una con las funciones y otra con el codigo)

import funciones_listas

lista_peliculas = []

while True:
    print("\n** Gestión de Películas **")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pelicula = input("Ingrese el nombre de la película a agregar: ")
        funciones_listas.agregar_pelicula(pelicula, lista_peliculas)
    elif opcion == "2":
        pelicula = input("Ingrese el nombre de la película a remover: ")
        funciones_listas.remover_pelicula(pelicula, lista_peliculas)
    elif opcion == "3":
        funciones_listas.consultar_peliculas(lista_peliculas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
"""