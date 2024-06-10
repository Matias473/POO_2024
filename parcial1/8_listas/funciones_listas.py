"""
def agregar_pelicula(pelicula, lista_peliculas):
    lista_peliculas.append(pelicula)
    print(f"¡{pelicula} ha sido agregada a la lista de películas!")

def remover_pelicula(pelicula, lista_peliculas):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print(f"¡{pelicula} ha sido removida de la lista de películas!")
    else:
        print(f"{pelicula} no se encuentra en la lista de películas.")

def consultar_peliculas(lista_peliculas):
    print("Lista de películas:")
    for pelicula in lista_peliculas:
        print(pelicula)
"""

paises = ["Mexico", "USA", "Brasil", "Japon"]
numeros = [23, 100, 3.1416, 0.100]
varios = ["Hola", True, 100,10.22]
"""
#orden de lista
#SOLO  se puede cuando hay valores str o numericos (osea un solo tipo en la lista)
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#añadir elementos
print(numeros)
numeros.insert(len(numeros), 100)
print(numeros)
numeros.append(100)

#eliminanar elementos
print(numeros)
numeros.pop(2) #elimina la posicion que esta en la lista
print(numeros)
numeros.remove(100) #elimina el elemento a querer borrar

#buscar en una lista
encotrar = "Brasil" in paises
print(encotrar) #muestra un boleano para encontrar en la lista 
#en este caso imprimira TRUE


#dar la vuelta
print(varios)
varios.reverse()
print(varios)  #en este caso da la vuelta al contenido dentro de la lista
#creemos que se puede usar con la funcion ordenar para despues acomodar de modo desendente

#unir lista
print(paises)
paises.extend()
print(paises)

#vaciar lista
print(varios)
varios.clear()
print(varios)
"""