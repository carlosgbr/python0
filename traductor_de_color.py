""" Funciones y condicionales if: traductor_de_color.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Entrada: 
  Salida: 
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: Complete la función completando las partes que faltan. La función 
traductor_de_color recibe el nombre de un color, luego imprime su valor 
hexadecimal. Actualmente, solo admite los tres colores primarios aditivos 
(rojo, verde, azul), por lo que devuelve "desconocido" para todos los demás 
colores.
"""
def traductor_de_color(color):
	if color == "rojo":
		hex_color = "#ff0000"
	elif color == "verde":
		hex_color = "#00ff00"
	elif color == "azul":
		hex_color = "#0000ff"
	else:
		hex_color = "desconocido"
	return hex_color

print(traductor_de_color("azul")) # Debiera ser #0000ff
print(traductor_de_color("amarillo")) # Debiera ser desconocido
print(traductor_de_color("rojo")) # Debiera ser #ff0000
print(traductor_de_color("negro")) # Debiera ser desconocido
print(traductor_de_color("verde")) # Debiera ser #00ff00
print(traductor_de_color("rosa")) # Debiera ser desconocido
