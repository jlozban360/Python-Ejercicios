'''
Ejercicio 8
Una juguetería tiene mucho éxito en dos de sus productos: tambores y patinetes. Suele hacer venta por correo y la empresa de logística
les cobra por peso de cada paquete así que deben calcular el peso de los tambores y patinetes que saldrán en cada paquete a demanda.
Cada tambor pesa 112 g y cada patinete 975 g. Escribir un programa que pida el número de tambores y patinetes vendidos y calcule el
peso total del paquete que será enviado.

'''

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