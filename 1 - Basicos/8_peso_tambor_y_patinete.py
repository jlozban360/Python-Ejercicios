# Peso de cada producto
peso_tambor = 112  # gramos
peso_patinete = 975  # gramos

# Pedir la cantidad de productos vendidos
tambores = int(input("¿Cuántos tambores se han vendido? "))
patinetes = int(input("¿Cuántos patinetes se han vendido? "))

# Calcular el peso total del paquete
peso_total = tambores * peso_tambor + patinetes * peso_patinete

# Mostrar el resultado
print(f"El peso total del paquete es: {peso_total} gramos.")