from coches import *

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

#crear un onbejo e imprimir los valores
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

#crear los objetos e instancias de las clases camiones y camionetas
print("objeto 3")
camion1=camiones("Negro","Dina","2020",180,300,12,8,2500)
camion1.getInfo()

print("Objeto 4")
camion2=camiones("Azul","Star","2019",150,300,14,6,2000)
camion2.getInfo()

print("objeto 5")
camioneta1 = camionetas("Amarilla", "Renault", "2025", 240, 250, 8,"delantera", True)
camioneta1.getInformacion()

print("objeto 6")
camioneta1 = camionetas("Blanca", "Nissan", "2020", 180, 160, 6,"trasera", False)
camioneta1.getInformacion()

#final