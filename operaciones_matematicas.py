"""Hacer un programa que solicite por teclado dos número y muestre la suma,
 la resta ,la multiplicación y la división de esos números"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


numero_uno = float(input("Ingrese el primer numero: "))
numero_dos = float(input("Ingrese el segundo numero: "))

while True:
    menu = input("\nSeleccione la operacion que desea realizar:\n\nS-Suma\nR-Resta\nM-Multiplicacion\nD-Division"
                 "\n\n0-SALIR\n\nOPCION:")
    if menu == "S" or menu == "s":
        print(f"\nEl resultado de la suma entre {numero_uno} y {numero_dos} es: {suma(numero_uno, numero_dos)}")
    elif menu == "R" or menu == "r":
        print(f"\nEl resultado de la resta entre {numero_uno} y {numero_dos} es: {resta(numero_uno, numero_dos)}")
    elif menu == "M" or menu == "m":
        print(f"\nEl resultado de la multiplicacion entre {numero_uno} y {numero_dos} es: "
              f"{multiplicacion(numero_uno, numero_dos)}")
    elif menu == "D" or menu == "d":
        try:
            print(f"\nEl resultado de la division entre {numero_uno} y {numero_dos} es: "
                  f"{division(numero_uno, numero_dos)}")
        except ZeroDivisionError:
            numero_dos = float(input("\nNo es posible dividir por 0 (cero). Debe ingresar un numero diferente."
                                     "\nIngrese el segundo numero: "))
    elif menu == "0":
        break
