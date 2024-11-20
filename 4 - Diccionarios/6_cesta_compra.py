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
