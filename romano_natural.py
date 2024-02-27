"""
Desarrollar una función que permita convertir un número romano en un número decimal.
"""

romano = "vi"
decimal = 0

for n in romano:
    if n == "x":
        decimal += 10
    elif n == "v":
        decimal += 5
    elif n == "i":
        decimal += 1


print(decimal)
