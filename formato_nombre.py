""" Funciones y condicionales if: formato_nombre.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: Complete el cuerpo de la función formato_nombre. Esta función recibe 
los parámetros primer_nombre y apellido y luego devuelve una cadena con el 
formato correcto.

Específicamente:
Si se proporcionan los parámetros apellido y primer_nombre, la función debería 
devolver:

"Nombre: apellido, nombre"

Si solo se proporciona un parámetro de nombre (ya sea el nombre o el apellido), 
la función debería devolver:

"Nombre: nombre"

Finalmente, si ambos nombres están en blanco, la función debería devolver la 
cadena vacía:

""
"""
def formato_nombre(primer_nombre, apellido):

    if (primer_nombre != "") and (apellido != ""):
        Nombre = "Nombre: " + apellido + ", " + primer_nombre
    else:
        if (primer_nombre == "") and (apellido == ""):
            Nombre = ""
        elif primer_nombre != "":
            Nombre = "Nombre: " + primer_nombre
        elif apellido != "":
            Nombre = "Nombre: " + apellido


    return Nombre

print(formato_nombre("Paulina", "Angel"))
# Should be "Name: Hemingway, Ernest"

print(formato_nombre("", "Stephanie"))
# Should be "Name: Madonna"

print(formato_nombre("Brozo", ""))
# Should be "Name: Voltaire"

print(formato_nombre("", ""))
# Should be ""
