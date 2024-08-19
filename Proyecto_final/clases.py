from conexion import *
class Animal:
    def __init__(self, especie, raza, sexo, edad, peso):
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
class Ganado(Animal):

    def __init__(self, especie, raza, sexo, edad, peso, salud, destino_productivo, ubicacion, estatus):
        super().__init__(especie, raza, sexo, edad, peso)
        self.salud = salud
        self.destino = destino_productivo
        self.ubicacion = ubicacion
        self.estatus = estatus


    def añadir(self):#se modifico
        try:
            # Sentencia SQL para insertar los datos
            sentencia = "INSERT INTO ganado (especie, raza, sexo, edad, peso, salud, destino, ubicacion, estatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (self.especie, self.raza, self.sexo, self.edad, self.peso, self.salud, self.destino, self.ubicacion, self.estatus)
            cursor.execute(sentencia, valores)
            conexion.commit() 
            print("Registro añadido con éxito.")
        except Exception as e:
            print(f"Error al añadir el registro: {e}")
        finally:
            print("Proceso de inserción finalizado.")

    def actualizar(id_ganado):
        set_clause = []
        parametros = []
        try:
            nueva_especie = input("Insertar especie (deja en blanco para no cambiar): ")
            if nueva_especie:
                set_clause.append("especie = %s")
                parametros.append(nueva_especie)
            nueva_raza = input("Insertar raza (deja en blanco para no cambiar): ")
            if nueva_raza:
                set_clause.append("raza = %s")
                parametros.append(nueva_raza)
            nuevo_sexo = input("Insertar sexo (MACHO/HEMBRA, deja en blanco para no cambiar): ").upper()
            if nuevo_sexo:
                set_clause.append("sexo = %s")
                parametros.append(nuevo_sexo)
            nueva_edad = input("Insertar fecha de nacimiento del animal (YYYY-MM-DD, deja en blanco para no cambiar): ")
            if nueva_edad:
                set_clause.append("edad = %s")
                parametros.append(nueva_edad)
            nuevo_peso = input("Insertar peso del animal en KILOS (deja en blanco para no cambiar): ")
            if nuevo_peso:
                nuevo_peso = float(nuevo_peso)
                set_clause.append("peso = %s")
                parametros.append(nuevo_peso)
            nueva_salud = input("Insertar salud del animal (deja en blanco para no cambiar): ")
            if nueva_salud:
                set_clause.append("salud = %s")
                parametros.append(nueva_salud)
            nuevo_destino_productivo = input("Insertar destino productivo (deja en blanco para no cambiar): ")
            if nuevo_destino_productivo:
                set_clause.append("destino = %s")
                parametros.append(nuevo_destino_productivo)
            nueva_ubicacion = input("Insertar ID del establo donde se encuentra actualmente (deja en blanco para no cambiar): ")
            if nueva_ubicacion:
                nueva_ubicacion = int(nueva_ubicacion)
                set_clause.append("ubicacion = %s")
                parametros.append(nueva_ubicacion)
            nuevo_estatus = input("Insertar estatus (1 para activo, 0 para inactivo, deja en blanco para no cambiar): ")
            if nuevo_estatus:
                nuevo_estatus = int(nuevo_estatus)
                set_clause.append("estatus = %s")
                parametros.append(nuevo_estatus)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE ganado SET {set_clause_str} WHERE id_ganado = %s"
                parametros.append(id_ganado)
                cursor.execute(sentencia, tuple(parametros))
                conexion.commit()
                print("Actualización hecha con éxito")
            else:
                print("No se realizaron cambios.")
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
        finally:
            print("Proceso de actualización finalizado.")
    
    def leer_todo(): #se modifico
        try:
            # Ejecuta la consulta para seleccionar todos los registros con estatus 1
            cursor.execute("SELECT * FROM ganado WHERE estatus = %s", (1,))
            resultados = cursor.fetchall()  # Obtiene todos los registros que coinciden con la consulta
        
            if resultados:
                return resultados  # Devuelve la lista de tuplas con los datos del ganado
            else:
                return []  # Devuelve una lista vacía si no hay resultados
        except Exception as e:
            print(f"Error al leer los registros: {e}")
            return []  # Devuelve una lista vacía en caso de error

        
    #aqui va el leer uno
    def leer_uno(id_ganado):#se coloca esta
        try:
            sentencia = "SELECT * FROM ganado WHERE id_ganado = %s"
            cursor.execute(sentencia, (id_ganado,))
            resultados = cursor.fetchone()  # Obtener solo un registro
            if resultados:
                return resultados  # Devuelve la tupla con los datos del animal
            else:
                return None
        except Exception as e:
            print(f"Error al leer el registro: {e}")
            return None
        
    def eliminar(id_ganado):#este se modifico
        estatus = 0
        try:
            sentencia = "UPDATE ganado SET estatus = %s WHERE id_ganado = %s"
            valores = (estatus, id_ganado)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro eliminado (estatus cambiado a 0) con éxito.")
            return True  # Indica que la eliminación fue exitosa
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
            return False  # Indica que la eliminación falló


