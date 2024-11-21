'''
Ejercicio 6
Escribir un programa en Python que pida al usuario su peso (en kg) y su estatura (en cm) y calcule su índice de masa corporal y lo almacene en una variable. 
A continuación, debe mostrar por pantalla la frase “Tu índice de masa corporal es …”, redondeado con dos decimales.

'''

# Pedir peso y altura al usuario
peso = float(input("Introduce tu peso en kg: "))
estatura_cm = float(input("Introduce tu estatura en cm: "))

# Convertir la altura a metros
estatura_m = estatura_cm / 100

# Calcular el IMC
imc = peso / (estatura_m ** 2)

# Mostrar el resultado redondeado a 2 decimales
print(f"Tu índice de masa corporal es: {imc:.2f}")
