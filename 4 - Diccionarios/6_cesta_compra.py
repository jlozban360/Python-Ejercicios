'''
Ejercicio 6. 
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa 
debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida 
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el 
siguiente formato: 

'''

# Diccionario para almacenar los artículos y precios
cesta = {}

while True:
    articulo = input("Introduce el artículo (o 'fin' para terminar): ")
    if articulo.lower() == 'fin':
        break
    precio = float(input(f"Introduce el precio de {articulo}: "))
    cesta[articulo] = precio

# Mostrar la lista de la compra y el coste total
print("\nLista de la compra:")
total = 0
for articulo, precio in cesta.items():
    print(f"{articulo}: {precio}€")
    total += precio

print(f"Total: {total}€")
