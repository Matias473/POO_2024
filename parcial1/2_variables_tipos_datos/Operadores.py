#   Operadores aritmeticos en Python

#   Operador de suma
suma = 2 + 2

#   Operador de resta
resta = 10 - 5

#   Operador de multiplicacion
multiplicacion = 4 * 4

#   Operador de division
division = 100 * 5

#   Operador de modulo o restos
modulo = 16 % 2

#   Operador de potencia
potencia = 4 ** 2

#   Operador de division entera
division_entera = 10 // 5
print(division_entera)

#   Operadores de asignacion
cuatro = 4

#   Los siguientes de asignacion son utilizados para ahorrar tiempo al momento de escribir el codigo
#   Donde el operador que va antes de la asignacion es lo mismo que el identificador principal

#Suma
id1 = 0
id1 = id1 + 2 
# Lo de arriba se simplifica asi:
id1 += 2

#Resta
id2 = 10
id2 -= 5

#Multiplicacion
id3 = 2
id3 *= 2

#Division
id4 = 10
id4 /= 2

#Modulo
id5 = 10
id5 %= 2

#Division entera
id6 = 10
id6 //= 2

#Potencia
id7 = 2
id7 **= 2


#Operadores de comparacion
#Operador de igualdad
a = 5
b = 5
a == b

#Operador de desigualdad
c = 5
d = 10
c != d

#Operador mayor que
e = 10
f = 2
e > f

#Operador menor que
g = 2
h = 30
g < h

#Operador mayor o igual que
i = 30
j = 30
i >= j

#Operador menor o igual que
k = 30
l = 25
l <= k

#Operadores logicos
#Operador AND
x = 5
x > 2 and x < 10

#   Operador OR
y = 5
y > 4 or y < 1

#   Operador NOT
z = 5
not (z < 600)


#   Operadores de identidad

#   Operador ES
ob1 = 600
ob2 = 600
print(ob1 is ob2)

#   Operador NO ES
ob3 = "hola"
ob4 = 3.14
print(ob3 is not ob4)


#   Operadores de pertenencia
#   Operador EN
ob5 = "l"
ob6 = "lolo"
print(ob5 in ob6)

#   Operador NO EN
ob7 = "z"
ob8 = "sorro"
print(ob7 not in ob8)


#   Python tiene otros operadores que se utilizan para comparar numeros binarios.
#   Estos serían "&", "|", "^", "~", "<<" y ">>"


#   Jerarquia de operadores
#   Por orden de prioridad:
#   ()
#   **
#   *, /, //, %
#   +, -
#   ==, !=, >, >=, <, <=, is, is not, in, not in
#   not
#   and
#   or

#   Si hay dos operadores del mismo nivel, se evalua la expresion de izquierda a derecha, segun el orden puesto aqui