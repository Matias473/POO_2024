from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    conexion.commit()
except:
    print(f"error en el sistema")
else:
    print("Registro Eliminado Correctamente")