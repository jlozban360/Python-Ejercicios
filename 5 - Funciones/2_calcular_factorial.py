# Función para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar al usuario un número
numero = int(input("Introduce un número: "))

# Calcular y mostrar el factorial
print(f"El factorial de {numero} es {factorial(numero)}.")
