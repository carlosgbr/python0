'''
 Ejercicios con strings 1: string02.py
 Por http://about.me/carlosgbr
 Fecha: 200607
 Versión 1
 Para Python 3.0 y superior
 Ejemplos de manipulación de cadenas de texto
 '''
'''
Enunciado: Modifique la función primero_y_ultimo para que devuelva True 
si la primera letra de la cadena es la misma que la última letra de la cadena, 
False si son diferentes. 
Tenga cuidado de cómo maneja la cadena vacía, que debería devolver True ya 
que nada es igual a nada.

def primero_y_ultimo(mensaje):
    return False

print(primero_y_ultimo("américa"))
print(primero_y_ultimo("arbol"))
print(primero_y_ultimo(""))

'''

def primero_y_ultimo(mensaje):
    if len(mensaje) == 0:
        return True
    elif mensaje[0] == mensaje[-1]:
        return True
    return False

print(primero_y_ultimo("américa"))
print(primero_y_ultimo("arbol"))
print(primero_y_ultimo(""))
