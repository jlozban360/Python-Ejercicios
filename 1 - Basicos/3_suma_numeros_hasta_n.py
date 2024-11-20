# Pedir al usuario un número entero
n = int(input("Introduce un número entero: "))

# Calcular la suma usando la fórmula Suma = n(n + 1) / 2
suma = n * (n + 1) // 2  # Usamos // para que la división sea entera

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")