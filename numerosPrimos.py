""" Funciones y condicionales if: numerosPrimos.py
  Por about.me/carlosgbr

  Versión 1
  Para Python 3.0 y superior
  Esta función encuentra dentro de un rango de valores introducidos 
  por medio del teclado todos los números primos contenidos en ese rango.
  El resultado se muestra en pantalla 

  https://github.com/carlosgbr/python0/blob/master/numerosPrimos.py
"""

'''
La función encontrar_numeros_primos(inicio, fin) determina los números 
primos contenidos en el rango recibido en inicio, fin
'''
import os #Para poder limpiar la pantalla

def encontrarNumerosPrimos(inicio, fin):
    
    numerosPrimos = []
    cadenaPrimos = ""

    for num in range(inicio, fin + 1):
        if num > 1:
            esPrimo = True
            # Determina si el número actual es primo
            for i in range(2, int(num ** 0.5) + 1):
                # Sino es primo toma el siguiente número
                if num % i == 0:
                    esPrimo = False
                    break
            # Si es primo lo añade al set de números
            if esPrimo:
                numerosPrimos.append(num)

    print("Los números primos en el rango dado son:")
    # Muestra los números contenidos en el set numerosPrimos
    for primo in numerosPrimos:
        cadenaPrimos += str(primo) + "\t"
        # print(str(primo) + "\n")
    print(cadenaPrimos)

# Solicitud de datos

terminar = False
while not terminar:
    os.system ("cls")  #Limpia la pantalla, requiere import os
    inicio = int(input("Ingrese el valor inicial del rango: "))
    fin = int(input("Ingrese el valor final del rango: "))  
    
    encontrarNumerosPrimos(inicio, fin)

    pregunta = input('''Si deseas ejecutar de nuevo, Presiona la tecla (s/S)
    pulsa cualquier otra para terminar el programa ''')
    if pregunta in ["s", "S"]:
        terminar = False
    else:
        terminar = True
