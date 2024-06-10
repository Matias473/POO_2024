#Los errores de ejecucuion en un lenuaje de proramacion sse presentan 
# cuando existe una anomalia dentro de la ejecucuion del codio lo cual 
# provoca que se detena la ejecucion del SW. Con el control y manejo 
# de exepciones sera posible minimizar o evitar la interrupcion del programa
# debido a una excpecion
"""
#Ejemplo 1 cuando una vairiable no se genera
try:
  nombre=input("Introduce el nombre completo de una persona:")

  if len(nombre)>0:
    nombre_usuario="El nombre completo del usuario es:", nombre

    print(f"{nombre_usuario}")

except:
    print("es necesario introducir un nombre\n verifica por favor")


x = 3 + 4
print("el valor de x es:",str(x))
"""
"""
#ejemplo 2 - cuando se solicita un numero y se ingresa otra cosa
try:
  numero = int(input("ingrese un numero entero positivo: "))

  if numero > 0:
    print("soy un numero entero positivo")
  elif numero == 0:
    print("soy un numero neutro")
  else:
    print("soy un numero entero negativa")
except ValueError:
  print("ERROR : coloca un valor numerico entero (0-9) por favor")"""


#Ejempo 3-cuando se generan multiples exepciones
try:
  numero = int(input("introduce un numero: "))
  print(f"el cuadrado de {numero} es: ", str(numero*numero))
except ValueError:   #este se usa para mostar posibles errores que se puedan preveer
  print("ERROR : coloca un valor numerico entero (0-9) por favor")
except TypeError:
  print("se debe convertir el numero a entero")
else:
  print("no se encontraron errores") #a diferencia es que este solo sale en caso 
                                     #de no haber errores
finally:
  print("termine la ejecucion")