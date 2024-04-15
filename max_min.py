"""
Implementa una función que tome una lista de números y devuelva una tupla con el valor mínimo y máximo.
"""

def max_min(a):
    max_min = (max(a), min(a))
    return max_min

numbers_list = [2, 10,  3, 4, 5, 9]

print(max_min(numbers_list))
