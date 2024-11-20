# Solicitar la operación en formato "número operador número"
operacion = input("Introduce una operación (ejemplo: 2 + 3): ")

# Separar los elementos de la operación
num1, operador, num2 = operacion.split()

# Convertir los números a flotantes
num1 = float(num1)
num2 = float(num2)

# Realizar la operación
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por 0"
else:
    resultado = "Operador no válido"

# Mostrar el resultado
print(f"Resultado: {resultado}")
