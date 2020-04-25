""" Recursividad: suma_uno_a_n.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Recibimos un número n, y sumamos todos los números positivos entre 1 y n. 
  Utilizando una función Recursiva
"""
"""
ENUNCIADO: Implemente la función sum_numeros_positivos, como una función 
recursiva que devuelve la suma de todos los números positivos entre el número 
n recibido y 1. Por ejemplo, cuando n es 3, debería devolver 1 + 2 + 3 = 6, 
y cuando n es 5 debería devuelve 1 + 2 + 3 + 4 + 5 = 15.
"""
def sum_numeros_positivos(n):
    # El caso base es n siendo menor que 1
    if n < 1:
        return 0

    # El caso recursivo es sumando éste número  
    # a la suma de números más pequeño que éste
    return n + sum_numeros_positivos(n-1)
    

print(sum_numeros_positivos(3)) # Debe ser 6
print(sum_numeros_positivos(5)) # Debe ser 15
