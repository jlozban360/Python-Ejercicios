'''
Ejercicio 10
Escribir un programa en Python que calcule potencias, es decir, solicite la base y el exponente y calcule el resultado de la base elevada al exponente.

'''

# Pedir base y exponente al usuario
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular la potencia
resultado = base ** exponente

# Mostrar el resultado
print(f"{base} elevado a la {exponente} es igual a {resultado}")