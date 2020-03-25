""" Funciones y condicionales while: tabla_multiplicacion.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura while en Python
"""
"""
ENUNCIADO: La función tabla_multiplicacion imprime los resultados de un número 
pasado multiplicado por 1 a 5. Un requisito adicional es que el resultado no 
exceda de 25, lo que se hace con la declaración de ruptura. Complete los 
espacios en blanco para completar la función para satisfacer estas condiciones.
"""
def tabla_multiplicacion(numero):
	# Inicializa el punto de partida de la tabla de multiplicar
	multiplicador = 1
	# Solo quiero recorrer 5
	while multiplicador <= 5:
		resultado = numero * multiplicador 
		# ¿Cuál es la condición adicional para salir del bucle?
		if resultado > 25:
			break
		print(str(numero) + "x" + str(multiplicador) + "=" + str(resultado))
		# Incrementar la variable para el bucle
		multiplicador += 1

tabla_multiplicacion(3) 
# Debe imprimir: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

tabla_multiplicacion(5) 
# Debe imprimir:5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

tabla_multiplicacion(8)	
# Debe imprimir: 8x1=8 8x2=16 8x3=24
