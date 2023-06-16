""" matrices.py
  Por https://about.me/carlosgbr & StackOverFlow en 
  https://es.stackoverflow.com/questions/351365/imprimir-un-rombo-con-asteriscos-de-ancho-n-con-n-impar

  Versión 1
  Para Python 3.0 y superior
  Esta función encuentra dentro de un rango de valores introducidos 
  por medio del teclado todos los números primos contenidos en ese rango.
  El resultado se muestra en pantalla 

  https://github.com/carlosgbr/python0/blob/master/matrices.py
"""

'''
La función encontrar_numeros_primos(inicio, fin) determina los números 
primos contenidos en el rango recibido en inicio, fin
'''
import os #Para poder limpiar la pantalla


"""
  generaRombo(diagonal) Genera un rombo utilizando matrices.
  Argumentos;
    diagonal (int): Tamaño de la diagonal del rombo.
  Devuelve:
    lista: Matriz que representa el rombo.
"""
def generaRombo(diagonal):
    n = diagonal // 2
    # Aquí se efectúa el llenado de la matriz
    romboSuperior = [[" " for _ in range(n-i)] + ["*" for _ in range(2*i+1)] for i in range(n+1)]
    # Genera medio rombo
    romboInferior = romboSuperior[:n][::-1]
    # Genera el "espejo" del rombopara completarlo
    romboCompleto = romboSuperior + romboInferior
    return romboCompleto

"""
  Imprime el rombo en la consola.
  Argumentos:
    rombo (lista): Matriz que representa el rombo.
"""
def imprimirRombo(rombo):
    for fila in rombo:
        # La función join() es un método de Python que concatena los elementos 
        # de una secuencia en una sola cadena.
        print("".join(fila))

# Inicia programa principal
os.system ("cls")  #Limpia la pantalla, requiere import os
while True:
    diagonal = int(input("Ingresa el tamaño de la diagonal del rombo (0 para salir): "))
    if diagonal == 0:
        break
    
    rombo = generaRombo(diagonal)
    imprimirRombo(rombo)

    continuar = input("Presiona Enter para generar otro rombo o 'q' para salir: ")
    if continuar == 'q':
        break
