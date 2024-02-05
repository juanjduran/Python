"""
Diccionario Vacío: Verifica si un diccionario está vacío o no.
"""

# Define una funcion que comprueba si el diccionario posee elementos o no
def comprobar_diccionario(a):
    if a == {}:
        print("El diccionario esta vacio.")
    else:
        print("El diccionario posee elementos.")

# Declaracion de diccionario vacio y llamada a la funcion
diccionario_vacio = {}
print(diccionario_vacio)
comprobar_diccionario(diccionario_vacio)
print("")
# Declaracion de diccionario con un elemento y llamada a la funcion
diccionario_elementos = {"un_elemento":1}
print(diccionario_elementos)
comprobar_diccionario(diccionario_elementos)
