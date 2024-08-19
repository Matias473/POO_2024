from conexion import *
from clases import *
def menu1():
    salida1 = True
    while salida1:
        try:
            print("\n--- Menú de Administración de Ganado ---")
            print("1. Añadir un animal")
            print("2. Actualizar información de un animal")
            print("3. Ver información de todos los animales")
            print("4. Ver información de un animal")
            print("5. Eliminar animal de los registros")
            print("6. Salir")  
            opcion = int(input("Selecciona una opción numérica: "))
            if 1 <= opcion <= 6:
                if opcion == 1:
                    try:
                        print("AÑADIR UN ANIMAL...")
                        especie = input("Especie del animal: ").strip()
                        raza = input("Raza del animal: ").strip()
                        sexo = input("Sexo del animal (M/F): ").upper().strip()
                        edad = input("Fecha de nacimiento del animal (YYYY-MM-DD): ").strip()
                        peso = float(input("Peso del animal: ").strip())
                        salud = input("Salud del animal (Saludable/Enfermo): ").strip()
                        destino_productivo = input("Destino productivo del animal: ").strip()
                        ubicacion = int(input("ID de la instalación donde se encuentra: ").strip())
                        estatus = 1
                        Ganado.añadir(especie, raza, sexo, edad, peso, salud, destino_productivo, ubicacion, estatus)
                    except ValueError:
                        print("Error: Entrada inválida. Asegúrate de ingresar los datos correctos.")
                    except Exception as e:
                        print(f"Error al añadir el animal: {e}")
                elif opcion == 2:
                    try:
                        print("ACTUALIZAR DATOS...")
                        id_ganado = int(input("ID del animal a actualizar: ").strip())
                        Ganado.actualizar(id_ganado)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al actualizar los datos del animal: {e}")
                elif opcion == 3:
                    try:
                        print("INFORMACION DE TODOS LOS ANIMALES...")
                        Ganado.leer_todo()
                    except Exception as e:
                        print(f"Error al obtener la información de los animales: {e}")
                elif opcion == 4:
                    try:
                        print("INFORMACION DE UN ANIMAL...")
                        id_ganado = int(input("ID del animal a inspeccionar: ").strip())
                        Ganado.leer_uno(id_ganado)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al obtener la información del animal: {e}")
                elif opcion == 5:
                    try:
                        print("ELIMINAR UN ANIMAL...")
                        id_ganado = int(input("ID del animal a dar de baja: ").strip())
                        Ganado.eliminar(id_ganado)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al eliminar el animal: {e}")
                elif opcion == 6:
                    print("Saliendo...")
                    salida1 = False
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")
def menu2():
    salida = True
    while salida:
        try:
            print("\n--- Menú de Administración de Empleados ---")
            print("1. Añadir un empleado")
            print("2. Actualizar información de un empleado")
            print("3. Ver información de todos los empleados")
            print("4. Ver información de un empleado")
            print("5. Dar de baja a un empleado")
            print("6. Salir")           
            opcion = int(input("Selecciona una opción numérica: "))
            if opcion == 1:
                try:
                    print("REGISTRAR EMPLEADO...")
                    nombre = input("Nombre del empleado (sin apellidos): ").strip()
                    apellido_p = input("Apellido paterno: ").strip()
                    apellido_m = input("Apellido materno: ").strip()
                    curp = input("CURP del empleado: ").upper().strip()
                    fecha_nac = input("Fecha nacimiento (YYYY-MM-DD): ").strip()
                    rol = input("Rol del empleado: ").strip()
                    salario = float(input("Salario del empleado: ").strip())
                    estatus = 1
                    ranchoID = int(input("ID del rancho donde trabajará: ").strip())
                    Empleado.añadir(nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID)
                except ValueError as ve:
                    print(f"Error: {ve}. Asegúrate de ingresar los datos correctos.")
            elif opcion == 2:
                try:
                    print("ACTUALIZAR INFORMACIÓN DEL EMPLEADO...")
                    id_empleado = int(input("ID del empleado: ").strip())
                    Empleado.actualizar(id_empleado)
                except ValueError:
                    print("Error: ID inválido. Debes ingresar un número entero.")
                except Exception as e:
                    print(f"Error al actualizar la información del empleado: {e}")
            elif opcion == 3:
                try:
                    print("VER INFORMACIÓN DE TODOS LOS EMPLEADOS...")
                    Empleado.leer_todo()
                except Exception as e:
                    print(f"Error al obtener la información de los empleados: {e}")
            elif opcion == 4:
                try:
                    print("VER INFORMACIÓN DEL EMPLEADO...")
                    id_empleado = int(input("ID del empleado: ").strip())
                    Empleado.leer_uno(id_empleado)
                except ValueError:
                    print("Error: ID inválido. Debes ingresar un número entero.")
                except Exception as e:
                    print(f"Error al obtener la información del empleado: {e}")
            elif opcion == 5:
                try:
                    print("DAR DE BAJA A UN EMPLEADO...")
                    id_empleado = int(input("ID del empleado: ").strip())
                    Empleado.eliminar(id_empleado)
                except ValueError:
                    print("Error: ID inválido. Debes ingresar un número entero.")
                except Exception as e:
                    print(f"Error al dar de baja al empleado: {e}")
            elif opcion == 6:
                print("Saliendo del programa...")
                salida = False 
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")