# Calculadora en Python
import math

def calculadora() :
    try :
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Debe ingresar un número!! \n")
        calculadora()

    opcion = 0
    while True:
        print("""
        Dime ¿Qué quieres hacer?

        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Raiz cuadrada
        6. Potencia
        7. Cambiar los números
        8. Salir
        """)

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            print("\n El resultado de la suma es: ", numero1 + numero2)
        elif opcion == 2:
            print("\n El resultado de la resta es: ", numero1 - numero2)
        elif opcion == 3:
            print("\n El resultado de la multiplicación es: ", numero1 * numero2)
        elif opcion == 4:
            print("\n El resultado de la división es: ", numero1 / numero2)
        elif opcion == 5:
            print("\n La raiz cuadrada de ", numero1, " es: ", math.sqrt(numero1))
        elif opcion == 6:
            print("\n El resultado de la potencia es: ", math.pow(numero1, numero2))
        elif opcion == 7:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
        elif opcion == 8:
            print("\n Adios")
            break
        else:
            print("\n Opción incorrecta")

calculadora()