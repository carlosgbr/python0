""" Funciones: ordena_numeros.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Entrada: 
  Salida: 
  Se ilustra el uso de funciones en Python
"""
"""
ENUNCIADO: Esta función compara dos números y los devuelve en orden creciente.
Complete los espacios en blanco para que la instrucción de impresión muestre 
el resultado de la llamada a la función en orden.
"""
# Esta función compara dos números y los devuelve
# en orden creciente.
def ordena_numeros(numero1, numero2):
	if numero2 > numero1:
		return numero1, numero2
	else:
		return numero2, numero1

# 1) Complete los espacios en blanco para que la declaración de impresión 
# muestre el resultado de la llamada a la función
menor, mayor = ordena_numeros(100, 99)
print(menor, mayor)
