#Convertir los tipos de datos

#Solo es posible en una concatenación concatenar entre tipos de datos iguales

texto = "Soy una cadena"
numero = 23

numero_cadena = str(numero)
print (texto + " " +numero_cadena)

# Convertir string a int

num_cad = '23'
num_cad_entero = int(num_cad)
print(type(num_cad_entero))

#   Convertir float a int

num_flotante = 33.0
num_f_entero = int(num_flotante)
print(type(num_f_entero))

#   Convertir int a float

num_entero = 66
num_ent_float = float(num_entero)
print(type(num_ent_float))