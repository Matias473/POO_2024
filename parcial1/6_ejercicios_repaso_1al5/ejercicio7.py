#7,- Hacer un programa que muestre 
#todos los numeros impares entre 2 numeros que decida el usuario 

rango1 = int(input("Ingrese el valor del rango inferior: "))
rango2 = int(input("Ingrese el valor del rango superior: "))

for contador in range(rango1, rango2 + 1):
    if contador % 2 != 0:
        print(contador)