from conexion import *
class Rancho:
    def __init__(self, nombre, propietario, direccion, extencion):
        self.nombre = nombre
        self.propietario = propietario
        self.direccion = direccion
        self.extencion = extencion
    @staticmethod
    def añadir(nombre, propietario, direccion, extencion):
        try:
            sentencia = """
            INSERT INTO rancho (nombre_rancho, propietario, direccion, extencion)
            VALUES (%s, %s, %s, %s)
            """
            valores = (nombre, propietario, direccion, extencion)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro añadido con éxito.")
        except Exception as e:
            print(f"Error al añadir el registro: {e}")   
    @staticmethod
    def actualizar(id_rancho):
        set_clause = []
        parametros = []
        try:
            nuevo_nombre = input("Insertar nombre del rancho (deja en blanco para no cambiar): ")
            if nuevo_nombre:
                set_clause.append("nombre_rancho = %s")
                parametros.append(nuevo_nombre)
            nuevo_propietario = input("Insertar nombre del propietario (deja en blanco para no cambiar): ")
            if nuevo_propietario:
                set_clause.append("propietario = %s")
                parametros.append(nuevo_propietario)             
            nueva_direccion = input("Insertar dirección (deja en blanco para no cambiar): ")
            if nueva_direccion:
                set_clause.append("direccion = %s")
                parametros.append(nueva_direccion)
            nueva_extencion = input("Insertar extensión en m² (deja en blanco para no cambiar): ")
            if nueva_extencion:
                set_clause.append("extencion = %s")
                parametros.append(nueva_extencion)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE rancho SET {set_clause_str} WHERE id_rancho = %s"
                parametros.append(id_rancho)
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
    @staticmethod
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM rancho")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"ID: {i[0]}, Nombre del Rancho: {i[1]}, Propietario: {i[2]}, Dirección: {i[3]}, Extensión: {i[4]} m²")
        except Exception as e:
            print(f"Error al leer los registros: {e}")
class Producto:
    def __init__(self, tipo, nombre, cantidad, descripcion, responsable):
        self.tipo = tipo
        self.nombre = nombre
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.responsable = responsable
    def añadir(tipo, nombre, cantidad, descripcion, responsable):
        try:
            sentencia = "INSERT INTO producto (tipo, nombre, cantidad, descripcion, responsable) VALUES (%s, %s, %s, %s, %s)"
            valores = (tipo, nombre, cantidad, descripcion, responsable)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Producto añadido con éxito.")
        except Exception as e:
            print(f"Error al añadir el producto: {e}")
    def actualizar(id_producto):
        set_clause = []
        parametros = []
        try:
            nuevo_tipo = input("Insertar tipo del producto (deja en blanco para no cambiar): ")
            if nuevo_tipo:
                set_clause.append("tipo = %s")
                parametros.append(nuevo_tipo)
            nuevo_nombre = input("Insertar nombre del producto (deja en blanco para no cambiar): ")
            if nuevo_nombre:
                set_clause.append("nombre = %s")
                parametros.append(nuevo_nombre)
            nueva_cantidad = input("Insertar cantidad (deja en blanco para no cambiar): ")
            if nueva_cantidad:
                nueva_cantidad = int(nueva_cantidad)
                set_clause.append("cantidad = %s")
                parametros.append(nueva_cantidad)
            nueva_descripcion = input("Insertar descripción (deja en blanco para no cambiar): ")
            if nueva_descripcion:
                set_clause.append("descripcion = %s")
                parametros.append(nueva_descripcion)
            nuevo_responsable = int(input("Insertar responsable (deja en blanco para no cambiar): "))
            if nuevo_responsable:
                set_clause.append("responsable = %s")
                parametros.append(nuevo_responsable)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE producto SET {set_clause_str} WHERE id_producto = %s"
                parametros.append(id_producto)
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
            print(f"Error al actualizar el producto: {e}")
    def leer_uno(id_producto):
        try:
            cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, nombre: {i[2]}, cantidad: {i[3]}, descripcion: {i[4]}, responsable: {i[5]}")
        except Exception as e:
            print(f"Error al leer el producto: {e}")
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM producto")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, nombre: {i[2]}, cantidad: {i[3]}, descripcion: {i[4]}, responsable: {i[5]}")
        except Exception as e:
            print(f"Error al leer los productos: {e}")
class Registro:
    def __init__(self, num_registro, animal, responsable, observacion, fecha_admin):
        self.num_registro = num_registro
        self.animal = animal
        self.responsable = responsable
        self.observacion = observacion
        self.fecha_admin = fecha_admin
    @staticmethod
    def añadir(animal, responsable, observacion, fecha_admin):
        try:
            sentencia = "INSERT INTO reg_vacunas (animal, responsable, observacion, fecha_admin) VALUES (%s, %s, %s, %s)"
            valores = (animal, responsable, observacion, fecha_admin)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro añadido con éxito.")
        except Exception as e:
            print(f"Error al añadir el registro: {e}")
    @staticmethod
    def actualizar(num_registro):
        set_clause = []
        parametros = []
        try:
            nuevo_animal = input("Insertar nuevo ID del animal (deja en blanco para no cambiar): ")
            if nuevo_animal:
                set_clause.append("animal = %s")
                parametros.append(nuevo_animal)
            nuevo_responsable = input("Insertar nuevo responsable (deja en blanco para no cambiar): ")
            if nuevo_responsable:
                set_clause.append("responsable = %s")
                parametros.append(nuevo_responsable)
            nueva_observacion = input("Insertar nueva observación (deja en blanco para no cambiar): ")
            if nueva_observacion:
                set_clause.append("observacion = %s")
                parametros.append(nueva_observacion)
            nueva_fecha_admin = input("Insertar nueva fecha de administración (deja en blanco para no cambiar): ")
            if nueva_fecha_admin:
                set_clause.append("fecha_admin = %s")
                parametros.append(nueva_fecha_admin)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE reg_vacunas SET {set_clause_str} WHERE num_registro = %s"
                parametros.append(num_registro)
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
    @staticmethod
    def leer_uno(num_registro):
        try:
            cursor.execute("SELECT * FROM reg_vacunas WHERE num_registro = %s", (num_registro,))
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"num_registro: {i[0]}, animal: {i[1]}, responsable: {i[2]}, observacion: {i[3]}, fecha_admin: {i[4]}")
        except Exception as e:
            print(f"Error al leer el registro: {e}")
    @staticmethod
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM reg_vacunas")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"num_registro: {i[0]}, animal: {i[1]}, responsable: {i[2]}, observacion: {i[3]}, fecha_admin: {i[4]}")
        except Exception as e:
            print(f"Error al leer los registros: {e}")
    @staticmethod
    def eliminar(num_registro):
        try:
            sentencia = "DELETE FROM reg_vacunas WHERE num_registro = %s"
            cursor.execute(sentencia, (num_registro,))
            conexion.commit()
            print("Registro eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")