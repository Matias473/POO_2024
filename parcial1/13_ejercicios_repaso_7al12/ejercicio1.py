# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

numeros = [1,2,3,4,5,6,7,8]

#a
for i in range (len(numeros)):
    print(numeros[i])

#b
def num(lista):
    resultado = ""
    for numero in lista:
        resultado += str(numero)
        return resultado

resultado = num(numeros)
print(resultado)
print(type(resultado))

#c
numeros_2 = [8,3,4,5,6,7,8,4]
numeros_2.sort()
print(numeros_2)

#d
print(len(numeros_2))

#e
elemento = int(input("coloca un numero a buscar dentro de la lista (1-8)"))
for i,p in enumerate(numeros):
    if p == elemento:
        print(f"{elemento} encontrado en la posicion {i}")
if not elemento:
    print(f"no se encontro {elemento} en la lista")