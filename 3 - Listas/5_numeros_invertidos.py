'''
Ejercicio 5. 
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
por pantalla en orden inverso separados por comas.

'''

# Almacenar los números del 1 al 10 en una lista
numeros = list(range(1, 11))

# Mostrar los números en orden inverso
print(", ".join(map(str, numeros[::-1])))
