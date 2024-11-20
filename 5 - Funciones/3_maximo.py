# Función max() para obtener el mayor de dos números
def maximo(a, b):
    if a > b:
        return a
    return b

# Solicitar dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Obtener el mayor y mostrarlo
print(f"El mayor número es {maximo(numero1, numero2)}.")