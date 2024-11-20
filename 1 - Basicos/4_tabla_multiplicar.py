# Preguntar qué tabla de multiplicar quiere calcular
tabla = int(input("¿Qué tabla de multiplicar quieres calcular? "))

# Mostrar la tabla del número introducido
print(f"Tabla del {tabla}:")
for i in range(1, 11):  # Iteramos del 1 al 10
    print(f"{tabla} x {i} = {tabla * i}")