#Variables Locales:
# Las variables locales son aquellas que están definidas dentro de una función
# y solo son accesibles dentro de esa función. No se pueden usar fuera de la 
# función donde se definieron.

def mi_funcion():
    #variable local
    local_variable = "Hola, mundo!"
    print(local_variable)

mi_funcion()
#print(local_variable) # Esto dará un error, ya que local_variable no está definida aquí.

#variables Globales
#son variables que se encuentran en todo el codigo y su valor se queda fija (amenos que se reescriba)
global_variable = "Hola, mundo!"

def mi_funcion():
    print(global_variable)

mi_funcion()
print(global_variable)  # La variable global es accesible aquí también

def otra_funcion():
    global global_variable
    global_variable = "¡Hola, todos!"  # Modificando la variable global
    print(global_variable)

otra_funcion()
print(global_variable)  # La variable global ha sido modificada
