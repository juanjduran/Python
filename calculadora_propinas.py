"""
Calculadora de Propinas:

Crea una calculadora de propinas simple que permita ingresar el monto de la factura y
calcular automáticamente la propina.
"""

# Funcion para calcular el porcentaje de la propina

def calcular_porcentaje(a):
    return a * 0.01

# Funcion que calcula la propina utilizando el porcentaje que quiere el cliente

def calcular_propina(a, b):
    return a * calcular_porcentaje(b)

# Cuerpo del programas

while True:
    try:
        factura = float(input("Ingresar el monto total de la factura: "))
        propina = float(input("Ingresar que porcentaje de la factura quiere dejar de propina: "))
        print(f"La propina final es ${calcular_propina(factura, propina)}.-")
    except ValueError:
        print("No ingreso un monto valido.")
    opc = input("Desea calcular otra factura? S/N")
    if opc == "n" or opc == "N":
        break
