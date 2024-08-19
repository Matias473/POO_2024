from conexion import conexion, cursor
from funciones import *
class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    @staticmethod
    def insertar(matricula, marca, modelo, color, nif):
        sentencia = "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)"
        valores = (matricula, marca, modelo, color, nif)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Registro exitoso")
        esperarTecla()
    
    @staticmethod
    def consultar():
        cursor.execute("SELECT * FROM autos")
        resultados = cursor.fetchall()
        for i in resultados:
            print(f"matricula: {i[0]}, marca: {i[1]}, modelo: {i[2]}, color: {i[3]}, nif: {i[4]}\n")
        esperarTecla()


    @staticmethod
    def actualizar(matricula): 
        matricula = input("matricula del auto: ").upper()
        marca = input("marca del auto: ")
        modelo = input("modelo del auto: ")
        color = input("color del auto: ")
        nif = int(input("nif:"))
        sentencia = "UPDATE autos SET marca = %s, modelo = %s, color = %s, nif = %s WHERE matricula = %s"
        valores = (marca, modelo, color, nif, matricula)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("actualizacion finalizada...")
        esperarTecla()

    @staticmethod
    def eliminar(matricula):
        cursor.execute("DELETE FROM autos WHERE matricula = %s", (matricula,))
        conexion.commit()
        print("eliminado...")
        esperarTecla()
