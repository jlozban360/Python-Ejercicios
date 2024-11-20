# Solicitar la cantidad de dinero
dinero = float(input("Introduce la cantidad de dinero: "))

# Definir los valores de los billetes y monedas
billetes = [500, 200, 100, 50, 20, 10, 5]
monedas = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

# Descomponer en billetes
for billete in billetes:
    cantidad_billetes = int(dinero // billete)
    if cantidad_billetes > 0:
        print(f"{cantidad_billetes} billetes de {billete}€")
        dinero -= cantidad_billetes * billete

# Descomponer en monedas
for moneda in monedas:
    cantidad_monedas = int(dinero // moneda)
    if cantidad_monedas > 0:
        print(f"{cantidad_monedas} monedas de {moneda}€")
        dinero -= cantidad_monedas * moneda
