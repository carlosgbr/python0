'''
 Ejercicios con strings 1: string01.py
 Por http://about.me/carlosgbr
 Fecha: 200607
 Versión 1
 Para Python 3.0 y superior
 Ejemplos de manipulación de cadenas de texto
 '''
'''
Enunciado: Modifique la función palabra_doble para que devuelva la misma palabra repetida dos veces, 
seguida de la longitud de la nueva palabra duplicada. Por ejemplo, palabra_doble ("hello") 
debería devolver hellohello10.

def palabra_doble(word):
    return

print(palabra_doble("hello")) # debería retornar holahola8
print(palabra_doble("abc"))   # debería retornar abcabc6
print(palabra_doble(""))      # debería retornar 0

'''

def palabra_doble(palabra):
    word = word*2
    word += str(len(palabra))
    return word

print(palabra_doble("hola"))  # debería retornar holahola8
print(palabra_doble("abc"))   # debería retornar abcabc6
print(palabra_doble(""))      # debería retornar 0
