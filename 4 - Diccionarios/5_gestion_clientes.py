'''
Ejercicio 5. 
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los 
clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor 
será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe 
preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, 
(3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En 
función de la opción elegida el programa tendrá que hacer lo siguiente: 

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de 
datos. 
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. 
3. Preguntar por el NIF del cliente y mostrar sus datos. 
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre. 
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre. 
6. Terminar el programa.

'''

# Diccionario de clientes
clientes = {}

# Menú de opciones
def menu():
    print("\nOpciones:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == '1':  # Añadir cliente
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        telefono = input("Introduce el teléfono: ")
        correo = input("Introduce el correo: ")
        preferente = input("¿Es cliente preferente? (sí/no): ").lower() == 'sí'

        clientes[nif] = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'preferente': preferente
        }
        print("Cliente añadido.")
        
    elif opcion == '2':  # Eliminar cliente
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado.")
        else:
            print("Cliente no encontrado.")
    
    elif opcion == '3':  # Mostrar cliente
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            cliente = clientes[nif]
            print(f"{cliente['nombre']} - {cliente['direccion']} - {cliente['telefono']} - {cliente['correo']} - Preferente: {cliente['preferente']}")
        else:
            print("Cliente no encontrado.")
    
    elif opcion == '4':  # Listar todos los clientes
        for nif, cliente in clientes.items():
            print(f"{nif}: {cliente['nombre']}")
    
    elif opcion == '5':  # Listar clientes preferentes
        for nif, cliente in clientes.items():
            if cliente['preferente']:
                print(f"{nif}: {cliente['nombre']}")
    
    elif opcion == '6':  # Terminar
        print("Fin del programa.")
        break
