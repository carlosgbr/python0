""" Funciones y condicionales if: parte_fraccional.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: La función parte_fraccional divide el numerador por el denominador y 
devuelve solo la parte fraccionaria (un número entre 0 y 1). Complete el cuerpo
de la función para que devuelva el número correcto. Nota: Dado que la división 
por 0 produce un error, si el denominador es 0, la función debería devolver 0 
en lugar de intentar la división.
"""
def parte_fraccional(numerador, denominador):
    if denominador == 0:
        resultado = 0
    else:
        resultado = (numerador // denominador) - numerador / denominador
        resultado = abs(resultado)
    return resultado

print(parte_fraccional(5, 5)) # Debe ser 0
print(parte_fraccional(5, 4)) # Debe ser 0.25
print(parte_fraccional(5, 3)) # Debe ser 0.66...
print(parte_fraccional(5, 2)) # Debe ser 0.5
print(parte_fraccional(5, 0)) # Debe ser 0
print(parte_fraccional(0, 5)) # Debe ser 0
