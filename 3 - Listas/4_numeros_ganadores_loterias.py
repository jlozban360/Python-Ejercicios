'''
Ejercicio 4. 
Escribir un programa que pregunte al usuario los números ganadores de la lotería 
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor 
a mayor.

'''

# Pedir los números ganadores de la lotería
numeros = []
for i in range(6):  # Lotería primitiva tiene 6 números
    numero = int(input(f"Introduce el {i + 1}º número ganador: "))
    numeros.append(numero)

# Ordenar los números de menor a mayor
numeros.sort()

# Mostrar los números ordenados
print("Los números ganadores son:", numeros)
