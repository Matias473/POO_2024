# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []

while len(lista) <= (120 - 1):
    valor = input("añadir un valor: ")
    lista.append(valor)

print(lista)


lista_2 = []
for i in range(1,121):
    valores = input("añadir un valor:")
    lista_2.append(valores)

print(lista_2)