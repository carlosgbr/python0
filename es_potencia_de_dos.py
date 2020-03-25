""" Funciones y condicionales while: es_potencia_de_dos.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura while en Python
"""
"""
ENUNCIADO: El siguiente código puede conducir a un bucle infinito. 
Arregle el código para que pueda terminar con éxito para todos los números.

Nota: ¡Intente ejecutar su función con el número 0 como entrada y vea lo 
que obtiene!
"""
def es_potencia_de_dos(n):
  # Compruebe si el número se puede dividir por dos sin residuo
  while n % 2 != 0:
    n = n / 2
# Si después de dividir entre dos el número es 1, es una potencia de dos
  if n == 0:
    return False
  return True
  

print(es_potencia_de_dos(0)) # Should be False
print(es_potencia_de_dos(1)) # Should be True
print(es_potencia_de_dos(8)) # Should be True
print(es_potencia_de_dos(9)) # Should be False
