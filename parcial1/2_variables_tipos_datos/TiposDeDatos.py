"""
Tipos de datos mas comunes
En Python son:
Simples o primitivos: int, float, bool
Estructurados: str, list, tuple, dict
"""

#Ejemplo de variables simples
entero = 122
flotante = 4.233
logico = True

#Ejemplo de estructurados
palabra = "UTD"
lista1 = [10, 20, 30, 40]
lista2 = [False, 100, 3.14, "UTD", '2']
tupla = ("Oye", "niño", "oye")
diccionario = {
    "nombre" : "Jose Antonio",
    "apellido" : "Primo de Rivera",
    "edad" : 30,
    "estatura" : 1.76
}

#Mostrar tipo de dato de cada identificador
print(type(entero))
print(type(flotante))
print(type(logico))
print(type(palabra))
print(type(lista1))
print(type(lista2))
print(type(tupla))
print(type(diccionario))