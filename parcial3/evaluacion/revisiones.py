from conexion import *
from funciones import *
class Revisiones():
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    @staticmethod
    def insertar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        sentencia = "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Registro exitoso")
        esperarTecla()

    @staticmethod
    def consultar():
        cursor.execute("SELECT * FROM revisiones")
        resultados = cursor.fetchall()
        for i in resultados:
            print(f"no_revision: {i[0]}, cambiofiltro: {i[1]}, cambioaceite: {i[2]}, cambiofrenos: {i[3]}, otros: {i[4]}, matricula: {i[5]}\n")
        esperarTecla()


    @staticmethod
    def actualizar(no_revision):
        no_revision = input("Número de revisión: ")
        cambiofiltro = input("Cambio de filtro: ")
        cambioaceite = input("Cambio de aceite: ")
        cambiofrenos = input("Cambio de frenos: ")
        otros = input("Otros: ")
        matricula = input("Matricula: ")
        sentencia = "UPDATE revisiones SET no_revision = %s, cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s WHERE no_revision = %s"
        valores = (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("actualizacion finalizada...")
        esperarTecla()

    @staticmethod
    def eliminar(no_revision):
        cursor.execute("DELETE FROM revisiones WHERE no_revision = %s", (no_revision,))
        conexion.commit()
        print("eliminado...")
        esperarTecla()
