from conexion import *
from autos import *
from clientes import *
from revisiones import *
from usuario import *
import getpass
from funciones import *


def menuAutos():
    ciclo1 = True
    while ciclo1:
        try:
            borrarPantalla()
            print("\n.:: BIENVENIDO AL MENU DE AUTOS ::.")
            print("""SELECCIONA UNA OPCIÓN:
            1.- Añadir auto
            2.- Consultar información de un auto
            3.- Actualizar información
            4.- Eliminar auto
            5.- Salir""")
            
            opcion = int(input("Selecciona una opción numérica: "))
            if 1 <= opcion <= 5:
                if opcion == 1:
                    borrarPantalla()
                    print("AÑADIR...")
                    matricula = input("matricula del auto: ").upper()
                    marca = input("marca del auto: ")
                    modelo = input("modelo del auto: ")
                    color = input("color del auto: ")
                    nif = int(input("nif:"))
                    Autos.insertar(matricula, marca, modelo, color, nif)
                    
                elif opcion == 2:
                    borrarPantalla()
                    print("CONSULTA..")
                    Autos.consultar()
                    
                elif opcion == 3:
                    borrarPantalla()
                    print("ACTUALIZAR DATOS")
                    matricula = input("matricula del auto a actualizar: ")
                    Autos.actualizar(matricula)
                    
                elif opcion == 4:
                    borrarPantalla()
                    print("ELIMINAR")
                    matricula = input("matricula del auto a eliminar: ")
                    Autos.eliminar(matricula)
                    print("auto eliminado con exito")
                    
                elif opcion == 5:
                    print("Saliendo...")
                    esperarTecla()
                    ciclo1 = False  
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número. Intenta de nuevo.")

def menuClientes():
    salida = True
    while salida:
        try:
            borrarPantalla()
            print("\n.: BIENVENIDO AL MENU DE CLIENTES :.")
            print("""
                  1.- Registrar un cliente
                  2.- Consultar información de un cliente
                  3.- Actualizar información del cliente
                  4.- Dar de baja un cliente
                  5.- Salir""")
            
            opcion = int(input("Selecciona una opción numérica: "))

            # Verificar si la opción está dentro del rango válido
            if 1 <= opcion <= 5:
                if opcion == 1:
                    borrarPantalla()
                    print("REGISTRAR...")
                    nif = int(input("inserta nif: "))
                    nombre = input("Nombre del cliente: ")
                    direccion = input("Direccion del cliente: ")
                    ciudad = input("Ciudad del cliente: ")
                    tel = int(input("numero de telefono del cliente: "))
                    Cliente.insertar(nif, nombre, direccion, ciudad, tel)
                    
                elif opcion == 2:
                    borrarPantalla()
                    print("CONSULTAR")
                    Cliente.consultar()
                    
                elif opcion == 3:
                    borrarPantalla()
                    print("ACTUALIZAR...")
                    nif = int(input("inserta nif del cliente a actualizar: "))
                    Cliente.actualizar(nif)
                    
                elif opcion == 4:
                    borrarPantalla()
                    print("ELIMINAR...")
                    nif = int(input("inserta nif del cliente: "))
                    Cliente.eliminar(nif)
                   
                elif opcion == 5:
                    print("Saliendo...")
                    esperarTecla()
                    salida = False
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número. Intenta de nuevo.")


def menuRevisiones():
    salida = True
    while salida:
        try:
            borrarPantalla()
            print(""".:    REVISIONES     :.
                  1.- Añadir revision
                  2.- Consultar revisiones
                  3.- Actualizar revision
                  4.- Eliminar revision
                  5.- Salir""")
            eleccion = int(input("Selecciona una opción numérica: "))
            if 1 <= eleccion <= 5:
                    if eleccion == 1:
                        borrarPantalla()
                        print("AÑADIR REVISION")
                        no_revision = int(input("No. revision: "))
                        cambiofiltro = input("cambio filtro (S/N): ")
                        cambioaceite = input("cambio aceite (S/N): ")
                        cambiofrenos = input("cambio frenos (S/N): ")
                        otros = input("Otros cambios: ")
                        matricula = input("matricula del auto: ").upper()
                        Revisiones.insertar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
                        
                    elif eleccion == 2:
                        borrarPantalla()
                        print("CONSULTA")
                        Revisiones.consultar()
                        
                    elif eleccion == 3:
                        borrarPantalla()
                        print("ACTUALIZAR INFO.")
                        no_revision = int(input("No. revision a actualizar: "))
                        Revisiones.actualizar(no_revision)
                        
                    elif eleccion == 4:
                        borrarPantalla()
                        print("ELIMINAR...")
                        no_revision = int(input("No. revision a eliminar: "))
                        Revisiones.eliminar(no_revision)
                        
                    elif eleccion == 5:
                        print("Saliendo...")
                        esperarTecla()
                        salida = False
                        
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida. Intenta de nuevo.")


def menu():
    salida = True
    while salida:
        try: 
            borrarPantalla()
            print(""".:BIENVENIDO:.
            1.- MENU CLIENTES
            2.- MENU AUTOS
            3.- MENU REVISIONES
            4.- SALIR""")
            eleccion = int(input("Selecciona una opción numérica: "))

            if 1 <= eleccion <= 4:
                if eleccion == 1:
                    menuClientes()
                elif eleccion == 2:
                    menuAutos()
                elif eleccion == 3:
                    menuRevisiones()
                elif eleccion == 4:
                    print("Saliendo...")
                    esperarTecla()
                    salida = False
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número. Intenta de nuevo.")
        

def menuInicio(conexion):
    salida = True
    while salida:
        try: 
            borrarPantalla()
            print("""\nMENU DE INICIO
            1.- INICIAR SESION
            2.- REGISTRAR
            3.- SALIR""")
            eleccion = int(input("Selecciona una opción numérica: "))

            if 1 <= eleccion <= 3:
                if eleccion == 1:
                    borrarPantalla()  # jala solo falta encriptar
                    print("INICIAR SESION") 
                    email = input("Introduce tu email: ")
                    contrasena = getpass.getpass("Introduce tu contraseña: ")
                    usuario = Usuario.iniciar_sesion(conexion, email, contrasena)
                    if usuario:
                        print(f"Bienvenido {usuario['nombre']} {usuario['apellidos']}")
                        menu()  
                    else:
                        print("Correo o contraseña incorrectos.")
                        esperarTecla()
                        
                elif eleccion == 2:
                    borrarPantalla()
                    print("REGISTRAR") #jalaaaa
                    nombre = input("Introduce tu nombre: ")
                    apellidos = input("Introduce tus apellidos: ")
                    email = input("Introduce tu email: ")
                    password = getpass.getpass("Introduce tu contraseña: ")
                    usuario = Usuario(nombre, apellidos, email, password)
                    if usuario.registrar(conexion):
                        print("Usuario registrado exitosamente.")

                    else:
                        print("Error al registrar el usuario.")
                        esperarTecla()
                elif eleccion == 3:
                    borrarPantalla()
                    print("Saliendo...")
                    salida = False       
            else:
                print("Opción no válida. Intenta de nuevo.")
                esperarTecla()
        except ValueError:
            print("Error: Debes ingresar un número. Intenta de nuevo.")


if __name__ == "__main__":
    menuInicio(conexion)