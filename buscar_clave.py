"""
Buscar Clave: Escribe una función que busque una clave en un diccionario y devuelva su
valor o un mensaje de error si no se encuentra.
"""

# Define la funcion que buscara una clave dentro del diccionario (Esta predefinida como 'clave' pero se puede cambiar,
# inclusive se puede hacer que ingrese la clave el usuario
def buscar_clave(a):
    if a.get('clave'):
        print("La clave existe en el diccionario.")
    else:
        print("La clave no existe en el diccionario")

# Define un diccionario que contiene la clave declarada previamente en la funcion
diccionario_con_clave = {'clave':1}
print(diccionario_con_clave)
buscar_clave(diccionario_con_clave)
print("")
# Define un diccionario que no contiene la clave declarada previemente en la funcion
diccionario_sin_clave = {'clave1':1, 'clave2':2}
print(diccionario_sin_clave)
buscar_clave(diccionario_sin_clave)
