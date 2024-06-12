# Una función lambda es una forma concisa de definir una función en línea. 
# No requieren una declaración formal y generalmente se utilizan en contextos 
# donde se necesitan funciones simples y temporales.

#como se hace / sintax
#lambda arguments: expression


#ejemplo
# Definir una función lambda que suma dos números
suma = lambda x, y: x + y
print(suma(3, 4))

#ejemplo 2
# Definir una función lambda que multiplique dos números
(lambda numero1 , numero2: print(numero1 * numero2))(45,12)

#ejemplo 3
# Filtrar números pares de una lista
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
