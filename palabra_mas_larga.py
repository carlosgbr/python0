""" Funciones y condicionales if: palabra_mas_larga.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: La función palabra_mas_larga se usa para comparar 3 palabras. Debería 
devolver la palabra con el mayor número de caracteres (y el primero en la lista
cuando tienen la misma longitud). Complete el espacio en blanco para que 
esto suceda.
"""
def palabra_mas_larga(palabra1, palabra2, palabra3):
	if len(palabra1) >= len(palabra2) and len(palabra1) >= len(palabra3):
		palabra = palabra1
	elif len(palabra2) >= len(palabra3):
		palabra = palabra2
	else:
		palabra = palabra3
	return(palabra)

print(palabra_mas_larga("silla", "sillón", "mesa"))
print(palabra_mas_larga("cama", "aro", "baúl"))
print(palabra_mas_larga("laptop", "notebook", "desktop"))
