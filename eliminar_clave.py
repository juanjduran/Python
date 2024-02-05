"""
Eliminar Clave: Elimina una clave específica de un diccionario si existe.
"""

# Define la funcion que buscara una clave dentro del diccionario y la elimina si la encuentra (Esta predefinida
# como 'clave' pero se puede cambiar, inclusive se puede hacer que ingrese la clave el usuario
def buscar_clave(a):
    if a.get('clave'):
        a.pop('clave')
        print("La clave fue eliminada.")
    else:
        print("La clave no existe en el diccionario")

# Define un diccionario que contiene la clave declarada previamente en la funcion, se impirme el diccionario con la
# clave y luego el diccionario sin la clave, lo cual comprueba su eliminacion
diccionario_con_clave = {'clave':1}
print(diccionario_con_clave)
buscar_clave(diccionario_con_clave)
print(diccionario_con_clave)
print("")
# Define un diccionario que no contiene la clave declarada previemente en la funcion
diccionario_sin_clave = {'clave1':1, 'clave2':2}
print(diccionario_sin_clave)
buscar_clave(diccionario_sin_clave)
