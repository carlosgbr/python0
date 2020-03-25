""" Funciones y condicionales while: imprimir_factores_primos.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura while en Python
"""
"""
ENUNCIADO: Complete los espacios en blanco para que la función 
imprimir_factores_primos imprima todos los factores primos de un número. 
Un factor primo es un número que es primo y divide a otro sin resto.
"""
def imprimir_factores_primos(numero):
    # Comience con dos, que es el primer primo
    factor = 2
    # Continúe hasta que el factor sea mayor que el número
    while factor <= numero:
    # Verificar si el factor es un divisor de número
        if not (numero % factor != 0):
        # Si es así, imprímalo y divida el número original
            print(factor)
            numero = numero / factor
        else:
        # Si no es así, incremente el factor en uno
            factor = factor + 1
    return "Done"

imprimir_factores_primos(100)
# Debe imprimir 2,2,5,5
