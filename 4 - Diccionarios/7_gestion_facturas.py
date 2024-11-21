'''
Ejercicio 7. 
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las factu
ras se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva 
factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el 
número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se pre
guntará por el número de factura y se eliminará del diccionario. Después de cada operación el 
programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pen
diente de cobro.

'''

# Diccionario para almacenar las facturas
facturas = {}

# Función para gestionar las facturas
def menu():
    print("\nOpciones:")
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Terminar")

total_cobrado = 0
while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == '1':  # Añadir factura
        numero_factura = input("Introduce el número de la factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[numero_factura] = coste
        print("Factura añadida.")
    
    elif opcion == '2':  # Pagar factura
        numero_factura = input("Introduce el número de la factura a pagar: ")
        if numero_factura in facturas:
            total_cobrado += facturas[numero_factura]
            del facturas[numero_factura]
            print("Factura pagada.")
        else:
            print("Factura no encontrada.")
    
    elif opcion == '3':  # Terminar
        print(f"Total cobrado: {total_cobrado}€")
        print(f"Total pendiente de cobro: {sum(facturas.values())}€")
        print("Fin del programa.")
        break
