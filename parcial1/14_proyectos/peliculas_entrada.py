from otras_funciones_2 import *

juanito = False
while not juanito:
    print("bienvenido al sistema de peliculas")
    print("\n")
    print("1-añadir pelicula al repertorio")
    print("2-eliminar una pelicula del repertorio")
    print("3-remplazar titulo")
    print("4-mostrar catalogo")
    print("5-buscar")
    print("6-salir")
    eleccion = input("selecciona una opcion: ").upper()
    
    clear_screen()

    if eleccion == "1" or eleccion == "AÑADIR":
        añadirPeliculas()
    elif eleccion == "2" or eleccion == "ELIMINAR":
        remover_pelicula()
    elif eleccion == "3" or eleccion == "REMPLAZAR":
        remplazar(lista_peliculas)
    elif eleccion == "4" or eleccion == "VER":
        repertorio()
    elif eleccion == "5" or eleccion == "BUSCAR":
        buscar_pelicula()
    elif eleccion == "6" or eleccion == "SALIR":
        salir()
        juanito = True
    else:
        print("opcion no encontrada, por favor seleccionar una opcion valida.")
        esperar_tecla()
    clear_screen()
