"""
Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
número dado.
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(0, 10):
    print(fibonacci(n))


