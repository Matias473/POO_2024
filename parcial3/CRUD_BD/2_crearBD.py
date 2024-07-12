import mysql.connector #esta linea se debe poner siempre en la primer linea

try: #se usa en las partes que podrian causar un error
#crear la conexion con la BD 
#aqui solo van estos parametros 
    conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

except:
    print("ocurrio un error en el servidor... intente de nuevo mas tarde")
else:
    #verificar la conexion a la base de datos (es opcional pero sirve para verificar)
    if conexion.is_connected():
        print(f"Se creo la conexion con la BD exitosamente")
    else:
        print(f"No fue posible conectar con la BD... Verifique...")

#crear un objeto para ejecutar las instrucciones
    micursor = conexion.cursor() #se usa para ejecutar las instucciones dentro de MySQL

#crear la BD desde Python
    sql = "create database bd_python"
    micursor.execute(sql)

#verifiar que se creo la BD
    if micursor:
        print(f"se creo la BD exitosamente")

#mostrar las BD que existen en mi MySQL
    micursor.execute("show databases")

    for x in micursor:
      print(x)