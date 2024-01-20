"""
Contar Letras: Dada una cadena de texto, crea un diccionario que cuente cuántas veces aparece cada letra.
"""

texto = "hola juanjo, como estas?"
dic = {}
dic2 = {}
for l in texto:
    i = 0
    cont = 0
    while i < len(texto):
        if l == texto[i]:
           cont += 1
        i += 1
    dic2 = {l:cont}
    dic.update(dic2)


print(dic)

