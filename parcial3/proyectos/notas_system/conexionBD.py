import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="bd_python"
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    