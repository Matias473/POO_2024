#8.- Hacer un programa que resuelva lo siguiente. 
#¿Cuanto es el X por ciento de X numero?

porcentaje = int(input("Ingrese el porcentaje que desea calcular: "))
numero = int(input("Ingrese el numero al cual desea obtener el porcentaje: "))

porcentaje_red = porcentaje / 100

res = numero * porcentaje_red

print(f"El porcentaje ({porcentaje}%) de {numero} es: {res}")