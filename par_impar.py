"""
Par o impar

Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000
Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos
el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""

# Se define una funcion que comprueb si el numero es par o si es impar
def answer(a):
    if a % 2 == 0:
        return print(f"El numero {a} es par.")
    else:
        return print(f"El numero {a} es impar.")

# Define el mensaje de bienvenida, puede ser cambiado con solo cambia el contenido de la variable "message", no
# compromete el resto del codigo
message = "BIENVENIDO, INGRESA UN NUMERO ENTRE 1 y 1000"
print(message.center(50, "*"))

# Cuerpo del programa, se mantiene activo hasta que encuentra un "break", la unica manera de que se termine el
# programa es indicando "n"
while True:
    try:
        number = int(input("Numero: "))
        answer(number)
        option = input("Ingresar otro numero? S/N")
        if option == "s" or option == "S":
            continue
        elif option == "n" or option == "N":
            break
        else:
            option = input("Opcion invalida. Ingresar otro numero? S/N")
    except ValueError:
        print("No ingreso un numero valido. Ingrese un numero entre 1 y 1000.")
