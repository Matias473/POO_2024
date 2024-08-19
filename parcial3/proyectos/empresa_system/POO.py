from conexion import *

class Empleado:
    def __init__(self,nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear_empleado(conexion, nombre, puesto, salario):
        cursor = conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado creado exitosamente")
    
    def leer_empleados(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")
            
    def actualizar_empleado(conexion, id, nombre, puesto, salario):
        cursor = conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE EmpleadoID = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado actualizado exitosamente")

    def eliminar_empleado(conexion, id):
        cursor = conexion.cursor()
        query = "DELETE FROM empleados WHERE EmpleadoID = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        print("Empleado eliminado exitosamente")
