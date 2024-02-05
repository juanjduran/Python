"""
Diccionario de Contactos: Crea un diccionario de contactos con nombres y números de
teléfono.
"""

def ingreso_datos(b):
    a = input("Ingrese nombre del contacto: ")
    b[a] = input("Ingrese numero de telefono: ")



diccionario_contactos = {}

while True:
    ingreso_datos(diccionario_contactos)
    opc = input("Ingresar otro? S/N")
    if opc == "n" or opc == "N":
        break

print(diccionario_contactos)
