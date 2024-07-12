from conexionBD import *

micursor=conexion.cursor()

sql="select nombre,direccion,tel from clientes"
micursor.execute(sql)
resultado=micursor.fetchall()#la funcion convierte lo que haya en una lista

if len(resultado)>0:
    print(f"Registros de la tabla: {len(resultado)}")#aqui usamos el len para ver el tamaño de la lista
    for x in resultado:
        print(x)