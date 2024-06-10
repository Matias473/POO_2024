#3.- Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


cuadrado = 0

for contador in range(1, 61):
    cuadrado = contador ** 2
    print(cuadrado)


print("\n")

contador2 = 1
cuadrado2 = 0

while contador2 < 61:
    cuadrado2 = contador2 ** 2
    contador2 += 1
    print(cuadrado2)