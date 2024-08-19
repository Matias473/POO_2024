from conexion import *
import hashlib
import datetime
import mysql.connector

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = self.hash_password(password)

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self, conexion):
        try:
            fecha = datetime.datetime.now()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO usuario (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.email, self.contrasena)
            )
            conexion.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    @staticmethod
    def iniciar_sesion(conexion, email, contrasena):
        try:
            contrasena_hashed = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM usuario WHERE email = %s AND password = %s",
                (email, contrasena_hashed)
            )
            usuario = cursor.fetchone()
            cursor.close()
            if usuario:
                return usuario
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
