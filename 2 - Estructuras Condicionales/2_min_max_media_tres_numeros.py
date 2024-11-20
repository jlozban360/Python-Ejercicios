# Pedir tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular mínimo, máximo y media
minimo = min(num1, num2, num3)
maximo = max(num1, num2, num3)
media = (num1 + num2 + num3) / 3

# Mostrar los resultados
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Media: {media}")
