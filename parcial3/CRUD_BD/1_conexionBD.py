import mysql.connector
try:
   #Conectar con la BD MySQL
    conexion= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python' #no accede porque no esta creada esta BD
)

except Exception as e:
    print(f"Error:{e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"error en el sistema")