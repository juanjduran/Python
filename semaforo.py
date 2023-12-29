"""Hacer un programa que solicite un color por teclado e imprima “Puede pasar“ si el
color ingresado es verde, “Precaución“ si es amarillo, “No pasar“ si es rojo o “Color
inválido” si es cualquier otro."""


def semaforo(a):
    if a == "verde":
        return print("Puede pasar.")
    elif a == "amarillo":
        return print("Precaucion.")
    elif a == "rojo":
        return print("No pasar.")
    else:
        return print("Color invalido.")


while True:
    luz = str(input("Ingrese un color de luz: "))
    semaforo(luz)
    menu = str(input("Desea indicar un nuevo color? s/n"))
    if menu == "n" or menu == "N":
        break
    
