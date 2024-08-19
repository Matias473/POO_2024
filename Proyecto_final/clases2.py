from conexion import *
class Instalacion:
    def __init__(self, tipo, fecha_creacion, extension, ubicacion, estado, fecha_revision, estatus, rancho_id):
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.extension = extension
        self.ubicacion = ubicacion
        self.estado = estado
        self.fecha_revision = fecha_revision
        self.estatus = estatus
        self.rancho_id = rancho_id
    def añadir(tipo, fecha_creacion, extension, ubicacion, estado, fecha_revision, estatus, rancho_id):
        try:
            sentencia = """
                INSERT INTO instalaciones 
                (tipo, fecha_creacion, extension, ubicacion, estado, fecha_revision, estatus, rancho_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (tipo, fecha_creacion, extension, ubicacion, estado, fecha_revision, estatus, rancho_id)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Instalación añadida exitosamente.")
        except Exception as e:
            print(f"Error al añadir la instalación: {e}")
    def actualizar(id_instalacion):
        tipos_validos = {
            1: "ESTABLO",
            2: "PORQUERIZA",
            3: "CABALLERIZA",
            4: "GALLINERO"
        }
        set_clause = []
        parametros = []
        try:
            nuevo_tipo = input("Seleccionar tipo de la instalación (1.- ESTABLO, 2.- PORQUERIZA, 3.- CABALLERIZA, 4.- GALLINERO) (deja en blanco para no cambiar): ")
            if nuevo_tipo:
                nuevo_tipo = int(nuevo_tipo)
                if nuevo_tipo in tipos_validos:
                    tipo_str = tipos_validos[nuevo_tipo]
                    set_clause.append("tipo = %s")
                    parametros.append(tipo_str)
                else:
                    print("Opción de tipo no válida.")
                    return  
            nueva_fecha_creacion = input("Insertar nueva fecha de creación (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_creacion:
                set_clause.append("fecha_creacion = %s")
                parametros.append(nueva_fecha_creacion)
            nueva_extension = input("Insertar nueva extensión (deja en blanco para no cambiar): ")
            if nueva_extension:
                nueva_extension = float(nueva_extension)
                set_clause.append("extension = %s")
                parametros.append(nueva_extension)
            nueva_ubicacion = input("Insertar nueva ubicación (deja en blanco para no cambiar): ")
            if nueva_ubicacion:
                set_clause.append("ubicacion = %s")
                parametros.append(nueva_ubicacion)
            nuevo_estado = input("Insertar nuevo estado (deja en blanco para no cambiar): ")
            if nuevo_estado:
                set_clause.append("estado = %s")
                parametros.append(nuevo_estado)
            nueva_fecha_revision = input("Insertar nueva fecha de revisión (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_revision:
                set_clause.append("fecha_revision = %s")
                parametros.append(nueva_fecha_revision)
            nuevo_estatus = input("Insertar nuevo estatus (1 para activo, 0 para inactivo) (deja en blanco para no cambiar): ")
            if nuevo_estatus:
                nuevo_estatus = int(nuevo_estatus)
                set_clause.append("estatus = %s")
                parametros.append(nuevo_estatus)
            nuevo_rancho_id = input("Insertar nuevo ID del rancho (deja en blanco para no cambiar): ")
            if nuevo_rancho_id:
                nuevo_rancho_id = int(nuevo_rancho_id)
                set_clause.append("rancho_id = %s")
                parametros.append(nuevo_rancho_id)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE instalaciones SET {set_clause_str} WHERE id_instalacion = %s"
                parametros.append(id_instalacion)
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
            print(f"Error al actualizar la instalación: {e}")
    def leer_uno(id_instalacion):
        try:
            cursor.execute("SELECT * FROM instalaciones WHERE id_instalacion = %s", (id_instalacion,))
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, fecha_creacion: {i[2]}, extension: {i[3]}, ubicacion: {i[4]}, estado: {i[5]}, fecha_revision: {i[6]}, estatus: {i[7]}, rancho_id: {i[8]}")
        except Exception as e:
            print(f"Error al leer la instalación: {e}")
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM instalaciones")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, fecha_creacion: {i[2]}, extension: {i[3]}, ubicacion: {i[4]}, estado: {i[5]}, fecha_revision: {i[6]}, estatus: {i[7]}, rancho_id: {i[8]}")
        except Exception as e:
            print(f"Error al leer las instalaciones: {e}")
    def eliminar(id_instalacion):
        try:
            estatus = 0
            sentencia = "UPDATE instalaciones SET estatus = %s WHERE id_instalacion = %s"
            valores = (estatus, id_instalacion)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro eliminado (estatus cambiado a 0) con éxito.")
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")
class Instalacion:
    def __init__(self, tipo, fecha_creacion, extencion, ubicacion, estado, fecha_revision, estatus, rancho_id):
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.extension = extencion
        self.ubicacion = ubicacion
        self.estado = estado
        self.fecha_revision = fecha_revision
        self.estatus = estatus
        self.rancho_id = rancho_id
    def añadir(tipo, fecha_creacion, extencion, ubicacion, estado, fecha_revision, estatus, rancho_id):
        try:
            sentencia = """
                INSERT INTO instalaciones 
                (tipo, fecha_creacion, extencion, ubicacion, estado, fecha_revision, estatus, rancho_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (tipo, fecha_creacion, extencion, ubicacion, estado, fecha_revision, estatus, rancho_id)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Instalación añadida exitosamente.")
        except Exception as e:
            print(f"Error al añadir la instalación: {e}")
    def actualizar(id_instalacion):
        tipos_validos = {
            1: "ESTABLO",
            2: "PORQUERIZA",
            3: "CABALLERIZA",
            4: "GALLINERO"
        }
        set_clause = []
        parametros = []
        try:
            nuevo_tipo = input("Seleccionar tipo de la instalación (1.- ESTABLO, 2.- PORQUERIZA, 3.- CABALLERIZA, 4.- GALLINERO) (deja en blanco para no cambiar): ")
            if nuevo_tipo:
                nuevo_tipo = int(nuevo_tipo)
                if nuevo_tipo in tipos_validos:
                    tipo_str = tipos_validos[nuevo_tipo]
                    set_clause.append("tipo = %s")
                    parametros.append(tipo_str)
                else:
                    print("Opción de tipo no válida.")
                    return 
            nueva_fecha_creacion = input("Insertar nueva fecha de creación (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_creacion:
                set_clause.append("fecha_creacion = %s")
                parametros.append(nueva_fecha_creacion)
            nueva_extencion = input("Insertar nueva extensión (deja en blanco para no cambiar): ")
            if nueva_extencion:
                nueva_extencion = float(nueva_extencion)
                set_clause.append("extencion = %s")
                parametros.append(nueva_extencion)
            nueva_ubicacion = input("Insertar nueva ubicación (deja en blanco para no cambiar): ")
            if nueva_ubicacion:
                set_clause.append("ubicacion = %s")
                parametros.append(nueva_ubicacion)
            nuevo_estado = input("Insertar nuevo estado (deja en blanco para no cambiar): ")
            if nuevo_estado:
                set_clause.append("estado = %s")
                parametros.append(nuevo_estado)
            nueva_fecha_revision = input("Insertar nueva fecha de revisión (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_revision:
                set_clause.append("fecha_revision = %s")
                parametros.append(nueva_fecha_revision)
            nuevo_estatus = input("Insertar nuevo estatus (1 para activo, 0 para inactivo) (deja en blanco para no cambiar): ")
            if nuevo_estatus:
                nuevo_estatus = int(nuevo_estatus)
                set_clause.append("estatus = %s")
                parametros.append(nuevo_estatus)
            nuevo_rancho_id = input("Insertar nuevo ID del rancho (deja en blanco para no cambiar): ")
            if nuevo_rancho_id:
                nuevo_rancho_id = int(nuevo_rancho_id)
                set_clause.append("rancho_id = %s")
                parametros.append(nuevo_rancho_id)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE instalaciones SET {set_clause_str} WHERE id_instalacion = %s"
                parametros.append(id_instalacion)
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
            print(f"Error al actualizar la instalación: {e}")
    def leer_uno(id_instalacion):
        try:
            cursor.execute("SELECT * FROM instalaciones WHERE id_instalacion = %s", (id_instalacion,))
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, fecha creacion: {i[2]}, extencion: {i[3]}, ubicacion: {i[4]}, estado: {i[5]}, fecha revision: {i[6]}, estatus: {i[7]}, rancho id: {i[8]}")
        except Exception as e:
            print(f"Error al leer la instalación: {e}")
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM instalaciones")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, fecha creacion: {i[2]}, extension: {i[3]}, ubicacion: {i[4]}, estado: {i[5]}, fecha revision: {i[6]}, estatus: {i[7]}, rancho id: {i[8]}")
        except Exception as e:
            print(f"Error al leer las instalaciones: {e}")
    def eliminar(id_instalacion):
        try:
            estatus = 0
            sentencia = "UPDATE instalaciones SET estatus = %s WHERE id_instalacion = %s"
            valores = (estatus, id_instalacion)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Registro eliminado (estatus cambiado a 0) con éxito.")
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")
class Actividad:
    def __init__(self, tipo, descripcion, fecha_elab, responsable):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha_elab = fecha_elab
        self.responsable = responsable
    def añadir(tipo, descripcion, fecha_elab, responsable):
        try:
            sentencia = """
                INSERT INTO actividades (tipo, descripcion, fecha_elab, responsable)
                VALUES (%s, %s, %s, %s)
            """
            valores = (tipo, descripcion, fecha_elab, responsable)
            cursor.execute(sentencia, valores)
            conexion.commit()
            print("Actividad añadida exitosamente.")
        except Exception as e:
            print(f"Error al añadir la actividad: {e}")
    def actualizar(id_actividad):
        set_clause = []
        parametros = []
        try:
            nuevo_tipo = input("Insertar tipo de la actividad (deja en blanco para no cambiar): ")
            if nuevo_tipo:
                set_clause.append("tipo = %s")
                parametros.append(nuevo_tipo)
            nueva_descripcion = input("Insertar descripción (deja en blanco para no cambiar): ")
            if nueva_descripcion:
                set_clause.append("descripcion = %s")
                parametros.append(nueva_descripcion)
            nueva_fecha_elab = input("Insertar nueva fecha de elaboración (YYYY-MM-DD) (deja en blanco para no cambiar): ")
            if nueva_fecha_elab:
                set_clause.append("fecha_elab = %s")
                parametros.append(nueva_fecha_elab)
            nuevo_responsable = input("Insertar nuevo responsable (ID) (deja en blanco para no cambiar): ")
            if nuevo_responsable:
                nuevo_responsable = int(nuevo_responsable)
                set_clause.append("responsable = %s")
                parametros.append(nuevo_responsable)
            if set_clause:
                set_clause_str = ", ".join(set_clause)
                sentencia = f"UPDATE actividades SET {set_clause_str} WHERE id_actividad = %s"
                parametros.append(id_actividad)
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
            print(f"Error al actualizar la actividad: {e}")
    def leer_uno(fecha_elab):
        try:
            cursor.execute("SELECT * FROM actividades WHERE fecha_elab = %s", (fecha_elab,))
            resultados = cursor.fetchall()
            if resultados:
                for i in resultados:
                    print(f"id: {i[0]}, tipo: {i[1]}, descripcion: {i[2]}, fecha_elab: {i[3]}, responsable: {i[4]}")
            else:
                print("No se encontraron actividades para la fecha proporcionada.")
        except Exception as e:
            print(f"Error al leer la actividad: {e}")
    def leer_todo():
        try:
            cursor.execute("SELECT * FROM actividades")
            resultados = cursor.fetchall()
            for i in resultados:
                print(f"id: {i[0]}, tipo: {i[1]}, descripcion: {i[2]}, fecha_elab: {i[3]}, responsable: {i[4]}")
        except Exception as e:
            print(f"Error al leer las actividades: {e}")