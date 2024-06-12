from otras_funciones_2 import sumar,restar,multiplicar,dividir

def calculadora():
    while True:
        print("Calculadora básica \n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir \n")
        eleccion = input("Elige la operación que quieres realizar: ")

        if eleccion in ["1", "2", "3", "4"]:
            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))

            if eleccion == "1":
                print(f"{n1} + {n2} = {sumar(n1, n2)}")
            elif eleccion == "2":
                print(f"{n1} - {n2} = {restar(n1, n2)}")
            elif eleccion == "3":
                print(f"{n1} * {n2} = {multiplicar(n1, n2)}")
            elif eleccion == "4":
                print(f"{n1} / {n2} = {dividir(n1, n2)}")
        elif eleccion == "5":
            print("programa finalizado")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

calculadora()