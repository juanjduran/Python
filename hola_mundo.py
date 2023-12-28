"""Hacer un programa donde se pida un nombre por teclado y se imprima “Hola ..el_nombre_ingresado”"""


def saludo(a):
    return print(f"Hola {a}")


nombre = str(input("Ingrese su nombre: "))

saludo(nombre)
