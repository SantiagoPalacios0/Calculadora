# Calculadora en consola
import math

# Preguntamos al usuario que operacion quiere hacer
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Que operacion quieres hacer?(Las respuestas deben ser numeros)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Creamos la funcion para las operaciones
def operaciones():
    opciones = int(input("\n 1. Suma, 2. Resta, 3. Multiplicacion, 4. Division, 5. Raiz Cuadrada: "))
    # Guardamos la eleccion anterior en una variable
    eleccion = opciones

    # Ejecutamos segun la eleccion del usuario
    if eleccion == 1:
        x = int(input("Elija el primer numero: "))
        y = int(input("Elija el segundo numero: "))
        print(x + y)
    elif eleccion == 2:
        x = int(input("Elija el primer numero: "))
        y = int(input("Elija el segundo numero: "))
        print(x - y)
    elif eleccion == 3:
        x = int(input("Elija el primer numero: "))
        y = int(input("Elija el segundo numero: "))
        print(x * y)
    elif eleccion == 4:
        x = int(input("Elija el primer numero: "))
        y = int(input("Elija el segundo numero: "))
        print(x / y)
    elif eleccion == 5:
        x = int(input("Elija un numero: "))
        raiz = math.sqrt(x)
        print(raiz)
    else:
        print("No ha elegido ninguna opcion valida")

    hacer_otra_operacion()


def hacer_otra_operacion():
    otra_operacion = input("Quiere realizar otra operacion? y/n: ")
    otra_operacion = otra_operacion.lower()
    if otra_operacion == "y":
        operaciones()
    else:
        print("\nGracias por usar esta calculadora!")


operaciones()
