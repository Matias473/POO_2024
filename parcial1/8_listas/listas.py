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
#ejemplo 2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra

palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra en la posición {i}")
else:
    print("No encontré la palabra en la lista")