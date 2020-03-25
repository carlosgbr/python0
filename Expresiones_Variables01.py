""" Expresiones y Variables: Expresiones_Variables01.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Entrada: 
  Salida: 
  Se ilustra el uso de variables y expresiones en Python
"""
"""
ENUNCIADO: En este escenario, dos amigos cenan en un restaurante. La cuenta 
viene en la cantidad de 47.28 dólares. Los amigos deciden dividir la cuenta 
de manera equitativa entre ellos, después de agregar un 15% de propina por
el servicio. Calcule la propina, el monto total a pagar y la parte que le 
corresponde a cada amigo, luego envíe un mensaje que diga 
"Cada persona debe pagar:" seguido del número resultante.
"""
cuenta = 47.28
subt = cuenta * 0.15
total = cuenta + subt
parte = total/2 
print("Cada persona debe pagar: " + str(parte))
