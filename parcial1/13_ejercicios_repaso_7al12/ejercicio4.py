#  4.- 
#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def tipo(variable):
    if isinstance(variable, list):
     return "Es una lista"
    elif isinstance(variable, str):
     return "Es una cadena de texto"
    elif isinstance(variable, bool):
       return "Es un valor booleano"
    elif isinstance(variable, int):
       return "Es un número entero"
    elif isinstance(variable, float):
       return "Es un valor flotante"
    else:
       return "Tipo de dato no reconocido"

lista = [1, 2, 3]
cadena = "Hola, mundo!"
entero = 42
logico = False
flotante = 1.0

print(tipo(lista))
print(tipo(cadena))
print(tipo(entero))
print(tipo(logico))
print(tipo(flotante))#este es extra porque queria comprobar algo