# 5.- 
# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION

lista = [
    ("ACCION", "TERROR", "DEPORTES"),
    ("MAXIMA VELOCIDAD", "LA MONJA", "ESPN"),
    ("ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"),
    ("RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION")
]
"""
for i in lista:
    print(" ".join(i))
"""

diccionario = {
    "fila_1":["ACCION", "TERROR", "DEPORTES"],
    "fila_2":["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    "fila_3":["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    "fila_4":["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
}
"""
for i, p in diccionario.items():
    print(f"{i} : {" ".join(p)}")
"""