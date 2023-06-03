""" Calculadora básica binaria: Calculadora01.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones
"""
"""
ENUNCIADO: Descripción: Realiza un programa que tenga una función de calculadora que permita sumar, potenciar, restar y multiplicar 2 números. 
Estos pueden ser números enteros ó números decimales. La función debe recibir 3 parámetros (a,op,b) donde a y b son números y op corresponde 
a la operación que se desea realizar.
Restricciones: La función debe validar las entradas, en caso de que no reciba números ó la operación no esté registrada dentro de las
operaciones válidas, debe mostrar un mensaje de error.
Entrada: Se deben solicitar los valores deseados al usuario. Salida: La función debe devolver el resultado de la operación.
""
"""

#Realiza la suma binaria 
def opSumar(sumando1, sumando2):
    sumando1 = float(sumando1)
    sumando2 = float(sumando2)
    return sumando1 + sumando2

#Realiza la resta binaria 
def opRestar(minuendo, sustraendo):
    minuendo = float(minuendo)
    sustraendo = float(sustraendo)
    return minuendo - sustraendo

#Realiza el producto binario
def opProducto(multiplicando1, multiplicando2):
    multiplicando1 = float(multiplicando1)
    multiplicando2 = float(multiplicando2)
    return multiplicando1 * multiplicando2

def opDivision(dividendo, divisor):
    dividendo = float(dividendo)
    divisor = float(divisor)
    return dividendo / divisor

#Eleva la base a la potencia especificada en exponente 
def opPotencia(base, exponente):
    base = float(base)
    exponente = float(exponente)
    return pow(base, exponente)

''' Realiza la operación de a y b de acuerdo al operador recibido en op
La validación de números y operadores se debe realizar antes de enviar 
los datos a esta función
'''
def realizaOperacion(a, op, b):
    if op == "+":
       suma = opSumar(a, b)
       print("La suma es: ", suma)
    if op == "-":
       resta = opRestar(a, b)
       print("La resta es: ", resta)
    if op == "*":
       producto = opProducto(a, b)
       print("El producto es: ", producto)
    if op == "/":
       division = opDivision(a, b)
       print("La suma es: ", division)
    if op == "pot":
       potencia = opPotencia(a, b)
       print("La suma es: ", potencia)

#Determina los operadores permitidos en el programa
def parsear_operacion(cadena):
    operadores = ['+', '-', '*', '/', "pot"]
    operandos = []
    signo_operacion = None

    for operador in operadores:
        if operador in cadena:
            signo_operacion = operador
            operandos = cadena.split(operador)
            break

    return operandos, signo_operacion

#Texto que se presenta al inicio del programa, ofrece instrucciones generales de uso del programa.
def txtPresentacion():
    print('''>> Bienvenid@ a la calculdora aritmética, a continuación te indicamos su funcionamiento.\n
    >> En primer lugar deberás escribir un número, a continuación pulsa ENTER
    >> Después deberás introducir el símbolo de la operación que deseas realizar
    >> Las operaciones válidos son:
    
    + \t para la suma
    - \t para la resta
    * \t para el producto
    / \t para la división 
    pot \t para calcular la potencia de un número
    
    >> NOTA: Si escribes la letra X el programa terminará inmediatamente.}

    Finalmente introduce la segunda cifra y pulsa Enter para que se realice la operación solicitada
    ''')

    input("Presiona Enter para continuar...")

'''
Presenta la cadena de texto de valor no válido y presenta los valores permitidos en caso de introducir una número no válido
'''
def txtOperando(operando):
        print(">> " + operando + " <<" , ''' No es un número válido, verifique por favor que:
        >> No tenga caracteres intercalados
        >> No haya entrado una cadena vacía
        >> El número no tenga caracteres especiales
        >>
        >> Escriba un número válido o Pulse la letra X para terminar el programa''')

'''
Presenta la cadena de texto de Operador no válido y presenta los operadores permitidos en caso de introducir una operación no válida
'''
def txtOperador(operacion):
        print(">> " + operacion + " <<" , ''' Operación no definida, únicamente son válidos los siguientes operandos
        + \t para la suma
        - \t para la resta
        * \t para el producto
        / \t para la división decimal
        pot \t para calcular la potencia de un número
        >>
        >> Escriba una operación válida o Pulse la letra X para terminar el programa''')

'''
Valida que el operador sea válido
'''
def ValidaOperador (Operador):
    operacionValida = ["+", "-", "*", "/", "pot"]
    if Operador in operacionValida:
        return True
    else: 
        return False

'''
Valida que el elemento introducido sea numérico
'''
def ValidaOperando(Operando):
    valor = Operando.isnumeric()
    if valor == True:
        return Operando
    else: 
        return False

'''
Punto de incio del programa, iniciamos con la presentaciòn del programa
indicando lo que hace y lo que espera de parte del usuario
'''
      
txtPresentacion()

terminar = False
while (terminar != True):
    
    while True:
        a = input("Operando 1: ")
        ValidaOperando(a)
        if (ValidaOperando(a) != False):
            break
        if (a == "x") or (a == "X"): 
            print(exit())
        txtOperando(a)

    while True:
        op = input("Operación: ")
        ValidaOperador(op)
        if (ValidaOperador(op) != False):
            break
        if (op == "x") or (op == "X"): 
            print(exit())
        txtOperador(op)

    while True:
        b = input("Operando 2: ")
        ValidaOperando(b)
        if (ValidaOperando(b) != False):
            break
        if (b == "x") or (b == "X"): 
            print(exit())
        txtOperando(b)

'''
Realiza la operación sobre los operandos 
'''      
realizaOperacion(a, op, b)

respuesta = input("Quieres salir? Escribe S para salir, cualquier otra letra para continuar: ")
if respuesta in ["S", "s"]:
    terminar = True
else:
    terminar = False

print("\n\nGacias por usar nuestros servicios, el cargo lo encontrará en su estado de cuenta")

cadena = input("Escribe la operación : ")
operandos, signo_operacion = parsear_operacion(cadena)
# realizaOperacion(operandos, signo_operacion, operandos) 
print("Operandos:", operandos)
print("Signo de operación:", signo_operacion)
