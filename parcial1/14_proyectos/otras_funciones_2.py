#funciones de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."


#funciones de pelicula
lista_peliculas = []

import os

def clear_screen():
    os.system('cls')

def añadirPeliculas(): #1
    pelicula = input("inserte nombre de la pelicula: \n")
    if pelicula in lista_peliculas:
        print("la pelicula ya está dentro del sistema")
    else:
        lista_peliculas.append(pelicula)
        print("pelicula añadida con exito")
    esperar_tecla()
   
def remover_pelicula():#2
    pelicula = input("pelicula a remover: ")
    seguro = input("desea remover la pelicula? SI/NO\n").upper()
    if seguro == "SI":
        if pelicula in lista_peliculas:
            lista_peliculas.remove(pelicula)
            print(f"¡{pelicula} ha sido removida de la lista de películas!")
        else:
            print(f"{pelicula} no se encuentra en la lista de películas.")
    esperar_tecla()


def remplazar(lista_peliculas): #3
    peli = input("Inserte película a reemplazar: ")
    if peli in lista_peliculas:
        indice = lista_peliculas.index(peli)
        remplazo = input(f"Añadir el reemplazo de {peli}: ")
        decision = input(f"¿Estás seguro de reemplazar {peli} por {remplazo}? (S/N)").upper()
        if decision == "S" or decision == "SI":
            lista_peliculas[indice] = remplazo
            print("Lista actualizada")
        else:
            print("Cambio no realizado.\nVolviendo al menú.")

    else:
        print(f"{peli} no fue encontrada en el sistema")
    esperar_tecla()

def repertorio():#4
    print("Peliculas en el repertorio:")
    for pelicula in lista_peliculas:
        print(pelicula)
    esperar_tecla()

def buscar_pelicula(): #5
    pelicula_buscada = input("Ingrese el nombre de la película que desea buscar: ")
    if pelicula_buscada in lista_peliculas:
        indices = [i for i, x in enumerate(lista_peliculas) if x == pelicula_buscada]
        if len(indices) == 1:
            print(f"{pelicula_buscada} se encuentra en la posición {indices[0]} en la lista de películas.")
        else:
            print(f"{pelicula_buscada} se encuentra en las siguientes posiciones en la lista de películas:")
            for indice in indices:
                print(f"- Posición {indice}")
    else:
        print(f"{pelicula_buscada} no fue encontrada en la lista de películas.")
    esperar_tecla()

def salir():#6
    print("saliendo del sistema")
    esperar_tecla()

def esperar_tecla():
    input("Presiona cualquier tecla para continuar...")

