from conexion import *
from clases2 import *
def menu3():
    salida = True
    while salida:
        try:
            print("\n--- Menú de Administración de Instalaciones ---")
            print("1. Añadir una instalación")
            print("2. Actualizar información de una instalación")
            print("3. Ver información de todas las instalaciones")
            print("4. Ver información de una instalación")
            print("5. Dar de baja una instalación")
            print("6. Salir")           
            opcion = int(input("Selecciona una opción numérica: "))           
            if 1 <= opcion <= 6:
                if opcion == 1:
                    try:
                        print("AÑADIR UNA INSTALACIÓN...")
                        print("Seleccionar tipo de la instalación:")
                        print("1. Establo")
                        print("2. Porqueriza")
                        print("3. Caballeriza")
                        print("4. Gallinero")
                        tipo_opcion = int(input("Selecciona una opción (1-4): "))                       
                        tipos = {
                            1: "Establo",
                            2: "Porqueriza",
                            3: "Caballeriza",
                            4: "Gallinero"
                        }                      
                        tipo = tipos.get(tipo_opcion, "Desconocido")
                        fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
                        extencion = float(input("Extensión de la instalación (en metros cuadrados): "))
                        ubicacion = input("Descripción de la ubicación: ")
                        estado = input("Estado de la instalación (Buenas condiciones/Falta mantenimiento): ")
                        fecha_revision = input("Fecha de última revisión (YYYY-MM-DD): ")
                        estatus = 1
                        rancho_id = int(input("ID del rancho donde se ubica: "))
                        Instalacion.añadir(tipo, fecha_creacion, extencion, ubicacion, estado, fecha_revision, estatus, rancho_id)
                    except ValueError:
                        print("Error: Entrada inválida. Asegúrate de ingresar los datos correctamente.")
                    except Exception as e:
                        print(f"Error al añadir la instalación: {e}")
                elif opcion == 2:
                    try:
                        print("ACTUALIZAR INFORMACIÓN DE UNA INSTALACIÓN...")
                        id_instalacion = int(input("ID de la instalación a actualizar: "))
                        Instalacion.actualizar(id_instalacion)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al actualizar la instalación: {e}")
                elif opcion == 3:
                    try:
                        print("VER TODA LA INFORMACIÓN DE INSTALACIONES...")
                        Instalacion.leer_todo()
                    except Exception as e:
                        print(f"Error al obtener la información de las instalaciones: {e}")
                elif opcion == 4:
                    try:
                        print("VER INFORMACIÓN DE UNA INSTALACIÓN...")
                        id_instalacion = int(input("ID de la instalación a inspeccionar: "))
                        Instalacion.leer_uno(id_instalacion)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al obtener la información de la instalación: {e}")
                elif opcion == 5:
                    try:
                        print("DAR DE BAJA UNA INSTALACIÓN...")
                        id_instalacion = int(input("ID de la instalación a dar de baja: "))
                        Instalacion.eliminar(id_instalacion)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al eliminar la instalación: {e}")
                elif opcion == 6:
                    print("Saliendo...")
                    salida = False
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")
def menu4():
    while True:
        try:
            print("\n--- Menú de Administración de Actividades ---")
            print("1. Registrar actividad")
            print("2. Editar información de una actividad")
            print("3. Ver todos los registros")
            print("4. Ver registros de un día")
            print("5. Salir")         
            opcion = int(input("Selecciona una opción numérica: "))
            if opcion == 1:
                try:
                    print("REGISTRAR ACTIVIDAD...")
                    tipo = input("Tipo de actividad: ").strip()
                    descripcion = input("Descripción de la actividad: ").strip()
                    fecha_elab = input("Fecha de la actividad (YYYY-MM-DD): ").strip()
                    responsable = input("Responsable de la actividad: ").strip()                 
                    Actividad.añadir(tipo, descripcion, fecha_elab, responsable)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrate de ingresar los datos correctamente.")
                except Exception as e:
                    print(f"Error al registrar la actividad: {e}")
            elif opcion == 2:
                try:
                    print("EDITAR INFORMACIÓN DE UNA ACTIVIDAD...")
                    id_actividad = int(input("ID de la actividad a editar: ").strip())
                    Actividad.actualizar(id_actividad)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrate de ingresar los datos correctamente.")
                except Exception as e:
                    print(f"Error al actualizar la actividad: {e}")
            elif opcion == 3:
                try:
                    print("VER TODOS LOS REGISTROS...")
                    Actividad.leer_todo()
                except Exception as e:
                    print(f"Error al obtener todos los registros: {e}")
            elif opcion == 4:
                try:
                    print("VER REGISTROS DE UN DÍA...")
                    fecha_elab = input("Fecha de los registros (YYYY-MM-DD): ").strip()
                    Actividad.leer_uno(fecha_elab)
                except ValueError:
                    print("Error: Fecha inválida. Asegúrate de ingresar la fecha en el formato correcto.")
                except Exception as e:
                    print(f"Error al obtener los registros de la fecha especificada: {e}")
            elif opcion == 5:
                print("Saliendo...")
                break 
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")