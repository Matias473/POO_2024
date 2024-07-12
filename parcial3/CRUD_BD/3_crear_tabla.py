import mysql.connector #esta linea se debe poner siempre en la primer linea

try:
#crear la conexion con la BD 
#aqui solo van estos parametros 
    conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'bd_python'
)
except:
    print("ocurrio un error en el sistema")

else:
#crear una tabla de BD desde python
    sql = "CREATE TABLE clientes (id int PRIMARY KEY AUTO_INCREMENT, nombre varchar(60), direccion varchar (120), tel varchar(10))"

    micursor = conexion.cursor()#esta ayuda a crear la conexion 
    micursor.execute(sql)
