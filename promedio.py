"""
Calcular Promedio: Dado un diccionario de estudiantes y sus calificaciones, calcula el
promedio de calificaciones.
"""

# Define una funcion que acumula (suma) el valor de las llaves del diccionario y lo divide por la longitud del mismo
def promedio_dic(a):
    acum = 0
    for key in a:
        acum = acum + a.get(key)
    return acum/len(a)

diccionario = {"key_1":7, "key_2":8, "key_3":10} # Diccionario creado previamente,
                                               # se podria hacer que losdatos los ingrese el usuario

print(f"Valores declarados en el diccionario: {diccionario.values()}") # Muestra los valores del diccionario

print(f"El promedio de los valores declarados en el diccionario es: {round(promedio_dic(diccionario), 2)}") # Llamada a
                                                                                                   # la funcion
                                                                                                   # utilizando el
                                                                                                   # diccionario
                                                                                                   # como parametro
