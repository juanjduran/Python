"""
Unir Diccionarios: Combina dos diccionarios en uno solo.
"""

# Declaracion de dos diccionarios diferentes
diccionario_uno = {"dato_1":1, "dato_2":2, "dato_3":3}
diccionario_dos = {"dato_4":4, "dato_5":5, "dato_6":6}

# Se imprimen los diccionarios por separado
print(f"DICCIONARIO UNO: {diccionario_uno}")
print(f"DICCIONARIO DOS: {diccionario_dos}")

# Se utiliza .update para actualizar el primer diccionario conlos datos del segundo diccionario
diccionario_uno.update(diccionario_dos)

# Se impirme el primer diccionario actualizado con los datos del segundo diccionario
print(f"DICCIONARIOS UNIDOS: {diccionario_uno}")