class Empleado:
    def __init__(self, nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID):
        self.nombre = nombre
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.curp = curp
        self.fecha_nac = fecha_nac
        self.rol = rol
        self.salario = salario
        self.estatus = estatus
        self.ranchoID = ranchoID
    def añadir(nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID):
        try:
            sentencia = """
                INSERT INTO empleado (nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, apellido_p, apellido_m, curp, fecha_nac, rol, salario, estatus, ranchoID)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Empleado añadido exitosamente.")
        except Exception as e:
            print(f"Error al añadir el empleado: {e}")
    def actualizar(id_empleado):
        set_clause = []
        parametros = []
        try:
            nuevo_nombre = input("Insertar nombre (deja en blanco para no cambiar): ")
            if nuevo_nombre:
                set_clause.append("nombre = %s")
                parametros.append(nuevo_nombre)
            nuevo_apellido_p = input("Insertar apellido paterno (deja en blanco para no cambiar): ")
            if nuevo_apellido_p:
                set_clause.append("apellido_p = %s")
                parametros.append(nuevo_apellido_p)
            nuevo_apellido_m = input("Insertar apellido materno (deja en blanco para no cambiar): ")
            if nuevo_apellido_m:
                set_clause.append("apellido_m = %s")
                parametros.append(nuevo_apellido_m)
            nueva_curp = input("Insertar CURP (deja en blanco para no cambiar): ").upper()
            if nueva_curp:
                set_clause.append("curp = %s")
                parametros.append(nueva_curp)
            nueva_fecha_nac = input("Insertar fecha de nacimiento (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_nac:
                set_clause.append("fecha_nac = %s")
                parametros.append(nueva_fecha_nac)
            nuevo_rol = input("Insertar rol del empleado (deja en blanco para no cambiar): ")
            if nuevo_rol:
                set_clause.append("rol = %s")
                parametros.append(nuevo_rol)
            nuevo_salario = input("Insertar salario (deja en blanco para no cambiar): ")
            if nuevo_salario:
                nuevo_salario = float(nuevo_salario)
                set_clause.append("salario = %s")
                parametros.append(nuevo_salario)
            nuevo_estatus = input("Insertar estatus del empleado (1/0) (deja en blanco para no cambiar): ")
            if nuevo_estatus:
                nuevo_estatus = int(nuevo_estatus)
                set_clause.append("estatus = %s")
                parametros.append(nuevo_estatus)
            nuevo_ranchoID = input("Insertar ID de rancho (deja en blanco para no cambiar): ")
            if nuevo_ranchoID:
                nuevo_ranchoID = int(nuevo_ranchoID)
                set_clause.append("ranchoID = %s")
                parametros.append(nuevo_ranchoID)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE empleado SET {set_clause_str} WHERE id_empleado = %s"
                parametros.append(id_empleado)
                continuar = input("¿Ejecutar cambios? (SI/NO): ").upper()
                if continuar == "SI":
                    cursor.execute(sentencia, tuple(parametros))
                    conexion.commit()
                    print("Actualización realizada con éxito.")
                else:
                    print("Actualización cancelada.")
            else:
                print("No se realizaron cambios.")
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM empleado WHERE estatus = 1")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, nombre: {i[1]}, apellido paterno: {i[2]}, apellido materno: {i[3]}, curp: {i[4]}, fecha nacimiento: {i[5]}, rol: {i[6]}, salario: {i[7]}, estatus: {i[8]}, ranchoID: {i[9]}")
        except Exception as e:
            print(f"Error al leer los empleados: {e}")
    def leer_uno(id_empleado):
        try:
            cursor.execute("SELECT * FROM empleado WHERE id_empleado = %s", (id_empleado,))
            resultados = cursor.fetchall()
            if resultados:
                for i in resultados:
                    print(f"id: {i[0]}, nombre: {i[1]}, apellido paterno: {i[2]}, apellido materno: {i[3]}, curp: {i[4]}, fecha nacimiento: {i[5]}, rol: {i[6]}, salario: {i[7]}, estatus: {i[8]}, ranchoID: {i[9]}")
            else:
                print("No se encontró el empleado con el ID proporcionado.")
        except Exception as e:
            print(f"Error al leer el empleado: {e}")
    def eliminar(id_empleado):
        try:
            estatus = 0
            sentencia = "UPDATE empleado SET estatus = %s WHERE id_empleado = %s"
            valores = (estatus, id_empleado)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro eliminado (estatus cambiado a 0) con éxito.")
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")