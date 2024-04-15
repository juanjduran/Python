"""
Implementa una función que reciba una lista de empleados (diccionarios) y calcule el
salario promedio.
"""

def average_salary(a):
    b = 0
    f = 0
    for c in a:
        for d, e in c.items():
            b = b + e
            f += 1
    return b / f


employees = [{"juan": 300}, {"paula": 400}, {"luli": 1000}]


print(average_salary(employees))


