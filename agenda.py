""" agenda.py
  Por https://about.me/carlosgbr 
  
  Versión 1
  Para Python 3.0 y superior
  Agenda simple telefónica con las siguientes funciones:
  1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Editar contacto
5. Mostrar todos los contactos
6. Ingresar múltiples contactos
0. Salir

  https://github.com/carlosgbr/python0/blob/master/matrices.py
"""


# Definición de la agenda como un diccionario
agenda = {}

# Función para agregar un nuevo contacto
def agregar_contacto(nombre, numero):
    if nombre in agenda:
        print("El contacto ya existe en la agenda.")
    elif numero.isdigit() and len(numero) >= 7:
        agenda[nombre] = numero
        print("Contacto agregado correctamente.")
    else:
        print("Número telefónico inválido. Asegúrese de ingresar un número válido de al menos 7 dígitos.")

# Función para buscar un contacto
def buscar_contacto(nombre):
    contactos_encontrados = []
    for contacto, numero in agenda.items():
        if nombre.lower() in contacto.lower():
            contactos_encontrados.append((contacto, numero))
    if contactos_encontrados:
        print("Contactos encontrados:")
        for contacto, numero in contactos_encontrados:
            print(contacto + ":", numero)
    else:
        print("Contacto no encontrado.")

# Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("Contacto no encontrado.")

# Función para editar un contacto
def editar_contacto(nombre, nuevo_numero):
    if nombre in agenda:
        if nuevo_numero.isdigit() and len(nuevo_numero) >= 7:
            agenda[nombre] = nuevo_numero
            print("Contacto editado correctamente.")
        else:
            print("Número telefónico inválido. Asegúrese de ingresar un número válido de al menos 7 dígitos.")
    else:
        print("Contacto no encontrado.")

# Función para mostrar todos los contactos
def mostrar_contactos():
    if agenda:
        print("Lista de contactos:")
        for nombre, numero in agenda.items():
            print(nombre + ":", numero)
    else:
        print("La agenda está vacía.")

# Función para ingresar múltiples contactos
def ingresar_multiples_contactos():
    while True:
        nombre = input("Ingrese el nombre del contacto ('parar' para detener): ")
        if nombre.lower() == "parar":
            break
        numero = input("Ingrese el número telefónico: ")
        agregar_contacto(nombre, numero)

# Menú principal
while True:
    print("\n---- AGENDA TELEFÓNICA ----")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Editar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Ingresar múltiples contactos")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ingrese el número telefónico: ")
        agregar_contacto(nombre, numero)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto: ")
        eliminar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto: ")
        nuevo_numero = input("Ingrese el nuevo número telefónico: ")
        editar_contacto(nombre, nuevo_numero)
    elif opcion == "5":
        mostrar_contactos()
    elif opcion == "6":
        ingresar_multiples_contactos()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
