#6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la 
#tabla y luego las multiplicaciones del 1 al 10

mult = 0
for contador1 in range(1, 11):
    for contador2 in range(1, 11):
        mult = contador1 * contador2
        print(f"{contador1} x {contador2} = {mult}")