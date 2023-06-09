""" Funciones y condicionales if: numeros_primos.py
  Por about.me/carlosgbr

  Versión 1
  Para Python 3.0 y superior
  Esta función encuentra dentro de un rango de valores introducidos 
  por medio del teclado todos los números primos contenidos en ese rango.
  El resultado se muestra en pantalla 

  https://github.com/carlosgbr/python0/blob/master/numeros_primos.py
"""

'''
La función encontrar_numeros_primos(inicio, fin) determina los números 
primos contenidos en el rango recibido en inicio, fin
'''
def encontrar_numeros_primos(inicio, fin):
    
    numeros_primos = []

    for num in range(inicio, fin + 1):
        if num > 1:
            es_primo = True
            # Determina si el número actual es primo
            for i in range(2, int(num ** 0.5) + 1):
                # Sino es primo toma el siguiente número
                if num % i == 0:
                    es_primo = False
                    break
            # Si es primo lo añade al set de números
            if es_primo:
                numeros_primos.append(num)

    print("Los números primos en el rango dado son:")
    # Muestra los números contenidos en el set numeros_primos
    for primo in numeros_primos:
        print(primo)

# Solicitud de datos

inicio = int(input("Ingrese el valor inicial del rango: "))
fin = int(input("Ingrese el valor final del rango: "))

encontrar_numeros_primos(inicio, fin)
