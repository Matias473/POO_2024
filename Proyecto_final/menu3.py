from conexion import *
from clases3 import *
def menu5():
    salida = True
    while salida:
        try:
            print("\n--- Menú de Administración de Inventario ---")
            print("1. Añadir inventario")
            print("2. Actualizar datos")
            print("3. Ver todo el inventario")
            print("4. Ver producto específico")
            print("5. Salir")          
            opcion = int(input("Selecciona una opción numérica: "))           
            if 1 <= opcion <= 5:
                if opcion == 1:
                    try:
                        print("AÑADIR INVENTARIO...")
                        tipo = input("Tipo de producto: ")
                        nombre = input("Nombre del producto: ")
                        cantidad = float(input("Cantidad: "))
                        descripcion = input("Descripción del producto: ")
                        responsable = int(input("ID del empleado responsable: "))
                        Producto.añadir(tipo, nombre, cantidad, descripcion, responsable)
                    except ValueError:
                        print("Error: Entrada inválida. Asegúrate de ingresar los datos correctamente.")
                    except Exception as e:
                        print(f"Error al añadir el producto: {e}")
                elif opcion == 2:
                    try:
                        print("ACTUALIZAR DATOS DEL INVENTARIO...")
                        id_producto = int(input("ID del producto a actualizar: "))
                        Producto.actualizar(id_producto)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al actualizar el producto: {e}")
                elif opcion == 3:
                    try:
                        print("VER INVENTARIO COMPLETO...")
                        Producto.leer_todo()
                    except Exception as e:
                        print(f"Error al obtener el inventario: {e}")
                elif opcion == 4:
                    try:
                        print("VER PRODUCTO ESPECÍFICO...")
                        id_producto = int(input("ID del producto a consultar: "))
                        Producto.leer_uno(id_producto)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al obtener el producto: {e}")
                elif opcion == 5:
                    print("Saliendo...")
                    salida = False
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")
def menu6():
    salida = True
    while salida:
        try:
            print("\n--- Menú del Rancho ---")
            print("1. Añadir Rancho")
            print("2. Actualizar datos del rancho")
            print("3. Ver datos del rancho")
            print("4. Salir")
            opcion = int(input("Selecciona una opción numérica: "))
            if 1 <= opcion <= 4:
                if opcion == 1:
                    try:
                        print("AÑADIR INFORMACIÓN DEL RANCHO")
                        nombre = input("Nombre del rancho: ")
                        propietario = input("Nombre del propietario: ")
                        direccion = input("Dirección del rancho: ")
                        extencion = float(input("Extensión del rancho en m²: "))
                        Rancho.añadir(nombre, propietario, direccion, extencion)
                    except ValueError:
                        print("Error: Entrada inválida. Asegúrate de ingresar los datos correctamente.")
                    except Exception as e:
                        print(f"Error al añadir el rancho: {e}")
                elif opcion == 2:
                    try:
                        print("ACTUALIZAR INFORMACIÓN DEL RANCHO")
                        id_rancho = int(input("ID del rancho a actualizar: "))
                        Rancho.actualizar(id_rancho)
                    except ValueError:
                        print("Error: ID inválido. Debes ingresar un número entero.")
                    except Exception as e:
                        print(f"Error al actualizar el rancho: {e}")
                elif opcion == 3:
                    try:
                        print("VER DATOS DEL RANCHO")
                        Rancho.leer_todo()
                    except Exception as e:
                        print(f"Error al obtener los datos del rancho: {e}")
                elif opcion == 4:
                    print("Saliendo del programa...")
                    salida = False
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
        
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")
def menu7():
    salida = True
    while salida:
        try:
            print("\n--- Menú de Registro de Vacunas ---")
            print("1. Añadir registro")
            print("2. Modificar registro")
            print("3. Ver datos de registro")
            print("4. Ver todos los registros")
            print("5. Salir")
            opcion = int(input("Selecciona una opción numérica: "))
            if 1 <= opcion <= 5:
                if opcion == 1:
                    try:
                        animal = int(input("ID del animal: "))
                        responsable = input("Responsable de la vacunación: ")
                        observacion = input("Observaciones: ")
                        fecha_admin = input("Fecha en que se realizó la vacunación (YYYY-MM-DD): ")
                        Registro.añadir(animal, responsable, observacion, fecha_admin)
                    except ValueError:
                        print("Error: El ID del animal debe ser un número entero.")
                    except Exception as e:
                        print(f"Error al añadir el registro: {e}")
                elif opcion == 2:
                    try:
                        num_registro = int(input("ID del registro: "))
                        Registro.actualizar(num_registro)
                    except ValueError:
                        print("Error: El ID del registro debe ser un número entero.")
                    except Exception as e:
                        print(f"Error al actualizar el registro: {e}")
                elif opcion == 3:
                    try:
                        num_registro = int(input("ID del registro: "))
                        Registro.leer_uno(num_registro)
                    except ValueError:
                        print("Error: El ID del registro debe ser un número entero.")
                    except Exception as e:
                        print(f"Error al leer el registro: {e}")
                elif opcion == 4:
                    try:
                        Registro.leer_todo()
                    except Exception as e:
                        print(f"Error al leer los registros: {e}")
                elif opcion == 5:
                    print("Saliendo del programa...")
                    salida = False
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")